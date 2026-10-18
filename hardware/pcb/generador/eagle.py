"""Exportador EAGLE (.sch / .brd) abribles en Fusion Electronics."""
import collections
from xml.sax.saxutils import escape
from engine import *
import netlist as N

LIB='pid4'
LAYERS=[(1,'Top',4,1,'yes','yes'),(16,'Bottom',1,1,'yes','yes'),(17,'Pads',2,1,'yes','yes'),(18,'Vias',2,1,'yes','yes'),
(19,'Unrouted',6,1,'yes','yes'),(20,'Dimension',15,1,'yes','yes'),(21,'tPlace',7,1,'yes','yes'),(22,'bPlace',7,1,'yes','yes'),
(23,'tOrigins',15,1,'yes','yes'),(24,'bOrigins',15,1,'yes','yes'),(25,'tNames',7,1,'yes','yes'),(26,'bNames',7,1,'yes','yes'),
(27,'tValues',7,1,'yes','yes'),(28,'bValues',7,1,'yes','yes'),(29,'tStop',7,3,'no','yes'),(30,'bStop',7,6,'no','yes'),
(31,'tCream',7,4,'no','yes'),(32,'bCream',7,5,'no','yes'),(33,'tFinish',6,3,'no','yes'),(34,'bFinish',6,6,'no','yes'),
(35,'tGlue',7,4,'no','yes'),(36,'bGlue',7,5,'no','yes'),(37,'tTest',7,1,'no','yes'),(38,'bTest',7,1,'no','yes'),
(39,'tKeepout',4,11,'yes','yes'),(40,'bKeepout',1,11,'yes','yes'),(41,'tRestrict',4,10,'yes','yes'),(42,'bRestrict',1,10,'yes','yes'),
(43,'vRestrict',2,10,'yes','yes'),(44,'Drills',7,1,'no','yes'),(45,'Holes',7,1,'no','yes'),(46,'Milling',3,1,'no','yes'),
(47,'Measures',7,1,'no','yes'),(48,'Document',7,1,'yes','yes'),(49,'Reference',7,1,'yes','yes'),(51,'tDocu',7,1,'yes','yes'),
(52,'bDocu',7,1,'yes','yes'),(91,'Nets',2,1,'yes','yes'),(92,'Busses',1,1,'yes','yes'),(93,'Pins',2,1,'no','yes'),
(94,'Symbols',4,1,'yes','yes'),(95,'Names',7,1,'yes','yes'),(96,'Values',7,1,'yes','yes'),(97,'Info',7,1,'yes','yes'),(98,'Guide',6,1,'yes','yes')]

def f(v): 
    s=('%.4f'%v).rstrip('0').rstrip('.')
    return '0' if s in('-0','') else s

def layers_xml():
    return '<layers>\n'+'\n'.join('<layer number="%d" name="%s" color="%d" fill="%d" visible="%s" active="%s"/>'%l for l in LAYERS)+'\n</layers>\n'

def wire(x1,y1,x2,y2,w,layer,extra=''):
    return '<wire x1="%s" y1="%s" x2="%s" y2="%s" width="%s" layer="%d"%s/>'%(f(x1),f(y1),f(x2),f(y2),f(w),layer,extra)

def rect_lines(x0,y0,x1,y1,w=0.2,layer=21):
    return [wire(x0,y0,x1,y0,w,layer),wire(x1,y0,x1,y1,w,layer),wire(x1,y1,x0,y1,w,layer),wire(x0,y1,x0,y0,w,layer)]

PADDIA=2.0
def pad(name,x,y,shape='round',drill=DRILL,dia=PAD_D):
    return '<pad name="%s" x="%s" y="%s" drill="%s" diameter="%s" shape="%s"/>'%(name,f(x),f(y),f(drill),f(dia),shape)

