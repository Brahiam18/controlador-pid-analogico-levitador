import heapq, random, collections, time
from engine import *

DIRS=((1,0),(-1,0),(0,1),(0,-1))
DIAG=((1,1),(1,-1),(-1,1),(-1,-1))

class PF:
    def __init__(s,W,H,parts,nets,jump_cost=35,via_cost=10,top_cost=3.0,bend=0.4):
        s.g=Grid(W,H); s.W=W; s.H=H
        s.jump_cost=jump_cost; s.via_cost=via_cost; s.top_cost=top_cost; s.bend=bend
        pad_net={}
        for name,pins in nets.items():
            for ref,pin in pins: pad_net[(ref,pin)]=name
        s.pads={}      # net -> [(i,j)]
        s.padset=set()
        for ref,p in parts.items():
            for pin,(x,y) in p.pads().items():
                net=pad_net.get((ref,pin),'NC_%s_%s'%(ref,pin))
                i,j=s.g.idx(x,y); s.g.add_pad(i,j,net); s.pads.setdefault(net,[]).append((i,j)); s.padset.add((i,j))
        s.nets=[n for n in s.pads if len(set(s.pads[n]))>=2]
        s.occ=[collections.defaultdict(set),collections.defaultdict(set)]
        s.shadow=[collections.defaultdict(set),collections.defaultdict(set)]
        s.hist=[collections.defaultdict(float),collections.defaultdict(float)]
        s.vdiag=collections.defaultdict(set)
        s.routes={}
        s.pf=0.6
    # --- consultas estáticas
    def sfree(s,l,i,j,net):
        g=s.g
        if not(0<=i<g.nx and 0<=j<g.ny): return False
        o=g.own[l].get((i,j))
        if o is not None and o!=net: return False
        r=g.res[l].get((i,j))
        if r is not None and r!=net: return False
        return True
    def users(s,l,n,net):
        u=s.occ[l].get(n); sh=s.shadow[l].get(n)
        c=0
        if u: c+=len(u-{net}) if net in u else len(u)
        if sh: c+=len(sh-{net}) if net in sh else len(sh)
        return c
    def ncost(s,l,n,net):
        base=1.0 if l==0 else s.top_cost
        return base+s.hist[l].get(n,0.0)+s.pf*s.users(l,n,net)*3
    # --- ripup / add
    def rip(s,net):
        r=s.routes.pop(net,None)
        if not r: return
        for (l,i,j) in r['nodes']:
            s.occ[l][(i,j)].discard(net)
        for (i,j) in r['vias']:
            for l in (0,1):
                for di,dj in DIRS: s.shadow[l][(i+di,j+dj)].discard(net)
            for di,dj in DIAG: s.vdiag[(i+di,j+dj)].discard(net)
    def add(s,net,r):
        s.routes[net]=r
        for (l,i,j) in r['nodes']: s.occ[l][(i,j)].add(net)
        for (i,j) in r['vias']:
            for l in (0,1):
                for di,dj in DIRS: s.shadow[l][(i+di,j+dj)].add(net)
            for di,dj in DIAG: s.vdiag[(i+di,j+dj)].add(net)
    # --- ruteo de una red (árbol por Dijkstra/A* sucesivos)
    def route(s,net,rng):
        pads=list(dict.fromkeys(s.pads[net]))
        nodes=set(); edges=set(); vias=set()
        tree={}
        f=pads[0]
        tree[(0,)+f]=0.0; tree[(1,)+f]=s.jump_cost
        nodes.add((0,)+f); nodes.add((1,)+f)
        remaining=pads[1:]
        while remaining:
            tg={}
            for p in remaining: tg[(0,)+p]=p; tg[(1,)+p]=p
            tl=list(remaining)
            def h(i,j): return min(abs(i-a)+abs(j-b) for a,b in tl)
            dist={}; prev={}; pq=[]
            for t,c in tree.items():
                dist[t]=c; heapq.heappush(pq,(c+h(t[1],t[2]),c,t,None))
            found=None
            while pq:
                f_,d,u,pd=heapq.heappop(pq)
                if d>dist.get(u,1e18): continue
                if u in tg: found=u; break
                l,i,j=u
                for k,(di,dj) in enumerate(DIRS):
                    ni,nj=i+di,j+dj
                    if not s.sfree(l,ni,nj,net): continue
                    v=(l,ni,nj)
                    c=s.ncost(l,(ni,nj),net)+rng.random()*0.15
                    if pd is not None and pd!=k: c+=s.bend
                    nd=d+c
                    if nd<dist.get(v,1e18):
                        dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd+h(ni,nj),nd,v,k))
                # cambio de capa
                ispad=(i,j) in s.padset and s.g.own[0].get((i,j))==net
                diag_ok=True
                if not ispad:
                    for di,dj in DIAG:
                        o=s.g.own[0].get((i+di,j+dj))
                        if o is not None and o!=net: diag_ok=False; break
                if (ispad or (diag_ok and s.sfree(0,i,j,net) and s.sfree(1,i,j,net))):
                    v=(1-l,i,j)
                    vd=len(s.vdiag.get((i,j),set())-{net}) if not ispad else 0
                    nd=d+(0 if ispad else s.via_cost)+(s.jump_cost if l==0 else 0)+s.pf*(s.users(1-l,(i,j),net)+vd)*3
                    if nd<dist.get(v,1e18):
                        dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd+h(i,j),nd,v,None))
            if not found: return None
            path=[found]; u=found
            while u not in tree or (dist[u]!=tree[u]):
                u=prev[u]; path.append(u)
                if u in tree and dist[u]==tree[u]: break
            path.reverse()
            for a,b in zip(path,path[1:]):
                if a[0]==b[0]: edges.add((a,b))
                else: vias.add((a[1],a[2]))
            for n in path:
                nodes.add(n); tree[n]=0.0
            for (i,j) in [(p[1],p[2]) for p in path if (p[1],p[2]) in vias]:
                tree[(0,i,j)]=0.0; tree[(1,i,j)]=s.jump_cost
                nodes.add((0,i,j)); nodes.add((1,i,j))
            e=path[-1]; tree[(0,e[1],e[2])]=0.0; tree[(1,e[1],e[2])]=s.jump_cost
            nodes.add((0,e[1],e[2])); nodes.add((1,e[1],e[2]))
            remaining=[p for p in remaining if p!=tg[found]]
        return {'nodes':nodes,'edges':edges,'vias':vias}
    def conflicts(s):
        c=0; bad=[]
        for l in (0,1):
            for n,u in s.occ[l].items():
                if len(u)>1: c+=1; bad.append((l,n))
            for n,sh in s.shadow[l].items():
                u=s.occ[l].get(n,set())
                if sh and (u-sh or len(sh)>1): c+=1; bad.append((l,n))
        # vias/pads vecinos en diagonal de redes distintas
        vp={}
        for net,r in s.routes.items():
            for v in r['vias']: vp.setdefault(v,set()).add(net)
        for (i,j),nets in vp.items():
            for di,dj in DIAG:
                o=vp.get((i+di,j+dj))
                if o and (o-nets or len(nets)>1) and not (o<=nets and len(nets)==1):
                    c+=1; bad.append((0,(i,j))); bad.append((1,(i,j)))
        return c,bad
    def solve(s,iters=40,seed=0,verbose=False,order=None):
        rng=random.Random(seed)
        nets=list(s.nets) if order is None else order
        t0=time.time()
        for it in range(iters):
            rng.shuffle(nets) if it>0 else None
            for net in nets:
                s.rip(net)
                r=s.route(net,rng)
                if r is None: return False
                s.add(net,r)
            c,bad=s.conflicts()
            jumps=sum(1 for n,r in s.routes.items() for (l,i,j) in r['nodes'] if False)
            if verbose: print('iter',it,'conf',c,round(time.time()-t0,1))
            if c==0: return True
            for (l,n) in bad: s.hist[l][n]+=0.8
            s.pf=min(s.pf*1.12,25)
        return False
