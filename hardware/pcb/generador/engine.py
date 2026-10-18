import math, random, heapq, itertools
G=1.27           # paso de rejilla de ruteo (mm)
PITCH=2.54
PAD_D=2.0; DRILL=0.9; TRACE=0.7; CLEAR=0.4

def rot(x,y,r):
    r%=4
    for _ in range(r): x,y=-y,x     # 90° antihorario
    return x,y

# huellas: lista de (pin, x, y) en mm, en coordenadas locales (origen = pin 1)
def fp_pads(kind):
    if kind=='DIP8':
        pads=[(str(n),0,-(n-1)*PITCH) for n in range(1,5)]
        pads+=[(str(n),7.62,-(8-n)*PITCH) for n in range(5,9)]
        return pads
    if kind=='RES': return [('1',0,0),('2',7.62,0)]
    if kind=='CAP': return [('1',0,0),('2',5.08,0)]
    if kind=='POT': return [('1',0,0),('2',5.08,0),('3',10.16,0)]
    if kind=='HDR1': return [('1',0,0)]
    if kind=='HDR2': return [('1',0,0),('2',PITCH,0)]
    if kind=='HDR4': return [('%d'%i,i*PITCH-PITCH,0) for i in range(1,5)]
    raise KeyError(kind)

def fp_box(kind):
    """caja de cuerpo (xmin,ymin,xmax,ymax) local, para evitar solapes"""
    p=fp_pads(kind); xs=[a[1] for a in p]; ys=[a[2] for a in p]
    m=2.54
    return (min(xs)-m,min(ys)-m,max(xs)+m,max(ys)+m)

class Placed:
    def __init__(s,ref,kind,x,y,r):
        s.ref,s.kind,s.x,s.y,s.r=ref,kind,x,y,r
    def pads(s):
        out={}
        for pin,px,py in fp_pads(s.kind):
            rx,ry=rot(px,py,s.r); out[pin]=(round(s.x+rx,4),round(s.y+ry,4))
        return out
    def box(s):
        x0,y0,x1,y1=fp_box(s.kind)
        pts=[rot(a,b,s.r) for a,b in ((x0,y0),(x1,y0),(x1,y1),(x0,y1))]
        xs=[s.x+p[0] for p in pts]; ys=[s.y+p[1] for p in pts]
        return (min(xs),min(ys),max(xs),max(ys))

class Grid:
    def __init__(s,W,H):
        s.nx=int(round(W/G))+1; s.ny=int(round(H/G))+1
        s.own=[{} ,{}]      # layer -> {(i,j):net}
        s.res=[{} ,{}]      # reservas alrededor de pads: (i,j)->net (o -1 si varias)
        s.blocked=set()
    def idx(s,x,y): return (int(round(x/G)),int(round(y/G)))
    def add_pad(s,i,j,net):
        for l in (0,1):
            s.own[l][(i,j)]=net
            for di,dj in ((0,0),(1,0),(-1,0),(0,1),(0,-1)):
                k=(i+di,j+dj); cur=s.res[l].get(k)
                if cur is None or cur==net: s.res[l][k]=net
                else: s.res[l][k]=-1
    def free(s,l,i,j,net):
        if not(0<=i<s.nx and 0<=j<s.ny): return False
        if (i,j) in s.blocked: return False
        o=s.own[l].get((i,j))
        if o is not None and o!=net: return False
        r=s.res[l].get((i,j))
        if r is not None and r!=net: return False
        return True
    def via_ok(s,i,j,net):
        if not(s.free(0,i,j,net) and s.free(1,i,j,net)): return False
        # un via es un pad: no puede quedar pegado a otro nodo ajeno
        for l in (0,1):
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                o=s.own[l].get((i+di,j+dj))
                if o is not None and o!=net: return False
        return True

def route_net(g,net,pads,via_cost=10,jump_cost=35,top_cost=3.0,noise=0.0,rng=None):
    """Ruteo de una red. Capa 0 = cobre inferior; capa 1 = puente de alambre (superior).
    jump_cost se cobra al subir de capa (un puente). via_cost = agujero extra."""
    padset=set(pads)
    tree={}       # nodo -> costo inicial
    edges=[]; vias=[]; jumps=0
    first=pads[0]
    tree[(0,)+first]=0; tree[(1,)+first]=jump_cost
    remaining=list(pads[1:])
    while remaining:
        targets={}
        for p in remaining: targets[(0,)+p]=p; targets[(1,)+p]=p
        dist={}; prev={}; pq=[]
        for t,c in tree.items():
            dist[t]=c; heapq.heappush(pq,(c,t))
        found=None
        while pq:
            d,u=heapq.heappop(pq)
            if d>dist.get(u,1e18): continue
            if u in targets: found=u; break
            l,i,j=u
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                v=(l,i+di,j+dj)
                if not g.free(l,v[1],v[2],net): continue
                c=1.0 if l==0 else top_cost
                if rng and noise: c+=rng.random()*noise
                nd=d+c
                if nd<dist.get(v,1e18): dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd,v))
            ispad=(i,j) in padset or g.own[0].get((i,j))==net and g.own[1].get((i,j))==net
            if ispad or g.via_ok(i,j,net):
                extra=0 if ispad else via_cost
                v=(1-l,i,j); nd=d+extra+(jump_cost if l==0 else 0)
                if nd<dist.get(v,1e18): dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd,v))
        if not found: return None
        u=found; path=[u]
        while u in prev and not (u in tree and prev.get(u) is None):
            if u in tree and dist[u]==tree[u]: break
            u=prev[u]; path.append(u)
        path.reverse()
        for a,b in zip(path,path[1:]):
            if a[0]==b[0]: edges.append((a,b))
            else:
                vias.append((a[1],a[2]))
                if a[0]==0: jumps+=1
        for n in path:
            tree[n]=0; g.own[n[0]][(n[1],n[2])]=net
        for a,b in zip(path,path[1:]):
            if a[0]!=b[0]:
                g.add_pad(a[1],a[2],net)
                tree[(0,a[1],a[2])]=0; tree[(1,a[1],a[2])]=jump_cost
        # extremos del camino: agujero pasante en ambas capas
        e=path[-1]; tree[(0,e[1],e[2])]=0; tree[(1,e[1],e[2])]=jump_cost
        remaining.remove(targets[found])
    return edges,vias
