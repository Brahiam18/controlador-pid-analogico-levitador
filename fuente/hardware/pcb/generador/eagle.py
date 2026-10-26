"""Exportador EAGLE (.sch / .brd) de la fuente, abrible en Fusion Electronics (Cargar .sch y .brd juntos)."""
import collections
from xml.sax.saxutils import escape
from engine import *
import netlist as N

LIB = 'fuente16'
LAYERS=[(1,'Top',4,1,'yes','yes'),(16,'Bottom',1,1,'yes','yes'),(17,'Pads',2,1,'yes','yes'),(18,'Vias',2,1,'yes','yes'),
(19,'Unrouted',6,1,'yes','yes'),(20,'Dimension',15,1,'yes','yes'),(21,'tPlace',7,1,'yes','yes'),(22,'bPlace',7,1,'yes','yes'),
(23,'tOrigins',15,1,'yes','yes'),(24,'bOrigins',15,1,'yes','yes'),(25,'tNames',7,1,'yes','yes'),(26,'bNames',7,1,'yes','yes'),
(27,'tValues',7,1,'yes','yes'),(28,'bValues',7,1,'yes','yes'),(29,'tStop',7,3,'no','yes'),(30,'bStop',7,6,'no','yes'),
(31,'tCream',7,4,'no','yes'),(32,'bCream',7,5,'no','yes'),(33,'tFinish',6,3,'no','yes'),(34,'bFinish',6,6,'no','yes'),
(35,'tGlue',7,4,'no','yes'),(36,'bGlue',7,5,'no','yes'),(37,'tTest',7,1,'no','yes'),(38,'bTest',7,1,'no','yes'),
(39,'tKeepout',4,11,'yes','yes'),(40,'bKeepout',1,11,'yes','yes'),(41,'tRestrict',4,10,'yes','yes'),(42,'bRestrict',1,10,'yes','yes'),
(43,'vRestrict',2,10,'yes','yes'),(44,'Drills',7,1,'no','yes'),(45,'Holes',7,1,'no','yes'),(46,'Milling',3,1,'no','yes'),
(47,'Measures',7,1,'no','yes'),(48,'Document',7,1,'yes','yes'),(49,'Reference',7,1,'yes','yes'),(51,'tDocu',7,1,'yes','yes'),
(52,'bDocu',7,1,'yes','yes'),(91,'Nets',2,1,'yes','yes'),(92,'Busses',1,1,'yes','yes'),(93,'Pins',2,1,'no','yes'),
(94,'Symbols',4,1,'yes','yes'),(95,'Names',7,1,'yes','yes'),(96,'Values',7,1,'yes','yes'),(97,'Info',7,1,'yes','yes'),(98,'Guide',6,1,'yes','yes')]
def f(v):
    s = ('%.4f' % v).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s
def layers_xml():
    return '<layers>\n'+'\n'.join('<layer number="%d" name="%s" color="%d" fill="%d" visible="%s" active="%s"/>' % l for l in LAYERS)+'\n</layers>\n'
def wire(x1, y1, x2, y2, w, layer, extra=''):
    return '<wire x1="%s" y1="%s" x2="%s" y2="%s" width="%s" layer="%d"%s/>' % (f(x1), f(y1), f(x2), f(y2), f(w), layer, extra)
def rect_lines(x0, y0, x1, y1, w=0.2, layer=21):
    return [wire(x0, y0, x1, y0, w, layer), wire(x1, y0, x1, y1, w, layer), wire(x1, y1, x0, y1, w, layer), wire(x0, y1, x0, y0, w, layer)]
def circ(x, y, r, w=0.2, layer=21): return '<circle x="%s" y="%s" radius="%s" width="%s" layer="%d"/>' % (f(x), f(y), f(r), f(w), layer)
def pad(name, x, y, shape='round', drill=DRILL, dia=PAD_D):
    return '<pad name="%s" x="%s" y="%s" drill="%s" diameter="%s" shape="%s"/>' % (name, f(x), f(y), f(drill), f(dia), shape)
def txt(x, y, s, size=1.27, layer=25, align='center', rot=''):
    return '<text x="%s" y="%s" size="%s" layer="%d" align="%s"%s>%s</text>' % (f(x), f(y), f(size), layer, align, ' rot="%s"' % rot if rot else '', escape(s))

