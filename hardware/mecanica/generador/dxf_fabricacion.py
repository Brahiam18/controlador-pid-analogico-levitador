"""Genera base_mdf_fabricacion.dxf: todas las piezas de MDF en un solo dibujo (mm, AutoCAD R2010), listo para enviar a corte.
Capas: CORTE (contorno exterior, pasante), TALADRO_PASANTE, TALADRO_CIEGO (con profundidad en el texto), GRABADO (0,5 mm, no cortar), TEXTO."""
import os, math, ezdxf
from base_mdf import PL, PT, COILS, HOLE_ROD_D, CABLE_D, CABLE_OFF, SCREW_D, SCREW_OFF, PED_HOLE_D, FL_D, SENS_XY, BB_W, BB_D, LEG_H, PLATE_C
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
d = ezdxf.new("R2010"); d.units = ezdxf.units.MM
for n, c in (("CORTE", 7), ("TALADRO_PASANTE", 1), ("TALADRO_CIEGO", 6), ("GRABADO", 3), ("TEXTO", 8)): d.layers.add(n, color=c)
m = d.modelspace()
def rect(x0, y0, w, h, layer):
    m.add_lwpolyline([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)], close=True, dxfattribs={"layer": layer})
def circ(x, y, dia, layer): m.add_circle((x, y), dia / 2, dxfattribs={"layer": layer})
def txt(x, y, s, h=4): m.add_text(s, dxfattribs={"layer": "TEXTO", "height": h, "insert": (x, y)})
# 1) Tablero base 400 x 260 x 15 (origen en esquina inferior izquierda)
rect(0, 0, BB_W, BB_D, "CORTE")
px, py = PLATE_C
for sx in (-SCREW_OFF, SCREW_OFF):
    for sy in (-SCREW_OFF, SCREW_OFF): circ(px + sx, py + sy, SCREW_D, "TALADRO_PASANTE")
txt(0, BB_D + 6, "1. TABLERO BASE  400 x 260 x 15 mm MDF  (cant. 1)  - 4 taladros pasantes D4.2", 5)
# 2) Placa del levitador 150 x 150 x 15 (centro en ox, oy)
ox, oy = 440 + PL / 2, PL / 2
rect(ox - PL / 2, oy - PL / 2, PL, PL, "CORTE")
for n, (x, y) in COILS.items():
    circ(ox + x, oy + y, HOLE_ROD_D, "TALADRO_CIEGO")                                            # D7, 9 mm de profundidad
    circ(ox + x, oy + y, FL_D + 0.4, "GRABADO")                                                 # ubica el carrete
    hx, hy = math.copysign(CABLE_OFF, x), math.copysign(CABLE_OFF, y)
    circ(ox + hx, oy + hy, CABLE_D, "TALADRO_PASANTE")                                          # D8 pasante
    sx, sy = math.copysign(SCREW_OFF, x), math.copysign(SCREW_OFF, y)
    circ(ox + sx, oy + sy, SCREW_D, "TALADRO_PASANTE")                                          # D4.2 pasante
    kx, ky = math.copysign(SENS_XY, x), math.copysign(SENS_XY, y)
    rect(ox + kx - 2, oy + ky - 2, 4, 4, "GRABADO")                                             # marca del sensor
circ(ox, oy, PED_HOLE_D, "TALADRO_CIEGO")                                                       # D12.2, 8 mm
txt(440, PL + 6, "2. PLACA DEL LEVITADOR  150 x 150 x 15 mm MDF  (cant. 1)", 5)
txt(440, -22, "D7 CIEGO prof. 9 (x4) | D12.2 CIEGO prof. 8 (centro) | D8 pasante (x4) | D4.2 pasante (x4)", 3.5)
txt(440, -28, "GRABADO = marcas de 0.5 mm de profundidad (circulos D36.4 y cuadros de 4 x 4); NO cortar", 3.5)
# 3) Postes: 4 piezas de 15 x 55 (de MDF de 15 mm -> poste 15 x 15 x 55)
for i in range(4): rect(440 + i * 25, 190, 15, LEG_H, "CORTE")
txt(440, 190 + LEG_H + 6, "3. POSTES  15 x 55 mm MDF de 15 mm  (cant. 4)", 5)
txt(0, -22, "Material: MDF 15 mm. Unidades: mm. Escala 1:1. Origen del tablero en la esquina inferior izquierda.", 3.5)
d.saveas(os.path.join(OUT, "base_mdf_fabricacion.dxf"))
print("ok")