def packages_xml():
    P=[]
    # DIL14
    L=[]
    for pin,x,y in fp_pads('DIP14'):
        L.append(pad(pin,x,y,'square' if pin=='1' else 'round'))
    L+=rect_lines(1.4,-16.5,6.2,1.3)
    L.append('<wire x1="3.2" y1="1.3" x2="4.4" y2="1.3" width="0.2" layer="21" curve="180"/>')
    L.append('<text x="3.81" y="-7.62" size="1.27" layer="25" rot="R90" align="center">&gt;NAME</text>')
    L.append('<text x="3.81" y="-12.5" size="1.0" layer="27" rot="R90" align="center">&gt;VALUE</text>')
    P.append(('DIL14','DIL14 (TL074CN), separación entre filas 7.62 mm',L))
    # RES
    L=[pad('1',0,0,'square'),pad('2',7.62,0)]
    L+=rect_lines(1.3,-1.1,6.3,1.1)+[wire(0,0,1.3,0,0.2,21),wire(6.3,0,7.62,0,0.2,21)]
    L.append('<text x="3.81" y="1.9" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>')
    L.append('<text x="3.81" y="-1.9" size="1.0" layer="27" align="top-center">&gt;VALUE</text>')
    P.append(('RES','Resistencia axial 1/4 W, 7.62 mm',L))
    # CAP
    L=[pad('1',0,0,'square'),pad('2',5.08,0)]
    L+=rect_lines(-1.5,-2.5,6.58,2.5)
    L.append('<text x="2.54" y="3.2" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>')
    L.append('<text x="2.54" y="-3.2" size="1.0" layer="27" align="top-center">&gt;VALUE</text>')
    P.append(('CAP','Capacitor no polarizado, separación 5.08 mm',L))
    # POT
    L=[pad('1',0,0,'square'),pad('2',5.08,0),pad('3',10.16,0)]
    L+=rect_lines(-2.6,-4.6,12.76,4.6)
    L.append('<text x="5.08" y="5.3" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>')
    L.append('<text x="5.08" y="-5.3" size="1.0" layer="27" align="top-center">&gt;VALUE</text>')
    P.append(('POT','Potenciómetro 3 pines, separación 5.08 mm',L))
    # HDR2/HDR4
    for nm,n in (('HDR1',1),('HDR2',2),('HDR4',4)):
        L=[pad(str(i+1),i*PITCH,0,'square' if i==0 else 'round') for i in range(n)]
        L+=rect_lines(-1.4,-1.4,(n-1)*PITCH+1.4,1.4)
        L.append('<text x="%s" y="2.1" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>'%f((n-1)*PITCH/2))
        P.append((nm,'Regleta de %d pines, 2.54 mm'%n,L))
    out='<packages>\n'
    for name,desc,L in P:
        out+='<package name="%s">\n<description>%s</description>\n'%(name,escape(desc))+'\n'.join(L)+'\n</package>\n'
    return out+'</packages>\n'

# ---------------- símbolos ----------------
def sym_pin(name,x,y,rot='R0',direction='pas',length='short'):
    r='' if rot=='R0' else ' rot="%s"'%rot
    return '<pin name="%s" x="%s" y="%s" length="%s" direction="%s"%s/>'%(name,f(x),f(y),length,direction,r)

