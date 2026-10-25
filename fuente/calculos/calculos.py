"""Cálculos de diseño de la fuente ±16 V / +5 V (método de la monografía Electrónica Tomo II, tema 3).
Ejecutar:  python3 calculos.py      (imprime todos los valores usados en el informe)
"""
import math, json

R = {}                      # resultados que se citan en el informe
def out(k, v, u=''):
    R[k] = v
    print(f'{k:<38s} = {v:10.4g} {u}')

# ---------------- 1. Cargas (especificaciones) ----------------
N_PID = 4
I_PID = 50e-3              # por PID y por riel (2 x TL074CN + base del TIP122 + salidas), con margen
I_HALL = 10e-3             # SS495A, máximo de hoja de datos
I_VREF = 5/(160e3+240e3)   # divisor R12/R13 de cada PID
VLED = 1.9
I_LED16 = (16-VLED)/2.2e3  # indicador del riel de 16 V
I_LED5 = (5-VLED)/470
VREF = 1.25; IADJ_317 = 50e-6; IADJ_337 = 65e-6
R1 = 120.0                 # resistencia OUT-ADJ (garantiza la carga mínima de 10 mA del LM317/LM337)
I1 = VREF/R1
out('I_ops (4 PID)', N_PID*I_PID*1e3, 'mA')
out('I1 = VA/R1', I1*1e3, 'mA')
I5 = N_PID*I_HALL + N_PID*I_VREF + I1 + IADJ_317 + I_LED5
out('I_L(+5 V)', I5*1e3, 'mA')
Ip = N_PID*I_PID + I1 + IADJ_317 + I_LED16 + I5
In = N_PID*I_PID + I1 + IADJ_337 + I_LED16
out('I_L(+16 V) (incluye la rama de +5 V)', Ip*1e3, 'mA')
out('I_L(-16 V)', In*1e3, 'mA')

# ---------------- 2. Transformador y rectificador ----------------
f = 60.0; VD = 1.0         # caída del 1N4007 con los picos de carga (~1-2 A)
VS = 18.0                  # devanado completo 9-0-9 (extremos), valor nominal a 2 A
k_vacio = 1.10             # subida típica sin carga de un transformador pequeño (se asume +10 %)
Vp = lambda vrms: vrms*math.sqrt(2) - VD
out('Vp nominal (115 V)', Vp(VS), 'V')
out('Vp linea -10 % (103.5 V)', Vp(0.9*VS), 'V')
out('Vp linea +10 % y sin carga (peor caso)', Vp(1.1*VS*k_vacio), 'V')
out('PIV de cada diodo (2 Vp max)', 2*(Vp(1.1*VS*k_vacio)+VD), 'V')

# ---------------- 3. Limitador de corriente (Fig. 3-26 / ec. 3.27) ----------------
VBE = 0.7                  # monografía: V_BE = 0.7 V (Si)
RSC_P, RSC_N = 1.8, 2.2    # valores comerciales E12
out('Rsc+ calculada para 0.39 A', VBE/0.39, 'ohm')
out('Ilim(+16) = 0.7/1.8', VBE/RSC_P, 'A')
out('Rsc- calculada para 0.32 A', VBE/0.32, 'ohm')
out('Ilim(-16) = 0.7/2.2', VBE/RSC_N, 'A')
# polarización del transistor de paso (TIP32C / TIP31C), hFE min 25 a 1 A
RB = 820.0; VEB_Q1 = 0.9; HFE_MIN = 25

