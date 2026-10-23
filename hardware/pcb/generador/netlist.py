"""Netlist de UN módulo PID (basado en el esquemático de Proteus del informe).
R1 <- V_ref (entrada inversora), R3 <- V_sensor (no inversora): Ve = V_sensor - V_ref.

Los 8 amplificadores se reparten en 2 TL074CN (DIP-14, 4 amp. c/u): IC1 e IC2.
  U1..U7 son las etapas del informe; U8 es el convertidor tensión-corriente de la etapa de potencia.
Etapa de potencia (una por PID): U8 + TIP122 + banco de 10 x 1 ohm / 5 W (0.1 ohm) + diodo de protección.
TL074 (DIP-14): 1 OUT1  2 IN1-  3 IN1+  4 V+  5 IN2+  6 IN2-  7 OUT2
                8 OUT3  9 IN3-  10 IN3+ 11 V-  12 IN4+ 13 IN4- 14 OUT4
"""
# canal -> (pin OUT, pin IN-, pin IN+) del TL074
from engine import RSB_COLS
CH = {1:('1','2','3'), 2:('7','6','5'), 3:('8','9','10'), 4:('14','13','12')}
GATE = {1:'A', 2:'B', 3:'C', 4:'D'}
SLOTS = [('IC1',1),('IC1',2),('IC1',3),('IC1',4),('IC2',1),('IC2',2),('IC2',3),('IC2',4)]
STAGES = ['U1','U2','U3','U4','U5','U6','U7','U8']
NAMES = {'U1':'U1 diferenciador','U2':'U2 P','U3':'U3 I','U4':'U4 D','U5':'U5 sumador','U6':'U6 Vref','U7':'U7 Voff','U8':'U8 V-I potencia'}

# Reparto final de las etapas en los 8 canales (IC1: canales 1-4, IC2: canales 1-4)
ASSIGNS = {
 'final':['U6','U1','U2','U3','U4','U5','U7','U8'],
}
ASSIGN = 'final'

# componente: (tipo, valor)
PARTS = {
 'IC1':('DIP14','TL074CN'),'IC2':('DIP14','TL074CN'),
 'R1':('RES','10k'),'R2':('RES','10k'),'R3':('RES','10k'),'R4':('RES','10k'),'R5':('RES','10k'),
 'R6':('RES','1k'),'R7':('RES','10k'),'R8':('RES','10k'),'R9':('RES','10k'),'ROFFSET':('RES','10k'),
 'R10':('RES','1k'),'RBIAS':('RES','4.4k'),'R11':('RES','1M'),'R12':('RES','160k'),
 'R13':('RES','240k'),'R14':('RES','96k'),'R15':('RES','160k'),
 'POT1':('POT','22k'),'POT2':('POT','220k'),'POT3':('POT','22k'),
 'C1':('CAP','1u'),'C2':('CAP','1u'),
 'R16':('RES','270'),'R17':('RES','10k'),'R18':('RES','1k'),'RBASE':('RES','270'),'C3':('CAP','10n (opc.)'),
 'POT4':('POT','10k'),'D1':('DIODE','1N5408'),'D2':('DIODE_S','1N4148'),'Q1':('TO220','TIP122'),
 'RS':('RSBANK','3 x 1R 5W'),
 'J_COIL':('TERM2','BOBINA'),'J_VBOB':('TERM2','VBOB'),'JP_GND':('HDR2','GND-PGND'),
 'J_IN':('HDR1','VSENSOR'),'J_OUT':('HDR1','VPID'),'J_PWR':('HDR4','PWR'),
}

def where(stage, assign=None):
    """(circuito integrado, canal) donde cae cada etapa"""
    a = ASSIGNS[assign or ASSIGN]
    ic, ch = SLOTS[a.index(stage)]
    return ic, ch

