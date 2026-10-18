import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
from matplotlib.backends.backend_pdf import PdfPages
import collections
from engine import *
import netlist as N
from eagle import merge_edges

MARG=8.0   # mm de margen de página alrededor de la placa

def _fig(W,H):
    fig=plt.figure(figsize=((W+2*MARG)/25.4,(H+2*MARG)/25.4))
    ax=fig.add_axes([0,0,1,1]); ax.set_xlim(-MARG,W+MARG); ax.set_ylim(-MARG,H+MARG); ax.set_aspect('equal'); ax.axis('off')
    return fig,ax

PT=72/25.4   # puntos por mm

def copper_pdf(path,parts,routes,W,H,mirror=True):
    fig,ax=_fig(W,H)
    if mirror: ax.invert_xaxis()
    for net,rt in routes.items():
        for (x0,y0,x1,y1) in merge_edges(rt['edges'],0):
            ax.plot([x0,x1],[y0,y1],color='k',lw=TRACE*PT,solid_capstyle='round',zorder=2)
    holes=[]
    for ref,p in parts.items():
        for pin,(x,y) in p.pads().items(): holes.append((x,y))
    for rt in routes.values():
        for (i,j) in rt['vias']: holes.append((i*G,j*G))
    for (x,y) in set(holes):
        ax.add_patch(Circle((x,y),PAD_D/2,fc='k',ec='k',lw=0,zorder=3))
        ax.add_patch(Circle((x,y),0.25,fc='w',ec='w',lw=0,zorder=4))
    # contorno de corte (fino) y marcas de esquina
    ax.add_patch(Rectangle((0,0),W,H,fc='none',ec='k',lw=0.4,ls=(0,(3,2)),zorder=1))
    for (x,y) in ((0,0),(W,0),(0,H),(W,H)):
        sx=-1 if x==0 else 1; sy=-1 if y==0 else 1
        ax.plot([x,x+sx*5],[y,y],color='k',lw=0.4); ax.plot([x,x],[y,y+sy*5],color='k',lw=0.4)
    # regla de verificación 50 mm
    x0=W/2-25; 
    ax.plot([x0,x0+50],[-4.5,-4.5],color='k',lw=0.6); 
    for t in range(0,51,10): ax.plot([x0+t,x0+t],[-5.3,-3.7],color='k',lw=0.6)
    ax.text(W/2,-7.2,'Verificar: esta regla debe medir 50 mm  |  Impresión 1:1 (sin escalar), cara de cobre ESPEJADA' if mirror else 'Verificar 50 mm',ha='center',va='center',fontsize=5.5,zorder=6)
    fig.savefig(path,format='pdf'); plt.close(fig)