# ---------------- 4. Capacitor de filtro (media onda: f_rizado = 60 Hz) ----------------
C = 3300e-6
def filtro(I, Rsc, nombre):
    Vpk = Vp(0.9*VS)
    IB = (Vpk - 1.5 - I*Rsc - VEB_Q1)/RB         # corriente por RB (pasa por Rsc), línea baja
    Iraw = I + IB
    Vr = Iraw/(f*C)
    out(f'IB por RB ({nombre}), linea baja', IB*1e3, 'mA')
    out(f'hFEmin*IB ({nombre})', HFE_MIN*IB, 'A')
    out(f'I por Rsc ({nombre})', Iraw*1e3, 'mA')
    out(f'Vr pico-pico ({nombre})', Vr, 'V')
    Vvalle = Vpk - Vr
    out(f'V valle linea baja ({nombre})', Vvalle, 'V')
    for Vo in (16.0, 16.95):
        need = Vo + 2.0 + 0.3 + Iraw*Rsc       # dropout LM317 2 V + VCEsat 0.3 V + caída en Rsc
        out(f'V minima requerida Vo={Vo} ({nombre})', need, 'V')
        out(f'margen Vo={Vo} ({nombre})', Vvalle-need, 'V')
    Vdc = Vp(VS) - Vr/2; Vrrms = Vr/(2*math.sqrt(3))
    out(f'Vdc nominal ({nombre})', Vdc, 'V')
    out(f'Vr rms ({nombre})', Vrrms, 'V')
    out(f'Fr = Vr,rms/Vdc ({nombre})', 100*Vrrms/Vdc, '%')
    Cmin = Iraw/(f*(Vpk-(16.95+2.3+Iraw*Rsc)))
    out(f'C minimo para Vo=16.95 ({nombre})', Cmin*1e6, 'uF')
    return Iraw, Vdc, Vrrms, IB
Iraw_p, Vdc_p, Vrr_p, IB_p = filtro(Ip, RSC_P, '+16')
Iraw_n, Vdc_n, Vrr_n, IB_n = filtro(In, RSC_N, '-16')
out('P_RB max (30 V sin carga)', (Vp(1.1*VS*k_vacio)-VEB_Q1)**2/RB, 'W')

# ---------------- 5. Red de ajuste del LM317 / LM337 (ec. 3.19, Probl. 3.6.10) ----------------
Vout = lambda Va, R2, Iadj: Va*(1+R2/R1) + R2*Iadj
for nombre, Iadj in (('LM317 +16', IADJ_317), ('LM337 -16', IADJ_337)):
    out(f'R2 para 16.00 V ({nombre})', (16-VREF)/(I1+Iadj), 'ohm')
    out(f'Vout min (R2=1.3k) ({nombre})', Vout(VREF, 1300, Iadj), 'V')
    out(f'Vout max (R2=1.5k) ({nombre})', Vout(VREF, 1500, Iadj), 'V')
out('R2 para 5.00 V', (5-VREF)/(I1+IADJ_317), 'ohm')
out('Vout min (R2=330)', Vout(VREF, 330, IADJ_317), 'V')
out('Vout max (R2=380)', Vout(VREF, 380, IADJ_317), 'V')
for Va in (1.20, 1.30):     # tolerancia del VREF del LM317 (1.20 a 1.30 V)
    out(f'rango 16 V con VA={Va}: min', Vout(Va, 1300, IADJ_317), 'V')
    out(f'rango 16 V con VA={Va}: max', Vout(Va, 1500, IADJ_317), 'V')
    out(f'rango 5 V con VA={Va}: min', Vout(Va, 330, IADJ_317), 'V')
    out(f'rango 5 V con VA={Va}: max', Vout(Va, 380, IADJ_317), 'V')

# ---------------- 6. Rama de +5 V (resistencia serie R9 desde +16 V) ----------------
R9 = 100.0
Vin5 = 16 - I5*R9
out('V_IN del LM317 de 5 V', Vin5, 'V')
out('I max con regulacion (V_IN >= 5.23+1.7)', (16-5.23-1.7)/R9*1e3, 'mA')
out('I de cortocircuito en +5 V', (16-1.5)/R9*1e3, 'mA')
out('P_R9 normal', I5**2*R9, 'W')
out('P_R9 en corto', ((16-1.5)/R9)**2*R9, 'W')
out('P_U3 normal', (Vin5-5)*I5, 'W')
out('+16 V con +5 V en corto', (N_PID*I_PID+I1+IADJ_317+I_LED16+(16-1.5)/R9)*1e3, 'mA')
fc = 1/(2*math.pi*R9*100e-6); out('fc filtro R9-C13', fc, 'Hz')
out('atenuacion a 60 Hz', 20*math.log10(1/math.sqrt(1+(60/fc)**2)), 'dB')