SYMS={}   # nombre -> dict(xml, pins{pinname:(x,y,dir)}) dir: 'L','R','D'
def build_symbols():
    S={}
    # amplificador (un canal del TL074)
    L=[wire(-5.08,-5.08,-5.08,5.08,0.254,94),wire(-5.08,5.08,5.08,0,0.254,94),wire(5.08,0,-5.08,-5.08,0.254,94),
       '<text x="-5.08" y="6.0" size="1.778" layer="95">&gt;NAME</text>','<text x="-5.08" y="-7.6" size="1.778" layer="96">&gt;VALUE</text>',
       '<text x="-4.3" y="2.0" size="1.27" layer="94">-</text>','<text x="-4.3" y="-3.6" size="1.27" layer="94">+</text>']
    pins={}
    for nm,x,y,rt,d,dr in (('IN-',-7.62,2.54,'R0','L','in'),('IN+',-7.62,-2.54,'R0','L','in'),('OUT',7.62,0,'R180','R','out')):
        L.append(sym_pin(nm,x,y,rt,dr)); pins[nm]=(x,y,d)
    S['OPAMP']=(L,pins)
    # alimentación del TL074
    L=rect_lines(-2.54,-2.54,2.54,2.54,0.254,94)+['<text x="3.2" y="0.5" size="1.778" layer="95">&gt;NAME</text>','<text x="-2.0" y="-0.6" size="1.27" layer="94">TL074</text>',
       sym_pin('V+',0,5.08,'R270','pwr'),sym_pin('V-',0,-5.08,'R90','pwr')]
    S['OPWR']=(L,{'V+':(0,5.08,'U'),'V-':(0,-5.08,'D')})
    # R
    L=rect_lines(-2.54,-1.016,2.54,1.016,0.254,94)+['<text x="-3.81" y="2.2" size="1.778" layer="95">&gt;NAME</text>','<text x="-3.81" y="-3.9" size="1.778" layer="96">&gt;VALUE</text>',
        sym_pin('1',-5.08,0),sym_pin('2',5.08,0,'R180')]
    S['R']=(L,{'1':(-5.08,0,'L'),'2':(5.08,0,'R')})
    # C
    L=[wire(-0.6,-2.54,-0.6,2.54,0.4,94),wire(0.6,-2.54,0.6,2.54,0.4,94),'<text x="-3.81" y="3.2" size="1.778" layer="95">&gt;NAME</text>','<text x="-3.81" y="-5.4" size="1.778" layer="96">&gt;VALUE</text>',
        sym_pin('1',-5.08,0),sym_pin('2',5.08,0,'R180')]
    S['C']=(L,{'1':(-5.08,0,'L'),'2':(5.08,0,'R')})
    # POT
    L=rect_lines(-3.81,-1.016,3.81,1.016,0.254,94)+[wire(0,-2.54,0,-1.016,0.254,94),'<text x="-5.08" y="2.2" size="1.778" layer="95">&gt;NAME</text>','<text x="-5.08" y="-7.4" size="1.778" layer="96">&gt;VALUE</text>',
        sym_pin('1',-7.62,0),sym_pin('3',7.62,0,'R180'),sym_pin('2',0,-5.08,'R90')]
    S['POT']=(L,{'1':(-7.62,0,'L'),'3':(7.62,0,'R'),'2':(0,-5.08,'D')})
    for nm,n in (('HDR1',1),('HDR2',2),('HDR4',4)):
        top=1.27; bot=-(n-1)*2.54-1.27
        L=rect_lines(-2.54,bot,2.54,top,0.254,94)+['<text x="-2.54" y="%s" size="1.778" layer="95">&gt;NAME</text>'%f(top+1.0)]
        pins={}
        for i in range(n):
            L.append(sym_pin(str(i+1),-5.08,-i*2.54)); pins[str(i+1)]=(-5.08,-i*2.54,'L')
        S[nm]=(L,pins)
    return S
SYMS=build_symbols()

def _single(sym,pk,pre,pins):
    return dict(prefix=pre,package=pk,gates=[('G$1',sym,'next')],connects=[('G$1',p,p) for p in pins])
DEVSETS={ # nombre: prefijo, paquete, compuertas [(nombre,símbolo,addlevel)], conexiones [(compuerta,pin símbolo,pad)]
 'TL074':dict(prefix='IC',package='DIL14',
    gates=[('A','OPAMP','next'),('B','OPAMP','next'),('C','OPAMP','next'),('D','OPAMP','next'),('P','OPWR','request')],
    connects=[('A','OUT','1'),('A','IN-','2'),('A','IN+','3'),
              ('B','IN+','5'),('B','IN-','6'),('B','OUT','7'),
              ('C','OUT','8'),('C','IN-','9'),('C','IN+','10'),
              ('D','IN+','12'),('D','IN-','13'),('D','OUT','14'),
              ('P','V+','4'),('P','V-','11')]),
 'R':_single('R','RES','R',['1','2']),
 'C':_single('C','CAP','C',['1','2']),
 'POT':_single('POT','POT','RV',['1','2','3']),
 'HDR1':_single('HDR1','HDR1','J',['1']),
 'HDR2':_single('HDR2','HDR2','J',['1','2']),
 'HDR4':_single('HDR4','HDR4','J',['1','2','3','4']),
}
KIND2DEV={'DIP14':'TL074','RES':'R','CAP':'C','POT':'POT','HDR1':'HDR1','HDR2':'HDR2','HDR4':'HDR4'}
KIND2PKG={'DIP14':'DIL14','RES':'RES','CAP':'CAP','POT':'POT','HDR1':'HDR1','HDR2':'HDR2','HDR4':'HDR4'}
# pad de componente -> (compuerta, pin de símbolo)
def sympin(kind,pad):
    dev=DEVSETS[KIND2DEV[kind]]
    for g,sp,pd in dev['connects']:
        if pd==pad: return g,sp
    raise KeyError((kind,pad))

