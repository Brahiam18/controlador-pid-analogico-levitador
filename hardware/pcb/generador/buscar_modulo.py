"""Busca una colocación + ruteo de UN módulo PID (con su etapa de potencia) de tamaño wc x hc (en pasos de 2.54 mm).
Uso:  python3 buscar_modulo.py WC HC SEMILLAS(1,2,3) etiqueta [asignacion]
Guarda el mejor resultado en best_<etiqueta>.pkl y lo convierte con a_json.py."""
import sys,pickle,time,multiprocessing as mp
sys.path.insert(0,'.')
import netlist as N
from engine import *
import place as P
from pf import PF

def analyze(r):
    """componentes de capa 1 -> puentes de alambre"""
    adj={}
    for net,rt in r.routes.items():
        for a,b in rt['edges']:
            if a[0]==1:
                adj.setdefault((net,a[1:]),set()).add((net,b[1:])); adj.setdefault((net,b[1:]),set()).add((net,a[1:]))
    seen=set(); comps=[]
    for k in adj:
        if k in seen: continue
        st=[k]; seen.add(k); n=0
        while st:
            u=st.pop(); n+=1
            for v in adj[u]:
                if v not in seen: seen.add(v); st.append(v)
        comps.append(n)
    bot=sum(1 for rt in r.routes.values() for a,b in rt['edges'] if a[0]==0)
    top=sum(1 for rt in r.routes.values() for a,b in rt['edges'] if a[0]==1)
    return len(comps),bot,top,sorted(comps)

def job(args):
    a,wc,hc,sd=args
    N.set_assign(a)
    P.WCELLS,P.HCELLS=wc,hc; P.W=wc*PITCH; P.H=hc*PITCH
    parts,b=P.anneal(sd,60000)
    W,H=P.W,P.H
    out=None
    for rs in (1,2):
        fz=frozen_routes(parts)
        r=PF(W,H,parts,N.NETS,jump_cost=35,top_cost=3.0,wide=N.WIDE,frozen=fz)
        if not r.solve(iters=150,seed=rs): continue
        j,bot,top,comps=analyze(r)
        score=j*120+bot*1.27+top*1.27*3+max(comps)*30
        if out is None or score<out['score']:
            out=dict(score=score,jumpers=j,bot=bot,top=top,comps=comps,seed=sd,rs=rs,wc=wc,hc=hc,assign=a,placecost=b,
              parts={k:(v.kind,v.x,v.y,v.r) for k,v in parts.items()},
              routes={n:{'edges':set(rt['edges']),'vias':set(rt['vias']),'nodes':set(rt['nodes'])} for n,rt in r.routes.items()})
    return (a,wc,hc,sd,b,out)

if __name__=='__main__':
    wc,hc=int(sys.argv[1]),int(sys.argv[2]); seeds=[int(x) for x in sys.argv[3].split(',')]
    tag=sys.argv[4]; assign=sys.argv[5] if len(sys.argv)>5 else 'final'
    jobs=[(assign,wc,hc,sd) for sd in seeds]
    t=time.time(); best=None
    with mp.Pool(2) as pool:
        for a,wc_,hc_,sd,b,o in pool.imap_unordered(job,jobs):
            print(a,wc_,hc_,sd,'colocacion',round(b),None if o is None else (round(o['score']),o['jumpers'],o['bot'],o['top'],o['comps']),round(time.time()-t),flush=True)
            if o and (best is None or o['score']<best['score']):
                best=o; pickle.dump(best,open('best_%s.pkl'%tag,'wb'))
    print('mejor',best and (best['assign'],best['wc'],best['hc'],best['seed'],best['jumpers'],round(best['score'])),flush=True)
