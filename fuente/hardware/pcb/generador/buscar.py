"""Busca colocación + ruteo de la placa de la fuente. Uso: python3 buscar.py SEMILLAS(1,2,3) salida.json"""
import sys, json, time, multiprocessing as mp
sys.path.insert(0, '.')
import netlist as N, place as P
from engine import *
from pf import PF

def analyze(r):
    adj = {}
    for net, rt in r.routes.items():
        for a, b in rt['edges']:
            if a[0] == 1:
                adj.setdefault((net, a[1:]), set()).add((net, b[1:])); adj.setdefault((net, b[1:]), set()).add((net, a[1:]))
    seen = set(); comps = []
    for k in adj:
        if k in seen: continue
        st = [k]; seen.add(k); n = 0
        while st:
            u = st.pop(); n += 1
            for v in adj[u]:
                if v not in seen: seen.add(v); st.append(v)
        comps.append(n)
    bot = sum(1 for rt in r.routes.values() for a, b in rt['edges'] if a[0] == 0)
    top = sum(1 for rt in r.routes.values() for a, b in rt['edges'] if a[0] == 1)
    return len(comps), bot, top, sorted(comps)

def job(sd):
    parts, b = P.anneal(sd, 60000)
    out = None
    for rs in (1, 2):
        r = PF(P.W, P.H, parts, N.NETS, jump_cost=35, top_cost=3.0, wide=N.WIDE)
        for (hx, hy) in P.HOLES:          # zona de los agujeros de montaje: sin cobre (radio 4 mm)
            for i in range(int((hx-5)/G), int((hx+5)/G)+2):
                for j in range(int((hy-5)/G), int((hy+5)/G)+2):
                    if (i*G-hx)**2 + (j*G-hy)**2 <= 4.0**2:
                        for l in (0, 1): r.g.own[l][(i, j)] = 'HOLE'
        if not r.solve(iters=150, seed=rs): continue
        j, bot, top, comps = analyze(r)
        score = j*120 + bot*1.27 + top*1.27*3 + max(comps or [0])*30
        if out is None or score < out['score']:
            out = dict(score=score, jumpers=j, bot=bot, top=top, comps=comps, seed=sd, placecost=b,
                       parts={k: (v.kind, v.x, v.y, v.r) for k, v in parts.items()},
                       routes={n: dict(edges=[[list(a), list(c)] for a, c in rt['edges']], vias=[list(v) for v in rt['vias']], nodes=[list(n_) for n_ in rt['nodes']]) for n, rt in r.routes.items()})
    return sd, b, out

if __name__ == '__main__':
    seeds = [int(x) for x in sys.argv[1].split(',')]; dst = sys.argv[2]
    t = time.time(); best = None
    with mp.Pool(min(4, len(seeds))) as pool:
        for sd, b, o in pool.imap_unordered(job, seeds):
            print(sd, 'colocacion', round(b), None if o is None else (round(o['score']), o['jumpers'], o['bot'], o['top']), round(time.time()-t), flush=True)
            if o and (best is None or o['score'] < best['score']):
                best = o; json.dump(best, open(dst, 'w'))
    print('mejor', best and (best['seed'], best['jumpers'], round(best['score'])))
