"""Guía de conexiones por colores: cada red (conjunto de pads que deben quedar unidos) con un color."""
import sys, json, math, collections
sys.path.insert(0,'.')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.backends.backend_pdf import PdfPages
import netlist as N, assemble as A, build as B, pdfs
from engine import *
from eagle import merge_edges

FIJOS={'GND':'#000000','+16V':'#e41a1c','-16V':'#1f4fd8','+5V':'#ff7f00','PGND':'#8b5a2b','+VBOB':'#d6006e',
       'ISENSE':'#7a3d00','COILN':'#00897b','IOUT':'#6a3d9a','BASE':'#6a3d9a'}
PAL=['#2ca02c','#17becf','#9467bd','#bcbd22','#e377c2','#8c564b','#0b7a75','#ff9896','#aec7e8','#98df8a','#c49c94','#f781bf',
     '#4daf4a','#984ea3','#a65628','#377eb8','#999900','#00bfa0','#d95f02','#7570b3','#66a61e','#e7298a','#1b9e77','#a6761d']

def colores(nets):
    base=sorted({n.split('_',1)[1] if n.startswith('P') and n[1:2].isdigit() else n for n in nets})
    col={}; i=0
    for b in base:
        if b in FIJOS: col[b]=FIJOS[b]
        else: col[b]=PAL[i%len(PAL)]; i+=1
    return col

def base(n): return n.split('_',1)[1] if n.startswith('P') and n[1:2].isdigit() else n

