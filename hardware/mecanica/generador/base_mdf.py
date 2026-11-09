#!/usr/bin/env python3
"""Genera el plano (PDF 1:1) y los DXF de la base de MDF del levitador.
Todas las medidas estan en mm. Ejecutar:  python3 base_mdf.py  (escribe en ..)
"""
import os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Circle, Rectangle
import ezdxf

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# ---------------------------------------------------------------- parametros
PL = 150.0        # lado de la placa del levitador
PT = 15.0         # espesor del MDF
FL_D = 36.0       # diametro de las pestanas del carrete
FL_T = 3.0        # espesor de cada pestana
WIND_L = 23.0     # largo del devanado entre pestanas
COIL_H = WIND_L + 2 * FL_T      # 29 mm de carrete
SP = 37.0         # separacion entre centros de bobinas (1 mm entre pestanas)
CC = SP / 2       # 18.5: centro de cada bobina en x e y
ROD_D, ROD_L = 6.0, 45.0
ROD_UP = ROD_DOWN = (ROD_L - COIL_H) / 2   # 8 mm sobre y bajo las pestanas
HOLE_ROD_D, HOLE_ROD_DEPTH = 7.0, 9.0
CABLE_OFF = CC + 25 / math.sqrt(2)         # agujero de cables a 25 mm del eje, en la diagonal
CABLE_D = 8.0
SCREW_OFF = 64.0
SCREW_D = 4.2
PED_D = 12.0
PED_HOLE_D, PED_HOLE_DEPTH = 12.2, 8.0
REST = 25.0       # imagen en reposo sobre la pestana superior
WORK = 30.0       # altura de trabajo
SENS = SP / 2 - 16 / math.sqrt(2) * 1.0    # no se usa; ver SENS_XY
SENS_XY = CC - 16 / math.sqrt(2)           # 7.19: sensor a 16 mm del eje de su bobina, hacia el centro
LEG_H = 55.0
BB_W, BB_D = 400.0, 260.0   # tablero base
BB_T = 15.0
PLATE_C = (85.0, 130.0)     # centro de la placa sobre el tablero
PED_H_ABOVE_PLATE = COIL_H + REST            # 54 mm
PED_LEN = PED_H_ABOVE_PLATE + PED_HOLE_DEPTH # 62 mm de varilla

COILS = {1: (+CC, +CC), 2: (-CC, +CC), 3: (-CC, -CC), 4: (+CC, -CC)}

# ---------------------------------------------------------------- dibujo (PDF)
class Page:
    def __init__(self, W, H, title, scale_note="Imprimir al 100 % (sin ajustar a la pagina)"):
        self.W, self.H = W, H
        self.fig = plt.figure(figsize=(W / 25.4, H / 25.4))
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, W); self.ax.set_ylim(0, H); self.ax.set_aspect("equal"); self.ax.axis("off")
        self.text(8, H - 10, title, size=13, weight="bold")
        self.text(8, H - 16.5, scale_note, size=7.5, color="#555")
    def text(self, x, y, s, size=8, ha="left", va="center", color="k", weight="normal", rot=0):
        self.ax.text(x, y, s, fontsize=size, ha=ha, va=va, color=color, weight=weight, rotation=rot)
    def line(self, x1, y1, x2, y2, lw=0.8, c="k", ls="-"):
        self.ax.plot([x1, x2], [y1, y2], color=c, lw=lw, ls=ls, solid_capstyle="butt")
    def rect(self, x, y, w, h, fc="none", ec="k", lw=1.0, ls="-", alpha=1):
        self.ax.add_patch(Rectangle((x, y), w, h, fc=fc, ec=ec, lw=lw, ls=ls, alpha=alpha))
    def circ(self, x, y, d, fc="none", ec="k", lw=0.9, ls="-"):
        self.ax.add_patch(Circle((x, y), d / 2, fc=fc, ec=ec, lw=lw, ls=ls))
    def cross(self, x, y, r=6, c="#c0392b"):
        self.line(x - r, y, x + r, y, 0.5, c); self.line(x, y - r, x, y + r, 0.5, c)
    def dim(self, x1, y1, x2, y2, off, label, size=7.5):
        """Cota entre (x1,y1) y (x2,y2) desplazada 'off' mm perpendicularmente."""
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy)
        nx, ny = -dy / L, dx / L
        a = (x1 + nx * off, y1 + ny * off); b = (x2 + nx * off, y2 + ny * off)
        for (px, py), (qx, qy) in (((x1, y1), a), ((x2, y2), b)):
            ext = 1.5 if off > 0 else -1.5
            self.line(px + nx * (0.8 if off > 0 else -0.8), py + ny * (0.8 if off > 0 else -0.8), qx + nx * ext, qy + ny * ext, 0.4, "#444")
        self.ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="<|-|>", lw=0.6, color="#222", mutation_scale=6, shrinkA=0, shrinkB=0))
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        ang = math.degrees(math.atan2(dy, dx))
        if ang > 90 or ang <= -90: ang += 180
        self.ax.text(mx + nx * 2.3, my + ny * 2.3, label, fontsize=size, ha="center", va="center", rotation=ang,
                     bbox=dict(fc="white", ec="none", pad=0.6))
    def scalebar(self, x, y, L=50):
        self.line(x, y, x + L, y, 1.2); 
        for k in range(0, int(L) + 1, 10): self.line(x + k, y - 1.5, x + k, y + 1.5, 0.8)
        self.text(x + L / 2, y - 4.5, "regla de comprobacion: %d mm" % L, size=7, ha="center")
    def save(self, pdf):
        pdf.savefig(self.fig); plt.close(self.fig)