DESC = {'TERM2':'Bornera de tornillo 2 vías, paso 5.08 mm','TERM4':'Bornera de tornillo 4 vías (2 x 2 vías), paso 5.08 mm',
 'FUSE':'Portafusible de PCB para fusible 5x20 mm, 22.86 mm entre clips','DO41':'Diodo DO-41 (1N4007), 10.16 mm; pad 2 = cátodo',
 'DO35':'Diodo DO-35 (1N4148), 7.62 mm; pad 2 = cátodo','CPOL25':'Electrolítico radial D28 mm, paso 10 mm (6800 uF/50 V); pad 1 = +',
 'CPOL6':'Electrolítico radial D6.3 mm, paso 2.54 mm; pad 1 = +','CPOL5':'Electrolítico radial D5 mm, paso 2.54 mm; pad 1 = +',
 'CTANT':'Tántalo de gota, paso 2.54 mm; pad 1 = +','CAP':'Cerámico/poliéster, paso 5.08 mm','RES10':'Resistencia 1/4 W, 10.16 mm',
 'RES1W':'Resistencia 1 W, 15.24 mm','RES2W':'Resistencia 2 W, 20.32 mm','RES3W':'Resistencia 3 W, 25.4 mm',
 'TO220':'TO-220 vertical; aleta hacia la línea gruesa (borde de la placa, disipador)','TO92':'TO-92 en línea, paso 2.54 mm (BC547/BC557: 1 C, 2 B, 3 E)',
 'TRIM':'Trimmer multivuelta 3296W, pines en línea 2.54 mm','LED5':'LED 5 mm; pad 1 = ánodo (pata larga)','HDR3':'Regleta 1x3, 2.54 mm'}
def packages_xml():
    out = '<packages>\n'
    for kind, desc in DESC.items():
        pads = fp_pads(kind); L = []
        for pin, x, y in pads: L.append(pad(pin, x, y, 'square' if pin == '1' else 'round', drill_of(kind), 2.4 if kind in ('TERM2','TERM4','FUSE','CPOL25') else PAD_D))
        x0, y0, x1, y1 = fp_box(kind); cx = (x0+x1)/2; cy = (y0+y1)/2
        if kind.startswith('CPOL') or kind == 'LED5':
            L.append(circ(cx, cy, (x1-x0)/2-0.2)); L.append(txt(-1.6, 1.4, '+', 1.2, 21))
        else:
            L += rect_lines(x0+0.3, y0+0.3, x1-0.3, y1-0.3)
        if kind == 'TO220': L.append(wire(x0+0.3, y1-0.9, x1-0.3, y1-0.9, 0.6, 21))
        if kind in ('DO41', 'DO35'): L.append(wire(pads[1][1]-2.6, y0+0.3, pads[1][1]-2.6, y1-0.3, 0.6, 21))
        L.append(txt(cx, y1+0.4, '>NAME', 1.27, 25, 'bottom-center')); L.append(txt(cx, y0-0.4, '>VALUE', 1.0, 27, 'top-center'))
        out += '<package name="%s">\n<description>%s</description>\n' % (kind, escape(desc)) + '\n'.join(L) + '\n</package>\n'
    return out + '</packages>\n'

def sym_pin(name, x, y, rot='R0', direction='pas', length='short'):
    r = '' if rot == 'R0' else ' rot="%s"' % rot
    return '<pin name="%s" x="%s" y="%s" length="%s" direction="%s"%s/>' % (name, f(x), f(y), length, direction, r)