def main(src='modulo_ruteado.json',out='salida/guia_colores_conexiones.pdf'):
    js=json.load(open(src)); N.set_assign(js.get('assign','a1'))
    parts,routes,W,H,nets=B.build(src,'salida') if False else (None,)*5
    import os; os.makedirs('salida',exist_ok=True)
    parts,routes,W,H,nets=B.build(src,'salida')
    import puentes
    jl=pdfs.jumpers(parts,routes,nets)
    col=colores(nets)
    padnet={}
    for n,pins in nets.items():
        for r,p in pins: padnet[(r,p)]=n
    ipe=sorted(col)
    with PdfPages(out) as pdf:
        for k in range(1,A.NMOD+1):
            pk={r:q for r,q in parts.items() if r.startswith('P%d_'%k)}
            bx=[q.box() for q in pk.values()]
            x0=min(b[0] for b in bx); y0=min(b[1] for b in bx); x1=max(b[2] for b in bx); y1=max(b[3] for b in bx)
            PW,PH=210.0,297.0
            z=min((PW-8)/(x1-x0),(PH-70)/(y1-y0)); z=math.floor(z*20)/20
            fig=plt.figure(figsize=(PW/25.4,PH/25.4)); ax=fig.add_axes([0,0,1,1])
            cx=(x0+x1)/2; cy=(y0+y1)/2-14
            ax.set_xlim(cx-PW/2/z,cx+PW/2/z); ax.set_ylim(cy-PH/2/z,cy+PH/2/z); ax.set_aspect('equal'); ax.axis('off')
            ax.add_patch(Rectangle((x0-2,y0-2),x1-x0+4,y1-y0+4,fc='#fbfaf4',ec='k',lw=0.6,zorder=0))
            clip=Rectangle((x0-2,y0-2),x1-x0+4,y1-y0+4,transform=ax.transData)
            # pistas (cobre) y puentes en color de su red
            for net,rt in routes.items():
                if not net.startswith('P%d_'%k) and net not in N.SHARED: continue
                c=col[base(net)]
                for (xa,ya,xb,yb) in merge_edges(rt['edges'],0):
                    if x0-3<=xa<=x1+3 and y0-3<=ya<=y1+3:
                        ax.plot([xa,xb],[ya,yb],color=c,lw=N.width_of(net)*pdfs.PT*z*0.9,solid_capstyle='round',zorder=1,alpha=0.55)[0].set_clip_path(clip)
            for j in jl:
                if not (x0-2<=j['label'][0]<=x1+2 and y0-2<=j['label'][1]<=y1+2): continue
                c=col[base(j['net'])]
                for (xa,ya,xb,yb) in j['segs']:
                    ax.plot([xa,xb],[ya,yb],color=c,lw=1.6*z*0.9,solid_capstyle='round',zorder=5,ls=(0,(2,1.2)))[0].set_clip_path(clip)
            # cuerpos de componentes (tenues) y pads coloreados
            for ref,p in pk.items():
                loc=ref.split('_',1)[1]
                xs=[a for a,b in p.pads().values()]; ys=[b for a,b in p.pads().values()]
                ax.add_patch(Rectangle((min(xs)-1.6,min(ys)-1.6),max(xs)-min(xs)+3.2,max(ys)-min(ys)+3.2,fc='#e8e6dc',ec='#9a9680',lw=0.4,zorder=1.2))
                for pin,(x,y) in p.pads().items():
                    n=padnet.get((ref,pin))
                    c=col[base(n)] if n else '#cccccc'
                    ax.add_patch(Circle((x,y),PAD_D/2+0.15,fc=c,ec='k',lw=0.4,zorder=6))
                    ax.add_patch(Circle((x,y),DRILL/2,fc='w',ec='none',zorder=7))
                    if n: ax.text(x,y+1.9,base(n),fontsize=3.1*z+1.3,ha='center',va='bottom',color=c if c!='#000000' else 'k',zorder=9,fontweight='bold',
                                  bbox=dict(boxstyle='round,pad=0.05',fc='white',ec='none',alpha=0.8))
                xc=(min(xs)+max(xs))/2; yc=(min(ys)+max(ys))/2
                ax.text(xc,yc,loc,fontsize=4.2*z+1.5,ha='center',va='center',color='#222',zorder=8,fontweight='bold',alpha=0.55)
            top=cy+PH/2/z
            ax.text(cx,top-4/z,'PID %d - GUIA DE COLORES: los pads (y pistas) del mismo color DEBEN estar unidos entre si'%k,ha='center',va='center',fontsize=9,fontweight='bold',zorder=30,bbox=dict(fc='white',ec='none',pad=2))
            ax.text(cx,top-8.5/z,'Pistas = cobre de abajo (translucido) | Linea punteada = puente de alambre por arriba | Texto sobre cada pad = nombre de la red | Gris = pad sin red (no conecta)',ha='center',va='center',fontsize=5.2,zorder=30,bbox=dict(fc='white',ec='none',pad=1))
            # leyenda
            ys=cy-PH/2/z+32/z
            items=[n for n in ipe if any(base(m)==n and (m in N.SHARED or m.startswith('P%d_'%k)) for m in nets)]
            nc=5; w=(PW-10)/nc/z
            xl=cx-PW/2/z+5/z
            for i,n in enumerate(items):
                r_,c_=divmod(i,nc)
                ax.add_patch(Rectangle((xl+c_*w,ys-r_*4.2/z),2.0/z*1.6,2.2/z*1.0,fc=col[n],ec='k',lw=0.3,zorder=9))
                ax.text(xl+c_*w+3.2/z*1.0,ys-r_*4.2/z+1.1/z,n,fontsize=7,va='center',zorder=9)
            pdf.savefig(fig); plt.close(fig)
        # pagina tabla
        fig=plt.figure(figsize=(297/25.4,210/25.4)); ax=fig.add_axes([0,0,1,1]); ax.axis('off'); ax.set_xlim(0,297); ax.set_ylim(210,0)
        ax.text(148.5,8,'Que pads van unidos (PID 1; el PID 2 es identico con prefijo P2_)',ha='center',fontsize=12,fontweight='bold')
        names=sorted(n for n in nets if n.startswith('P1_') or n in N.SHARED)
        y=16; xcol=[6,153]; ci=0; rows_per=int((200-16)/4.4)
        for i,n in enumerate(names):
            ci,rw=divmod(i,rows_per)
            xx=xcol[ci] if ci<2 else 6; yy=16+rw*4.4
            ax.add_patch(Rectangle((xx,yy-2.2),4,3,fc=col[base(n)],ec='k',lw=0.3))
            pins=', '.join('%s.%s'%(r.split('_',1)[1] if r.startswith('P') and r[1:2].isdigit() and r[2:3]=='_' else r,p) for r,p in nets[n] if (not n in N.SHARED) and r.startswith('P1_') or n in N.SHARED and r.startswith('P1_'))
            ax.text(xx+5,yy,'%s: %s'%(base(n),pins),fontsize=5.4,va='center',family='monospace')
        pdf.savefig(fig); plt.close(fig)
    print('ok',out)
if __name__=='__main__': main()
