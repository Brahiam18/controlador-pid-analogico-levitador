"""Hojas para imprimir: cobre espejado 1:1 y ensamble (lado componentes)."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon as MPoly
from matplotlib.backends.backend_pdf import PdfPages
import collections
from engine import *
import netlist as N
from eagle import merge_edges

PT = 72/25.4
PAGE = (210.0, 279.0)          # entra en A4 y en Carta sin escalar
PINLAB = {'Q1': ('B', 'C', 'E'), 'Q3': ('B', 'C', 'E'), 'U1': ('ADJ', 'OUT', 'IN'), 'U3': ('ADJ', 'OUT', 'IN'), 'U2': ('ADJ', 'IN', 'OUT'),
          'Q2': ('C', 'B', 'E'), 'Q4': ('C', 'B', 'E'), 'J1': ('GND', 'AC'), 'J2': ('+16', '-16', 'GND', '+5'), 'J3': ('V+', 'GND', 'V-')}
def padd(kind): return 2.4 if kind in ('TERM2', 'TERM4', 'FUSE', 'CPOL25') else PAD_D

def _fig(W, H, page=PAGE, top=12):
    PW, PH = page
    fig = plt.figure(figsize=(PW/25.4, PH/25.4)); ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(W/2-PW/2, W/2+PW/2); ax.set_ylim(H+top-PH, H+top); ax.set_aspect('equal'); ax.axis('off')
    return fig, ax

def copper_pdf(path, parts, routes, W, H, holes, png=None):
    fig, ax = _fig(W, H); ax.invert_xaxis()
    for net, rt in routes.items():
        for (x0, y0, x1, y1) in merge_edges(rt['edges'], 0):
            ax.plot([x0, x1], [y0, y1], color='k', lw=N.width_of(net)*PT, solid_capstyle='round', zorder=2)
    pts = []
    for ref, p in parts.items():
        for pin, (x, y) in p.pads().items(): pts.append((x, y, padd(p.kind)))
    for rt in routes.values():
        for (i, j) in rt['vias']: pts.append((i*G, j*G, PAD_D))
    for (x, y, d) in set(pts):
        ax.add_patch(Circle((x, y), d/2, fc='k', lw=0, zorder=3)); ax.add_patch(Circle((x, y), 0.25, fc='w', lw=0, zorder=4))
    for (x, y) in holes:
        ax.add_patch(Circle((x, y), 3.0, fc='none', ec='k', lw=0.8, zorder=3)); ax.add_patch(Circle((x, y), 0.4, fc='k', lw=0, zorder=3))
    ax.add_patch(Rectangle((0, 0), W, H, fc='none', ec='k', lw=0.4, ls=(0, (3, 2)), zorder=1))
    for (x, y) in ((0, 0), (W, 0), (0, H), (W, H)):
        sx = -1 if x == 0 else 1; sy = -1 if y == 0 else 1
        ax.plot([x, x+sx*5], [y, y], color='k', lw=0.4); ax.plot([x, x], [y, y+sy*5], color='k', lw=0.4)
    x0 = W/2-25; ax.plot([x0, x0+50], [-5, -5], color='k', lw=0.6)
    for t in range(0, 51, 10): ax.plot([x0+t, x0+t], [-5.8, -4.2], color='k', lw=0.6)
    ax.text(W/2, -8.5, 'Fuente ±16 V / +5 V  |  CARA DE COBRE ESPEJADA  |  imprimir 1:1 sin escalar: la regla debe medir 50 mm  |  placa %.1f x %.1f mm' % (W, H), ha='center', fontsize=6)
    fig.savefig(path, format='pdf')
    if png: fig.savefig(png, dpi=200)
    plt.close(fig)

def _draw(ax, parts, routes, jl, fs=3.6, values=True):
    for net, rt in routes.items():
        for (x0, y0, x1, y1) in merge_edges(rt['edges'], 0):
            ax.plot([x0, x1], [y0, y1], color='#d9cfa8', lw=N.width_of(net)*PT, solid_capstyle='round', zorder=1)
    for k, jp in enumerate(jl, 1):
        for (x0, y0, x1, y1) in jp['segs']: ax.plot([x0, x1], [y0, y1], color='#d62728', lw=1.3, solid_capstyle='round', zorder=6)
        ax.text(jp['label'][0], jp['label'][1], 'J%d' % k, color='#d62728', fontsize=fs*1.1, ha='center', va='bottom', fontweight='bold', zorder=9)
    for ref, p in parts.items():
        x0, y0, x1, y1 = p.box(); pads = p.pads(); kind = p.kind
        cx, cy = (x0+x1)/2, (y0+y1)/2
        col = {'TO220': '#6b6b6b', 'TO92': '#333', 'CPOL25': '#3b6ea8', 'CPOL6': '#3b6ea8', 'CPOL5': '#3b6ea8', 'CTANT': '#d9a62b', 'LED5': '#5cc85c',
               'TERM2': '#2a6fb0', 'TERM4': '#2a6fb0', 'FUSE': '#bbbbbb', 'TRIM': '#2a6fb0', 'DO41': '#222', 'DO35': '#d98c2b', 'HDR3': '#222', 'CAP': '#e2c15a'}.get(kind, '#d9b77e')
        if kind in ('CPOL25', 'CPOL6', 'CPOL5', 'LED5'):
            ax.add_patch(Circle((cx, cy), (x1-x0)/2-0.3, fc=col, ec='k', lw=0.4, alpha=0.55, zorder=2))
            px, py = pads['1']; ax.text(px+(px-cx)*0.0, py+2.2 if kind != 'CPOL25' else py, '+' if kind != 'LED5' else 'A', fontsize=fs*1.6, ha='center', va='center', fontweight='bold', zorder=8, color='#b00000')
        else:
            ax.add_patch(Rectangle((x0+0.3, y0+0.3), x1-x0-0.6, y1-y0-0.6, fc=col, ec='k', lw=0.4, alpha=0.55 if kind not in ('TO220',) else 0.75, zorder=2))
        if kind == 'TO220':     # línea gruesa = aleta metálica
            q = [rot(a, b, p.r) for a, b in ((-3.0, 5.4), (8.1, 5.4))]
            ax.plot([p.x+q[0][0], p.x+q[1][0]], [p.y+q[0][1], p.y+q[1][1]], color='k', lw=2.5, zorder=3)
        if kind in ('DO41', 'DO35'):   # banda del cátodo junto al pad 2
            (ax_, ay_), (bx_, by_) = pads['1'], pads['2']; tx, ty = ax_+(bx_-ax_)*0.72, ay_+(by_-ay_)*0.72
            if abs(bx_-ax_) > abs(by_-ay_): ax.plot([tx, tx], [ty-1.6, ty+1.6], color='w' if kind == 'DO41' else 'k', lw=2, zorder=4)
            else: ax.plot([tx-1.6, tx+1.6], [ty, ty], color='w' if kind == 'DO41' else 'k', lw=2, zorder=4)
        if kind == 'CTANT':
            px, py = pads['1']; ax.text(px, py+2.0, '+', fontsize=fs*1.6, ha='center', fontweight='bold', color='#b00000', zorder=8)
        for pin, (x, y) in pads.items():
            ax.add_patch(Circle((x, y), padd(kind)/2, fc='#d4a017', ec='k', lw=0.3, zorder=5)); ax.add_patch(Circle((x, y), 0.45, fc='w', ec='k', lw=0.2, zorder=6))
        x, y = pads['1']; ax.add_patch(Circle((x, y), padd(kind)/2+0.5, fc='none', ec='#0b3d91', lw=0.6, zorder=6))
        lab = ref + ('\n' + N.PARTS[ref][1] if values else '')
        ax.text(cx, cy, lab, fontsize=fs, ha='center', va='center', zorder=10, color='#0b3d91' if kind not in ('TO220', 'TO92', 'DO41', 'HDR3') else 'w', fontweight='bold')
        if ref in PINLAB:
            for pin, t in zip(sorted(pads, key=int), PINLAB[ref]):
                x, y = pads[pin]
                dy = -2.6 if (kind == 'TO220' and p.r == 0) else 2.6
                ax.text(x, y+dy if kind in ('TO220', 'TO92') else y-3.4, t, fontsize=fs*0.8, ha='center', va='center', color='#8b0000', fontweight='bold', zorder=11)

def assembly_pdf(path, parts, routes, W, H, holes, jl, png=None):
    with PdfPages(path) as pdf:
        fig, ax = _fig(W, H)
        ax.add_patch(Rectangle((0, 0), W, H, fc='#f6f3e8', ec='k', lw=0.8, zorder=0))
        for (x, y) in holes: ax.add_patch(Circle((x, y), 1.6, fc='w', ec='k', lw=0.6, zorder=1))
        _draw(ax, parts, routes, jl, fs=3.0, values=False)
        ax.text(W/2, -5, 'Lado de componentes 1:1  |  rojo = puentes de alambre aislado (J1..J%d)  |  círculo azul = pin 1  |  línea gruesa del TO-220 = aleta (va al disipador)' % len(jl), ha='center', fontsize=5.5)
        ax.text(W/2, -8.5, 'Disipadores: Q1+U1 en el borde superior y Q3+U2 en el borde inferior, cada par sobre un disipador de <= 5 °C/W con mica y buje aislante', ha='center', fontsize=5.5)
        pdf.savefig(fig)
        if png: fig.savefig(png, dpi=200)
        plt.close(fig)
        PW, PH = 297.0, 210.0; z = min((PW-12)/W, (PH-24)/H)
        fig = plt.figure(figsize=(PW/25.4, PH/25.4)); ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(W/2-PW/2/z, W/2+PW/2/z); ax.set_ylim(H/2-PH/2/z-2, H/2+PH/2/z-2); ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(Rectangle((0, 0), W, H, fc='#f6f3e8', ec='k', lw=0.8, zorder=0))
        for (x, y) in holes: ax.add_patch(Circle((x, y), 1.6, fc='w', ec='k', lw=0.6, zorder=1))
        _draw(ax, parts, routes, jl, fs=3.6*z, values=True)
        ax.text(W/2, H+4/z*2, 'Fuente ±16 V / +5 V  -  ensamble ampliado (escala %.2f:1, A4 horizontal): referencia y valor de cada pieza' % z, ha='center', fontsize=9, fontweight='bold')
        pdf.savefig(fig); plt.close(fig)

def jumpers(parts, routes):
    padat = {}
    for ref, p in parts.items():
        for pin, (x, y) in p.pads().items(): padat[(round(x/G), round(y/G))] = (ref, pin)
    out = []
    for net, rt in routes.items():
        adj = collections.defaultdict(set)
        for a, b in rt['edges']:
            if a[0] == 1: adj[a[1:]].add(b[1:]); adj[b[1:]].add(a[1:])
        seen = set()
        for s in list(adj):
            if s in seen: continue
            comp = []; st = [s]; seen.add(s)
            while st:
                u = st.pop(); comp.append(u)
                for v in adj[u]:
                    if v not in seen: seen.add(v); st.append(v)
            ends = [u for u in comp if len(adj[u]) == 1]
            def desc(u):
                if u in padat: return '%s.%s' % padat[u]
                b = min(padat, key=lambda q: (q[0]-u[0])**2+(q[1]-u[1])**2)
                return 'agujero (%.1f; %.1f) mm junto a %s.%s' % (u[0]*G, u[1]*G, padat[b][0], padat[b][1])
            segs = merge_edges([((1,)+u, (1,)+v) for u in comp for v in adj[u]], 1)
            n_e = sum(len(adj[u]) for u in comp)//2
            out.append(dict(net=net, segs=segs, ends=[desc(u) for u in sorted(ends)], length=n_e*G,
                            label=(sum(u[0] for u in comp)/len(comp)*G, max(u[1] for u in comp)*G+0.6)))
    out.sort(key=lambda j: (-j['label'][1], j['label'][0]))
    return out