def build_symbols():
    S = {}
    nm = ['<text x="-3.81" y="2.4" size="1.778" layer="95">&gt;NAME</text>', '<text x="-3.81" y="-4.2" size="1.778" layer="96">&gt;VALUE</text>']
    S['R'] = (rect_lines(-2.54, -1.016, 2.54, 1.016, 0.254, 94)+nm+[sym_pin('1', -5.08, 0), sym_pin('2', 5.08, 0, 'R180')], {'1': (-5.08, 0, 'L'), '2': (5.08, 0, 'R')})
    S['FUSE'] = (rect_lines(-2.54, -0.8, 2.54, 0.8, 0.254, 94)+[wire(-2.54, 0, 2.54, 0, 0.15, 94)]+nm+[sym_pin('1', -5.08, 0), sym_pin('2', 5.08, 0, 'R180')], {'1': (-5.08, 0, 'L'), '2': (5.08, 0, 'R')})
    S['C'] = ([wire(-0.6, -2.54, -0.6, 2.54, 0.4, 94), wire(0.6, -2.54, 0.6, 2.54, 0.4, 94)]+nm+[sym_pin('1', -5.08, 0), sym_pin('2', 5.08, 0, 'R180')], {'1': (-5.08, 0, 'L'), '2': (5.08, 0, 'R')})
    S['CPOL'] = ([wire(-0.6, -2.54, -0.6, 2.54, 0.4, 94), wire(0.6, -2.54, 0.6, 2.54, 0.9, 94), '<text x="-2.6" y="0.6" size="1.27" layer="94">+</text>']+nm+[sym_pin('+', -5.08, 0), sym_pin('-', 5.08, 0, 'R180')], {'+': (-5.08, 0, 'L'), '-': (5.08, 0, 'R')})
    dl = [wire(-1.27, 1.27, -1.27, -1.27, 0.254, 94), wire(-1.27, -1.27, 1.27, 0, 0.254, 94), wire(1.27, 0, -1.27, 1.27, 0.254, 94), wire(1.27, 1.27, 1.27, -1.27, 0.254, 94)]
    S['D'] = (dl+nm+[sym_pin('A', -3.81, 0), sym_pin('K', 3.81, 0, 'R180')], {'A': (-3.81, 0, 'L'), 'K': (3.81, 0, 'R')})
    S['LED'] = (dl+[wire(0, 1.6, 1.2, 2.8, 0.15, 94), wire(0.8, 1.6, 2.0, 2.8, 0.15, 94)]+nm+[sym_pin('A', -3.81, 0), sym_pin('K', 3.81, 0, 'R180')], {'A': (-3.81, 0, 'L'), 'K': (3.81, 0, 'R')})
    for t in ('NPN', 'PNP'):
        L = [wire(0, -2.54, 0, 2.54, 0.4, 94), wire(0, 1.27, 2.54, 2.54, 0.254, 94), wire(0, -1.27, 2.54, -2.54, 0.254, 94), wire(-2.54, 0, 0, 0, 0.254, 94),
             '<text x="3.8" y="1.0" size="1.778" layer="95">&gt;NAME</text>', '<text x="3.8" y="-1.8" size="1.778" layer="96">&gt;VALUE</text>',
             '<text x="1.2" y="%s" size="1.0" layer="94">%s</text>' % ('-2.4' if t == 'NPN' else '1.6', 'E' if t == 'NPN' else 'E')]
        L += [sym_pin('B', -5.08, 0), sym_pin('C', 2.54, 5.08, 'R270'), sym_pin('E', 2.54, -5.08, 'R90')] if t == 'NPN' else [sym_pin('B', -5.08, 0), sym_pin('E', 2.54, 5.08, 'R270'), sym_pin('C', 2.54, -5.08, 'R90')]
        S[t] = (L, {'B': (-5.08, 0, 'L'), 'C': (2.54, 5.08, 'U') if t == 'NPN' else (2.54, -5.08, 'D'), 'E': (2.54, -5.08, 'D') if t == 'NPN' else (2.54, 5.08, 'U')})
    L = rect_lines(-5.08, -2.54, 5.08, 2.54, 0.254, 94)+['<text x="-5.08" y="3.2" size="1.778" layer="95">&gt;NAME</text>', '<text x="-5.08" y="-5.0" size="1.778" layer="96">&gt;VALUE</text>',
        sym_pin('IN', -7.62, 0), sym_pin('OUT', 7.62, 0, 'R180'), sym_pin('ADJ', 0, -5.08, 'R90')]
    S['REG'] = (L, {'IN': (-7.62, 0, 'L'), 'OUT': (7.62, 0, 'R'), 'ADJ': (0, -5.08, 'D')})
    L = rect_lines(-3.81, -1.016, 3.81, 1.016, 0.254, 94)+[wire(0, -2.54, 0, -1.016, 0.254, 94)]+nm+[sym_pin('1', -7.62, 0), sym_pin('3', 7.62, 0, 'R180'), sym_pin('2', 0, -5.08, 'R90')]
    S['POT'] = (L, {'1': (-7.62, 0, 'L'), '3': (7.62, 0, 'R'), '2': (0, -5.08, 'D')})
    for nm_, n in (('HDR2', 2), ('HDR3', 3), ('HDR4', 4)):
        top = 1.27; bot = -(n-1)*2.54-1.27
        L = rect_lines(-2.54, bot, 2.54, top, 0.254, 94)+['<text x="-2.54" y="%s" size="1.778" layer="95">&gt;NAME</text>' % f(top+1.0)]
        pins = {}
        for i in range(n): L.append(sym_pin(str(i+1), -5.08, -i*2.54)); pins[str(i+1)] = (-5.08, -i*2.54, 'L')
        S[nm_] = (L, pins)
    return S
