import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
from matplotlib.backends.backend_pdf import PdfPages
import collections, math
from engine import *
import netlist as N
from assemble import NMOD
from eagle import merge_edges
from matplotlib.patches import Polygon as MPoly

MARG=8.0   # mm de margen de página alrededor de la placa

PAGE=(210.0,279.0)   # hoja que entra en A4 y en Carta sin escalar; la placa va arriba y centrada
def _fig(W,H,page=PAGE):
    PW,PH=page
    fig=plt.figure(figsize=(PW/25.4,PH/25.4))
    ax=fig.add_axes([0,0,1,1]); ax.set_xlim(W/2-PW/2,W/2+PW/2); ax.set_ylim(H+MARG+4-PH,H+MARG+4); ax.set_aspect('equal'); ax.axis('off')
    return fig,ax

PT=72/25.4   # puntos por mm

def copper_pdf(path,parts,routes,W,H,mirror=True):
    fig,ax=_fig(W,H)
    if mirror: ax.invert_xaxis()
    for net,rt in routes.items():
        for (x0,y0,x1,y1) in merge_edges(rt['edges'],0):
            ax.plot([x0,x1],[y0,y1],color='k',lw=N.width_of(net)*PT,solid_capstyle='round',zorder=2)
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

def _draw_assembly(ax,parts,routes,nets,jitems,fs=3.4,short=False,jfs=4.5):
    # cobre inferior (fantasma)
    for net,rt in routes.items():
        for (x0,y0,x1,y1) in merge_edges(rt['edges'],0):
            ax.plot([x0,x1],[y0,y1],color='#c9c2a6',lw=N.width_of(net)*PT,solid_capstyle='round',zorder=1)
    # puentes
    for k,jp in jitems:
        for (x0,y0,x1,y1) in jp['segs']:
            ax.plot([x0,x1],[y0,y1],color='#d62728',lw=1.2,solid_capstyle='round',zorder=5)
        mx,my=jp['label']
        ax.text(mx,my,'J%d'%k,fontsize=jfs,color='#d62728',ha='center',va='bottom',zorder=7,fontweight='bold')
    # componentes
    for ref,p in parts.items():
        loc=ref.split('_',1)[1]; val=N.PARTS[loc][1]
        name=loc if short else ref.replace('_',' ',1)
        x0,y0,x1,y1=p.box()
        pads=p.pads(); pts=list(pads.values())
        if p.kind.startswith('DIP'):
            xs=[a for a,b in pts]; ys=[b for a,b in pts]
            ax.add_patch(Rectangle((min(xs)+1.3,min(ys)-1.3),max(xs)-min(xs)-2.6,max(ys)-min(ys)+2.6,fc='#222',ec='k',lw=0.5,zorder=2,alpha=0.85) if p.r%2==0 else Rectangle((min(xs)-1.3,min(ys)+1.3),max(xs)-min(xs)+2.6,max(ys)-min(ys)-2.6,fc='#222',ec='k',lw=0.5,zorder=2,alpha=0.85))
        elif p.kind=='RES':
            (ax1,ay1),(ax2,ay2)=pads['1'],pads['2']
            mx,my=(ax1+ax2)/2,(ay1+ay2)/2
            if p.r%2==0: ax.add_patch(Rectangle((mx-2.6,my-1.1),5.2,2.2,fc='#d9b77e',ec='k',lw=0.4,zorder=2))
            else: ax.add_patch(Rectangle((mx-1.1,my-2.6),2.2,5.2,fc='#d9b77e',ec='k',lw=0.4,zorder=2))
            ax.plot([ax1,ax2],[ay1,ay2],color='k',lw=0.4,zorder=1.5)
        elif p.kind in('TO220','DIODE','DIODE_S','TERM2','RSBANK'):
            def poly(x0_,y0_,x1_,y1_,fc,ec='k',z=2,lw=0.4):
                q=[rot(a_,b_,p.r) for a_,b_ in ((x0_,y0_),(x1_,y0_),(x1_,y1_),(x0_,y1_))]
                ax.add_patch(MPoly([(p.x+a_,p.y+b_) for a_,b_ in q],closed=True,fc=fc,ec=ec,lw=lw,zorder=z))
            if p.kind=='TO220':
                poly(-2.56,1.4,7.64,5.9,'#6b6b6b'); poly(-2.56,5.0,7.64,5.9,'#222')
            elif p.kind=='DIODE':
                poly(2.87,-2.7,12.37,2.7,'#222'); poly(10.4,-2.7,11.4,2.7,'#e8e8e8',ec='none',z=2.1)
            elif p.kind=='DIODE_S':
                poly(2.0,-1.1,5.6,1.1,'#d98c2b'); poly(4.7,-1.1,5.3,1.1,'#222',ec='none',z=2.1)
            elif p.kind=='TERM2':
                poly(-2.54,-3.8,7.62,4.4,'#2a6fb0')
            else:
                for k_ in range(RSB_COLS):
                    yc=RSB_YI*G/2; poly(k_*RSB_DX*G-4.75,yc-11.0,k_*RSB_DX*G+4.75,yc+11.0,'#d9b77e')
        elif p.kind in('CAP','POT','HDR1','HDR2','HDR4'):
            xs=[a for a,b in pts]; ys=[b for a,b in pts]
            ax.add_patch(Rectangle((min(xs)-1.4,min(ys)-1.4),max(xs)-min(xs)+2.8,max(ys)-min(ys)+2.8,fc='#8fb8d8' if p.kind!='CAP' else '#b9d89b',ec='k',lw=0.4,zorder=2,alpha=0.8))
        for pin,(x,y) in pads.items():
            ax.add_patch(Circle((x,y),PAD_D/2,fc='#d4a017',ec='k',lw=0.3,zorder=3))
            ax.add_patch(Circle((x,y),DRILL/2,fc='w',ec='k',lw=0.2,zorder=4))
        cx,cy=(x0+x1)/2,(y0+y1)/2
        if p.kind=='RSBANK':
            cx,cy=p.x+rot((RSB_COLS-1)*RSB_DX*G/2,RSB_YI*G/2,p.r)[0],p.y+rot((RSB_COLS-1)*RSB_DX*G/2,RSB_YI*G/2,p.r)[1]
        ax.text(cx,cy,name+'\n'+val if p.kind!='RES' else name+' '+val,fontsize=fs,ha='center',va='center',zorder=8,color='#0b3d91' if not p.kind.startswith('DIP') else 'w')
        # marca pin 1
        x,y=pads['1']; ax.add_patch(Circle((x,y),PAD_D/2+0.5,fc='none',ec='#0b3d91',lw=0.5,zorder=6))
    # nombre de cada pin de regletas, borneras, transistor y diodos
    PINLAB={'J_PWR':('+16V','-16V','GND','+5V'),'J_IN':('VSEN',),'J_OUT':('VPID',),'J_COIL':('BOB+','BOB-'),
            'J_VBOB':('+VBOB','PGND'),'JP_GND':('GND','PGND'),'Q1':('B','C','E'),'D1':('A','K'),'D2':('A','K')}
    for ref,p in parts.items():
        loc=ref.split('_',1)[1]
        if loc not in PINLAB: continue
        pads=p.pads()
        for pin,txt in zip(sorted(pads,key=int),PINLAB[loc]):
            x,y=pads[pin]
            ax.text(x,y+2.0,txt,fontsize=fs*0.8,rotation=90,ha='center',va='bottom',color='#8b0000',fontweight='bold',zorder=9)
    # etapas U1..U8 sobre el cuerpo de cada TL074 (en la fila del pin de salida)
    for ref,p in parts.items():
        if not p.kind.startswith('DIP'): continue
        k,ic=ref.split('_',1)
        pads=p.pads(); xs=[a for a,b in pads.values()]; ys=[b for a,b in pads.values()]
        cx,cy=sum(xs)/len(xs),sum(ys)/len(ys)
        for (ic_,pin),stage in N.chan_labels().items():
            if ic_!=ic: continue
            x,y=pads[pin]
            tx,ty,rt=(cx+(x-cx)*0.33,y,0) if p.r%2==0 else (x,cy+(y-cy)*0.33,90)
            ax.text(tx,ty,stage,fontsize=fs*1.3,fontweight='bold',color='k',ha='center',va='center',rotation=rt,zorder=9,
                    bbox=dict(boxstyle='round,pad=0.12',fc='#ffd54a',ec='none'))

