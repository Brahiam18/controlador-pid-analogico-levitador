"""Ensambla 4 módulos idénticos en una placa y conecta los rieles compartidos."""
import heapq, pickle, collections
from engine import *
import netlist as N

NMOD=4
class Board: pass

def module_data(sel):
    parts={k:Placed(k,v[0],v[1],v[2],v[3]) for k,v in sel['parts'].items()}
    return parts,sel['routes']

def assemble(sel,gap_x=8*PITCH, gap_y=5*PITCH, margin=3*PITCH):
    """devuelve parts (con prefijo), routes (por red global), W,H"""
    wc,hc=sel['wc'],sel['hc']
    MW,MH=wc*PITCH,hc*PITCH
    W=margin*2+2*MW+gap_x; H=margin*2+2*MH+gap_y
    mparts,mroutes=module_data(sel)
    parts={}; routes=collections.defaultdict(lambda:{'edges':set(),'vias':set(),'nodes':set()})
    offs=[]
    k=0
    for row in (1,0):          # fila superior = P1,P2 ; inferior = P3,P4
        for col in (0,1):
            k+=1
            ox=margin+col*(MW+gap_x); oy=margin+row*(MH+gap_y)
            offs.append((k,ox,oy))
    di=lambda v:int(round(v/G))
    for k,ox,oy in offs:
        pre='P%d_'%k
        for ref,p in mparts.items():
            parts[pre+ref]=Placed(pre+ref,p.kind,p.x+ox,p.y+oy,p.r)
        oi,oj=di(ox),di(oy)
        for net,rt in mroutes.items():
            gname=net if net in N.SHARED else pre+net
            R=routes[gname]
            for a,b in rt['edges']:
                R['edges'].add(((a[0],a[1]+oi,a[2]+oj),(b[0],b[1]+oi,b[2]+oj)))
            for (i,j) in rt['vias']: R['vias'].add((i+oi,j+oj))
            for (l,i,j) in rt['nodes']: R['nodes'].add((l,i+oi,j+oj))
    return parts,dict(routes),W,H

def global_nets():
    nets={}
    for k in range(1,NMOD+1):
        pre='P%d_'%k
        for net,pins in N.NETS.items():
            gname=net if net in N.SHARED else pre+net
            nets.setdefault(gname,[]).extend((pre+r,p) for r,p in pins)
    return nets

def connect_shared(parts,routes,W,H,nets,jump_cost=40,top_cost=6.0,via_cost=10):
    g=Grid(W,H)
    padnet={}
    for name,pins in nets.items():
        for ref,pin in pins: padnet[(ref,pin)]=name
    padnodes=set()
    for ref,p in parts.items():
        for pin,(x,y) in p.pads().items():
            net=padnet.get((ref,pin),'NC_%s_%s'%(ref,pin)); i,j=g.idx(x,y); g.add_pad(i,j,net); padnodes.add((i,j))
    # trazas congeladas -> propiedad dura
    for net,rt in routes.items():
        for (l,i,j) in rt['nodes']: g.own[l][(i,j)]=net
        for (i,j) in rt['vias']: g.add_pad(i,j,net)
    # nodos de cada red: separar en componentes conexas (por módulo)
    log={}
    for net in sorted(N.SHARED):
        rt=routes[net]
        # componentes: conectividad de edges + pads
        adj=collections.defaultdict(set)
        for a,b in rt['edges']:
            adj[a].add(b); adj[b].add(a)
        for (i,j) in set(v for v in rt['vias']):
            adj[(0,i,j)].add((1,i,j)); adj[(1,i,j)].add((0,i,j))
        pads=[]
        for ref,pin in nets[net]:
            x,y=parts[ref].pads()[pin]; i,j=g.idx(x,y); pads.append((i,j)); adj[(0,i,j)]; adj[(1,i,j)].add((0,i,j)); adj[(0,i,j)].add((1,i,j))
        seen={}; comps=[]
        for n0 in list(adj):
            if n0 in seen: continue
            comp=set(); st=[n0]; seen[n0]=len(comps)
            while st:
                u=st.pop(); comp.add(u)
                for v in adj[u]:
                    if v not in seen: seen[v]=len(comps); st.append(v)
            comps.append(comp)
        # solo componentes con pads de la red
        padcomp={}
        for (i,j) in pads:
            padcomp[(i,j)]=seen[(0,i,j)]
        cids=sorted(set(padcomp.values()))
        merged=set(comps[cids[0]]); rest=[comps[c] for c in cids[1:]]
        new_edges=set(); new_vias=set(); new_nodes=set()
        while rest:
            # Dijkstra desde 'merged' hasta cualquiera de 'rest'
            targ={}
            for ci,c in enumerate(rest):
                for n in c: targ[n]=ci
            dist={}; prev={}; pq=[]
            for n in merged: dist[n]=0.0; heapq.heappush(pq,(0.0,n))
            found=None
            while pq:
                d,u=heapq.heappop(pq)
                if d>dist.get(u,1e18): continue
                if u in targ: found=u; break
                l,i,j=u
                for di_,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    v=(l,i+di_,j+dj)
                    if not g.free(l,v[1],v[2],net): continue
                    nd=d+(1.0 if l==0 else top_cost)
                    if nd<dist.get(v,1e18): dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd,v))
                ispad=(i,j) in padnodes and g.own[0].get((i,j))==net
                if ispad or g.via_ok(i,j,net):
                    v=(1-l,i,j); nd=d+(0 if ispad else via_cost)+(jump_cost if l==0 else 0)
                    if nd<dist.get(v,1e18): dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd,v))
            if not found: raise RuntimeError('no se pudo conectar '+net)
            path=[found]; u=found
            while u not in merged:
                u=prev[u]; path.append(u)
            path.reverse()
            for a,b in zip(path,path[1:]):
                if a[0]==b[0]: new_edges.add((a,b))
                else:
                    new_vias.add((a[1],a[2]))
            for n in path:
                g.own[n[0]][(n[1],n[2])]=net; new_nodes.add(n)
            for a,b in zip(path,path[1:]):
                if a[0]!=b[0]: g.add_pad(a[1],a[2],net)
            ci=targ[found]; merged|=rest.pop(ci); merged|=set(path)
        routes[net]['edges']|=new_edges; routes[net]['vias']|=new_vias; routes[net]['nodes']|=new_nodes
        log[net]=(len(new_edges),len(new_vias))
    return log
