"""Cálculos de diseño de la fuente ±16 V / 1,5 A y +5 V (versión 2).
Método: monografía Electrónica Tomo II, tema 3. Ejecutar: python3 calculos.py
Imprime todos los valores que cita el informe y los guarda en resultados_calculos.json.
"""
import math, json
R = {}
def out(k, v, u=''):
    R[k] = v
    print(f'{k:<52s} = {v:10.4g} {u}')

# ---------------- 1. Especificación y cargas ----------------
VO = 16.0
RL = 10.0                       # resistencia de prueba (removible, borneras J4/J5)
I_RL = VO/RL                    # 1,6 A >= 1,5 A pedidos
VREF = 1.25; IADJ = 50e-6; R1 = 120.0
I1 = VREF/R1
I_LED16 = (16-1.9)/2.2e3; I_LED5 = (5-1.9)/470
I5 = 4*10e-3 + 4*5/400e3 + I1 + IADJ + I_LED5        # rama de +5 V
I_int_p = I1 + IADJ + I_LED16 + I5                   # consumo interno del riel +16
I_int_n = I1 + 65e-6 + I_LED16
out('I por RL = 16/10', I_RL, 'A')
out('I rama +5 V', I5*1e3, 'mA')
out('I_L(+16) diseño = RL + interno', I_RL + I_int_p, 'A')
out('I_L(-16) diseño = RL + interno', I_RL + I_int_n, 'A')
IP = I_RL + I_int_p; IN = I_RL + I_int_n
out('I_L(+16) con los 4 PID (sin RL)', 0.2 + I_int_p, 'A')

# ---------------- 2. Transformador 18-0-18 V / 3 A y puente ----------------
VS = 18.0; VD = 1.1; f = 120.0                       # onda completa: rizado a 120 Hz
Vp = lambda v: v*math.sqrt(2) - VD
out('Vp nominal (115 V)', Vp(VS), 'V')
out('Vp linea -10 %', Vp(0.9*VS), 'V')
out('Vp linea +10 % y vacio (+10 %)', Vp(1.1*1.1*VS), 'V')
out('PIV por diodo (2 Vp max)', 2*(Vp(1.21*VS)+VD), 'V')
# corriente eficaz de cada mitad del secundario: un riel a 1,6 A y el otro con los PID (0,27 A)
k_rms = 1.6        # Irms(mitad) ~ 1.6 Idc por riel (filtro capacitivo, onda completa con toma central)
Irms_half = math.hypot(k_rms*IP/math.sqrt(2), k_rms*(0.2+I_int_n)/math.sqrt(2))*math.sqrt(2)
out('I rms por mitad del secundario (aprox.)', Irms_half, 'A')

# ---------------- 3. Filtros ----------------
CP, CN = 15000e-6, 2*6800e-6
IB_DRV = 7e-3; I_AUX = 2e-3                          # base del Darlington y R_BE / divisor
def filtro(I, C, nombre):
    Ir = I + IB_DRV + I_AUX
    Vr = Ir/(f*C); Vval = Vp(0.9*VS) - Vr
    out(f'Vr pp ({nombre})', Vr, 'V'); out(f'Valle linea baja ({nombre})', Vval, 'V')
    Vdc = Vp(VS) - Vr/2; Vrr = Vr/(2*math.sqrt(3))
    out(f'Vdc nominal ({nombre})', Vdc, 'V'); out(f'Fr ({nombre})', 100*Vrr/Vdc, '%')
    return Ir, Vr, Vval, Vdc, Vrr
Irp, Vrp, Vvalp, Vdcp, Vrrp = filtro(IP, CP, '+16, 15000 uF')
Irn, Vrn, Vvaln, Vdcn, Vrrn = filtro(IN, CN, '-16, 2x6800 uF')

# ---------------- 4. Booster (Fig. 3-21) y caída mínima ----------------
VEB_BOOST = 0.95; HFE_BOOST = 30; IU_target = 0.39
RU = 2.7                                             # R = V_BE/(I_U - I_B), ec. (3.24)
IB_boost = (IP - IU_target)/HFE_BOOST
out('R calculada (3.24)', VEB_BOOST/(IU_target - IB_boost), 'ohm')
IU = VEB_BOOST/RU + IB_boost
out('I_U del regulador con R=2.7', IU, 'A'); out('I_C del booster', IP-IU, 'A')
out('I_U / I_max del LM317 (1,5 A)', 100*IU/1.5, '%')
V_BOOST = VEB_BOOST + 2.0                            # V_R + dropout del LM317 a 0,4 A (máx.)
RSC = 0.27; VDARL = 1.2
for nombre, Ir, Vval in (('+16', Irp, Vvalp), ('-16', Irn, Vvaln)):
    need = VO + V_BOOST + VDARL + Ir*RSC
    out(f'V minima requerida a 16,00 V ({nombre})', need, 'V'); out(f'margen linea baja ({nombre})', Vval-need, 'V')

