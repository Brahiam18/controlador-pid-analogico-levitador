"""Netlist de UN módulo PID (basado en el esquemático de Proteus del informe).
R1 <- V_ref (entrada inversora), R3 <- V_sensor (no inversora): Ve = V_sensor - V_ref."""
# componente: (tipo, valor)
PARTS = {
 'U1':('DIP8','LM741'),'U2':('DIP8','LM741'),'U3':('DIP8','LM741'),'U4':('DIP8','LM741'),
 'U5':('DIP8','LM741'),'U6':('DIP8','LM741'),'U7':('DIP8','LM741'),
 'R1':('RES','10k'),'R2':('RES','10k'),'R3':('RES','10k'),'R4':('RES','10k'),'R5':('RES','10k'),
 'R6':('RES','1k'),'R7':('RES','10k'),'R8':('RES','10k'),'R9':('RES','10k'),'ROFFSET':('RES','10k'),
 'R10':('RES','1k'),'RBIAS':('RES','4.4k'),'R11':('RES','1M'),'R12':('RES','160k'),
 'R13':('RES','240k'),'R14':('RES','96k'),'R15':('RES','160k'),
 'POT1':('POT','22k'),'POT2':('POT','220k'),'POT3':('POT','22k'),
 'C1':('CAP','1u'),'C2':('CAP','1u'),
 'J_IN':('HDR1','VSENSOR'),'J_OUT':('HDR1','VPID'),'J_PWR':('HDR4','PWR'),
}
# red -> lista de (comp, pin)   (nombres locales; globales se prefijan por módulo)
NETS = {
 'GND':[('U1',None)],  # se llena abajo
}
def build():
    n = {}
    def add(name,*pins): n.setdefault(name,[]).extend(pins)
    # alimentación
    for u in ['U1','U2','U3','U4','U5','U6','U7']:
        add('+16V',(u,'7')); add('-16V',(u,'4'))
    # U6: Vref
    add('VREFD',('R12','1'),('R13','1'),('U6','3')); add('GND',('R12','2')); add('+5V',('R13','2'))
    add('VREF',('U6','6'),('U6','2'),('R1','1'))
    # U1: error
    add('U1N',('R1','2'),('R2','1'),('U1','2'))
    add('VSEN',('R3','1'),('J_IN','1'))
    add('U1P',('R3','2'),('R4','1'),('U1','3')); add('GND',('R4','2'))
    add('VE',('U1','6'),('R2','2'),('R5','1'),('POT2','1'),('R6','1'))
    # U2: P
    add('U2N',('R5','2'),('POT1','1'),('U2','2')); add('GND',('U2','3'))
    add('VP',('U2','6'),('POT1','2'),('POT1','3'),('R7','1'))
    # U3: I
    add('U3N',('POT2','2'),('POT2','3'),('C1','1'),('R11','1'),('U3','2')); add('GND',('U3','3'))
    add('VI',('U3','6'),('C1','2'),('R11','2'),('R8','1'))
    # U4: D
    add('R6C2',('R6','2'),('C2','1'))
    add('U4N',('C2','2'),('POT3','1'),('U4','2')); add('GND',('U4','3'))
    add('VD',('U4','6'),('POT3','2'),('POT3','3'),('R9','1'))
    # U5: sumador
    add('SUMN',('R7','2'),('R8','2'),('R9','2'),('ROFFSET','2'),('R10','1'),('U5','2'))
    add('U5P',('U5','3'),('RBIAS','1')); add('GND',('RBIAS','2'))
    add('VPID',('U5','6'),('R10','2'),('J_OUT','1'))
    # U7: Voff
    add('VOFFD',('R14','2'),('R15','1'),('U7','3')); add('-16V',('R14','1')); add('GND',('R15','2'))
    add('VOFF',('U7','6'),('U7','2'),('ROFFSET','1'))
    # conectores de alimentación del módulo
    add('+16V',('J_PWR','1')); add('-16V',('J_PWR','2')); add('GND',('J_PWR','3')); add('+5V',('J_PWR','4'))
    return n
NETS = build()
SHARED = {'GND','+16V','-16V','+5V'}
if __name__=='__main__':
    for k,v in NETS.items(): print(k,len(v),v)
    pins=set(p for v in NETS.values() for p in v)
    print(len(pins),'pins')