SYMS = build_symbols()
def single(sym, pk, pre, pins, pads=None):
    return dict(prefix=pre, package=pk, gates=[('G$1', sym, 'next')], connects=[('G$1', p, d) for p, d in zip(pins, pads or pins)])
DEVSETS = {
 'R10': single('R', 'RES10', 'R', ['1', '2']), 'R1W': single('R', 'RES1W', 'R', ['1', '2']), 'R2W': single('R', 'RES2W', 'R', ['1', '2']), 'R3W': single('R', 'RES3W', 'R', ['1', '2']),
 'C': single('C', 'CAP', 'C', ['1', '2']),
 'CPOL25': single('CPOL', 'CPOL25', 'C', ['+', '-'], ['1', '2']), 'CPOL6': single('CPOL', 'CPOL6', 'C', ['+', '-'], ['1', '2']),
 'CPOL5': single('CPOL', 'CPOL5', 'C', ['+', '-'], ['1', '2']), 'CTANT': single('CPOL', 'CTANT', 'C', ['+', '-'], ['1', '2']),
 'D41': single('D', 'DO41', 'D', ['A', 'K'], ['1', '2']), 'D35': single('D', 'DO35', 'D', ['A', 'K'], ['1', '2']),
 'LED': single('LED', 'LED5', 'LED', ['A', 'K'], ['1', '2']),
 'TIP31C': single('NPN', 'TO220', 'Q', ['B', 'C', 'E'], ['1', '2', '3']), 'TIP32C': single('PNP', 'TO220', 'Q', ['B', 'C', 'E'], ['1', '2', '3']),
 'BC547': single('NPN', 'TO92', 'Q', ['C', 'B', 'E'], ['1', '2', '3']), 'BC557': single('PNP', 'TO92', 'Q', ['C', 'B', 'E'], ['1', '2', '3']),
 'LM317T': single('REG', 'TO220', 'U', ['ADJ', 'OUT', 'IN'], ['1', '2', '3']), 'LM337T': single('REG', 'TO220', 'U', ['ADJ', 'IN', 'OUT'], ['1', '2', '3']),
 'TRIM': single('POT', 'TRIM', 'RV', ['1', '2', '3']), 'FUSE': single('FUSE', 'FUSE', 'F', ['1', '2']),
 'TERM2': single('HDR2', 'TERM2', 'J', ['1', '2']), 'TERM4': single('HDR4', 'TERM4', 'J', ['1', '2', '3', '4']), 'HDR3': single('HDR3', 'HDR3', 'J', ['1', '2', '3']),
}
def dev_of(ref):
    kind, val = N.PARTS[ref]
    if kind == 'TO220': return val
    if kind == 'TO92': return val
    return {'RES10': 'R10', 'RES1W': 'R1W', 'RES2W': 'R2W', 'RES3W': 'R3W', 'CAP': 'C', 'DO41': 'D41', 'DO35': 'D35', 'LED5': 'LED'}.get(kind, kind)
def sympin(ref, padn):
    for g, sp, pd in DEVSETS[dev_of(ref)]['connects']:
        if pd == padn: return g, sp
    raise KeyError((ref, padn))
def libraries(sch=True):
    out = '<libraries>\n<library name="%s">\n' % LIB + packages_xml()
    if sch:
        out += '<symbols>\n' + ''.join('<symbol name="%s">\n' % k + '\n'.join(L) + '\n</symbol>\n' for k, (L, p) in SYMS.items()) + '</symbols>\n<devicesets>\n'
        for nm, d in DEVSETS.items():
            out += '<deviceset name="%s" prefix="%s">\n<gates>\n' % (nm, d['prefix'])
            out += ''.join('<gate name="%s" symbol="%s" x="0" y="0" addlevel="%s"/>\n' % (g, s, l) for g, s, l in d['gates'])
            out += '</gates>\n<devices>\n<device name="" package="%s">\n<connects>\n' % d['package']
            out += '\n'.join('<connect gate="%s" pin="%s" pad="%s"/>' % c for c in d['connects'])
            out += '\n</connects>\n<technologies>\n<technology name=""/>\n</technologies>\n</device>\n</devices>\n</deviceset>\n'
        out += '</devicesets>\n'
    return out + '</library>\n</libraries>\n'
