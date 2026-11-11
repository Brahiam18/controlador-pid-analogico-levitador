"""Placa de la carga de prueba R_L: 4 resistencias de cemento 10 Ω / 10 W en serie-paralelo.
  JP1 puenteado (alambre o interruptor): (R1+R2) ‖ (R3+R4) = 10 Ω  -> 1,6 A con 16 V (corriente completa)
  JP1 abierto:                            R1+R2           = 20 Ω  -> 0,8 A con 16 V (media corriente)
En los dos casos cada resistencia disipa 6,4 W. Genera carga.sch, carga.brd (EAGLE / Fusion),
cobre_espejado_1a1.pdf, ensamble_1a1.pdf e img/*.png.   Uso: python3 generar.py"""
import os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'pcb', 'generador'))
from xml.sax.saxutils import escape
import eagle as E
import xmlcheck as X
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.backends.backend_pdf import PdfPages

W, H = 95.0, 95.0
HOLES = [(4.5, 4.5), (W-4.5, 4.5), (4.5, H-4.5), (W-4.5, H-4.5)]
TW = 2.5                    # ancho de pista (mm): 1,6 A con margen
PITCH_R = 55.88             # separación de patas de la resistencia de 10 W (cuerpo ~ 49 x 10 mm)
PKG = {   # nombre: (pads [(pin, x, y)], taladro, diámetro, caja del cuerpo)
 'R10W': ([('1', 0, 0), ('2', PITCH_R, 0)], 1.2, 3.2, (PITCH_R/2-25.5, -5.5, PITCH_R/2+25.5, 5.5)),
 'TERM2': ([('1', 0, 0), ('2', 5.08, 0)], 1.3, 3.0, (-2.5, -5.2, 7.58, 5.6)),
}
DESC = {'R10W': 'Resistencia de cemento 10 W (cuerpo ~49 x 10 x 9 mm), patas a 55,88 mm; montar levantada 5-10 mm',
        'TERM2': 'Bornera de tornillo 2 vías, paso 5,08 mm'}
# ref: (paquete, valor, x, y, giro en grados)
PARTS = {
 'R1': ('R10W', '10R 10W', 25.0, 80.0, 0), 'R2': ('R10W', '10R 10W', 25.0+PITCH_R, 60.0, 180),
 'R3': ('R10W', '10R 10W', 25.0, 40.0, 0), 'R4': ('R10W', '10R 10W', 25.0+PITCH_R, 20.0, 180),
 'J1': ('TERM2', 'A J4 o J5', 8.0, 80.0, 270), 'JP1': ('TERM2', 'SEL 10/20R', 8.0, 25.08, 270),
}
NETS = {'X': [('J1', '1'), ('R1', '1'), ('JP1', '1')], 'GND': [('J1', '2'), ('R2', '2'), ('R3', '1')],
        'MA': [('R1', '2'), ('R2', '1')], 'MB': [('R3', '2'), ('R4', '1')], 'Y': [('R4', '2'), ('JP1', '2')]}
X8 = 25.0+PITCH_R
TRACES = {   # polilíneas con quiebres a 45°
 'X': [[(8, 80), (25, 80)], [(8, 80), (5.5, 80), (3.5, 78), (3.5, 27.08), (5.5, 25.08), (8, 25.08)]],
 'GND': [[(8, 74.92), (13, 74.92), (15, 72.92), (15, 42), (17, 40), (25, 40)], [(15, 62), (17, 60), (25, 60)]],
 'MA': [[(X8, 80), (X8, 60)]], 'MB': [[(X8, 40), (X8, 20)]], 'Y': [[(8, 20), (25, 20)]],
}

