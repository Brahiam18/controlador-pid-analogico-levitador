"""Colocación de la placa de la fuente: piezas fijas a mano (entrada, condensadores grandes,
TO-220 en los bordes para el disipador, borneras) y el resto por recocido simulado dentro de
regiones por etapa (+16 V, -16 V, +5 V)."""
import random, math
from engine import *
import netlist as N

W, H = 165.1, 109.22          # mm (65 x 43 pasos de 2.54): cabe en una baquela de 20 x 15 cm
FIXED = {   # ref: (x, y, giro)  giro en pasos de 90° antihorario
 'J1': (7.62, 50.8, 1), 'F2': (12.7, 58.42, 0),
 'D1': (40.64, 63.5, 1), 'D2': (40.64, 40.64, 1),
 'C1': (15.24, 83.82, 0), 'C2': (15.24, 25.4, 0),
 'J3': (48.26, 58.42, 3),
 'Q1': (60.96, 101.6, 0), 'U1': (81.28, 101.6, 0),      # disipador superior (aleta hacia el borde)
 'Q3': (66.04, 7.62, 2), 'U2': (86.36, 7.62, 2),         # disipador inferior
 'U3': (127.0, 101.6, 0),
 'J2': (157.48, 40.64, 1),
}
REG = {   # región (xmin, ymin, xmax, ymax) de cada grupo
 'pos': (40, 62, 112, 96), 'neg': (40, 14, 150, 50), 'p5': (112, 56, 150, 96),
}
GROUP = {}
for r in ('RSC1','Q2','R3','C5','R5','R7','RV1','C7','D3','D4','C9','C10','D7','R12','LED1'): GROUP[r] = 'pos'
for r in ('RSC2','Q4','R4','C6','R6','R8','RV2','C8','D5','D6','C11','C12','D8','R13','LED2'): GROUP[r] = 'neg'
for r in ('R9','C13','C14','R10','R11','RV3','C15','D9','D10','C16','C17','D11','R14','LED3'): GROUP[r] = 'p5'
assert set(FIXED) | set(GROUP) == set(N.PARTS), set(N.PARTS) ^ (set(FIXED) | set(GROUP))
MARGIN = 1.5
HOLES = [(4.0, 4.0), (W-4.0, 4.0), (4.0, H-4.0), (W-4.0, H-4.0)]   # agujeros de montaje de 3.2 mm
def snap(v): return round(v/PITCH)*PITCH

def make(seed):
    rng = random.Random(seed); parts = {}
    for ref, (kind, val) in N.PARTS.items():
        if ref in FIXED:
            x, y, r = FIXED[ref]; parts[ref] = Placed(ref, kind, x, y, r)
        else:
            x0, y0, x1, y1 = REG[GROUP[ref]]
            parts[ref] = Placed(ref, kind, snap(rng.uniform(x0, x1)), snap(rng.uniform(y0, y1)), rng.choice([0, 1, 2, 3]))
    return parts, [r for r in parts if r not in FIXED]

def cost(parts):
    c = 0.0
    for name, pins in N.NETS.items():
        xs = []; ys = []
        for ref, pin in pins:
            x, y = parts[ref].pads()[pin]; xs.append(x); ys.append(y)
        w = 0.35 if name == 'GND' else (2.0 if name in N.WIDE else 1.0)
        c += w*((max(xs)-min(xs)) + (max(ys)-min(ys)))
    bx = {r: p.box() for r, p in parts.items()}; refs = list(parts); pen = 0
    for i, a in enumerate(refs):
        A = bx[a]
        if A[0] < MARGIN or A[1] < MARGIN or A[2] > W-MARGIN or A[3] > H-MARGIN: pen += 2 + max(0, MARGIN-A[0]) + max(0, MARGIN-A[1]) + max(0, A[2]-W+MARGIN) + max(0, A[3]-H+MARGIN)
        if a in GROUP:
            x0, y0, x1, y1 = REG[GROUP[a]]; cx = (A[0]+A[2])/2; cy = (A[1]+A[3])/2
            pen += 0.05*(max(0, x0-cx) + max(0, cx-x1) + max(0, y0-cy) + max(0, cy-y1))
        for b in refs[i+1:]:
            B = bx[b]
            ox = min(A[2], B[2]) - max(A[0], B[0]); oy = min(A[3], B[3]) - max(A[1], B[1])
            if ox > -0.6 and oy > -0.6: pen += 1 + (ox+0.6)*(oy+0.6)/40
    return c + pen*300

def anneal(seed, iters=40000):
    rng = random.Random(seed); parts, free = make(seed)
    cur = cost(parts); best = cur; bst = None
    for it in range(iters):
        T = 50.0*(1-it/iters)**2 + 0.2
        r = rng.choice(free); p = parts[r]; old = (p.x, p.y, p.r); m = rng.random()
        if m < 0.65:
            p.x += rng.choice([-3, -2, -1, 1, 2, 3])*PITCH*(rng.random() < .5); p.y += rng.choice([-3, -2, -1, 1, 2, 3])*PITCH*(rng.random() < .5)
        elif m < 0.85: p.r = (p.r + rng.choice([1, 2, 3])) % 4
        else:
            x0, y0, x1, y1 = REG[GROUP[r]]; p.x = snap(rng.uniform(x0, x1)); p.y = snap(rng.uniform(y0, y1))
        nc = cost(parts)
        if nc <= cur or rng.random() < math.exp((cur-nc)/T): cur = nc
        else: p.x, p.y, p.r = old
        if cur < best - 1e-9: best = cur; bst = {k: (v.x, v.y, v.r) for k, v in parts.items()}
    for k, (x, y, r) in bst.items(): parts[k].x, parts[k].y, parts[k].r = x, y, r
    return parts, best