def libraries_sch():
    out='<libraries>\n<library name="%s">\n'%LIB+packages_xml()+'<symbols>\n'
    for nm,(L,pins) in SYMS.items():
        out+='<symbol name="%s">\n'%nm+'\n'.join(L)+'\n</symbol>\n'
    out+='</symbols>\n<devicesets>\n'
    for nm,d in DEVSETS.items():
        out+='<deviceset name="%s" prefix="%s">\n<gates>\n'%(nm,d['prefix'])
        for gi,(g,sym,lvl) in enumerate(d['gates']):
            out+='<gate name="%s" symbol="%s" x="%d" y="%d" addlevel="%s"/>\n'%(g,sym,0,-gi*20,lvl)
        out+='</gates>\n<devices>\n<device name="" package="%s">\n<connects>\n'%d['package']
        out+='\n'.join('<connect gate="%s" pin="%s" pad="%s"/>'%c for c in d['connects'])
        out+='\n</connects>\n<technologies>\n<technology name=""/>\n</technologies>\n</device>\n</devices>\n</deviceset>\n'
    return out+'</devicesets>\n</library>\n</libraries>\n'

def libraries_brd():
    return '<libraries>\n<library name="%s">\n'%LIB+packages_xml()+'</library>\n</libraries>\n'

HEAD='<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE eagle SYSTEM "eagle.dtd">\n<eagle version="9.6.2">\n<drawing>\n<settings>\n<setting alwaysvectorfont="no"/>\n<setting verticaltext="up"/>\n</settings>\n<grid distance="1.27" unitdist="mm" unit="mm" style="lines" multiple="1" display="yes" altdistance="0.635" altunitdist="mm" altunit="mm"/>\n'
TAIL='</drawing>\n</eagle>\n'

# ---------------- esquemático ----------------
def vals_of(ref_local):
    return N.PARTS[ref_local][1]