def assembly_pdf(path,parts,routes,W,H,nets):
    fig,ax=_fig(W,H)
    ax.add_patch(Rectangle((0,0),W,H,fc='#f6f3e8',ec='k',lw=0.8,zorder=0))
    # cobre inferior (fantasma)
    for net,rt in routes.items():
        for (x0,y0,x1,y1) in merge_edges(rt['edges'],0):
            ax.plot([x0,x1],[y0,y1],color='#c9c2a6',lw=TRACE*PT,solid_capstyle='round',zorder=1)
    # puentes
    jl=jumpers(parts,routes,nets)
    for k,jp in enumerate(jl,1):
        for (x0,y0,x1,y1) in jp['segs']:
            ax.plot([x0,x1],[y0,y1],color='#d62728',lw=1.2,solid_capstyle='round',zorder=5)
        mx,my=jp['label']
        ax.text(mx,my,'J%d'%k,fontsize=4.5,color='#d62728',ha='center',va='bottom',zorder=7,fontweight='bold')
    # componentes
    for ref,p in parts.items():
        loc=ref.split('_',1)[1]; val=N.PARTS[loc][1]
        x0,y0,x1,y1=p.box()
        pads=p.pads(); pts=list(pads.values())
        if p.kind=='DIP8':
            xs=[a for a,b in pts]; ys=[b for a,b in pts]
            ax.add_patch(Rectangle((min(xs)+1.3,min(ys)-1.3),max(xs)-min(xs)-2.6,max(ys)-min(ys)+2.6,fc='#222',ec='k',lw=0.5,zorder=2,alpha=0.85) if p.r%2==0 else Rectangle((min(xs)-1.3,min(ys)+1.3),max(xs)-min(xs)+2.6,max(ys)-min(ys)-2.6,fc='#222',ec='k',lw=0.5,zorder=2,alpha=0.85))
        elif p.kind=='RES':
            (ax1,ay1),(ax2,ay2)=pads['1'],pads['2']
            mx,my=(ax1+ax2)/2,(ay1+ay2)/2
            if p.r%2==0: ax.add_patch(Rectangle((mx-2.6,my-1.1),5.2,2.2,fc='#d9b77e',ec='k',lw=0.4,zorder=2))
            else: ax.add_patch(Rectangle((mx-1.1,my-2.6),2.2,5.2,fc='#d9b77e',ec='k',lw=0.4,zorder=2))
            ax.plot([ax1,ax2],[ay1,ay2],color='k',lw=0.4,zorder=1.5)
        elif p.kind in('CAP','POT','HDR1','HDR2','HDR4'):
            xs=[a for a,b in pts]; ys=[b for a,b in pts]
            ax.add_patch(Rectangle((min(xs)-1.4,min(ys)-1.4),max(xs)-min(xs)+2.8,max(ys)-min(ys)+2.8,fc='#8fb8d8' if p.kind!='CAP' else '#b9d89b',ec='k',lw=0.4,zorder=2,alpha=0.8))
        for pin,(x,y) in pads.items():
            sq=(pin=='1')
            ax.add_patch(Circle((x,y),PAD_D/2,fc='#d4a017',ec='k',lw=0.3,zorder=3))
            ax.add_patch(Circle((x,y),DRILL/2,fc='w',ec='k',lw=0.2,zorder=4))
        cx,cy=(x0+x1)/2,(y0+y1)/2
        ax.text(cx,cy,ref.replace('_',' ',1)+'\n'+val if p.kind!='RES' else ref.replace('_',' ',1)+' '+val,fontsize=3.4,ha='center',va='center',zorder=8,color='#0b3d91' if p.kind!='DIP8' else 'w')
        # marca pin 1
        x,y=pads['1']; ax.add_patch(Circle((x,y),PAD_D/2+0.5,fc='none',ec='#0b3d91',lw=0.5,zorder=6))
    # agujeros de fijación
    ax.text(W/2,-4,'Vista de ensamble (lado componentes)  |  rojo = puentes de alambre aislado en el lado componentes  |  1:1',ha='center',fontsize=5.5)
    fig.savefig(path,format='pdf'); plt.close(fig)
    return jl

def jumpers(parts,routes,nets):
    """componentes conexas de aristas en capa 1 -> puentes numerados"""
    padat={}
    for ref,p in parts.items():
        for pin,(x,y) in p.pads().items(): padat[(round(x/G),round(y/G))]=(ref,pin)
    out=[]
    for net,rt in routes.items():
        adj=collections.defaultdict(set)
        for a,b in rt['edges']:
            if a[0]==1: adj[a[1:]].add(b[1:]); adj[b[1:]].add(a[1:])
        seen=set()
        for s in list(adj):
            if s in seen: continue
            comp=[]; st=[s]; seen.add(s)
            while st:
                u=st.pop(); comp.append(u)
                for v in adj[u]:
                    if v not in seen: seen.add(v); st.append(v)
            ends=[u for u in comp if len(adj[u])==1 or u in padat or any(u==v for v in rt['vias'])]
            nedges=sum(len(adj[u]) for u in comp)//2
            segs=merge_edges([((1,)+u,(1,)+v) for u in comp for v in adj[u]],1)
            pts=sorted(ends)
            def desc(u):
                if u in padat: return '%s.%s'%padat[u]
                best=min(padat,key=lambda q:(q[0]-u[0])**2+(q[1]-u[1])**2)
                return 'agujero (%.1f; %.1f) mm, junto a %s.%s'%(u[0]*G,u[1]*G,padat[best][0],padat[best][1])
            endpts=[u for u in comp if len(adj[u])==1] or comp[:2]
            # endpoints reales: nodos de grado 1 (o pads)
            lab=(sum(u[0] for u in comp)/len(comp)*G,max(u[1] for u in comp)*G+0.6)
            out.append(dict(net=net,comp=comp,segs=segs,ends=[desc(u) for u in sorted(endpts)],length=nedges*G,label=lab))
    out.sort(key=lambda j:(j['label'][1]*-1,j['label'][0]))
    return out
