import math, random, heapq, itertools
G=1.27           # paso de rejilla de ruteo (mm)
PITCH=2.54
PAD_D=2.0; DRILL=0.9; TRACE=0.7; CLEAR=0.4

def rot(x,y,r):
    r%=4
    for _ in range(r): x,y=-y,x     # 90° antihorario
    return x,y

# huellas: lista de (pin, x, y) en mm, en coordenadas locales (origen = pin 1)
RSB_COLS=5; RSB_DX=8     # banco de sensado: 5 columnas separadas 8 celdas (10.16 mm)
RSB_YA,RSB_YI1,RSB_YT,RSB_YI2,RSB_YC=0,20,21,22,42   # filas (en celdas de 1.27 mm)
RSB_XB=-4                # columna del puente de tierra (celdas)

def fp_pads(kind):
    if kind=='DIP8':
        pads=[(str(n),0,-(n-1)*PITCH) for n in range(1,5)]
        pads+=[(str(n),7.62,-(8-n)*PITCH) for n in range(5,9)]
        return pads
    if kind=='DIP14':
        pads=[(str(n),0,-(n-1)*PITCH) for n in range(1,8)]
        pads+=[(str(n),7.62,-(14-n)*PITCH) for n in range(8,15)]
        return pads
    if kind=='RES': return [('1',0,0),('2',7.62,0)]
    if kind=='CAP': return [('1',0,0),('2',5.08,0)]
    if kind=='POT': return [('1',0,0),('2',5.08,0),('3',10.16,0)]
    if kind=='HDR1': return [('1',0,0)]
    if kind=='HDR2': return [('1',0,0),('2',PITCH,0)]
    if kind=='HDR4': return [('%d'%i,i*PITCH-PITCH,0) for i in range(1,5)]
    if kind=='TO220': return [('1',0,0),('2',PITCH,0),('3',2*PITCH,0)]          # B, C, E
    if kind=='DIODE': return [('1',0,0),('2',15.24,0)]                          # 1 = ánodo, 2 = cátodo (raya)
    if kind=='DIODE_S': return [('1',0,0),('2',7.62,0)]
    if kind=='TERM2': return [('1',0,0),('2',5.08,0)]
    if kind=='RSBANK':
        p=[]
        for k in range(RSB_COLS):
            x=k*RSB_DX*G
            p.append(('%d'%(k+1),x,RSB_YA*G))        # abajo: tierra de potencia
            p.append(('%d'%(k+6),x,RSB_YI1*G))       # ISENSE (mitad inferior)
            p.append(('%d'%(k+11),x,RSB_YI2*G))      # ISENSE (mitad superior)
            p.append(('%d'%(k+16),x,RSB_YC*G))       # arriba: tierra de potencia
        return sorted(p,key=lambda t:int(t[0]))
    raise KeyError(kind)

# taladro por tipo de huella (mm); el resto usa DRILL
DRILL_OF={'TO220':1.0,'DIODE':1.3,'TERM2':1.3,'RSBANK':1.1}
def drill_of(kind): return DRILL_OF.get(kind,DRILL)

# cajas de cuerpo especiales (xmin,ymin,xmax,ymax) locales, en mm
BOX_OF={
 'TO220':(-3.0,-4.0,8.1,6.0),
 'TERM2':(-3.6,-5.2,8.7,5.6),
 'RSBANK':((RSB_XB-2)*G-1.0,-3.2,(RSB_COLS-1)*RSB_DX*G+3.6,RSB_YC*G+3.2),
}
def fp_box(kind):
    """caja de cuerpo (xmin,ymin,xmax,ymax) local, para evitar solapes"""
    if kind in BOX_OF: return BOX_OF[kind]
    p=fp_pads(kind); xs=[a[1] for a in p]; ys=[a[2] for a in p]
    m=2.54
    return (min(xs)-m,min(ys)-m,max(xs)+m,max(ys)+m)

def frozen_routes(parts):
    """Pistas fijas que forman parte de una huella (troncales del banco de sensado).
    Devuelve {red_local: {'nodes','edges'}} en celdas de la placa/módulo (capa 0)."""
    out={}
    def seg(net,i0,j0,i1,j1,R):
        di=(i1>i0)-(i1<i0); dj=(j1>j0)-(j1<j0)
        i,j=i0,j0
        while (i,j)!=(i1,j1):
            a=(0,i,j); b=(0,i+di,j+dj)
            R['edges'].add((a,b)); R['nodes'].add(a); R['nodes'].add(b)
            i,j=i+di,j+dj
        R['nodes'].add((0,i1,j1))
    for ref,p in parts.items():
        if p.kind!='RSBANK': continue
        i0=int(round(p.x/G)); j0=int(round(p.y/G))
        P=out.setdefault('PGND',{'nodes':set(),'edges':set()}); I=out.setdefault('ISENSE',{'nodes':set(),'edges':set()})
        xe=(RSB_COLS-1)*RSB_DX
        seg('PGND',i0+RSB_XB,j0+RSB_YA,i0+xe,j0+RSB_YA,P)
        seg('PGND',i0+RSB_XB,j0+RSB_YC,i0+xe,j0+RSB_YC,P)
        seg('PGND',i0+RSB_XB,j0+RSB_YA,i0+RSB_XB,j0+RSB_YC,P)
        seg('ISENSE',i0,j0+RSB_YT,i0+xe,j0+RSB_YT,I)
        for k in range(RSB_COLS):
            seg('ISENSE',i0+k*RSB_DX,j0+RSB_YI1,i0+k*RSB_DX,j0+RSB_YT,I)
            seg('ISENSE',i0+k*RSB_DX,j0+RSB_YI2,i0+k*RSB_DX,j0+RSB_YT,I)
    return out

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
