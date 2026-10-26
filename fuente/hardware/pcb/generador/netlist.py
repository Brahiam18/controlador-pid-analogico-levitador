"""Netlist de la fuente ±16 V / +5 V (misma numeración que el esquemático e informe).
Pines: TO-220  TIP31C/TIP32C 1=B 2=C 3=E | LM317T 1=ADJ 2=OUT 3=IN | LM337T 1=ADJ 2=IN 3=OUT
       TO-92   BC547/BC557 1=C 2=B 3=E (cara plana al frente)
       diodos y LED 1=ánodo 2=cátodo | electrolíticos y tántalo 1=+ 2=−
       trimmer 3296W 1, 2=cursor, 3
"""
PARTS = {
 'J1':('TERM2','SEC 18V'), 'F2':('FUSE','T1A 5x20'),
 'D1':('DO41','1N4007'), 'D2':('DO41','1N4007'),
 'C1':('CPOL25','6800u/50V'), 'C2':('CPOL25','6800u/50V'),
 'RSC1':('RES1W','1R8 1W'), 'RSC2':('RES1W','2R2 1W'),
 'Q1':('TO220','TIP32C'), 'Q2':('TO92','BC557'), 'R3':('RES2W','820 2W'),
 'Q3':('TO220','TIP31C'), 'Q4':('TO92','BC547'), 'R4':('RES2W','820 2W'),
 'C5':('CAP','100n'), 'C6':('CAP','100n'),
 'U1':('TO220','LM317T'), 'U2':('TO220','LM337T'), 'U3':('TO220','LM317T'),
 'R5':('RES10','120 1%'), 'R7':('RES10','1k3 1%'), 'RV1':('TRIM','200 3296W'), 'C7':('CPOL5','10u/25V'),
 'D3':('DO41','1N4007'), 'D4':('DO35','1N4148'), 'C9':('CTANT','10u tant'), 'C10':('CAP','100n'),
 'D7':('DO41','1N4007'), 'R12':('RES10','2k2'), 'LED1':('LED5','verde'),
 'R6':('RES10','120 1%'), 'R8':('RES10','1k3 1%'), 'RV2':('TRIM','200 3296W'), 'C8':('CPOL5','10u/25V'),
 'D5':('DO41','1N4007'), 'D6':('DO35','1N4148'), 'C11':('CTANT','10u tant'), 'C12':('CAP','100n'),
 'D8':('DO41','1N4007'), 'R13':('RES10','2k2'), 'LED2':('LED5','verde'),
 'R9':('RES3W','100 3W'), 'C13':('CPOL6','100u/25V'), 'C14':('CAP','100n'),
 'R10':('RES10','120 1%'), 'R11':('RES10','330 1%'), 'RV3':('TRIM','50 3296W'), 'C15':('CPOL5','10u/25V'),
 'D9':('DO41','1N4007'), 'D10':('DO35','1N4148'), 'C16':('CTANT','10u tant'), 'C17':('CAP','100n'),
 'D11':('DO41','1N4007'), 'R14':('RES10','470'), 'LED3':('LED5','verde'),
 'J2':('TERM4','SALIDA'), 'J3':('HDR3','TP'),
}
def build():
    n = {}
    def add(name, *pins): n.setdefault(name, []).extend(pins)
    add('ACIN', ('J1','2'), ('F2','1'))
    add('AC', ('F2','2'), ('D1','1'), ('D2','2'))
    add('VRAWP', ('D1','2'), ('C1','1'), ('RSC1','1'), ('Q2','3'), ('J3','1'))
    add('VRAWN', ('D2','1'), ('C2','2'), ('RSC2','1'), ('Q4','3'), ('J3','3'))
    # +16 V
    add('VE1', ('RSC1','2'), ('Q1','3'), ('Q2','2'))
    add('VB1', ('Q1','1'), ('Q2','1'), ('R3','1'))
    add('VIN1', ('Q1','2'), ('C5','1'), ('U1','3'), ('D3','2'))
    add('ADJ1', ('U1','1'), ('R5','2'), ('R7','1'), ('C7','1'), ('D4','1'))
    add('RV1A', ('R7','2'), ('RV1','1'))
    add('+16V', ('U1','2'), ('R5','1'), ('D3','1'), ('D4','2'), ('C9','1'), ('C10','1'), ('D7','2'), ('R12','1'), ('R9','1'), ('J2','1'))
    add('LED1A', ('R12','2'), ('LED1','1'))
    # -16 V
    add('VE3', ('RSC2','2'), ('Q3','3'), ('Q4','2'))
    add('VB3', ('Q3','1'), ('Q4','1'), ('R4','1'))
    add('VIN2', ('Q3','2'), ('C6','2'), ('U2','2'), ('D5','1'))
    add('ADJ2', ('U2','1'), ('R6','2'), ('R8','1'), ('C8','2'), ('D6','2'))
    add('RV2A', ('R8','2'), ('RV2','1'))
    add('-16V', ('U2','3'), ('R6','1'), ('D5','2'), ('D6','1'), ('C11','2'), ('C12','2'), ('D8','1'), ('LED2','2'), ('J2','2'))
    add('LED2A', ('R13','2'), ('LED2','1'))
    # +5 V
    add('VIN3', ('R9','2'), ('C13','1'), ('C14','1'), ('U3','3'), ('D9','2'))
    add('ADJ3', ('U3','1'), ('R10','2'), ('R11','1'), ('C15','1'), ('D10','1'))
    add('RV3A', ('R11','2'), ('RV3','1'))
    add('+5V', ('U3','2'), ('R10','1'), ('D9','1'), ('D10','2'), ('C16','1'), ('C17','1'), ('D11','2'), ('R14','1'), ('J2','4'))
    add('LED3A', ('R14','2'), ('LED3','1'))
    # tierra
    add('GND', ('J1','1'), ('C1','2'), ('C2','1'), ('R3','2'), ('R4','2'), ('C5','2'), ('C6','1'),
        ('RV1','2'), ('RV1','3'), ('C7','2'), ('C9','2'), ('C10','2'), ('D7','1'), ('LED1','2'),
        ('RV2','2'), ('RV2','3'), ('C8','1'), ('C11','1'), ('C12','1'), ('D8','2'), ('R13','1'),
        ('C13','2'), ('C14','2'), ('RV3','2'), ('RV3','3'), ('C15','2'), ('C16','2'), ('C17','2'), ('D11','1'), ('LED3','2'),
        ('J2','3'), ('J3','2'))
    return n
NETS = build()
SHARED = set()
WIDE = {'ACIN','AC','VRAWP','VRAWN','GND'}
WIDE_W = 1.6
TRACE = 0.8
def base_net(name): return name
def width_of(name, trace=TRACE):
    return WIDE_W if name in WIDE else trace
if __name__ == '__main__':
    pins = [p for v in NETS.values() for p in v]
    assert len(pins) == len(set(pins)), 'pin repetido'
    allp = {(r, p) for r, (k, _) in PARTS.items() for p in __import__('engine').fp_pads(k) and [q[0] for q in __import__('engine').fp_pads(k)]}
    print('sin conectar:', sorted(allp - set(pins)))
    for k, v in NETS.items(): print(k, len(v))
