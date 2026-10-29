import math, random, heapq, itertools
G=1.27           # paso de rejilla de ruteo (mm)
PITCH=2.54
PAD_D=2.0; DRILL=0.9; TRACE=0.7; CLEAR=0.4

def rot(x,y,r):
    r%=4
    for _ in range(r): x,y=-y,x     # 90° antihorario
    return x,y

# huellas: lista de (pin, x, y) en mm, en coordenadas locales (origen = pin 1)
RSB_COLS=3; RSB_DX=8     # banco de sensado: 3 resistencias de 5 W en una fila, separadas 8 celdas (10.16 mm)
RSB_YA=0; RSB_YI=20; RSB_YT=RSB_YI   # pads de tierra de potencia abajo (y=0) y de ISENSE arriba (y=20 celdas = 25.4 mm, largo de la resistencia)

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
            p.append(('%d'%(k+1),x,RSB_YA*G))                # abajo: tierra de potencia (PGND)
            p.append(('%d'%(k+1+RSB_COLS),x,RSB_YI*G))       # arriba: ISENSE (emisor del TIP122)
        return sorted(p,key=lambda t:int(t[0]))
    # ---- huellas agregadas para la fuente ----
    SIMPLE2={'RES10':10.16,'RES1W':15.24,'RES2W':20.32,'RES3W':25.4,'RES5W':27.94,'DO41':10.16,'DO35':7.62,
             'CPOL25':10.16,'CPOL35':10.16,'CPOL8':3.81,'CPOL6':2.54,'CPOL5':2.54,'CTANT':2.54,'LED5':2.54,'FUSE':22.86}
    if kind in SIMPLE2: return [('1',0,0),('2',SIMPLE2[kind],0)]
    if kind=='TERM3': return [('%d'%i,(i-1)*5.08,0) for i in range(1,4)]
    if kind in ('TO92','TRIM','HDR3','TO126'): return [('1',0,0),('2',PITCH,0),('3',2*PITCH,0)]
    if kind=='TERM4': return [('%d'%i,(i-1)*5.08,0) for i in range(1,5)]
    raise KeyError(kind)

# taladro por tipo de huella (mm); el resto usa DRILL
DRILL_OF={'TERM3':1.3,'RES5W':1.1,'CPOL35':1.3,'TO126':1.0,'TO220':1.0,'DIODE':1.3,'TERM2':1.3,'RSBANK':1.1,'TERM4':1.3,'FUSE':1.3,'DO41':1.0,'CPOL25':1.3,'RES1W':1.0,'RES2W':1.0,'RES3W':1.1}
def drill_of(kind): return DRILL_OF.get(kind,DRILL)
BIG_PADS=('TERM2','TERM3','TERM4','FUSE','CPOL25','CPOL35','DIODE','RES5W')
def pad_d(kind): return 2.6 if kind in BIG_PADS else PAD_D

# cajas de cuerpo especiales (xmin,ymin,xmax,ymax) locales, en mm
BOX_OF={
 'TO220':(-3.0,-4.0,8.1,6.0),
 'TERM2':(-3.6,-5.2,8.7,5.6),
 'RSBANK':(-5.5,-3.2,(RSB_COLS-1)*RSB_DX*G+5.5,RSB_YI*G+3.2),
 'TERM4':(-3.6,-5.2,18.84,5.6),
 'TERM3':(-3.6,-5.2,13.76,5.6),
 'CPOL35':(5.08-18.0,-18.0,5.08+18.0,18.0),
 'CPOL8':(1.905-4.4,-4.4,1.905+4.4,4.4),
 'RES5W':(-1.5,-5.2,29.44,5.2),
 'TO126':(-2.6,-1.6,7.68,3.4),
 'CPOL25':(5.08-14.0,-14.0,5.08+14.0,14.0),
 'CPOL6':(1.27-3.5,-3.5,1.27+3.5,3.5),
 'CPOL5':(1.27-3.0,-3.0,1.27+3.0,3.0),
 'CTANT':(-1.6,-2.4,4.14,2.4),
 'LED5':(1.27-3.1,-3.1,1.27+3.1,3.1),
 'TRIM':(-2.3,-3.2,7.4,2.2),
 'TO92':(-1.6,-2.6,6.7,2.0),
 'FUSE':(-3.0,-4.0,25.86,4.0),
 'RES3W':(-1.5,-3.6,26.9,3.6),
 'RES2W':(-1.5,-3.0,21.8,3.0),
 'RES1W':(-1.5,-2.6,16.7,2.6),
 'DO41':(-1.5,-2.2,11.7,2.2),
}
def fp_box(kind):
    """caja de cuerpo (xmin,ymin,xmax,ymax) local, para evitar solapes"""
    if kind in BOX_OF: return BOX_OF[kind]
    p=fp_pads(kind); xs=[a[1] for a in p]; ys=[a[2] for a in p]
    m=2.54
    return (min(xs)-m,min(ys)-m,max(xs)+m,max(ys)+m)

def frozen_routes(parts):
    """Pistas fijas que forman parte de una huella (troncales del banco de sensado):
    una barra de PGND por los pads inferiores y otra de ISENSE por los superiores.
    Se calculan con las coordenadas reales de los pads, así que valen con cualquier giro."""
    out={}
    def seg(i0,j0,i1,j1,R):
        di=(i1>i0)-(i1<i0); dj=(j1>j0)-(j1<j0)
        i,j=i0,j0
        R['nodes'].add((0,i,j))
        while (i,j)!=(i1,j1):
            a=(0,i,j); b=(0,i+di,j+dj)
            R['edges'].add((a,b)); R['nodes'].add(a); R['nodes'].add(b)
            i,j=i+di,j+dj
    for ref,p in parts.items():
        if p.kind!='RSBANK': continue
        pads=p.pads()
        for net,pins in (('PGND',range(1,RSB_COLS+1)),('ISENSE',range(RSB_COLS+1,2*RSB_COLS+1))):
            R=out.setdefault(net,{'nodes':set(),'edges':set()})
            pts=sorted((int(round(pads[str(k)][0]/G)),int(round(pads[str(k)][1]/G))) for k in pins)
            for a_,b_ in zip(pts,pts[1:]): seg(a_[0],a_[1],b_[0],b_[1],R)
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
