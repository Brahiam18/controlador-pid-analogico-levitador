import collections, itertools
from shapely.geometry import LineString, Point
from shapely.strtree import STRtree
from engine import *
from eagle import merge_edges

def verify(parts,routes,nets,W,H,min_clear=0.30,verbose=True):
    problems=[]
    padpos={}
    for ref,p in parts.items():
        for pin,(x,y) in p.pads().items(): padpos[(ref,pin)]=(x,y)
    # geometría de cobre inferior por red
    geoms=[]   # (net, geom, kind)
    for net,pins in nets.items():
        for ref,pin in pins:
            x,y=padpos[(ref,pin)]; geoms.append((net,Point(x,y).buffer(PAD_D/2),'pad'))
    nc=0
    for ref,p in parts.items():
        for pin,(x,y) in p.pads().items():
            if not any((ref,pin) in set(v) for v in nets.values()):
                geoms.append(('NC_%s_%s'%(ref,pin),Point(x,y).buffer(PAD_D/2),'pad'))
    for net,rt in routes.items():
        for s in merge_edges(rt['edges'],0):
            geoms.append((net,LineString([(s[0],s[1]),(s[2],s[3])]).buffer(TRACE/2,cap_style=1),'trace'))
        for (i,j) in rt['vias']:
            geoms.append((net,Point(i*G,j*G).buffer(PAD_D/2),'via'))
    tree=STRtree([g for _,g,_ in geoms])
    mind=1e9
    for k,(net,g,kind) in enumerate(geoms):
        for m in tree.query(g.buffer(min_clear+0.01)):
            if m<=k: continue
            n2,g2,k2=geoms[m]
            if n2==net: continue
            d=g.distance(g2)
            mind=min(mind,d)
            if d<min_clear: problems.append(('clearance',net,n2,round(d,3),kind,k2,tuple(round(c,1) for c in g.centroid.coords[0]),tuple(round(c,1) for c in g2.centroid.coords[0])))
    # conectividad
    for net,pins in nets.items():
        rt=routes.get(net,{'edges':set(),'vias':set()})
        parent={}
        def find(a):
            while parent.setdefault(a,a)!=a:
                parent[a]=parent[parent[a]]; a=parent[a]
            return a
        def union(a,b): parent[find(a)]=find(b)
        for a,b in rt['edges']: union(a,b)
        # pads y vias unen capas
        pp=set()
        for ref,pin in pins:
            x,y=padpos[(ref,pin)]; i,j=round(x/G),round(y/G); pp.add((i,j)); union((0,i,j),(1,i,j))
        for (i,j) in rt['vias']: union((0,i,j),(1,i,j))
        roots={find((0,i,j)) for (i,j) in pp}
        if len(roots)>1: problems.append(('abierta',net,len(roots)))
    # puentes superiores: contacto con pads ajenos
    top=[]
    for net,rt in routes.items():
        for s in merge_edges(rt['edges'],1):
            top.append((net,LineString([(s[0],s[1]),(s[2],s[3])])))
    cross=0
    for (n1,l1),(n2,l2) in itertools.combinations(top,2):
        if n1!=n2 and l1.distance(l2)<0.6: cross+=1
    padg=[(n,Point(*padpos[(r,p)]).buffer(PAD_D/2)) for n,pins in nets.items() for r,p in pins]
    touch=0
    for n1,l1 in top:
        for n2,g in padg:
            if n1!=n2 and l1.distance(g)<0.5: touch+=1; problems.append(('puente-toca-pad',n1,n2))
    if verbose: print('min distancia entre redes distintas: %.3f mm'%mind,'| cruces de puentes entre redes:',cross,'| problemas:',len(problems))
    return problems,mind,cross
