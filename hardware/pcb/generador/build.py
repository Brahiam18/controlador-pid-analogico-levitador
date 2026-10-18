import sys,json,collections
sys.path.insert(0,'.')
import netlist as N, assemble as A, verify as V, eagle as E, pdfs
from engine import *
import xml.etree.ElementTree as ET

def build(selfile,outdir,gx=3,gy=2,m=2,name='pid4'):
    js=json.load(open(selfile))
    N.set_assign(js.get('assign','a1'))
    sel=dict(wc=js['wc'],hc=js['hc'],parts={k:tuple(v) for k,v in js['parts'].items()},
      routes={n:dict(edges={(tuple(a),tuple(b_)) for a,b_ in rt['edges']},vias={tuple(v) for v in rt['vias']},nodes={tuple(n_) for n_ in rt['nodes']}) for n,rt in js['routes'].items()})
    parts,routes,W,H=A.assemble(sel,gap_x=gx*PITCH,gap_y=gy*PITCH,margin=m*PITCH)
    nets=A.global_nets()
    A.connect_shared(parts,routes,W,H,nets)
    prob,mind,cross=V.verify(parts,routes,nets,W,H)
    assert not prob,prob[:5]
    # etiquetas de serigrafía
    labels=[]
    for k in range(1,5):
        p=parts['P%d_J_PWR'%k]
        for pin,txt in zip('1234',('+16V','-16V','GND','+5V')):
            x,y=p.pads()[pin]; labels.append((x,y-3.6,txt,1.0,'R0'))
        p=parts['P%d_J_IN'%k]
        x,y=p.pads()['1']; labels.append((x-2.2,y-1.2,'VSEN',1.0,'R0'))
        p=parts['P%d_J_OUT'%k]
        x,y=p.pads()['1']; labels.append((x+2.2,y-1.2,'VPID',1.0,'R0'))
        # titulo del módulo
        x0,y0,x1,y1=[min(v) if i<2 else max(v) for i,v in enumerate(zip(*[q.box() for r,q in parts.items() if r.startswith('P%d_'%k)]))]
        labels.append((x0+1,y1-1.5,'PID %d'%k,2.2,'R0'))
    for k in range(1,5):
        for (ic,pin),stage in N.chan_labels().items():
            p=parts['P%d_%s'%(k,ic)]
            x,y=p.pads()[pin]
            txt=stage if stage!='SPARE' else 'libre'
            labels.append((p.x+3.81-0.55*len(txt)*0.9,y-0.5,txt,1.0,'R0'))
    open(outdir+'/'+name+'.brd','w',encoding='utf-8').write(E.brd_xml(parts,routes,W,H,nets,labels))
    # esquemático
    bymod={k:{} for k in range(1,5)}
    for k in range(1,5):
        pre='P%d_'%k
        for net,pins in N.NETS.items():
            g=net if net in N.SHARED else pre+net
            bymod[k][g]=list(pins)
    open(outdir+'/'+name+'.sch','w',encoding='utf-8').write(E.sch_xml(4,bymod))
    for f_ in ('.brd','.sch'): ET.parse(outdir+'/'+name+f_)
    return parts,routes,W,H,nets
if __name__=='__main__':
    import os, puentes
    src=sys.argv[1] if len(sys.argv)>1 else 'modulo_ruteado.json'
    out=sys.argv[2] if len(sys.argv)>2 else 'salida'
    os.makedirs(out,exist_ok=True)
    parts,routes,W,H,nets=build(src,out)
    jl=pdfs.assembly_pdf(out+'/ensamble_1a1.pdf',parts,routes,W,H,nets)
    pdfs.copper_pdf(out+'/cobre_espejado_1a1.pdf',parts,routes,W,H)
    open(out+'/puentes.md','w',encoding='utf-8').write(puentes.tabla(jl))
    print('placa %.1f x %.1f mm | %d puentes'%(W,H,len(jl)))