def page1_placa():
    p = Page(210, 297, "Placa del levitador: MDF %d x %d x %d mm  (vista superior, 1:1)" % (PL, PL, PT))
    cx, cy = 105, 196
    X = lambda x: cx + x; Y = lambda y: cy + y
    p.rect(X(-PL / 2), Y(-PL / 2), PL, PL, fc="#f0e2c8", lw=1.6)
    p.cross(X(0), Y(0), 7)
    p.line(X(-PL / 2 - 4), Y(0), X(PL / 2 + 4), Y(0), 0.4, "#c0392b", "-.")
    p.line(X(0), Y(-PL / 2 - 4), X(0), Y(PL / 2 + 4), 0.4, "#c0392b", "-.")
    for n, (x, y) in COILS.items():
        p.circ(X(x), Y(y), FL_D, ec="#7a4a1b", lw=0.7, ls="--")                         # marca de la bobina (grabar 0.5 mm)
        p.circ(X(x), Y(y), HOLE_ROD_D, fc="#777", ec="k", lw=1.0)                       # agujero de la varilla (A)
        p.cross(X(x), Y(y), 3, "#fff")
        sx = x - math.copysign(CC - SENS_XY, x) * 0 ; 
        sxx = math.copysign(SENS_XY, x); syy = math.copysign(SENS_XY, y)
        p.rect(X(sxx) - 2, Y(syy) - 2, 4, 4, ec="#1f4e9e", lw=0.8, ls=":")             # sensor (sobre la pestana)
        hx, hy = math.copysign(CABLE_OFF, x), math.copysign(CABLE_OFF, y)
        p.circ(X(hx), Y(hy), CABLE_D, fc="#222", ec="k", lw=1.0)                        # agujero de cables (B)
        sx2, sy2 = math.copysign(SCREW_OFF, x), math.copysign(SCREW_OFF, y)
        p.circ(X(sx2), Y(sy2), SCREW_D, fc="#222", ec="k", lw=1.0)                      # tornillo del poste (C)
        lx = x * 1.0; ly = y * 1.0
        p.text(X(x + (FL_D / 2 + 3) * (1 if x > 0 else -1) * 0), Y(y + (14 if y > 0 else -14)), "PID %d" % n, size=8, ha="center", weight="bold", color="#7a4a1b")
    p.circ(X(0), Y(0), PED_HOLE_D, fc="#777", ec="k", lw=1.0)
    p.text(X(0), Y(0) - 0.0, "D", size=7, ha="center", color="white", weight="bold")
    # etiquetas de tipo
    p.text(X(COILS[1][0]), Y(COILS[1][1]) + 0, "A", size=8, ha="center", color="white", weight="bold")
    p.text(X(CABLE_OFF), Y(CABLE_OFF), "B", size=8, ha="center", color="white", weight="bold")
    p.text(X(SCREW_OFF), Y(SCREW_OFF), "C", size=7, ha="center", color="white", weight="bold")
    # cotas
    p.dim(X(-PL / 2), Y(-PL / 2), X(PL / 2), Y(-PL / 2), -8, "%d" % PL)
    p.dim(X(PL / 2), Y(-PL / 2), X(PL / 2), Y(PL / 2), 9, "%d" % PL)
    p.dim(X(-CC), Y(-PL / 2), X(CC), Y(-PL / 2), -24, "%.1f (entre centros de bobinas)" % SP)
    p.dim(X(-PL / 2), Y(0), X(-PL / 2), Y(CC), -9, "%.1f" % CC)
    p.dim(X(0), Y(-PL / 2), X(CABLE_OFF), Y(-PL / 2), -17, "%.1f" % CABLE_OFF) if False else None
    p.dim(X(0), Y(-PL / 2), X(SCREW_OFF), Y(-PL / 2), -16, "%.0f (a los tornillos C)" % SCREW_OFF)
    p.dim(X(-PL / 2), Y(0), X(-PL / 2), Y(-SENS_XY), -17, "sensor: %.2f" % SENS_XY)
    p.scalebar(25, 14)
    # tabla de taladros
    y0 = 84
    p.text(8, y0 + 2, "TALADROS Y MARCAS  (origen = centro de la placa, x a la derecha, y arriba)", size=8.5, weight="bold")
    rows = [
        ("A", "4", "Ø%.1f ciego, %.0f mm de profundidad" % (HOLE_ROD_D, HOLE_ROD_DEPTH), "(±%.1f ; ±%.1f)" % (CC, CC), "aloja los %.0f mm de varilla bajo el carrete" % ROD_DOWN),
        ("B", "4", "Ø%.0f pasante" % CABLE_D, "(±%.1f ; ±%.1f)" % (CABLE_OFF, CABLE_OFF), "cables del sensor y de la bobina"),
        ("C", "4", "Ø%.1f pasante" % SCREW_D, "(±%.0f ; ±%.0f)" % (SCREW_OFF, SCREW_OFF), "tornillos M4 (laton o nylon) a los postes"),
        ("D", "1", "Ø%.1f ciego, %.0f mm de profundidad" % (PED_HOLE_D, PED_HOLE_DEPTH), "(0 ; 0)", "pedestal de varilla Ø%.0f (se pega)" % PED_D),
        ("--", "4", "circulo grabado Ø%.1f, 0,5 mm" % (FL_D + 0.4), "centros en A", "ubica el carrete (no es un bolsillo)"),
        ("[ ]", "4", "marca punteada 4 x 4", "(±%.2f ; ±%.2f)" % (SENS_XY, SENS_XY), "sensor SS495A (va sobre la pestaña)"),
    ]
    hdr = ["", "Cant.", "Operacion", "Posicion (x ; y) mm", "Funcion"]
    xs = [8, 18, 30, 92, 128]
    for xx, h in zip(xs, hdr): p.text(xx, y0 - 5, h, size=7.5, weight="bold")
    p.line(8, y0 - 8, 205, y0 - 8, 0.6)
    for i, r in enumerate(rows):
        yy = y0 - 13 - i * 6
        for xx, t in zip(xs, r): p.text(xx, yy, t, size=7)
    p.text(8, 32, "Notas: las 4 bobinas son iguales; PID 1 arriba a la derecha, PID 2 arriba a la izquierda, PID 3 abajo a la izquierda, PID 4 abajo a la derecha.", size=7)
    p.text(8, 27.5, "Los agujeros B estan a 25 mm del eje de cada bobina, en la diagonal hacia afuera. Usar tornilleria de laton, aluminio o nylon cerca de las bobinas.", size=7)
    p.text(8, 23, "Tolerancia de los agujeros A: la varilla Ø6 debe entrar con holgura (Ø7). El MDF se puede pintar o sellar para evitar que absorba humedad.", size=7)
    return p

