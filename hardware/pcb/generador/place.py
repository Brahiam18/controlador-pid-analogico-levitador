import random, math, sys
from engine import *
import netlist as N

WCELLS,HCELLS=int(sys.argv[1]) if len(sys.argv)>1 else 31, int(sys.argv[2]) if len(sys.argv)>2 else 47
W=WCELLS*PITCH; H=HCELLS*PITCH

FIXED=('J_IN','J_OUT','J_PWR','RS','J_VBOB','J_COIL')
def make_parts(seed):
    rng=random.Random(seed)
    parts={}
    for ref,(kind,val) in N.PARTS.items():
        parts[ref]=Placed(ref,kind,0,0,0)
    # fijos
    parts['J_IN'].r=1; parts['J_IN'].x=2*PITCH; parts['J_IN'].y=(HCELLS//2+8)*PITCH
    parts['J_OUT'].r=1; parts['J_OUT'].x=(WCELLS-2)*PITCH; parts['J_OUT'].y=(HCELLS//2+8)*PITCH
    parts['J_PWR'].r=0; parts['J_PWR'].x=6*PITCH; parts['J_PWR'].y=(HCELLS-2)*PITCH
    # banco de sensado (huella con pistas troncales) abajo a la izquierda; bornes de alimentación y bobina a su derecha
    parts['RS'].r=0; parts['RS'].x=5*PITCH; parts['RS'].y=4*PITCH
    parts['J_VBOB'].r=0; parts['J_VBOB'].x=(WCELLS-9)*PITCH; parts['J_VBOB'].y=3*PITCH
    parts['J_COIL'].r=0; parts['J_COIL'].x=(WCELLS-9)*PITCH; parts['J_COIL'].y=9*PITCH
    free=[r for r in parts if r not in FIXED]
    for r in free:
        p=parts[r]; p.r=rng.choice([0,1,2,3]) if not p.kind.startswith('DIP') else 0
        p.x=rng.randint(4,WCELLS-8)*PITCH; p.y=rng.randint(4,HCELLS-5)*PITCH
    return parts,free

def pin_xy(parts,ref,pin): return parts[ref].pads()[pin]

def cost(parts,nets,boxes=None):
    c=0.0
    for name,pins in nets.items():
        xs=[];ys=[]
        for ref,pin in pins:
            x,y=pin_xy(parts,ref,pin); xs.append(x); ys.append(y)
        w=0.15 if name in N.SHARED else (3.0 if name in N.WIDE else 1.0)
        c+=w*((max(xs)-min(xs))+(max(ys)-min(ys)))
    bx={r:p.box() for r,p in parts.items()}
    refs=list(parts)
    pen=0
    for i in range(len(refs)):
        a=bx[refs[i]]
        # fuera de la región
        if a[0]<1 or a[1]<1 or a[2]>W-1 or a[3]>H-1: pen+=1+ (max(0,1-a[0])+max(0,1-a[1])+max(0,a[2]-W+1)+max(0,a[3]-H+1))
        for j in range(i+1,len(refs)):
            b=bx[refs[j]]
            ox=min(a[2],b[2])-max(a[0],b[0]); oy=min(a[3],b[3])-max(a[1],b[1])
            if ox>0.01 and oy>0.01: pen+=1+ox*oy/50
    return c+pen*400

def anneal(seed,iters=60000):
    rng=random.Random(seed)
    parts,free=make_parts(seed)
    cur=cost(parts,N.NETS); T=60.0
    best=cur; bestst=None
    for it in range(iters):
        T=60.0*(1-it/iters)**2+0.3
        r=rng.choice(free); p=parts[r]; old=(p.x,p.y,p.r)
        m=rng.random()
        if m<0.6: p.x+=rng.choice([-3,-2,-1,1,2,3])*PITCH if rng.random()<.5 else 0; p.y+=rng.choice([-3,-2,-1,1,2,3])*PITCH if rng.random()<.5 else 0
        elif m<0.8 and not p.kind.startswith('DIP'): p.r=(p.r+rng.choice([1,2,3]))%4
        else: p.x=rng.randint(3,WCELLS-3)*PITCH; p.y=rng.randint(3,HCELLS-3)*PITCH
        nc=cost(parts,N.NETS)
        if nc<=cur or rng.random()<math.exp((cur-nc)/T): cur=nc
        else: p.x,p.y,p.r=old
        if cur<best-1e-9:
            best=cur; bestst={k:(v.x,v.y,v.r) for k,v in parts.items()}
    for k,(x,y,r) in bestst.items(): parts[k].x,parts[k].y,parts[k].r=x,y,r
    return parts,best

if __name__=='__main__':
    import time
    t=time.time(); parts,b=anneal(int(sys.argv[3]) if len(sys.argv)>3 else 1,20000)
    print('cost',b,'time',time.time()-t)
