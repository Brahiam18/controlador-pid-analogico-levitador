"""Cambio incremental de la placa v2.1 -> v2.2 sin rehacer el ruteo:
  * R7 y R15 pasan a ser dos resistencias en paralelo (R7A ‖ R7B, R15A ‖ R15B, 2 x 5,6 Ω / 1 W).
  * 15 puntos de prueba (TP1..TP15) para medir con el multímetro.
Cada pieza nueva se coloca en un hueco libre y se une a la pista existente de su red con una pista corta en la
cara de cobre (sin puentes). Uso: python3 incremental.py placa_ruteada.json placa_ruteada.json"""
import sys, json, heapq, math
sys.path.insert(0, '.')
from shapely.geometry import Point, LineString, box
from shapely.ops import unary_union
from shapely.strtree import STRtree
from engine import *
import netlist as N, place as P
from eagle import merge_edges

CLR = 0.55          # holgura mínima para lo nuevo (mm)
MARG = 2.0          # cobre a borde de placa
src, dst = sys.argv[1], sys.argv[2]
js = json.load(open(src))
ren = {'R7': 'R7A', 'R15': 'R15A'}
parts = {ren.get(k, k): Placed(ren.get(k, k), v[0], v[1], v[2], v[3]) for k, v in js['parts'].items()}
routes = {n: dict(edges={(tuple(a), tuple(b)) for a, b in rt['edges']}, vias={tuple(v) for v in rt['vias']}, nodes={tuple(x) for x in rt['nodes']}) for n, rt in js['routes'].items()}
pad_net = {(r, p): n for n, pins in N.NETS.items() for r, p in pins}

def copper():
    """geometría de cobre inferior por red: lista (net, geom)"""
    g = []
    for ref, p in parts.items():
        for pin, (x, y) in p.pads().items(): g.append((pad_net[(ref, pin)], Point(x, y).buffer(pad_d(p.kind)/2)))
    for net, rt in routes.items():
        for s in merge_edges(rt['edges'], 0): g.append((net, LineString([(s[0], s[1]), (s[2], s[3])]).buffer(N.width_of(net)/2)))
        for (i, j) in rt['vias']: g.append((net, Point(i*G, j*G).buffer(PAD_D/2)))
    for (hx, hy) in P.HOLES: g.append(('HOLE', Point(hx, hy).buffer(3.6)))
    return g

class Obst:
    def __init__(s):
        s.g = copper(); s.tree = STRtree([x for _, x in s.g])
        s.bodies = [p.box() for p in parts.values()]
        s.top = [(n, LineString([(a[0], a[1]), (a[2], a[3])])) for n, rt in routes.items() for a in merge_edges(rt['edges'], 1)]
    def top_ok(s, geom, net):
        return all(n == net or geom.distance(l) >= 0.8 for n, l in s.top)
    def clear(s, geom, net, c=CLR):
        for k in s.tree.query(geom.buffer(c)):
            n, g = s.g[k]
            if n != net and geom.distance(g) < c: return False
        return True
    def body_ok(s, b, m=0.6):
        if b[0] < MARG or b[1] < MARG or b[2] > P.W-MARG or b[3] > P.H-MARG: return False
        for q in s.bodies:
            if min(b[2], q[2])+m > max(b[0], q[0]) and min(b[3], q[3])+m > max(b[1], q[1]): return False
        return True

def stub(ob, net, start, maxlen=70):
    """Dijkstra en la cara de cobre desde la celda start hasta cualquier nodo existente de la red."""
    w = N.width_of(net)
    tg = {(n[1], n[2]) for n in routes.get(net, {'nodes': ()})['nodes'] if n[0] == 0}
    for (r, p), n in pad_net.items():
        if n == net and r in parts:
            x, y = parts[r].pads()[p]; c = (round(x/G), round(y/G))
            if c != start: tg.add(c)
    ok = {}
    def free(c):
        if c not in ok:
            x, y = c[0]*G, c[1]*G
            ok[c] = (MARG+w/2 <= x <= P.W-MARG-w/2 and MARG+w/2 <= y <= P.H-MARG-w/2 and ob.clear(Point(x, y).buffer(w/2), net))
        return ok[c]
    dist = {start: 0}; prev = {}; pq = [(0, start, None)]
    while pq:
        d, u, pd = heapq.heappop(pq)
        if d > dist[u]: continue
        if u in tg and u != start: break
        if d > maxlen: return None
        for k, (di, dj) in enumerate(((1, 0), (-1, 0), (0, 1), (0, -1))):
            v = (u[0]+di, u[1]+dj)
            if v not in tg and not free(v): continue
            if v in tg and not free(v) and not ob.clear(LineString([(u[0]*G, u[1]*G), (v[0]*G, v[1]*G)]).buffer(w/2), net): continue
            nd = d+1+(0.5 if pd is not None and pd != k else 0)
            if nd < dist.get(v, 1e9): dist[v] = nd; prev[v] = u; heapq.heappush(pq, (nd, v, k))
    else: return None
    path = [u]
    while u != start: u = prev[u]; path.append(u)
    # comprobar el trazo completo
    if len(path) > 1:
        ln = LineString([(c[0]*G, c[1]*G) for c in path]).buffer(w/2)
        if not ob.clear(ln, net): return None
    return path[::-1], dist[path[0]]

