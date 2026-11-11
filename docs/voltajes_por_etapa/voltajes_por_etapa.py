#!/usr/bin/env python3
"""Mapa de voltajes por nodo de un PID con Vref = 2 V y V_sensor = 3 V (estado estable).
Valores calculados con las ecuaciones y componentes del README (R1..R4 = 10k, Kp = 2.2,
K_I,max = R11/Pot2 = 4.5, derivativo ~0 en DC, sumador 0.1 por rama, Voff = -10 V)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

V_SENSOR, V_REF = 3.0, 2.0
VE   = V_SENSOR - V_REF                 # U1: Vsensor - Vref
VP   = -2.2 * VE                        # U2: -(Pot1/R5) Ve
VI   = -4.5 * VE                        # U3 en DC: -(R11/Pot2) Ve, K_max = 4.5 (README)
VD   = 0.0                              # U4 en DC ~ 0
VOFF = -10.1                            # divisor R14/R15 desde -16 V (medido -10.2)
VPID = -0.1 * (VP + VI + VD + VOFF)     # U5
CAL  = 3.3e3                            # ejemplo: POT4 (parte a tierra) = 3.3 kOhm
VPLUS = VPID * CAL / 20e3
I_A  = VPLUS / 0.33

BG, FG, MUT, LINE, WIRE = "#ffffff", "#17202a", "#5d6b78", "#c9d2da", "#8796a5"
C_POS, C_NEG, C_ZERO = "#1b6ca8", "#c8651b", "#6b7785"
BOX, BOXE = "#f3f6f9", "#9fb0c0"
col = lambda v: C_ZERO if abs(v) < 0.05 else (C_POS if v > 0 else C_NEG)
fmt = lambda v: f"{v:+.2f} V" if abs(v) >= 0.005 else "≈ 0 V"

fig, ax = plt.subplots(figsize=(18, 12.6), dpi=160)
ax.set_xlim(0, 200); ax.set_ylim(-5, 134); ax.axis("off")
fig.patch.set_facecolor(BG)

def box(x, y, w, h, title, sub=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.6", fc=BOX, ec=BOXE, lw=1.6))
    ax.text(x + 2, y + h - 2.2, title, fontsize=13.5, fontweight="bold", color=FG, va="top")
    if sub:
        ax.text(x + 2, y + h - 7.0, sub, fontsize=10.2, color=MUT, va="top")

def pill(x, y, text, v, w=26, h=6.6, size=15, tag=None):
    c = col(v)
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=3.2", fc=c, ec=c))
    ax.text(x + w / 2, y + h / 2, text, fontsize=size, fontweight="bold", color="white", ha="center", va="center")
    if tag:
        ax.text(x + w + 1.5, y + h / 2, tag, fontsize=10.2, color=MUT, va="center")

def seg(pts, arrow=False, lw=2.0):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=WIRE, lw=lw, solid_capstyle="round", solid_joinstyle="round")
    if arrow:
        ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=16, lw=lw, color=WIRE))

# ---- título y leyenda
ax.text(2, 133, "PID analógico: voltaje esperado en cada nodo", fontsize=23, fontweight="bold", color=FG, va="top")
ax.text(2, 127.2, f"Con  V_ref = {V_REF:.0f} V  y  V_sensor = {V_SENSOR:.0f} V  (estado estable; esperar unos 5 s a que el integrador se asiente)",
        fontsize=12.5, color=MUT, va="top")
for i, (t, c) in enumerate([("positivo", C_POS), ("negativo", C_NEG), ("≈ 0 V", C_ZERO)]):
    ax.add_patch(FancyBboxPatch((150 + i * 17, 130.3), 3, 3, boxstyle="round,pad=0,rounding_size=0.8", fc=c, ec=c))
    ax.text(154.4 + i * 17, 131.8, t, fontsize=10.5, color=FG, va="center")

# ---- entradas (columna izquierda)
box(2, 98, 30, 20, "Sensor Hall", "SS495A, salida")
pill(4, 100.2, f"{V_SENSOR:.2f} V", V_SENSOR, w=26)
box(2, 72, 30, 20, "Vref  (U6)", "5 V × 160k/400k")
pill(4, 74.2, f"{V_REF:.2f} V", V_REF, w=18, size=14, tag="pin 1")
ax.text(23.5, 73.3, "", fontsize=1)
seg([(32, 103.5), (42, 103.5)], arrow=True); seg([(32, 77.5), (42, 77.5)], arrow=True)
ax.text(33, 105.0, "pin 5", fontsize=9.5, color=MUT); ax.text(33, 79.0, "pin 6", fontsize=9.5, color=MUT)

# ---- U1
box(42, 70, 44, 48, "U1 · error", "IC1: pines 5, 6 y 7")
ax.text(44, 105.5, "pin 5 (+) = 3 V × 10k/20k = 1.50 V", fontsize=10.3, color=FG, va="top")
ax.text(44, 101.3, "pin 6 (−) = (2 V + 1 V)/2 = 1.50 V", fontsize=10.3, color=FG, va="top")
ax.text(44, 97.1, "iguales: cortocircuito virtual", fontsize=9.6, color=MUT, va="top")
ax.text(44, 90.0, "V_e = V_sensor − V_ref", fontsize=11.5, fontweight="bold", color=FG, va="top")
pill(46, 73.5, fmt(VE), VE, w=26, tag="pin 7")

# ---- P, I, D
def stage(y, name, pin, expr, v):
    box(98, y, 44, 16, name)
    ax.text(100, y + 6.9, pin, fontsize=10.2, color=MUT, va="center")
    ax.text(100, y + 3.4, expr, fontsize=10.2, color=MUT, va="center")
    pill(118, y + 2.2, fmt(v), v, w=22, h=6.6, size=14)
stage(102, "U2 · proporcional", "IC1 pin 8", "−2.2 × V_e", VP)
stage(83, "U3 · integral", "IC1 pin 14", "−4.5 × V_e", VI)
stage(64, "U4 · derivativo", "IC2 pin 1", "solo mV en DC", VD)
seg([(86, 79.7), (92, 79.7)])
seg([(92, 72), (92, 110)])
for yy in (110, 91, 72):
    seg([(92, yy), (98, yy)], arrow=True)

# ---- Voff
box(42, 48, 44, 20, "Voff  (U7)", "−16 V × 160k/256k")
pill(46, 50.2, "−10.0 V", -10.0, w=26, tag="IC2 pin 8")
ax.text(44, 47.0, "medido en el montaje: −10.2 V", fontsize=9.5, color=MUT, va="top")

# ---- U5
box(154, 64, 44, 54, "U5 · sumador", "IC2: pines 5, 6 y 7")
ax.text(156, 106.5, "V_PID = −0.1·(V_P + V_I + V_D + V_off)", fontsize=10.0, color=FG, va="top")
yy = 99.0
for n, v in [("aporta P", -0.1 * VP), ("aporta I", -0.1 * VI), ("aporta D", abs(-0.1 * VD)), ("aporta Voff", -0.1 * VOFF)]:
    ax.text(158, yy, n, fontsize=10.5, color=MUT, va="center")
    ax.text(194, yy, f"{v + 0.0:+.2f} V", fontsize=11, color=FG, va="center", ha="right", fontweight="bold")
    yy -= 4.8
ax.plot([156, 196], [yy + 2.2, yy + 2.2], color=LINE, lw=1.3)
ax.text(158, yy - 1.4, "V_PID  (IC2 pin 7)", fontsize=11, color=FG, va="center", fontweight="bold")
pill(158, 66.4, f"{VPID:.2f} V", VPID, w=36, h=8.2, size=18)
# bus de P, I, D hacia el sumador
seg([(142, 110), (148, 110), (148, 72), (142, 72)]); seg([(142, 91), (148, 91)])
seg([(148, 91), (154, 91)], arrow=True)
# Voff al sumador
seg([(86, 58), (164, 58), (164, 64)], arrow=True)

# ---- etapa de potencia
ax.plot([2, 198], [37.5, 37.5], color=LINE, lw=1.4)
ax.text(32, 35.6, "Etapa de potencia  (IC2 canal 4 = U8, TIP122 y R_sense 0.33 Ω)", fontsize=14, fontweight="bold", color=FG, va="top")
seg([(186, 64), (186, 41.5), (26, 41.5), (26, 31)], arrow=True)
ax.text(100, 42.7, f"V_PID = {VPID:.2f} V", fontsize=10.5, color=MUT, va="bottom")

box(2, 2, 48, 29, "Divisor de entrada", "R17 10k + POT4 10k")
ax.text(4, 19.6, "V₊ = V_PID × R_abajo / 20 kΩ", fontsize=11, color=FG, va="top", fontweight="bold")
ax.text(4, 15.2, "ejemplo: POT4 (a tierra) = 3.3 kΩ", fontsize=10, color=MUT, va="top")
pill(5, 4.2, f"{VPLUS:.2f} V", VPLUS, w=22, h=6.4, size=14, tag="V₊ = IC2 pin 12")

box(62, 2, 52, 29, "U8 · convertidor V-I", "IC2: pines 12, 13 y 14")
ax.text(64, 19.6, f"pin 13 (−) = V_isense = {VPLUS:.2f} V", fontsize=10.2, color=FG, va="top")
ax.text(64, 15.4, "pin 14 = V_isense + 1.3 V + 0.65 V", fontsize=10.2, color=FG, va="top")
pill(65, 4.2, "≈ 2.2 V", 2.2, w=22, h=6.4, size=14, tag="IC2 pin 14")

box(126, 2, 36, 29, "TIP122 y R_sense", "emisor = sensado")
ax.text(128, 19.6, "I = V₊ / 0.33 Ω", fontsize=11, color=FG, va="top", fontweight="bold")
ax.text(128, 15.4, f"V en R_sense = {VPLUS:.2f} V", fontsize=10, color=MUT, va="top")
pill(129, 4.2, f"{I_A:.2f} A", I_A, w=22, h=6.4, size=14)

box(172, 2, 26, 29, "Bobina", "≈ 4 Ω")
ax.text(174, 19.6, "colector =", fontsize=10, color=FG, va="top")
ax.text(174, 15.6, "V_alim − I·R_bob", fontsize=10, color=FG, va="top")
for a, b in [(50, 62), (114, 126), (162, 172)]:
    seg([(a, 14), (b, 14)], arrow=True)

# ---- pie
ax.text(2, -1.2, "Corriente con V_PID = 1.68 V:  POT4 (a tierra) 2.2k → 0.56 A  |  3.3k → 0.84 A  |  5k → 1.27 A.   "
        "Con error cero (V_PID = 1 V):  0.33 A  |  0.50 A  |  0.76 A.", fontsize=10.2, color=FG, va="center")
ax.text(2, -3.6, "Tolerancia al medir ±10 % (resistencias y op-amps); la salida de U3 puede desviarse más. "
        "Cada TL074: +16 V en el pin 4 y −16 V en el pin 11.", fontsize=9.5, color=MUT, va="center")

fig.savefig("voltajes_por_etapa.png", dpi=160, facecolor=BG, bbox_inches="tight", pad_inches=0.3)
fig.savefig("voltajes_por_etapa.pdf", facecolor=BG, bbox_inches="tight", pad_inches=0.3)
print(f"Ve={VE:.2f} VP={VP:.2f} VI={VI:.2f} VPID={VPID:.3f} V+={VPLUS:.3f} I={I_A:.2f}")