HEAD = '<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE eagle SYSTEM "eagle.dtd">\n<eagle version="9.6.2">\n<drawing>\n<settings>\n<setting alwaysvectorfont="no"/>\n<setting verticaltext="up"/>\n</settings>\n<grid distance="1.27" unitdist="mm" unit="mm" style="lines" multiple="1" display="yes" altdistance="0.635" altunitdist="mm" altunit="mm"/>\n'
TAIL = '</drawing>\n</eagle>\n'
ROWS = [('Entrada y rectificadores', ['J1', 'F2', 'D1', 'D2', 'C1', 'C2', 'J3']),
        ('Limitador +16 V', ['RSC1', 'Q1', 'Q2', 'R3', 'C5']), ('Regulador +16 V', ['U1', 'R5', 'R7', 'RV1', 'C7', 'D3', 'D4']),
        ('Salida +16 V', ['C9', 'C10', 'D7', 'R12', 'LED1', 'J2']),
        ('Limitador -16 V', ['RSC2', 'Q3', 'Q4', 'R4', 'C6']), ('Regulador -16 V', ['U2', 'R6', 'R8', 'RV2', 'C8', 'D5', 'D6']),
        ('Salida -16 V', ['C11', 'C12', 'D8', 'R13', 'LED2']),
        ('Rama +5 V', ['R9', 'C13', 'C14', 'U3', 'R10', 'R11', 'RV3']), ('Salida +5 V', ['C15', 'D9', 'D10', 'C16', 'C17', 'D11', 'R14', 'LED3'])]
def sch_xml():
    flat = [r for _, rr in ROWS for r in rr]; assert sorted(flat) == sorted(N.PARTS), set(flat) ^ set(N.PARTS)
    pos = {}; plain = ''; inst = ''
    for ri, (title, refs) in enumerate(ROWS):
        y = -ri*30.48 - 15.24
        plain += '<text x="5.08" y="%s" size="2.54" layer="97">%s</text>\n' % (f(y+11.43), escape(title))
        for ci, ref in enumerate(refs):
            x = 20.32 + ci*40.64; pos[ref] = (x, y)
            inst += '<instance part="%s" gate="G$1" x="%s" y="%s"/>\n' % (ref, f(x), f(y))
    nets = collections.defaultdict(list)
    for net, pins in N.NETS.items():
        for ref, pd in pins:
            g, sp = sympin(ref, pd); sym = DEVSETS[dev_of(ref)]['gates'][0][1]
            px, py, d = SYMS[sym][1][sp]; x, y = pos[ref]; px += x; py += y; Lw = 10.16; rot = ''
            if d == 'L': ex, ey = px-Lw, py; lab = (ex, ey)
            elif d == 'R': ex, ey = px+Lw, py; lab = (px+1.27, py)
            elif d == 'U': ex, ey = px, py+5.08; lab = (ex, ey); rot = ' rot="R90"'
            else: ex, ey = px, py-5.08; lab = (ex, ey); rot = ' rot="R270"'
            nets[net].append('<segment>\n<pinref part="%s" gate="%s" pin="%s"/>\n' % (ref, g, sp) + wire(px, py, ex, ey, 0.1524, 91) + '\n<label x="%s" y="%s" size="1.27" layer="95"%s/>\n</segment>\n' % (f(lab[0]), f(lab[1]), rot))
    netxml = ''.join('<net name="%s" class="0">\n' % n + ''.join(s) + '</net>\n' for n, s in nets.items())
    plain += '<text x="5.08" y="12.7" size="3.81" layer="97">Fuente ±16 V / +5 V para los 4 PID del levitador (conexiones por etiquetas de red; ver esquematicos/ para el dibujo)</text>\n'
    parts = ''.join('<part name="%s" library="%s" deviceset="%s" device="" value="%s"/>\n' % (r, LIB, dev_of(r), escape(N.PARTS[r][1])) for r in N.PARTS)
    out = HEAD + layers_xml() + '<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">\n<description>Fuente ±16 V / +5 V - Brahiam Alberto Campiño Romero</description>\n'
    out += libraries(True) + '<attributes>\n</attributes>\n<variantdefs>\n</variantdefs>\n<classes>\n<class number="0" name="default" width="0" drill="0"/>\n</classes>\n<parts>\n' + parts + '</parts>\n<sheets>\n<sheet>\n<plain>\n' + plain + '</plain>\n<instances>\n' + inst + '</instances>\n<busses>\n</busses>\n<nets>\n' + netxml + '</nets>\n</sheet>\n</sheets>\n</schematic>\n' + TAIL
    return out