def commit(net, path):
    rt = routes.setdefault(net, dict(edges=set(), vias=set(), nodes=set()))
    for a, b in zip(path, path[1:]): rt['edges'].add(((0,)+a, (0,)+b))
    for c in path: rt['nodes'].add((0,)+c)

def place(ref, kind, near, radius, rots=(0, 1, 2, 3), wlen=1.0, wdist=0.15, bm=0.6):
    nets = [pad_net[(ref, p)] for p, _, _ in fp_pads(kind)]
    best = None; ob = Obst()
    cx, cy = near
    for i in range(int((cx-radius)/G), int((cx+radius)/G)+1):
        for j in range(int((cy-radius)/G), int((cy+radius)/G)+1):
            for r in rots:
                p = Placed(ref, kind, i*G, j*G, r)
                if not ob.body_ok(p.box(), bm): continue
                pads = p.pads()
                if not all(ob.clear(Point(*pads[pin]).buffer(pad_d(kind)/2), net) and ob.top_ok(Point(*pads[pin]).buffer(pad_d(kind)/2), net) for pin, net in zip(sorted(pads), nets)): continue
                d0 = math.hypot(i*G-cx, j*G-cy)
                if best and wdist*d0 >= best[0]: continue
                tot = wdist*d0; paths = []
                for pin, net in zip(sorted(pads), nets):
                    x, y = pads[pin]; res = stub(ob, net, (round(x/G), round(y/G)))
                    if res is None: break
                    paths.append((net, res[0])); tot += wlen*res[1]
                else:
                    if best is None or tot < best[0]: best = (tot, p, paths)
    if not best:
        print('SIN LUGAR', ref); return False
    parts[ref] = best[1]
    for net, path in best[2]: commit(net, path)
    print('%-5s %-6s en (%.2f, %.2f) giro %d, pista nueva %.1f mm' % (ref, kind, best[1].x, best[1].y, best[1].r, sum(len(pp)-1 for _, pp in best[2])*G))
    return True

# resistencias en paralelo: junto a R7A / R15A
if 'R7B' not in parts:
    r7 = parts['R7A']; place('R7B', 'RES1W', (r7.x+7.6, r7.y), 34)
if 'R15B' not in parts:
    r15 = parts['R15A']; place('R15B', 'RES1W', (r15.x, r15.y+7.6), 34)
# puntos de prueba: cerca del componente donde se mide
def padxy(ref, pin): return parts[ref].pads()[pin]
NEAR = {'TP1': padxy('RSC1', '1'), 'TP2': padxy('RSC1', '2'), 'TP3': padxy('Q4', '3'), 'TP4': padxy('U1', '3'), 'TP5': padxy('J4', '1'),
        'TP6': padxy('RSC2', '1'), 'TP7': padxy('RSC2', '2'), 'TP8': padxy('Q8', '3'), 'TP9': padxy('U2', '2'), 'TP10': padxy('J5', '1'),
        'TP11': padxy('U3', '3'), 'TP12': padxy('J2B', '2'), 'TP13': (125, 100), 'TP14': (130, 40), 'TP15': (170, 80)}
SKIP = []
for tp in sorted(NEAR, key=lambda t: int(t[2:])):
    if not place(tp, 'TP', NEAR[tp], 22, rots=(0,), wdist=0.25):
        if not place(tp, 'TP', NEAR[tp], 45, rots=(0,), wdist=0.1):
            if not place(tp, 'TP', NEAR[tp], 30, rots=(0,), wdist=0.1, bm=-1.2): SKIP.append(tp)
SKIP = SKIP if 'SKIP' in dir() else []
print('omitidos:', SKIP)
json.dump(dict(js, parts={k: (v.kind, v.x, v.y, v.r) for k, v in parts.items()},
               routes={n: dict(edges=[[list(a), list(c)] for a, c in rt['edges']], vias=[list(v) for v in rt['vias']], nodes=[list(x) for x in rt['nodes']]) for n, rt in routes.items()}),
          open(dst, 'w'))
print('guardado', dst)
