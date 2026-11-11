<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="1.27" unitdist="mm" unit="mm" style="lines" multiple="1" display="yes" altdistance="0.635" altunitdist="mm" altunit="mm"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="yes" active="yes"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="yes" active="yes"/>
<layer number="17" name="Pads" color="2" fill="1" visible="yes" active="yes"/>
<layer number="18" name="Vias" color="2" fill="1" visible="yes" active="yes"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="yes" active="yes"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="yes" active="yes"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="yes" active="yes"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="yes" active="yes"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="yes" active="yes"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="yes" active="yes"/>
<layer number="25" name="tNames" color="7" fill="1" visible="yes" active="yes"/>
<layer number="26" name="bNames" color="7" fill="1" visible="yes" active="yes"/>
<layer number="27" name="tValues" color="7" fill="1" visible="yes" active="yes"/>
<layer number="28" name="bValues" color="7" fill="1" visible="yes" active="yes"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="yes"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="yes"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="yes"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="yes"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="yes"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="yes"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="yes"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="yes"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="yes"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="yes"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="yes" active="yes"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="yes" active="yes"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="yes" active="yes"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="yes" active="yes"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="yes" active="yes"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="yes"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="yes"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="yes"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="yes"/>
<layer number="48" name="Document" color="7" fill="1" visible="yes" active="yes"/>
<layer number="49" name="Reference" color="7" fill="1" visible="yes" active="yes"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="yes" active="yes"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic>
<description>Carga de prueba R_L 10/20 ohm</description>
<libraries>
<library name="carga">
<packages>
<package name="R10W">
<description>Resistencia de cemento 10 W (cuerpo ~49 x 10 x 9 mm), patas a 55,88 mm; montar levantada 5-10 mm</description>
<pad name="1" x="0" y="0" drill="1.2" diameter="3.2" shape="square"/>
<pad name="2" x="55.88" y="0" drill="1.2" diameter="3.2" shape="round"/>
<wire x1="2.44" y1="-5.5" x2="53.44" y2="-5.5" width="0.2" layer="21"/>
<wire x1="53.44" y1="-5.5" x2="53.44" y2="5.5" width="0.2" layer="21"/>
<wire x1="53.44" y1="5.5" x2="2.44" y2="5.5" width="0.2" layer="21"/>
<wire x1="2.44" y1="5.5" x2="2.44" y2="-5.5" width="0.2" layer="21"/>
<text x="27.94" y="5.9" size="1.6" layer="25" align="bottom-center">&gt;NAME</text>
<text x="27.94" y="-5.9" size="1.2" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="TERM2">
<description>Bornera de tornillo 2 vías, paso 5,08 mm</description>
<pad name="1" x="0" y="0" drill="1.3" diameter="3" shape="square"/>
<pad name="2" x="5.08" y="0" drill="1.3" diameter="3" shape="round"/>
<wire x1="-2.5" y1="-5.2" x2="7.58" y2="-5.2" width="0.2" layer="21"/>
<wire x1="7.58" y1="-5.2" x2="7.58" y2="5.6" width="0.2" layer="21"/>
<wire x1="7.58" y1="5.6" x2="-2.5" y2="5.6" width="0.2" layer="21"/>
<wire x1="-2.5" y1="5.6" x2="-2.5" y2="-5.2" width="0.2" layer="21"/>
<text x="2.54" y="6" size="1.6" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.54" y="-5.6" size="1.2" layer="27" align="top-center">&gt;VALUE</text>
</package>
</packages>
<symbols>
<symbol name="R">
<wire x1="-2.54" y1="-1.016" x2="2.54" y2="-1.016" width="0.254" layer="94"/>
<wire x1="2.54" y1="-1.016" x2="2.54" y2="1.016" width="0.254" layer="94"/>
<wire x1="2.54" y1="1.016" x2="-2.54" y2="1.016" width="0.254" layer="94"/>
<wire x1="-2.54" y1="1.016" x2="-2.54" y2="-1.016" width="0.254" layer="94"/>
<text x="-3.81" y="2.4" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-4.2" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="5.08" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="HDR2">
<wire x1="-2.54" y1="-3.81" x2="2.54" y2="-3.81" width="0.254" layer="94"/>
<wire x1="2.54" y1="-3.81" x2="2.54" y2="1.27" width="0.254" layer="94"/>
<wire x1="2.54" y1="1.27" x2="-2.54" y2="1.27" width="0.254" layer="94"/>
<wire x1="-2.54" y1="1.27" x2="-2.54" y2="-3.81" width="0.254" layer="94"/>
<text x="-2.54" y="2.27" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="-5.08" y="-2.54" length="short" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="R10W" prefix="R">
<gates>
<gate name="G$1" symbol="R" x="0" y="0"/>
</gates>
<devices>
<device name="" package="R10W">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TERM2" prefix="J">
<gates>
<gate name="G$1" symbol="HDR2" x="0" y="0"/>
</gates>
<devices>
<device name="" package="TERM2">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0"/>
</classes>
<parts>
<part name="R1" library="carga" deviceset="R10W" device="" value="10R 10W"/>
<part name="R2" library="carga" deviceset="R10W" device="" value="10R 10W"/>
<part name="R3" library="carga" deviceset="R10W" device="" value="10R 10W"/>
<part name="R4" library="carga" deviceset="R10W" device="" value="10R 10W"/>
<part name="J1" library="carga" deviceset="TERM2" device="" value="A J4 o J5"/>
<part name="JP1" library="carga" deviceset="TERM2" device="" value="SEL 10/20R"/>
</parts>
<sheets>
<sheet>
<plain>
<text x="0" y="25.4" size="2.54" layer="97">Carga de prueba R_L: (R1+R2) || (R3+R4). JP1 puenteado = 10 ohm (1,6 A); JP1 abierto = 20 ohm (0,8 A)</text>
<text x="0" y="20.32" size="1.778" layer="97">Conexion por etiquetas de red: X, Y, MA, MB, GND. Polaridad indiferente (sirve para +16 V y -16 V)</text>
</plain>
<instances>
<instance part="J1" gate="G$1" x="10.16" y="0"/>
<instance part="R1" gate="G$1" x="40.64" y="10.16"/>
<instance part="R2" gate="G$1" x="71.12" y="10.16"/>
<instance part="R3" gate="G$1" x="40.64" y="-10.16"/>
<instance part="R4" gate="G$1" x="71.12" y="-10.16"/>
<instance part="JP1" gate="G$1" x="10.16" y="-25.4"/>
</instances>
<busses>
</busses>
<nets>
<net name="X" class="0">
<segment>
<pinref part="J1" gate="G$1" pin="1"/>
<wire x1="5.08" y1="0" x2="0" y2="0" width="0.1524" layer="91"/>
<label x="0" y="0" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R1" gate="G$1" pin="1"/>
<wire x1="35.56" y1="10.16" x2="30.48" y2="10.16" width="0.1524" layer="91"/>
<label x="30.48" y="10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="JP1" gate="G$1" pin="1"/>
<wire x1="5.08" y1="-25.4" x2="0" y2="-25.4" width="0.1524" layer="91"/>
<label x="0" y="-25.4" size="1.27" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="J1" gate="G$1" pin="2"/>
<wire x1="5.08" y1="-2.54" x2="0" y2="-2.54" width="0.1524" layer="91"/>
<label x="0" y="-2.54" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R2" gate="G$1" pin="2"/>
<wire x1="76.2" y1="10.16" x2="81.28" y2="10.16" width="0.1524" layer="91"/>
<label x="76.2" y="10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R3" gate="G$1" pin="1"/>
<wire x1="35.56" y1="-10.16" x2="30.48" y2="-10.16" width="0.1524" layer="91"/>
<label x="30.48" y="-10.16" size="1.27" layer="95"/>
</segment>
</net>
<net name="MA" class="0">
<segment>
<pinref part="R1" gate="G$1" pin="2"/>
<wire x1="45.72" y1="10.16" x2="50.8" y2="10.16" width="0.1524" layer="91"/>
<label x="45.72" y="10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R2" gate="G$1" pin="1"/>
<wire x1="66.04" y1="10.16" x2="60.96" y2="10.16" width="0.1524" layer="91"/>
<label x="60.96" y="10.16" size="1.27" layer="95"/>
</segment>
</net>
<net name="MB" class="0">
<segment>
<pinref part="R3" gate="G$1" pin="2"/>
<wire x1="45.72" y1="-10.16" x2="50.8" y2="-10.16" width="0.1524" layer="91"/>
<label x="45.72" y="-10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R4" gate="G$1" pin="1"/>
<wire x1="66.04" y1="-10.16" x2="60.96" y2="-10.16" width="0.1524" layer="91"/>
<label x="60.96" y="-10.16" size="1.27" layer="95"/>
</segment>
</net>
<net name="Y" class="0">
<segment>
<pinref part="R4" gate="G$1" pin="2"/>
<wire x1="76.2" y1="-10.16" x2="81.28" y2="-10.16" width="0.1524" layer="91"/>
<label x="76.2" y="-10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="JP1" gate="G$1" pin="2"/>
<wire x1="5.08" y1="-27.94" x2="0" y2="-27.94" width="0.1524" layer="91"/>
<label x="0" y="-27.94" size="1.27" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