def page2_elevacion():
    p = Page(210, 297, "Vista frontal (1:1): alturas y posicion de las piezas")
    cx = 105
    X = lambda x: cx + x
    yb = 80                 # cara inferior del tablero base
    ybt = yb + BB_T         # cara superior del tablero
    yp0 = ybt + LEG_H       # cara inferior de la placa
    yp1 = yp0 + PT          # cara superior de la placa
    # tablero (cortado)
    p.rect(X(-85), yb, 170, BB_T, fc="#e3cfa6", lw=1.2)
    p.text(X(-83), yb + BB_T / 2, "tablero base 15 mm", size=7)
    # postes
    for sx in (-SCREW_OFF, SCREW_OFF):
        p.rect(X(sx) - 7.5, ybt, 15, LEG_H, fc="#d8b98a", lw=1.0)
    p.text(X(-SCREW_OFF) , ybt + LEG_H / 2, "poste\n15x15x55", size=6.5, ha="center")
    # placa
    p.rect(X(-PL / 2), yp0, PL, PT, fc="#f0e2c8", lw=1.4)
    p.text(X(PL / 2) + 3, yp0 + PT / 2, "placa MDF 15 mm", size=7)
    # pedestal (detras de los carretes delanteros)
    p.rect(X(-PED_D / 2), yp1 - PED_HOLE_DEPTH, PED_D, PED_LEN, fc="#bbb", lw=1.0)
    # bobinas (dos columnas visibles x=±18.5)
    for x in (-CC, CC):
        # agujero A
        p.rect(X(x) - HOLE_ROD_D / 2, yp1 - HOLE_ROD_DEPTH, HOLE_ROD_D, HOLE_ROD_DEPTH, fc="#999", ec="#555", lw=0.6)
        # carrete
        p.rect(X(x) - FL_D / 2, yp1, FL_D, FL_T, fc="#e8761f", lw=0.9)
        p.rect(X(x) - FL_D / 2, yp1 + COIL_H - FL_T, FL_D, FL_T, fc="#e8761f", lw=0.9)
        p.rect(X(x) - 33 / 2, yp1 + FL_T, 33, WIND_L, fc="#b87333", lw=0.9)
        # varilla
        p.rect(X(x) - ROD_D / 2, yp1 - ROD_DOWN, ROD_D, ROD_L, fc="#9aa3ab", lw=0.9)
    # sensores
    for x in (-SENS_XY, SENS_XY):
        p.rect(X(x) - 2, yp1 + COIL_H, 4, 1.6, fc="#111", lw=0.5)
    ymr = yp1 + PED_H_ABOVE_PLATE
    p.rect(X(-10), ymr, 20, 4.2, fc="#c0392b", lw=1.0)
    p.rect(X(-10), yp1 + COIL_H + WORK, 20, 4.2, fc="none", ec="#c0392b", lw=1.2, ls="--")
    p.text(X(14), ymr + 2.1, "imán en reposo (sobre el pedestal)", size=7, color="#c0392b")
    p.text(X(14), yp1 + COIL_H + WORK + 2.1, "imán en trabajo", size=7, color="#c0392b")
    # cotas
    xr = X(PL / 2) + 22
    p.dim(X(PL / 2) + 5, yp0, X(PL / 2) + 5, yp1, 6, "15")
    p.dim(X(PL / 2) + 5, yp1, X(PL / 2) + 5, yp1 + COIL_H, 6, "29 (carrete)")
    p.dim(X(PL / 2) + 5, yp1 + COIL_H, X(PL / 2) + 5, yp1 + COIL_H + REST, 6, "25 (reposo)")
    p.dim(X(PL / 2) + 5, yp1 + COIL_H, X(PL / 2) + 5, yp1 + COIL_H + WORK, 22, "30 (trabajo)")
    p.dim(X(-PL / 2) - 5, yp1, X(-PL / 2) - 5, yp1 + PED_H_ABOVE_PLATE, -6, "54 (pedestal sobre la placa)")
    p.dim(X(-PL / 2) - 5, ybt, X(-PL / 2) - 5, yp0, -6, "55 (postes)")
    p.text(X(-68), yp1 + COIL_H + 22, "la varilla sobresale 8 mm arriba\ny 8 mm abajo de las pestañas", size=7)
    p.line(X(-48), yp1 + COIL_H + 18, X(-CC) - 4, yp1 + COIL_H + 8, 0.5, "#555")
    p.text(X(30), yp1 + 8, "pestañas Ø36 x 3 mm\ndevanado Ø33 x 23 mm", size=7)
    p.scalebar(25, 40)
    return p

