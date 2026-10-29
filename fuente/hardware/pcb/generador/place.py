"""Colocación de la placa v2 (±16 V / 1,5 A): piezas grandes y de disipador fijas a mano; el resto por
recocido simulado dentro de regiones por etapa."""
import random, math
from engine import *
import netlist as N

W, H = 190.5, 139.7            # mm (75 x 55 pasos de 2.54): cabe en una baquela de 20 x 15 cm
FIXED = {   # ref: (x, y, giro)
 'J1': (6.35, 71.12, 1), 'F2': (15.24, 88.9, 0), 'F3': (15.24, 68.58, 0),
 'C1': (17.78, 116.84, 0), 'C2A': (10.16, 49.53, 0), 'C2B': (10.16, 20.32, 0),
 'D1': (45.72, 96.52, 1), 'D2': (53.34, 96.52, 1), 'D3': (45.72, 50.8, 1), 'D4': (53.34, 50.8, 1),
 'J3': (35.56, 78.74, 0),
 # disipador superior (aletas hacia el borde de arriba)
 'Q1': (66.04, 132.08, 0), 'Q2': (81.28, 132.08, 0), 'Q4': (96.52, 132.08, 0), 'U1': (111.76, 132.08, 0),
 # disipador inferior
 'Q5': (71.12, 7.62, 2), 'Q6': (86.36, 7.62, 2), 'Q8': (101.6, 7.62, 2), 'U2': (116.84, 7.62, 2),
 'U3': (160.02, 132.08, 0),
 'J2': (182.88, 58.42, 1), 'J4': (182.88, 96.52, 1), 'J5': (182.88, 30.48, 1),
}
REG = {'pos': (60, 80, 150, 124), 'neg': (35, 16, 160, 50), 'p5': (148, 70, 176, 124), 'mid': (55, 56, 172, 84)}
GROUP = {}
for r in ('RSC1','Q3','R3','R4','R5','R6','R7','C5','R8','R9','RV1','C6','D5','D6','C7','C8','C9','D7','R10','LED1','C3'): GROUP[r] = 'pos'
for r in ('RSC2','Q7','R11','R12','R13','R14','R15','C10','R16','R17','RV2','C11','D8','D9','C12','C13','C14','D10','R18','LED2','C4'): GROUP[r] = 'neg'
for r in ('R19','C15','C16','R20','R21','RV3','C17','D11','D12','C18','C19','D13','R22','LED3'): GROUP[r] = 'p5'
assert set(FIXED) | set(GROUP) == set(N.PARTS), set(N.PARTS) ^ (set(FIXED) | set(GROUP))
MARGIN = 1.5
HOLES = [(4.0, 4.0), (W-4.0, 4.0), (4.0, H-4.0), (W-4.0, H-4.0)]
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
        w = 0.3 if name == 'GND' else (2.0 if name in N.WIDE else 1.0)
        c += w*((max(xs)-min(xs)) + (max(ys)-min(ys)))
    bx = {r: p.box() for r, p in parts.items()}; refs = list(parts); pen = 0
    for i, a in enumerate(refs):
        A = bx[a]
        if A[0] < MARGIN or A[1] < MARGIN or A[2] > W-MARGIN or A[3] > H-MARGIN: pen += 2 + max(0, MARGIN-A[0]) + max(0, MARGIN-A[1]) + max(0, A[2]-W+MARGIN) + max(0, A[3]-H+MARGIN)
        for (hx, hy) in HOLES:
            if A[0]-5 < hx < A[2]+5 and A[1]-5 < hy < A[3]+5: pen += 3
        if a in GROUP:
            x0, y0, x1, y1 = REG[GROUP[a]]; cx = (A[0]+A[2])/2; cy = (A[1]+A[3])/2
            pen += 0.05*(max(0, x0-cx) + max(0, cx-x1) + max(0, y0-cy) + max(0, cy-y1))
        for b in refs[i+1:]:
            B = bx[b]
            ox = min(A[2], B[2]) - max(A[0], B[0]); oy = min(A[3], B[3]) - max(A[1], B[1])
            if ox > -0.8 and oy > -0.8: pen += 1 + (ox+0.8)*(oy+0.8)/40
    return c + pen*300

def anneal(seed, iters=60000):
    rng = random.Random(seed); parts, free = make(seed)
    cur = cost(parts); best = cur; bst = None
    for it in range(iters):
        T = 60.0*(1-it/iters)**2 + 0.2
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
if __name__ == '__main__':
    import itertools
    parts, _ = make(1)
    bx = {r: parts[r].box() for r in FIXED}
    for a, b in itertools.combinations(FIXED, 2):
        A, B = bx[a], bx[b]
        if min(A[2], B[2]) > max(A[0], B[0]) and min(A[3], B[3]) > max(A[1], B[1]): print('solapan', a, b, A, B)
    for r in FIXED:
        A = bx[r]
        if A[0] < 0 or A[1] < 0 or A[2] > W or A[3] > H: print('fuera', r, A)
    print('ok fijas')