# ---------------- 5. Limitador con foldback (Fig. 3-26 + 3-27) ----------------
VBE = 0.7; Ra, Rb = 270.0, 12e3; k = Ra/(Ra+Rb)
out("k' = Ra/(Ra+Rb)", k)
out('I_lim con el Darlington saturado (sobrecarga)', (VBE - k*VDARL)/RSC, 'A')
E1 = {'nominal': Vp(VS)-Vrp/2, 'baja': Vp(0.9*VS)-Vrp/2, 'alta': Vp(1.1*VS)-Vrp/2}
for lab, e in E1.items():
    d = e - 0.3 - 2.9                                # E1 - V_A con la salida en corto
    isc = (VBE - k*d)/RSC
    out(f'I_sc corto franco linea {lab}', isc, 'A'); out(f'P Darlington en corto linea {lab}', d*isc, 'W')
# arranque con RL a linea alta: limite(x) > demanda(x) en 0..16 V
e = E1['alta']; worst = 1e9
for i in range(161):
    x = i/10; d = e - 0.5 - (x + 2.9)
    lim = (0.65 - k*d)/RSC                          # V_BE pesimista 0,65 V
    dem = x/RL + I_int_p
    worst = min(worst, lim - dem)
out('margen minimo limite-demanda al arrancar con RL (A)', worst, 'A')

# ---------------- 6. Polarización del Darlington ----------------
RB = 2.7e3
IBd = (Vvalp - Irp*RSC - 2*0.8)/RB
out('I base del driver (linea baja)', IBd*1e3, 'mA')
out('I max del Darlington = hFE1*hFE2*IB (15*40)', 15*40*IBd, 'A')
out('P_RB max', Vp(1.21*VS)**2/RB, 'W')

# ---------------- 7. Disipación ----------------
def pot(Vdc, Ir, I, IU_):
    VA = Vdc - Ir*RSC - VDARL
    return VA, VDARL*Ir, (VA-VO)*(I-IU_), (VA-VEB_BOOST-VO)*IU_, Ir**2*RSC
for lab, vp in (('nominal', Vp(VS)), ('linea +10 %', Vp(1.1*VS))):
    VA, Pd, Pb, Pu, Pr = pot(vp - Vrp/2, Irp, IP, IU)
    out(f'V_A {lab}', VA, 'V'); out(f'P Darlington {lab}', Pd, 'W'); out(f'P booster {lab}', Pb, 'W')
    out(f'P LM317 {lab}', Pu, 'W'); out(f'P total disipador {lab}', Pd+Pb+Pu, 'W')
TA = 40; TH_SA = 2.0
out('T disipador plena carga linea alta', TA + TH_SA*(pot(Vp(1.1*VS)-Vrp/2, Irp, IP, IU)[1]+pot(Vp(1.1*VS)-Vrp/2, Irp, IP, IU)[2]+pot(Vp(1.1*VS)-Vrp/2, Irp, IP, IU)[3]), 'C')
# ---------------- 8. Regulador y red (igual que v1) ----------------
out('R2 para 16 V', (16-1.25)/(I1+IADJ), 'ohm')
out('Vout min/max (1.3k / 1.5k)', 1.25*(1+1300/120)+1300*IADJ, 'V')
out('Vout max', 1.25*(1+1500/120)+1500*IADJ, 'V')
out('Rizado salida (66 dB) +16', Vrrp*10**(-66/20)*1e3, 'mV rms')
out('Reg. carga max 0,5 %', 0.005*16*1e3, 'mV')
# ---------------- 9. Fusibles ----------------
Pin = Vdcp*Irp + Vdcn*(0.2+I_int_n)
out('Potencia DC (un riel a 1,6 A)', Pin, 'W'); out('I primario aprox (75 %)', Pin/0.75/115, 'A')
json.dump(R, open('resultados_calculos.json', 'w'), indent=1, ensure_ascii=False)