def rot(x, y, deg):
    for _ in range((deg//90) % 4): x, y = -y, x
    return x, y
def pads_of(ref):
    k, v, x0, y0, r = PARTS[ref]
    return {p: (x0+rot(px, py, r)[0], y0+rot(px, py, r)[1]) for p, px, py in PKG[k][0]}
def box_of(ref):
    k, v, x0, y0, r = PARTS[ref]; a, b, c, d = PKG[k][3]
    pts = [rot(px, py, r) for px, py in ((a, b), (c, b), (c, d), (a, d))]
    return (x0+min(p[0] for p in pts), y0+min(p[1] for p in pts), x0+max(p[0] for p in pts), y0+max(p[1] for p in pts))
def segs(net):
    return [(a[0], a[1], b[0], b[1]) for pl in TRACES[net] for a, b in zip(pl, pl[1:])]

# ---------------- EAGLE ----------------
def packages():
    out = '<packages>\n'
    for k, (pads, dr, dia, bx) in PKG.items():
        L = [E.pad(p, x, y, 'square' if p == '1' else 'round', dr, dia) for p, x, y in pads]
        L += E.rect_lines(bx[0], bx[1], bx[2], bx[3])
        L += [E.txt((bx[0]+bx[2])/2, bx[3]+0.4, '>NAME', 1.6, 25, 'bottom-center'), E.txt((bx[0]+bx[2])/2, bx[1]-0.4, '>VALUE', 1.2, 27, 'top-center')]
        out += '<package name="%s">\n<description>%s</description>\n' % (k, escape(DESC[k])) + '\n'.join(L) + '\n</package>\n'
    return out + '</packages>\n'
DEV = {'R10W': ('R', 'R', ['1', '2']), 'TERM2': ('HDR2', 'J', ['1', '2'])}
def library(sch):
    out = '<libraries>\n<library name="carga">\n' + packages()
    if sch:
        out += '<symbols>\n' + ''.join('<symbol name="%s">\n' % s + '\n'.join(E.SYMS[s][0]) + '\n</symbol>\n' for s in ('R', 'HDR2')) + '</symbols>\n<devicesets>\n'
        for k, (sym, pre, pins) in DEV.items():
            out += '<deviceset name="%s" prefix="%s">\n<gates>\n<gate name="G$1" symbol="%s" x="0" y="0"/>\n</gates>\n<devices>\n<device name="" package="%s">\n<connects>\n' % (k, pre, sym, k)
            out += '\n'.join('<connect gate="G$1" pin="%s" pad="%s"/>' % (p, p) for p in pins)
            out += '\n</connects>\n<technologies>\n<technology name=""/>\n</technologies>\n</device>\n</devices>\n</deviceset>\n'
        out += '</devicesets>\n'
    return out + '</library>\n</libraries>\n'
def brd():
    plain = ''.join(E.wire(*a, 0, 20)+'\n' for a in [(0, 0, W, 0), (W, 0, W, H), (W, H, 0, H), (0, H, 0, 0)])
    plain += ''.join('<hole x="%s" y="%s" drill="3.2"/>\n' % (E.f(x), E.f(y)) for x, y in HOLES)
    plain += '<text x="52" y="50" size="3" layer="16" rot="MR0" align="center">CARGA RL 10/20 OHM</text>\n'
    plain += '<text x="52" y="30" size="2" layer="16" rot="MR0" align="center">B. Campino - U. Ibague</text>\n'
    plain += E.txt(14, 88, 'J1: a J4 (+16) o J5 (-16)', 1.6, 21, 'center-left') + '\n' + E.txt(12, 10, 'JP1 puenteado = 10 ohm / 1,6 A; abierto = 20 ohm / 0,8 A', 1.4, 21, 'center-left') + '\n'
    el = ''.join('<element name="%s" library="carga" package="%s" value="%s" x="%s" y="%s"%s/>\n' % (r, k, escape(v), E.f(x), E.f(y), '' if g == 0 else ' rot="R%d"' % g) for r, (k, v, x, y, g) in PARTS.items())
    sig = ''
    for n, pins in NETS.items():
        sig += '<signal name="%s">\n' % n + ''.join('<contactref element="%s" pad="%s"/>\n' % p for p in pins) + ''.join(E.wire(*s, TW, 16)+'\n' for s in segs(n)) + '</signal>\n'
    dr = '<designrules name="default">\n' + ''.join('<param name="%s" value="%s"/>\n' % kv for kv in (('layerSetup', '(1*16)'), ('mdWireWire', '0.4mm'), ('mdWirePad', '0.4mm'), ('mdPadPad', '0.4mm'), ('mdCopperDimension', '1mm'), ('msWidth', '2.5mm'))) + '</designrules>\n'
    return (E.HEAD + E.layers_xml() + '<board>\n<description>Carga de prueba R_L 10/20 ohm para la fuente +-16 V (una cara)</description>\n<plain>\n' + plain + '</plain>\n'
            + library(False) + '<attributes>\n</attributes>\n<variantdefs>\n</variantdefs>\n<classes>\n<class number="0" name="default" width="2.5" drill="1.2"/>\n</classes>\n'
            + dr + '<elements>\n' + el + '</elements>\n<signals>\n' + sig + '</signals>\n</board>\n' + E.TAIL)
def sch():
    pos = {'J1': (10.16, 0), 'R1': (40.64, 10.16), 'R2': (71.12, 10.16), 'R3': (40.64, -10.16), 'R4': (71.12, -10.16), 'JP1': (10.16, -25.4)}
    inst = ''.join('<instance part="%s" gate="G$1" x="%s" y="%s"/>\n' % (r, E.f(x), E.f(y)) for r, (x, y) in pos.items())
    nets = ''
    for n, pins in NETS.items():
        nets += '<net name="%s" class="0">\n' % n
        for r, p in pins:
            sym = DEV[PARTS[r][0]][0]; px, py, d = E.SYMS[sym][1][p]; x, y = pos[r]; px += x; py += y
            ex = px-5.08 if d == 'L' else px+5.08
            nets += '<segment>\n<pinref part="%s" gate="G$1" pin="%s"/>\n' % (r, p) + E.wire(px, py, ex, py, 0.1524, 91) + '\n<label x="%s" y="%s" size="1.27" layer="95"/>\n</segment>\n' % (E.f(min(px, ex)), E.f(py))
        nets += '</net>\n'
    plain = ('<text x="0" y="25.4" size="2.54" layer="97">Carga de prueba R_L: (R1+R2) || (R3+R4). JP1 puenteado = 10 ohm (1,6 A); JP1 abierto = 20 ohm (0,8 A)</text>\n'
             '<text x="0" y="20.32" size="1.778" layer="97">Conexion por etiquetas de red: X, Y, MA, MB, GND. Polaridad indiferente (sirve para +16 V y -16 V)</text>\n')
    parts = ''.join('<part name="%s" library="carga" deviceset="%s" device="" value="%s"/>\n' % (r, k, escape(v)) for r, (k, v, *_) in PARTS.items())
    return (E.HEAD + E.layers_xml() + '<schematic>\n<description>Carga de prueba R_L 10/20 ohm</description>\n' + library(True)
            + '<attributes>\n</attributes>\n<variantdefs>\n</variantdefs>\n<classes>\n<class number="0" name="default" width="0" drill="0"/>\n</classes>\n<parts>\n' + parts
            + '</parts>\n<sheets>\n<sheet>\n<plain>\n' + plain + '</plain>\n<instances>\n' + inst + '</instances>\n<busses>\n</busses>\n<nets>\n' + nets + '</nets>\n</sheet>\n</sheets>\n</schematic>\n' + E.TAIL)

# ---------------- PDF ----------------
PT = 72/25.4; PAGE = (210.0, 279.0)
def fig_page():
    fig = plt.figure(figsize=(PAGE[0]/25.4, PAGE[1]/25.4)); ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(W/2-PAGE[0]/2, W/2+PAGE[0]/2); ax.set_ylim(H+20-PAGE[1], H+20); ax.set_aspect('equal'); ax.axis('off'); return fig, ax
def copper(path, png):
    fig, ax = fig_page(); ax.invert_xaxis()
    for n in NETS:
        for s in segs(n): ax.plot([s[0], s[2]], [s[1], s[3]], color='k', lw=TW*PT, solid_capstyle='round')
    for r in PARTS:
        d = PKG[PARTS[r][0]][2]
        for x, y in pads_of(r).values(): ax.add_patch(Circle((x, y), d/2, fc='k', lw=0)); ax.add_patch(Circle((x, y), 0.35, fc='w', lw=0, zorder=4))
    for x, y in HOLES: ax.add_patch(Circle((x, y), 1.6, fc='none', ec='k', lw=0.8)); ax.add_patch(Circle((x, y), 0.4, fc='k'))
    # texto en cobre: se dibuja como trazo en coordenadas de la placa, así queda espejado igual que las pistas
    from matplotlib.textpath import TextPath
    from matplotlib.patches import PathPatch
    from matplotlib.font_manager import FontProperties
    for t, (cx, cy), hgt in (('CARGA RL 10/20 Ω', (52, 50), 4.0), ('B. Campiño - U. Ibagué', (52, 30), 2.5)):
        tp = TextPath((0, 0), t, size=hgt, prop=FontProperties(weight='bold'))
        bb = tp.get_extents()
        tr = matplotlib.transforms.Affine2D().translate(cx-(bb.x0+bb.x1)/2, cy-(bb.y0+bb.y1)/2) + ax.transData
        ax.add_patch(PathPatch(tp, fc='k', lw=0, transform=tr))
    ax.add_patch(Rectangle((0, 0), W, H, fc='none', ec='k', lw=0.4, ls=(0, (3, 2))))
    x0 = W/2-25; ax.plot([x0, x0+50], [-6, -6], color='k', lw=0.6)
    for t in range(0, 51, 10): ax.plot([x0+t, x0+t], [-6.8, -5.2], color='k', lw=0.6)
    ax.text(W/2, -10, 'Carga de prueba R_L  |  CARA DE COBRE ESPEJADA  |  imprimir 1:1 sin escalar: la regla debe medir 50 mm  |  placa %.0f x %.0f mm' % (W, H), ha='center', fontsize=6)
    fig.savefig(path); fig.savefig(png, dpi=200); plt.close(fig)
def assembly(path, png):
    with PdfPages(path) as pdf:
        fig, ax = fig_page()
        ax.add_patch(Rectangle((0, 0), W, H, fc='#f6f3e8', ec='k', lw=0.8))
        for n in NETS:
            for s in segs(n): ax.plot([s[0], s[2]], [s[1], s[3]], color='#d9cfa8', lw=TW*PT, solid_capstyle='round', zorder=1)
        for x, y in HOLES: ax.add_patch(Circle((x, y), 1.6, fc='w', ec='k', lw=0.6))
        for r, (k, v, *_) in PARTS.items():
            b = box_of(r)
            ax.add_patch(Rectangle((b[0], b[1]), b[2]-b[0], b[3]-b[1], fc='#e8e8e0' if k == 'R10W' else '#2a6fb0', ec='k', lw=0.5, alpha=0.6, zorder=2))
            for p, (x, y) in pads_of(r).items():
                d = PKG[k][2]; ax.add_patch(Circle((x, y), d/2, fc='#d4a017', ec='k', lw=0.3, zorder=5)); ax.add_patch(Circle((x, y), 0.5, fc='w', ec='k', lw=0.2, zorder=6))
            ax.text((b[0]+b[2])/2, (b[1]+b[3])/2, r + ('\n' + v if k == 'R10W' else ''), ha='center', va='center', fontsize=6 if k == 'R10W' else 5, fontweight='bold', color='#0b3d91' if k == 'R10W' else 'w', zorder=7)
        for (x, y, t) in ((8, 80, 'IN'), (8, 74.92, 'GND'), (8, 25.08, 'X'), (8, 20, 'Y')):
            ax.text(x+4.2, y, t, fontsize=4.5, va='center', color='#8b0000', fontweight='bold', zorder=8)
        ax.text(10, 89, 'J1: a J4 (+16 V / GND) o a J5 (−16 V / GND) de la fuente', fontsize=6, fontweight='bold')
        ax.text(10, 6.5, 'JP1 puenteado = 10 Ω → 1,6 A  |  JP1 abierto = 20 Ω → 0,8 A', fontsize=6, fontweight='bold')
        ax.text(W/2, -6, 'Lado de componentes 1:1. Resistencias de cemento 10 Ω / 10 W LEVANTADAS 5–10 mm de la placa (se calientan a más de 150 °C).', ha='center', fontsize=5.5)
        ax.text(W/2, -10, 'Cada resistencia disipa 6,4 W en los dos modos. No tocar durante la prueba; dejar enfriar antes de manipular.', ha='center', fontsize=5.5)
        pdf.savefig(fig); fig.savefig(png, dpi=200); plt.close(fig)

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'img'), exist_ok=True)
    for b_ in (box_of(r) for r in PARTS):
        assert b_[0] >= 0.5 and b_[1] >= 0.5 and b_[2] <= W-0.5 and b_[3] <= H-0.5, b_
    open(os.path.join(HERE, 'carga.brd'), 'w', encoding='utf-8').write(brd())
    open(os.path.join(HERE, 'carga.sch'), 'w', encoding='utf-8').write(sch())
    bad, md, ns = X.check_board(os.path.join(HERE, 'carga.brd'), min_clear=0.4)
    print('placa: %d redes, holgura mínima %.2f mm, problemas:' % (ns, md), bad or 'ninguno')
    print('sch vs brd:', X.check_sch_vs_brd(os.path.join(HERE, 'carga.sch'), os.path.join(HERE, 'carga.brd')) or 'consistentes')
    from shapely.geometry import LineString, Point
    edge = min(LineString(s[:2] and [(s[0], s[1]), (s[2], s[3])]).buffer(TW/2).distance(Point(hx, hy).buffer(1.6)) for n in NETS for s in segs(n) for hx, hy in HOLES)
    cu = min(min(s[0], s[2])-TW/2 for n in NETS for s in segs(n)); print('distancia pista-agujero de montaje %.1f mm, pista-borde izquierdo %.2f mm' % (edge, cu))
    copper(os.path.join(HERE, 'cobre_espejado_1a1.pdf'), os.path.join(HERE, 'img', 'cobre_espejado.png'))
    assembly(os.path.join(HERE, 'ensamble_1a1.pdf'), os.path.join(HERE, 'img', 'ensamble.png'))
    print('listo')