def page3_tablero():
    p = Page(420, 297, "Tablero base: %d x %d x %d mm  (vista superior, 1:1)" % (BB_W, BB_D, BB_T))
    ox, oy = 10, 18
    X = lambda x: ox + x; Y = lambda y: oy + y
    p.rect(X(0), Y(0), BB_W, BB_D, fc="#f0e2c8", lw=1.6)
    px, py = PLATE_C
    p.rect(X(px - PL / 2), Y(py - PL / 2), PL, PL, ec="#7a4a1b", lw=0.9, ls="--")
    p.text(X(px), Y(py), "placa del levitador\n(sobre los 4 postes)", size=8, ha="center", color="#7a4a1b")
    for sx in (-SCREW_OFF, SCREW_OFF):
        for sy in (-SCREW_OFF, SCREW_OFF):
            p.circ(X(px + sx), Y(py + sy), SCREW_D, fc="#222", lw=1.0)
            p.rect(X(px + sx) - 7.5, Y(py + sy) - 7.5, 15, 15, ec="#7a4a1b", lw=0.5, ls=":")
    # PCBs
    p.rect(X(185), Y(135), 170, 117, fc="#cfe8d5", ec="#1f7a3a", lw=1.2)
    p.text(X(270), Y(193), "PCB A: PID 1 y PID 2\n170 x 117 mm", size=9, ha="center", color="#1f5a2a")
    p.rect(X(185), Y(8), 170, 117, fc="#cfe8d5", ec="#1f7a3a", lw=1.2)
    p.text(X(270), Y(66), "PCB B: PID 3 y PID 4\n170 x 117 mm", size=9, ha="center", color="#1f5a2a")
    p.rect(X(362), Y(12), 34, 236, fc="#cfdcf0", ec="#1f4e9e", lw=1.2)
    p.text(X(379), Y(130), "fuente\nmodulos\nXL4015\n+ entrada", size=8, ha="center", color="#1f3f7a")
    # recorrido de cables
    for y in (200, 215, 55, 70):
        p.line(X(px + 40), Y(py), X(185), Y(y), 0.5, "#e07b00", "--")
    p.text(X(170), Y(130), "cables (por debajo de la placa)", size=7, ha="center", color="#e07b00", rot=90)
    # cotas
    p.dim(X(0), Y(0), X(BB_W), Y(0), -7, "%d" % BB_W)
    p.dim(X(0), Y(0), X(0), Y(BB_D), -9, "%d" % BB_D)
    p.dim(X(0), Y(py), X(px), Y(py), 10, "%d" % px) if False else None
    p.text(10, 3, "Postes: x = %.0f y %.0f ; y = %.0f y %.0f  (desde la esquina inferior izquierda)." % (px - SCREW_OFF, px + SCREW_OFF, py - SCREW_OFF, py + SCREW_OFF), size=7)
    p.scalebar(330, 3)
    return p

