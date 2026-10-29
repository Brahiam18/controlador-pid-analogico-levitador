"""Genera .sch, .brd, PDF de cobre y de ensamble y la lista de puentes a partir de placa_ruteada.json.
Uso: python3 build.py placa_ruteada.json ../   (escribe en la carpeta destino)"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import netlist as N, eagle as E, pdfs, place as P
from engine import *
import verify as V, xmlcheck as X
import xml.etree.ElementTree as ET

def load(path):
    js = json.load(open(path))
    parts = {k: Placed(k, v[0], v[1], v[2], v[3]) for k, v in js['parts'].items()}
    routes = {n: dict(edges={(tuple(a), tuple(b)) for a, b in rt['edges']}, vias={tuple(v) for v in rt['vias']}, nodes={tuple(x) for x in rt['nodes']}) for n, rt in js['routes'].items()}
    return parts, routes
if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    parts, routes = load(src); W, H = P.W, P.H
    nets = {n: v for n, v in N.NETS.items()}
    prob, mind, cross = V.verify(parts, routes, nets, W, H)
    assert not prob, prob[:5]
    jl = pdfs.jumpers(parts, routes)
    labels = [(W/2, 1.6, 'Fuente +-16V 1.5A / +5V (v2) - B. Campino - U. Ibague 2026', 1.2, 'R0')]
    open(os.path.join(dst, 'fuente.brd'), 'w', encoding='utf-8').write(E.brd_xml(parts, routes, W, H, P.HOLES, labels))
    open(os.path.join(dst, 'fuente.sch'), 'w', encoding='utf-8').write(E.sch_xml())
    for e in ('.brd', '.sch'): ET.parse(os.path.join(dst, 'fuente'+e))
    bad, md, ns = X.check_board(os.path.join(dst, 'fuente.brd'))
    print('xmlcheck placa:', ns, 'señales, holgura mínima %.3f mm, problemas:' % md, bad[:5])
    print('sch vs brd:', X.check_sch_vs_brd(os.path.join(dst, 'fuente.sch'), os.path.join(dst, 'fuente.brd')) or 'consistentes')
    pdfs.copper_pdf(os.path.join(dst, 'cobre_espejado_1a1.pdf'), parts, routes, W, H, P.HOLES, png=os.path.join(dst, 'img', 'cobre_espejado.png'))
    pdfs.assembly_pdf(os.path.join(dst, 'ensamble_1a1.pdf'), parts, routes, W, H, P.HOLES, jl, png=os.path.join(dst, 'img', 'ensamble.png'))
    L = ['| N.º | Red | Longitud aprox. | Extremos |', '|:-:|---|--:|---|']
    for k, j in enumerate(jl, 1): L.append('| P%d | `%s` | %d mm | %s |' % (k, j['net'], round(j['length']), ' ↔ '.join(j['ends'])))
    open(os.path.join(dst, 'puentes.md'), 'w', encoding='utf-8').write('# Puentes de alambre (lado de componentes)\n\n' + '\n'.join(L) + '\n')
    json.dump(dict(W=W, H=H, puentes=len(jl), holgura_min=mind, parts={k: [p.kind, p.x, p.y, p.r] for k, p in parts.items()}), open(os.path.join(dst, 'resumen_placa.json'), 'w'), indent=1)
    print('placa %.1f x %.1f mm | %d puentes | holgura mínima %.2f mm' % (W, H, len(jl), mind))
