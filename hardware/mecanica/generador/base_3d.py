#!/usr/bin/env python3
"""Genera los STL de la base impresa en 3D del levitador magnético.

Piezas (medidas en mm, origen en el centro de cada pieza, z hacia arriba):
  soporte_bobinas.stl  plantilla con 4 alojamientos para las bobinas + 4 postes
  tapa_bobinas.stl     tapa de 2,5 mm que sujeta las bobinas (se atornilla a los postes)
  bandeja_baqueta.stl  bandeja para una baqueta de 200x150 (imprimir 2)

Uso:  python3 base_3d.py [carpeta_de_salida]
Requiere: trimesh, manifold3d
"""
import sys, os
import numpy as np
import trimesh

# ---------------- parámetros medidos / de diseño ----------------
D_FL   = 36.0     # diámetro de las pestañas (flanges) de la bobina
H_BOB  = 29.0     # altura de la bobina = 23 bobinado + 2x3 pestañas
D_NUC  = 6.0      # núcleo de hierro Ø6 x 45 (sobresale 8 mm por cada lado)
L_NUC  = 45.0
SEP    = 37.0     # separación entre centros de bobinas vecinas
C      = SEP / 2  # 18,5 -> centros en (+-C, +-C)
HOLG   = 0.25     # holgura radial del alojamiento
PROF   = 8.0      # profundidad del alojamiento
PISO   = L_NUC / 2 - H_BOB / 2   # 8 mm: el núcleo queda a ras del fondo
PLACA  = PISO + PROF             # 16 mm
LADO   = 120.0
H      = LADO / 2
POST_X = 52.0     # postes en (+-52,0) y (0,+-52)
Z_TOP  = PISO + H_BOB            # 37: parte alta de las bobinas
TAPA_E = 2.5

SEC = 96

def cyl(x, y, z0, z1, d):
    m = trimesh.creation.cylinder(radius=d / 2, height=z1 - z0, sections=SEC)
    m.apply_translation([x, y, (z0 + z1) / 2])
    return m

def box(x0, x1, y0, y1, z0, z1):
    m = trimesh.creation.box(extents=[x1 - x0, y1 - y0, z1 - z0])
    m.apply_translation([(x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2])
    return m

def union(ms):
    return trimesh.boolean.union(ms, engine="manifold")

def diff(a, ms):
    return trimesh.boolean.difference([a] + list(ms), engine="manifold")

CENTROS = [(sx * C, sy * C) for sx in (-1, 1) for sy in (-1, 1)]
POSTES  = [(POST_X, 0), (-POST_X, 0), (0, POST_X), (0, -POST_X)]

def soporte():
    base = union([box(-H, H, -H, H, 0, PLACA)] +
                 [cyl(px, py, PLACA - 0.1, Z_TOP, 10.0) for px, py in POSTES])
    cortes = []
    # alojamientos (union de círculos + cruz para eliminar paredes de <1 mm)
    for cx, cy in CENTROS:
        cortes.append(cyl(cx, cy, PISO, PLACA + 1, D_FL + 2 * HOLG))
    cortes.append(box(-C, C, -C, C, PISO, PLACA + 1))
    for s in (-1, 1):
        cortes.append(box(-C, C, s * C - 4, s * C + 4, PISO, PLACA + 1))
        cortes.append(box(s * C - 4, s * C + 4, -C, C, PISO, PLACA + 1))
    # núcleos (Ø6 -> agujero Ø7) a través del piso
    for cx, cy in CENTROS:
        cortes.append(cyl(cx, cy, -1, PISO + 1, D_NUC + 1.0))
    # canal para los cables de cada bobina, hacia el lado exterior
    for cx, cy in CENTROS:
        x1 = H + 1 if cx > 0 else -H - 1
        cortes.append(box(min(cx, x1), max(cx, x1), cy - 4, cy + 4, PISO, PLACA + 1))
    # hueco central (cables / sin interferencia)
    cortes.append(cyl(0, 0, -1, PLACA + 1, 14.0))
    # tornillos M4 de fijación (con avellanado) en (+-52, +-45)
    for sx in (-1, 1):
        for sy in (-1, 1):
            cortes.append(cyl(sx * 52, sy * 45, -1, PLACA + 1, 4.5))
            cortes.append(cyl(sx * 52, sy * 45, PLACA - 3.0, PLACA + 1, 8.5))
    # agujero piloto M3 (autorroscante) en cada poste
    for px, py in POSTES:
        cortes.append(cyl(px, py, Z_TOP - 12, Z_TOP + 1, 2.6))
    return diff(base, cortes)

def tapa():
    base = box(-H, H, -H, H, 0, TAPA_E)
    cortes = [cyl(cx, cy, -1, TAPA_E + 1, 32.0) for cx, cy in CENTROS]
    cortes.append(cyl(0, 0, -1, TAPA_E + 1, 14.0))
    for px, py in POSTES:
        cortes.append(cyl(px, py, -1, TAPA_E + 1, 3.4))
        cortes.append(cyl(px, py, TAPA_E - 1.2, TAPA_E + 1, 6.5))
    return diff(base, cortes)

def bandeja():
    LX, LY, E = 214.0, 164.0, 4.0
    hx, hy = LX / 2, LY / 2
    ms = [box(-hx, hx, -hy, hy, 0, E),
          box(-hx, -hx + 2, -hy, hy, 0, E + 4),      # lateral izq
          box(hx - 2, hx, -hy, hy, 0, E + 4),        # lateral der
          box(-hx, hx, hy - 2, hy, 0, E + 4)]        # trasero
    soportes = [(sx * 96, sy * 71) for sx in (-1, 1) for sy in (-1, 1)] + [(0, 71), (0, -71)]
    for x, y in soportes:
        ms.append(cyl(x, y, E - 0.1, E + 8, 8.0))
    base = union(ms)
    cortes = [cyl(x, y, E + 8 - 7, E + 9, 2.8) for x, y in soportes]
    for sx in (-1, 1):
        for sy in (-1, 1):
            cortes.append(cyl(sx * 50, sy * 40, -1, E + 1, 4.5))
            cortes.append(cyl(sx * 50, sy * 40, E - 2.5, E + 1, 8.5))
    return diff(base, cortes)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(out, exist_ok=True)
    for nombre, f in (("soporte_bobinas", soporte), ("tapa_bobinas", tapa), ("bandeja_baqueta", bandeja)):
        m = f()
        m.export(os.path.join(out, nombre + ".stl"))
        print(f"{nombre}: watertight={m.is_watertight} volumen={m.volume/1000:.1f} cm3 "
              f"dim={np.round(m.extents,1)} mm")