def page4_lista():
    p = Page(210, 297, "Resumen de diseño, piezas y verificaciones")
    y = 270
    def sec(t):
        nonlocal y
        p.text(8, y, t, size=9.5, weight="bold"); y -= 6
    def ln(t, d=5.2, size=7.8):
        nonlocal y
        p.text(10, y, t, size=size); y -= d
    sec("Diseño (resultado de la simulacion)")
    for t in ["Configuracion: repulsion, 4 bobinas abajo con nucleo de hierro, imán de neodimio arriba.",
              "Carrete: pestañas Ø36 x 3 mm, devanado Ø33 x 23 mm (29 mm de largo total), agujero Ø6, 4 Ω.",
              "Nucleo: varilla de hierro o acero comun Ø6 x 45 mm, centrada (8 mm sobre y 8 mm bajo las pestañas). No usar acero inoxidable 304.",
              "Imán: neodimio N42, disco Ø20 x 4,2 mm (~10 g) (supuesto; confirmar).",
              "Altura de trabajo: 25 a 30 mm sobre la pestaña; corriente por bobina de ~0,7 A en trabajo (una bobina sobre el eje; 4 bobinas: estimar 1 a 1,5 A).",
              "Pedestal: reposo a 25 mm sobre la pestaña; el imán se despega con ~0,7 a 0,9 A."]: ln(t)
    y -= 3; sec("Lista de piezas")
    parts = [("MDF 15 mm", "1", "placa %d x %d" % (PL, PL)),
             ("MDF 15 mm", "1", "tablero %d x %d" % (BB_W, BB_D)),
             ("Poste de madera o MDF apilado", "4", "15 x 15 x %d mm" % LEG_H),
             ("Varilla de hierro/acero Ø6", "4", "45 mm (nucleos)"),
             ("Varilla o taco de madera Ø12", "1", "%d mm (pedestal)" % PED_LEN),
             ("Tornillos M4 de laton/nylon", "8", "25 mm (4 placa-poste, 4 tablero-poste)"),
             ("Cable trenzado 3 hilos 26-28 AWG con malla", "4", "~35 cm (sensores)"),
             ("Cable 2 hilos 18-20 AWG", "4", "~35 cm (bobinas)")]
    for n, c, d in parts: 
        p.text(10, y, n, size=7.8); p.text(92, y, c, size=7.8); p.text(105, y, d, size=7.8); y -= 5.2
    y -= 3; sec("Antes de cortar, comprobar con la pieza real")
    for t in ["1. Medir otra vez el diametro y el espesor de las pestañas y el diametro del devanado (el plano usa 36, 3 y 33 mm).",
              "2. Probar que la varilla Ø6 entra en el agujero del carrete y que el carrete cabe sobre su marca.",
              "3. Medir el imán (diametro, espesor, peso) y confirmar N42.",
              "4. Imprimir la pagina 1 al 100 % y poner un carrete encima para verificar posiciones antes de taladrar.",
              "5. Con 1 A en la bobina y sin imán, mover el sensor sobre la pestaña hasta que su voltaje no cambie al conectar la corriente;",
              "   esa posicion (cerca de 16 mm del eje) es la que se marca como sensor. Fijar el sensor ahi."]: ln(t)
    y -= 3; sec("Armado")
    for t in ["a. Pegar los postes al tablero (tornillos desde abajo) y atornillar la placa arriba; usar solo tornilleria no magnetica.",
              "b. Colocar los carretes sobre las marcas con la varilla ya dentro del agujero A; fijar con epoxico o silicona.",
              "c. Pegar los sensores sobre la pestaña con la cara plana hacia arriba; pasar los cables por el agujero B de cada bobina.",
              "d. Pegar el pedestal en el agujero D (62 mm de largo, queda 54 mm sobre la placa).",
              "e. Llevar los cables a las regletas J_IN, J_PWR y J_COIL de la PCB que corresponde (A: PID 1 y 2; B: PID 3 y 4)."]: ln(t)
    return p

