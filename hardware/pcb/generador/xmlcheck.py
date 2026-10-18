import sys, math, collections
import xml.etree.ElementTree as ET
from shapely.geometry import LineString, Point
from shapely.ops import unary_union

def rotpt(x,y,rot):
    r=int(rot.lstrip('MSR') or 0)//90 if rot else 0
    for _ in range(r%4): x,y=-y,x
    return x,y

def load_board(path):
    t=ET.parse(path).getroot(); b=t.find('.//board')
    pk={}
    for p in b.findall('.//library/packages/package'):
        pk[p.get('name')]={pd.get('name'):(float(pd.get('x')),float(pd.get('y')),float(pd.get('diameter'))) for pd in p.findall('pad')}
    pads={}
    for e in b.findall('elements/element'):
        rot=e.get('rot','R0'); ex,ey=float(e.get('x')),float(e.get('y'))
        for n,(x,y,d) in pk[e.get('package')].items():
            rx,ry=rotpt(x,y,rot); pads[(e.get('name'),n)]=(ex+rx,ey+ry,d)
    sigs={}
    for s in b.findall('signals/signal'):
        sigs[s.get('name')]=dict(
          refs=[(c.get('element'),c.get('pad')) for c in s.findall('contactref')],
          wires=[(float(w.get('x1')),float(w.get('y1')),float(w.get('x2')),float(w.get('y2')),float(w.get('width')),int(w.get('layer'))) for w in s.findall('wire')],
          vias=[(float(v.get('x')),float(v.get('y')),float(v.get('diameter'))) for v in s.findall('via')])
    return pads,sigs

def check_board(path,min_clear=0.3):
    pads,sigs=load_board(path)
    bad=[]; allbottom=[]
    for name,s in sigs.items():
        geo16=[]; 
        for x1,y1,x2,y2,w,l in s['wires']:
            if l==16: geo16.append(LineString([(x1,y1),(x2,y2)]).buffer(w/2,cap_style=1))
        padg=[Point(*pads[r][:2]).buffer(pads[r][2]/2) for r in s['refs']]
        viag=[Point(v[0],v[1]).buffer(v[2]/2) for v in s['vias']]
        bot=unary_union(geo16+padg+viag)
        # puentes: wires layer 1 conectan pads/vias por sus extremos
        top=[LineString([(x1,y1),(x2,y2)]).buffer(0.3) for x1,y1,x2,y2,w,l in s['wires'] if l==1]
        allg=unary_union([bot]+top) if top else bot
        comps=list(allg.geoms) if allg.geom_type=='MultiPolygon' else [allg]
        # cada pad en alguna componente
        ids=set()
        for r in s['refs']:
            p=Point(*pads[r][:2])
            for k,c in enumerate(comps):
                if c.buffer(0.01).contains(p): ids.add(k); break
            else: bad.append(('pad-sin-cobre',name,r))
        if len(ids)>1: bad.append(('red-abierta',name,len(ids)))
        allbottom.append((name,bot))
    # cortos y holguras en el cobre inferior
    from shapely.strtree import STRtree
    tr=STRtree([g for _,g in allbottom]); mind=1e9
    for i,(n,g) in enumerate(allbottom):
        for j in tr.query(g.buffer(min_clear+0.01)):
            if j<=i: continue
            d=g.distance(allbottom[j][1]); mind=min(mind,d)
            if d<min_clear: bad.append(('holgura',n,allbottom[j][0],round(d,3)))
    # pads sin red
    return bad,mind,len(sigs)

def check_sch_vs_brd(sch,brd):
    t=ET.parse(sch).getroot()
    dsmap={}
    for ds in t.findall('.//deviceset'):
        mp={(c.get('gate'),c.get('pin')):c.get('pad') for c in ds.findall('.//connect')}
        dsmap[ds.get('name')]=mp
    parts={p.get('name'):p.get('deviceset') for p in t.findall('.//parts/part')}
    nets=collections.defaultdict(set)
    for n in t.findall('.//sheet/nets/net'):
        for pr in n.findall('.//pinref'):
            nets[n.get('name')].add((pr.get('part'),dsmap[parts[pr.get('part')]][(pr.get('gate'),pr.get('pin'))]))
    pads,sigs=load_board(brd)
    bad=[]
    for name,s in sigs.items():
        if set(s['refs'])!=nets.get(name,set()): bad.append(('difiere',name,set(s['refs'])^nets.get(name,set())))
    for name in nets:
        if name not in sigs: bad.append(('solo-sch',name))
    # componentes
    b=ET.parse(brd).getroot()
    el={e.get('name') for e in b.findall('.//elements/element')}
    if el!=set(parts): bad.append(('componentes',el^set(parts)))
    return bad
if __name__=='__main__':
    bad,mind,n=check_board(sys.argv[1]); print('placa:',n,'señales | min holgura %.3f'%mind,'| problemas',len(bad),bad[:5])
    print('sch vs brd:',check_sch_vs_brd(sys.argv[2],sys.argv[1])[:5] or 'consistentes')