def _leyenda():
    pines={}
    for (ic,pin),st in N.chan_labels().items(): pines.setdefault(ic,[]).append((int(pin),st))
    t1='   '.join('%s: '%ic+', '.join('pin %d = %s'%(a,b) for a,b in sorted(v)) for ic,v in sorted(pines.items()))
    t2='U1 diferenciador de error · U2 P · U3 I · U4 D · U5 sumador · U6 Vref · U7 Voff · U8 convertidor V-I (potencia)'
    return t1,t2

def assembly_pdf(path,parts,routes,W,H,nets):
    jl=jumpers(parts,routes,nets)
    jall=list(enumerate(jl,1))
    t1,t2=_leyenda()
    with PdfPages(path) as pdf:
        # pagina 1: placa completa 1:1
        fig,ax=_fig(W,H)
        ax.add_patch(Rectangle((0,0),W,H,fc='#f6f3e8',ec='k',lw=0.8,zorder=0))
        _draw_assembly(ax,parts,routes,nets,jall)
        ax.text(W/2,-3.2,'Vista de ensamble (lado componentes)  |  rojo = puentes de alambre aislado en el lado componentes  |  1:1',ha='center',fontsize=5.5)
        ax.text(W/2,-5.2,'Cuadro amarillo = amplificador del TL074 (U1..U8 del informe), en la fila de su pin de salida',ha='center',fontsize=4.6)
        ax.text(W/2,-6.9,t2,ha='center',fontsize=4.2)
        pdf.savefig(fig); plt.close(fig)
        # paginas 2-5: cada PID ampliado
        PW,PH=210.0,297.0
        for k in range(1,NMOD+1):
            pk={r:q for r,q in parts.items() if r.startswith('P%d_'%k)}
            bx=[q.box() for q in pk.values()]
            x0=min(b[0] for b in bx); y0=min(b[1] for b in bx); x1=max(b[2] for b in bx); y1=max(b[3] for b in bx)
            z=min((PW-10)/(x1-x0),(PH-30)/(y1-y0)); z=math.floor(z*20)/20
            fig=plt.figure(figsize=(PW/25.4,PH/25.4)); ax=fig.add_axes([0,0,1,1])
            cx=(x0+x1)/2; cy=(y0+y1)/2-1.0
            ax.set_xlim(cx-PW/2/z,cx+PW/2/z); ax.set_ylim(cy-PH/2/z,cy+PH/2/z); ax.set_aspect('equal'); ax.axis('off')
            ax.add_patch(Rectangle((x0-2,y0-2),x1-x0+4,y1-y0+4,fc='#f6f3e8',ec='k',lw=0.6,zorder=0))
            ji=[(n,jp) for n,jp in jall if x0-2<=jp['label'][0]<=x1+2 and y0-2<=jp['label'][1]<=y1+2]
            fsz=3.4+(z-1)*1.0
            _draw_assembly(ax,pk,routes,nets,ji,fs=fsz,short=True,jfs=4.5+(z-1)*1.0)
            top=cy+PH/2/z
            ax.text(cx,top-5/z,'PID %d  |  vista de ensamble (lado componentes)  |  escala %.2f:1'%(k,z),ha='center',va='center',fontsize=9,fontweight='bold')
            ax.text(cx,top-10/z,'Cuadro amarillo = amplificador U1..U8 del informe sobre el TL074 (pin 1 = círculo azul)',ha='center',va='center',fontsize=6)
            bot=cy-PH/2/z
            ax.text(cx,bot+9/z,t1,ha='center',va='center',fontsize=5.2)
            ax.text(cx,bot+5/z,t2,ha='center',va='center',fontsize=5.2)
            pdf.savefig(fig); plt.close(fig)
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