# ---------------------------------------------------------------- DXF
def dxf():
    d = ezdxf.new("R2010"); d.units = ezdxf.units.MM
    for n, c in (("CORTE", 7), ("TALADROS", 1), ("MARCAS", 3), ("EJES", 5), ("TEXTO", 7)): d.layers.add(n, color=c)
    m = d.modelspace()
    m.add_lwpolyline([(-PL / 2, -PL / 2), (PL / 2, -PL / 2), (PL / 2, PL / 2), (-PL / 2, PL / 2)], close=True, dxfattribs={"layer": "CORTE"})
    m.add_line((-PL / 2 - 5, 0), (PL / 2 + 5, 0), dxfattribs={"layer": "EJES"}); m.add_line((0, -PL / 2 - 5), (0, PL / 2 + 5), dxfattribs={"layer": "EJES"})
    for n, (x, y) in COILS.items():
        m.add_circle((x, y), HOLE_ROD_D / 2, dxfattribs={"layer": "TALADROS"})             # A ciego 9 mm
        m.add_circle((x, y), (FL_D + 0.4) / 2, dxfattribs={"layer": "MARCAS"})              # marca de la bobina
        hx, hy = math.copysign(CABLE_OFF, x), math.copysign(CABLE_OFF, y)
        m.add_circle((hx, hy), CABLE_D / 2, dxfattribs={"layer": "TALADROS"})              # B pasante
        sx, sy = math.copysign(SCREW_OFF, x), math.copysign(SCREW_OFF, y)
        m.add_circle((sx, sy), SCREW_D / 2, dxfattribs={"layer": "TALADROS"})              # C pasante
        kx, ky = math.copysign(SENS_XY, x), math.copysign(SENS_XY, y)
        m.add_lwpolyline([(kx - 2, ky - 2), (kx + 2, ky - 2), (kx + 2, ky + 2), (kx - 2, ky + 2)], close=True, dxfattribs={"layer": "MARCAS"})
        m.add_text("PID %d" % n, dxfattribs={"layer": "TEXTO", "height": 3, "insert": (x - 5, y + 20)})
    m.add_circle((0, 0), PED_HOLE_D / 2, dxfattribs={"layer": "TALADROS"})                  # D ciego 8 mm
    m.add_text("A: Ø7 ciego 9 | B: Ø8 pasante | C: Ø4.2 pasante | D: Ø12.2 ciego 8", dxfattribs={"layer": "TEXTO", "height": 3, "insert": (-70, -PL / 2 - 10)})
    d.saveas(os.path.join(OUT, "placa_levitador.dxf"))
    t = ezdxf.new("R2010"); t.units = ezdxf.units.MM
    for n, c in (("CORTE", 7), ("TALADROS", 1), ("MARCAS", 3), ("TEXTO", 7)): t.layers.add(n, color=c)
    m = t.modelspace()
    m.add_lwpolyline([(0, 0), (BB_W, 0), (BB_W, BB_D), (0, BB_D)], close=True, dxfattribs={"layer": "CORTE"})
    px, py = PLATE_C
    for sx in (-SCREW_OFF, SCREW_OFF):
        for sy in (-SCREW_OFF, SCREW_OFF): m.add_circle((px + sx, py + sy), SCREW_D / 2, dxfattribs={"layer": "TALADROS"})
    m.add_lwpolyline([(px - PL / 2, py - PL / 2), (px + PL / 2, py - PL / 2), (px + PL / 2, py + PL / 2), (px - PL / 2, py + PL / 2)], close=True, dxfattribs={"layer": "MARCAS"})
    for (x0, y0, w, h, nm) in ((185, 135, 170, 117, "PCB A"), (185, 8, 170, 117, "PCB B"), (362, 12, 34, 236, "FUENTE")):
        m.add_lwpolyline([(x0, y0), (x0 + w, y0), (x0 + w, y0 + h), (x0, y0 + h)], close=True, dxfattribs={"layer": "MARCAS"})
        m.add_text(nm, dxfattribs={"layer": "TEXTO", "height": 5, "insert": (x0 + 5, y0 + h / 2)})
    t.saveas(os.path.join(OUT, "tablero_base.dxf"))

def main():
    with PdfPages(os.path.join(OUT, "plano_base_mdf_1a1.pdf")) as pdf:
        for f in (page1_placa, page2_elevacion, page3_tablero, page4_lista): f().save(pdf)
    dxf()
    print("ok")

if __name__ == "__main__":
    main()