def sch_xml(nmod,nets_global_by_module):
    """nets_global_by_module: {k: {net_global: [(ref_local,pin)]}}"""
    sheets=''
    allparts=[]
    gk=lambda st:(N.where(st)[0],N.GATE[N.where(st)[1]])
    rows=[[gk('U6'),'R12','R13'],['R1'] and [gk('U1'),'R1','R2','R3','R4'],[gk('U2'),'R5','POT1','R7'],[gk('U3'),'POT2','C1','R11','R8'],
          [gk('U4'),'R6','C2','POT3','R9'],[gk('U5'),'ROFFSET','R10','RBIAS'],[gk('U7'),'R14','R15'],
          [gk('SPARE'),'J_IN','J_OUT','J_PWR'],[('IC1','P'),('IC2','P')]]
    keyof=lambda it: it if isinstance(it,tuple) else (it,'G$1')
    stage_of={gk(st):N.NAMES[st] for st in N.STAGES+['SPARE']}
    stage_of[('IC1','P')]='alimentación IC1'; stage_of[('IC2','P')]='alimentación IC2'
    flat=sorted({keyof(r)[0] for row in rows for r in row})
    assert flat==sorted(N.PARTS),set(N.PARTS)^set(flat)
    for k in range(1,nmod+1):
        pre='P%d_'%k
        inst=''; nets=collections.defaultdict(list); plain=''
        pos={}
        CW=62.0; RH=34.0
        for ri,row in enumerate(rows):
            for ci,it in enumerate(row):
                key=keyof(it); ref=key[0]
                kind=N.PARTS[ref][0]
                x=20+ci*CW+12; y=-ri*RH-14
                x=round(x/2.54)*2.54; y=round(y/2.54)*2.54
                pos[key]=(x,y)
                inst+='<instance part="%s%s" gate="%s" x="%s" y="%s"/>\n'%(pre,ref,key[1],f(x),f(y))
                if key in stage_of:
                    plain+='<text x="%s" y="%s" size="1.778" layer="97">%s</text>\n'%(f(x-5.08),f(y+8.5 if key[1]!='P' else y+8.5),escape(stage_of[key]))
        for net,pins in nets_global_by_module[k].items():
            for ref,pin in pins:
                kind=N.PARTS[ref][0]
                g,sp=sympin(kind,pin)
                x,y=pos[(ref,g)]; px,py,d=SYMS[DEVSETS[KIND2DEV[kind]]['gates'][[q[0] for q in DEVSETS[KIND2DEV[kind]]['gates']].index(g)][1]][1][sp]
                px+=x; py+=y
                L=12.7
                rot=''
                if d=='L': ex,ey=px-L,py; lab=(ex,ey)
                elif d=='R': ex,ey=px+L,py; lab=(px,py)
                elif d=='U': ex,ey=px,py+5.08; lab=(ex,ey); rot=' rot="R90"'
                else: ex,ey=px,py-5.08; lab=(ex,ey); rot=' rot="R270"'
                nets[net].append(('<segment>\n<pinref part="%s%s" gate="%s" pin="%s"/>\n'%(pre,ref,g,sp)+
                    wire(px,py,ex,ey,0.1524,91)+'\n<label x="%s" y="%s" size="1.27" layer="95"%s/>\n</segment>\n'%(f(lab[0]),f(lab[1]),rot)))
        netxml=''
        for net,segs in nets.items():
            netxml+='<net name="%s" class="0">\n'%net+''.join(segs)+'</net>\n'
        plain+='<text x="20" y="8" size="3.81" layer="97">Módulo PID %d: controlador PID analógico (2 x TL074CN)</text>\n'%k
        sheets+='<sheet>\n<plain>\n%s</plain>\n<instances>\n%s</instances>\n<busses>\n</busses>\n<nets>\n%s</nets>\n</sheet>\n'%(plain,inst,netxml)
        for ref in N.PARTS:
            kind,val=N.PARTS[ref]
            allparts.append('<part name="%s%s" library="%s" deviceset="%s" device="" value="%s"/>'%(pre,ref,LIB,KIND2DEV[kind],escape(val)))
    out=HEAD+layers_xml()+'<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">\n<description>Cuatro controladores PID analógicos (levitador magnético) - Brahiam Alberto Campiño Romero</description>\n'
    out+=libraries_sch()+'<attributes>\n</attributes>\n<variantdefs>\n</variantdefs>\n<classes>\n<class number="0" name="default" width="0" drill="0"/>\n</classes>\n<parts>\n'+'\n'.join(allparts)+'\n</parts>\n<sheets>\n'+sheets+'</sheets>\n</schematic>\n'+TAIL
    return out

# ---------------- placa ----------------
def merge_edges(edges,layer):
    """aristas unitarias de la rejilla -> segmentos maximales (mm)"""
    H=collections.defaultdict(set); V=collections.defaultdict(set)
    for a,b in edges:
        if a[0]!=layer: continue
        (i0,j0),(i1,j1)=(a[1],a[2]),(b[1],b[2])
        if j0==j1:
            if i0>i1: i0,i1=i1,i0
            for i in range(i0,i1): H[j0].add(i)
        else:
            if j0>j1: j0,j1=j1,j0
            for j in range(j0,j1): V[i0].add(j)
    segs=[]
    for j,s in sorted(H.items()):
        s=sorted(s); st=s[0]; pr=s[0]
        for v in s[1:]+[None]:
            if v is None or v!=pr+1:
                segs.append((st*G,j*G,(pr+1)*G,j*G)); 
                if v is not None: st=v
            if v is not None: pr=v
    for i,s in sorted(V.items()):
        s=sorted(s); st=s[0]; pr=s[0]
        for v in s[1:]+[None]:
            if v is None or v!=pr+1:
                segs.append((i*G,st*G,i*G,(pr+1)*G))
                if v is not None: st=v
            if v is not None: pr=v
    return segs