# ---------------- 7. Disipación y disipadores ----------------
def pot_reg(Vpk_line, I, Rsc, Vo, IB):
    Vdc = Vpk_line - (I+IB)/(f*C)/2
    Vin = Vdc - (I+IB)*Rsc - 0.3
    return Vin, (Vin-Vo)*I
for nombre, I, Rsc, IB in (('LM317 +16', Ip, RSC_P, IB_p), ('LM337 -16', In, RSC_N, IB_n)):
    for lab, Vpk in (('nominal', Vp(VS*k_vacio)), ('linea +10 %', Vp(1.1*VS*k_vacio))):
        Vin, P = pot_reg(Vpk, I, Rsc, 16, IB)
        out(f'P {nombre} {lab} (V_IN={Vin:.1f} V)', P, 'W')
TA = 40.0; TJ_REG = 125.0; TJ_TIP = 150.0
TH_JC_REG, TH_CS = 5.0, 1.0      # LM317T/LM337T; mica + grasa
TH_JC_TIP = 3.125                # TIP31C/TIP32C
out('theta_SA max LM317 (P=3.6 W)', (TJ_REG-TA)/3.6 - TH_JC_REG - TH_CS, 'C/W')
for nombre, Ilim, Iq in (('Q1 TIP32C (+16 en corto)', VBE/RSC_P, 0), ('Q3 TIP31C (-16 en corto)', VBE/RSC_N, 0)):
    for lab, Vpk in (('nominal', Vp(VS*k_vacio)), ('linea +10 %', Vp(1.1*VS*k_vacio))):
        Vdc = Vpk - Ilim/(f*C)/2
        P = (Vdc - VBE - 1.8)*Ilim          # 1.8 V = dropout del regulador con su salida en 0 V
        out(f'P {nombre} {lab}', P, 'W')
        out(f'Tj {nombre} {lab} con 5 C/W', TA + P*(TH_JC_TIP+TH_CS+5.0), 'C')
out('theta_SA max TIP32C (P=9.9 W)', (TJ_TIP-TA)/9.9 - TH_JC_TIP - TH_CS, 'C/W')

# ---------------- 8. Regulación esperada (hoja de datos LM317) ----------------
dVin = (Vp(1.1*VS) - Vp(0.9*VS))
out('Delta Vin por linea +-10 %', dVin, 'V')
out('Reg. de linea max (0.04 %/V)', 0.0004*dVin*16*1e3, 'mV')
out('Reg. de carga max (0.5 %)', 0.005*16*1e3, 'mV')
for RR in (66, 80):
    out(f'rizado de salida +16 con RR={RR} dB', Vrr_p*10**(-RR/20)*1e3, 'mV rms')

# ---------------- 9. Transformador: corriente y fusibles ----------------
Irms = 2.4*math.hypot(Iraw_p, Iraw_n)          # media onda con filtro capacitivo: Irms ~ 2.4 Idc
out('I rms secundario (aprox.)', Irms, 'A')
out('I rms secundario con ambos rieles al limite', 2.4*math.hypot(VBE/RSC_P, VBE/RSC_N), 'A')
out('Componente DC neta en el devanado', (Iraw_p-Iraw_n)*1e3, 'mA')
Pdc = Vdc_p*Iraw_p + Vdc_n*Iraw_n
out('Potencia DC tomada de los filtros', Pdc, 'W')
out('I primario aprox (eficiencia 70 %)', Pdc/0.7/115*1e3, 'mA')
json.dump(R, open('resultados_calculos.json', 'w'), indent=1, ensure_ascii=False)