def build(assign=None):
    n = {}
    def add(name,*pins): n.setdefault(name,[]).extend(pins)
    def op(stage):
        ic, ch = where(stage, assign); o, m, p = CH[ch]
        return (ic,o),(ic,m),(ic,p)
    OUT = {s:op(s)[0] for s in STAGES}; INM = {s:op(s)[1] for s in STAGES}; INP = {s:op(s)[2] for s in STAGES}
    # alimentación de los dos CI
    for ic in ('IC1','IC2'):
        add('+16V',(ic,'4')); add('-16V',(ic,'11'))
    # U6: Vref
    add('VREFD',('R12','1'),('R13','1'),INP['U6']); add('GND',('R12','2')); add('+5V',('R13','2'))
    add('VREF',OUT['U6'],INM['U6'],('R1','1'))
    # U1: error
    add('U1N',('R1','2'),('R2','1'),INM['U1'])
    add('VSEN',('R3','1'),('J_IN','1'))
    add('U1P',('R3','2'),('R4','1'),INP['U1']); add('GND',('R4','2'))
    add('VE',OUT['U1'],('R2','2'),('R5','1'),('POT2','1'),('R6','1'))
    # U2: P
    add('U2N',('R5','2'),('POT1','1'),INM['U2']); add('GND',INP['U2'])
    add('VP',OUT['U2'],('POT1','2'),('POT1','3'),('R7','1'))
    # U3: I
    add('U3N',('POT2','2'),('POT2','3'),('C1','1'),('R11','1'),INM['U3']); add('GND',INP['U3'])
    add('VI',OUT['U3'],('C1','2'),('R11','2'),('R8','1'))
    # U4: D
    add('R6C2',('R6','2'),('C2','1'))
    add('U4N',('C2','2'),('POT3','1'),INM['U4']); add('GND',INP['U4'])
    add('VD',OUT['U4'],('POT3','2'),('POT3','3'),('R9','1'))
    # U5: sumador
    add('SUMN',('R7','2'),('R8','2'),('R9','2'),('ROFFSET','2'),('R10','1'),INM['U5'])
    add('U5P',INP['U5'],('RBIAS','1')); add('GND',('RBIAS','2'))
    add('VPID',OUT['U5'],('R10','2'),('J_OUT','1'))
    # U7: Voff
    add('VOFFD',('R14','2'),('R15','1'),INP['U7']); add('-16V',('R14','1')); add('GND',('R15','2'))
    add('VOFF',OUT['U7'],INM['U7'],('ROFFSET','1'))
    # ---------------- etapa de potencia ----------------
    # divisor de calibración: VPID -> R17 -> POT4 -> GND ; cursor -> R16 (270) -> entrada + de U8
    add('VPID',('R17','1'))
    add('VDIV',('R17','2'),('POT4','1')); add('GND',('POT4','3'))
    add('VCAL',('POT4','2'),('R16','1'))
    add('VINP',('R16','2'),INP['U8'])
    # realimentación de corriente: emisor -> R18 -> entrada - ; C3 opcional (salida -> entrada -)
    add('ISENSE',('Q1','3'),('R18','1'))
    for k in range(RSB_COLS+1,2*RSB_COLS+1): add('ISENSE',('RS','%d'%k))
    add('INMU',('R18','2'),('C3','1'),INM['U8'])
    add('IOUT',OUT['U8'],('C3','2'),('RBASE','1'))
    add('BASEA',('RBASE','2'),('D2','1'))
    add('BASE',('D2','2'),('Q1','1'))
    # colector, bobina y protección
    add('COILN',('Q1','2'),('D1','1'),('J_COIL','2'))
    add('+VBOB',('D1','2'),('J_COIL','1'),('J_VBOB','1'))
    for k in range(1,RSB_COLS+1): add('PGND',('RS','%d'%k))
    add('PGND',('J_VBOB','2'),('JP_GND','2')); add('GND',('JP_GND','1'))
    # conectores de alimentación del módulo
    add('+16V',('J_PWR','1')); add('-16V',('J_PWR','2')); add('GND',('J_PWR','3')); add('+5V',('J_PWR','4'))
    return n
def set_assign(a):
    global ASSIGN, NETS
    ASSIGN = a; NETS = build(a)

def chan_labels(assign=None):
    """{(ic, pin_salida): nombre de etapa}"""
    out = {}
    for stage in STAGES:
        ic, ch = where(stage, assign)
        out[(ic, CH[ch][0])] = stage
    return out

NETS = build()
SHARED = {'GND','+16V','-16V','+5V'}
# redes de potencia: pista ancha (2.0 mm, ~3.9 A con +10 C) y sin puentes de alambre
WIDE = {'ISENSE','COILN','+VBOB','PGND'}
WIDE_W = 2.0
import re as _re
def base_net(name):
    m=_re.match(r'^P\d_(.*)$',name)
    return m.group(1) if m else name
def width_of(name,trace=0.7):
    return WIDE_W if base_net(name) in WIDE else trace
if __name__=='__main__':
    for k,v in NETS.items(): print(k,len(v),v)
    pins=[p for v in NETS.values() for p in v]
    print(len(pins),'pines', len(set(pins)),'únicos')