def merge_edges(edges, layer):
    Hh = collections.defaultdict(set); V = collections.defaultdict(set)
    for a, b in edges:
        if a[0] != layer: continue
        (i0, j0), (i1, j1) = (a[1], a[2]), (b[1], b[2])
        if j0 == j1:
            if i0 > i1: i0, i1 = i1, i0
            for i in range(i0, i1): Hh[j0].add(i)
        else:
            if j0 > j1: j0, j1 = j1, j0
            for j in range(j0, j1): V[i0].add(j)
    segs = []
    for j, s in sorted(Hh.items()):
        s = sorted(s); st = pr = s[0]
        for v in s[1:]+[None]:
            if v is None or v != pr+1:
                segs.append((st*G, j*G, (pr+1)*G, j*G))
                if v is not None: st = v
            if v is not None: pr = v
    for i, s in sorted(V.items()):
        s = sorted(s); st = pr = s[0]
        for v in s[1:]+[None]:
            if v is None or v != pr+1:
                segs.append((i*G, st*G, i*G, (pr+1)*G))
                if v is not None: st = v
            if v is not None: pr = v
    return segs
def brd_xml(parts, routes, W, H, holes=(), labels=()):
    plain = ''.join(wire(*a, 0, 20)+'\n' for a in [(0, 0, W, 0), (W, 0, W, H), (W, H, 0, H), (0, H, 0, 0)])
    for (x, y) in holes: plain += '<hole x="%s" y="%s" drill="3.2"/>\n' % (f(x), f(y))
    for (x, y, t, size, rot) in labels: plain += '<text x="%s" y="%s" size="%s" layer="21"%s>%s</text>\n' % (f(x), f(y), f(size), '' if rot == 'R0' else ' rot="%s"' % rot, escape(t))
    elems = ''.join('<element name="%s" library="%s" package="%s" value="%s" x="%s" y="%s"%s/>\n' % (ref, LIB, p.kind, escape(N.PARTS[ref][1]), f(p.x), f(p.y), '' if p.r % 4 == 0 else ' rot="R%d"' % (90*(p.r % 4))) for ref, p in parts.items())
    sig = ''
    for net, pins in N.NETS.items():
        sig += '<signal name="%s">\n' % net + ''.join('<contactref element="%s" pad="%s"/>\n' % (r, p) for r, p in pins)
        rt = routes.get(net)
        if rt:
            for s in merge_edges(rt['edges'], 0): sig += wire(*s, N.width_of(net), 16)+'\n'
            for s in merge_edges(rt['edges'], 1): sig += wire(*s, 0.6, 1)+'\n'
            for (i, j) in sorted(rt['vias']): sig += '<via x="%s" y="%s" extent="1-16" drill="%s" diameter="%s"/>\n' % (f(i*G), f(j*G), f(DRILL), f(PAD_D))
        sig += '</signal>\n'
    dr = '<designrules name="default">\n<description>Placa de una cara para quemado casero (tóner)</description>\n'
    for k, v in (('layerSetup', '(1*16)'), ('mdWireWire', '0.4mm'), ('mdWirePad', '0.4mm'), ('mdWireVia', '0.4mm'), ('mdPadPad', '0.4mm'), ('mdPadVia', '0.4mm'), ('mdViaVia', '0.4mm'),
                 ('mdCopperDimension', '0.6mm'), ('msWidth', '0.8mm'), ('msDrill', '0.9mm')):
        dr += '<param name="%s" value="%s"/>\n' % (k, v)
    dr += '</designrules>\n'
    out = HEAD + layers_xml() + '<board>\n<description>Fuente ±16 V / +5 V, una cara (cobre inferior) con puentes de alambre</description>\n<plain>\n' + plain + '</plain>\n'
    out += libraries(False) + '<attributes>\n</attributes>\n<variantdefs>\n</variantdefs>\n<classes>\n<class number="0" name="default" width="0.8" drill="0.9"/>\n</classes>\n'
    out += dr + '<elements>\n' + elems + '</elements>\n<signals>\n' + sig + '</signals>\n</board>\n' + TAIL
    return out