def brd_xml(parts,routes,W,H,nets,labels=()):
    plain=''.join(wire(*a,0,20) +'\n' for a in [(0,0,W,0),(W,0,W,H),(W,H,0,H),(0,H,0,0)])
    for (x,y,txt,size,rot) in labels:
        plain+='<text x="%s" y="%s" size="%s" layer="21"%s>%s</text>\n'%(f(x),f(y),f(size),'' if rot=='R0' else ' rot="%s"'%rot,escape(txt))
    elems=''
    for ref,p in parts.items():
        loc=ref.split('_',1)[1]; kind=p.kind
        elems+='<element name="%s" library="%s" package="%s" value="%s" x="%s" y="%s"%s/>\n'%(ref,LIB,KIND2PKG[kind],escape(N.PARTS[loc][1]),f(p.x),f(p.y),'' if p.r%4==0 else ' rot="R%d"'%(90*(p.r%4)))
    sig=''
    for net,pins in nets.items():
        sig+='<signal name="%s">\n'%net
        for ref,pin in pins: sig+='<contactref element="%s" pad="%s"/>\n'%(ref,pin)
        rt=routes.get(net)
        if rt:
            for s in merge_edges(rt['edges'],0): sig+=wire(*s,TRACE,16)+'\n'
            for s in merge_edges(rt['edges'],1): sig+=wire(*s,0.6,1)+'\n'
            for (i,j) in sorted(rt['vias']): sig+='<via x="%s" y="%s" extent="1-16" drill="%s" diameter="%s"/>\n'%(f(i*G),f(j*G),f(DRILL),f(PAD_D))
        sig+='</signal>\n'
    dr='<designrules name="default">\n<description>Placa de una cara para quemado casero (toner)</description>\n'
    for k,v in (('layerSetup','(1*16)'),('mtCopper','0.035mm 0.035mm'),('mtIsolate','1.5mm'),('mdWireWire','0.4mm'),('mdWirePad','0.4mm'),('mdWireVia','0.4mm'),
                ('mdPadPad','0.4mm'),('mdPadVia','0.4mm'),('mdViaVia','0.4mm'),('mdViaViaSameLayer','0.4mm'),('mnLayersViaInSmd','2'),
                ('mdCopperDimension','0.6mm'),('mdDrill','0.4mm'),('mdSmdStop','0mil'),('msWidth','0.7mm'),('msDrill','0.9mm'),
                ('rvPadTop','0.25'),('rvPadBottom','0.25'),('rvViaOuter','0.25'),('rlMinPadTop','0.5mm'),('rlMaxPadTop','2mm'),
                ('rlMinPadBottom','0.5mm'),('rlMaxPadBottom','2mm'),('rlMinViaOuter','0.5mm'),('rlMaxViaOuter','2mm')):
        dr+='<param name="%s" value="%s"/>\n'%(k,v)
    dr+='</designrules>\n'
    out=HEAD+layers_xml()+'<board>\n<description>Placa de 4 controladores PID analógicos, una cara (cobre inferior) con puentes de alambre</description>\n<plain>\n'+plain+'</plain>\n'
    out+=libraries_brd()+'<attributes>\n</attributes>\n<variantdefs>\n</variantdefs>\n<classes>\n<class number="0" name="default" width="%s" drill="%s"/>\n</classes>\n'%(f(TRACE),f(DRILL))
    out+=dr+'<elements>\n'+elems+'</elements>\n<signals>\n'+sig+'</signals>\n</board>\n'+TAIL
    return out
