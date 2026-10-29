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
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<description>Fuente ±16 V / 1,5 A y +5 V (v2) - Brahiam Alberto Campiño Romero</description>
<libraries>
<library name="fuente16">
<packages>
<package name="TERM3">
<description>Bornera de tornillo 3 vías, paso 5.08 mm</description>
<pad name="1" x="0" y="0" drill="1.3" diameter="2.6" shape="square"/>
<pad name="2" x="5.08" y="0" drill="1.3" diameter="2.6" shape="round"/>
<pad name="3" x="10.16" y="0" drill="1.3" diameter="2.6" shape="round"/>
<wire x1="-3.3" y1="-4.9" x2="13.46" y2="-4.9" width="0.2" layer="21"/>
<wire x1="13.46" y1="-4.9" x2="13.46" y2="5.3" width="0.2" layer="21"/>
<wire x1="13.46" y1="5.3" x2="-3.3" y2="5.3" width="0.2" layer="21"/>
<wire x1="-3.3" y1="5.3" x2="-3.3" y2="-4.9" width="0.2" layer="21"/>
<text x="5.08" y="6" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="5.08" y="-5.6" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="RES5W">
<description>Resistencia de potencia 5 W (cemento), 27.94 mm</description>
<pad name="1" x="0" y="0" drill="1.1" diameter="2.6" shape="square"/>
<pad name="2" x="27.94" y="0" drill="1.1" diameter="2.6" shape="round"/>
<wire x1="-1.2" y1="-4.9" x2="29.14" y2="-4.9" width="0.2" layer="21"/>
<wire x1="29.14" y1="-4.9" x2="29.14" y2="4.9" width="0.2" layer="21"/>
<wire x1="29.14" y1="4.9" x2="-1.2" y2="4.9" width="0.2" layer="21"/>
<wire x1="-1.2" y1="4.9" x2="-1.2" y2="-4.9" width="0.2" layer="21"/>
<text x="13.97" y="5.6" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="13.97" y="-5.6" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="CPOL35">
<description>Electrolítico radial D35 mm, paso 10 mm (15000 uF/50 V); pad 1 = +</description>
<pad name="1" x="0" y="0" drill="1.3" diameter="2.6" shape="square"/>
<pad name="2" x="10.16" y="0" drill="1.3" diameter="2.6" shape="round"/>
<circle x="5.08" y="0" radius="17.8" width="0.2" layer="21"/>
<text x="-1.6" y="1.4" size="1.2" layer="21" align="center">+</text>
<text x="5.08" y="18.4" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="5.08" y="-18.4" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="CPOL8">
<description>Electrolítico radial D8 mm, paso 3.5 mm (220 uF/25 V); pad 1 = +</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="3.81" y="0" drill="0.9" diameter="2" shape="round"/>
<circle x="1.905" y="0" radius="4.2" width="0.2" layer="21"/>
<text x="-1.6" y="1.4" size="1.2" layer="21" align="center">+</text>
<text x="1.905" y="4.8" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="1.905" y="-4.8" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="TO126">
<description>TO-126 vertical (BD139/BD140): 1 = E, 2 = C, 3 = B; cara metálica hacia la línea gruesa (disipador)</description>
<pad name="1" x="0" y="0" drill="1" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="1" diameter="2" shape="round"/>
<pad name="3" x="5.08" y="0" drill="1" diameter="2" shape="round"/>
<wire x1="-2.3" y1="-1.3" x2="7.38" y2="-1.3" width="0.2" layer="21"/>
<wire x1="7.38" y1="-1.3" x2="7.38" y2="3.1" width="0.2" layer="21"/>
<wire x1="7.38" y1="3.1" x2="-2.3" y2="3.1" width="0.2" layer="21"/>
<wire x1="-2.3" y1="3.1" x2="-2.3" y2="-1.3" width="0.2" layer="21"/>
<wire x1="-2.3" y1="2.5" x2="7.38" y2="2.5" width="0.6" layer="21"/>
<text x="2.54" y="3.8" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.54" y="-2" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="DIODE">
<description>Diodo DO-201 (1N5408), 15.24 mm; pad 2 = cátodo</description>
<pad name="1" x="0" y="0" drill="1.3" diameter="2.6" shape="square"/>
<pad name="2" x="15.24" y="0" drill="1.3" diameter="2.6" shape="round"/>
<wire x1="-2.24" y1="-2.24" x2="17.48" y2="-2.24" width="0.2" layer="21"/>
<wire x1="17.48" y1="-2.24" x2="17.48" y2="2.24" width="0.2" layer="21"/>
<wire x1="17.48" y1="2.24" x2="-2.24" y2="2.24" width="0.2" layer="21"/>
<wire x1="-2.24" y1="2.24" x2="-2.24" y2="-2.24" width="0.2" layer="21"/>
<wire x1="12.64" y1="-2.24" x2="12.64" y2="2.24" width="0.6" layer="21"/>
<text x="7.62" y="2.94" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="7.62" y="-2.94" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="TERM2">
<description>Bornera de tornillo 2 vías, paso 5.08 mm</description>
<pad name="1" x="0" y="0" drill="1.3" diameter="2.6" shape="square"/>
<pad name="2" x="5.08" y="0" drill="1.3" diameter="2.6" shape="round"/>
<wire x1="-3.3" y1="-4.9" x2="8.4" y2="-4.9" width="0.2" layer="21"/>
<wire x1="8.4" y1="-4.9" x2="8.4" y2="5.3" width="0.2" layer="21"/>
<wire x1="8.4" y1="5.3" x2="-3.3" y2="5.3" width="0.2" layer="21"/>
<wire x1="-3.3" y1="5.3" x2="-3.3" y2="-4.9" width="0.2" layer="21"/>
<text x="2.55" y="6" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.55" y="-5.6" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="TERM4">
<description>Bornera de tornillo 4 vías (2 x 2 vías), paso 5.08 mm</description>
<pad name="1" x="0" y="0" drill="1.3" diameter="2.6" shape="square"/>
<pad name="2" x="5.08" y="0" drill="1.3" diameter="2.6" shape="round"/>
<pad name="3" x="10.16" y="0" drill="1.3" diameter="2.6" shape="round"/>
<pad name="4" x="15.24" y="0" drill="1.3" diameter="2.6" shape="round"/>
<wire x1="-3.3" y1="-4.9" x2="18.54" y2="-4.9" width="0.2" layer="21"/>
<wire x1="18.54" y1="-4.9" x2="18.54" y2="5.3" width="0.2" layer="21"/>
<wire x1="18.54" y1="5.3" x2="-3.3" y2="5.3" width="0.2" layer="21"/>
<wire x1="-3.3" y1="5.3" x2="-3.3" y2="-4.9" width="0.2" layer="21"/>
<text x="7.62" y="6" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="7.62" y="-5.6" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="FUSE">
<description>Portafusible de PCB para fusible 5x20 mm, 22.86 mm entre clips</description>
<pad name="1" x="0" y="0" drill="1.3" diameter="2.6" shape="square"/>
<pad name="2" x="22.86" y="0" drill="1.3" diameter="2.6" shape="round"/>
<wire x1="-2.7" y1="-3.7" x2="25.56" y2="-3.7" width="0.2" layer="21"/>
<wire x1="25.56" y1="-3.7" x2="25.56" y2="3.7" width="0.2" layer="21"/>
<wire x1="25.56" y1="3.7" x2="-2.7" y2="3.7" width="0.2" layer="21"/>
<wire x1="-2.7" y1="3.7" x2="-2.7" y2="-3.7" width="0.2" layer="21"/>
<text x="11.43" y="4.4" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="11.43" y="-4.4" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="DO41">
<description>Diodo DO-41 (1N4007), 10.16 mm; pad 2 = cátodo</description>
<pad name="1" x="0" y="0" drill="1" diameter="2" shape="square"/>
<pad name="2" x="10.16" y="0" drill="1" diameter="2" shape="round"/>
<wire x1="-1.2" y1="-1.9" x2="11.4" y2="-1.9" width="0.2" layer="21"/>
<wire x1="11.4" y1="-1.9" x2="11.4" y2="1.9" width="0.2" layer="21"/>
<wire x1="11.4" y1="1.9" x2="-1.2" y2="1.9" width="0.2" layer="21"/>
<wire x1="-1.2" y1="1.9" x2="-1.2" y2="-1.9" width="0.2" layer="21"/>
<wire x1="7.56" y1="-1.9" x2="7.56" y2="1.9" width="0.6" layer="21"/>
<text x="5.1" y="2.6" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="5.1" y="-2.6" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="DO35">
<description>Diodo DO-35 (1N4148), 7.62 mm; pad 2 = cátodo</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="7.62" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-2.24" y1="-2.24" x2="9.86" y2="-2.24" width="0.2" layer="21"/>
<wire x1="9.86" y1="-2.24" x2="9.86" y2="2.24" width="0.2" layer="21"/>
<wire x1="9.86" y1="2.24" x2="-2.24" y2="2.24" width="0.2" layer="21"/>
<wire x1="-2.24" y1="2.24" x2="-2.24" y2="-2.24" width="0.2" layer="21"/>
<wire x1="5.02" y1="-2.24" x2="5.02" y2="2.24" width="0.6" layer="21"/>
<text x="3.81" y="2.94" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="3.81" y="-2.94" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="CPOL25">
<description>Electrolítico radial D28 mm, paso 10 mm (6800 uF/50 V); pad 1 = +</description>
<pad name="1" x="0" y="0" drill="1.3" diameter="2.6" shape="square"/>
<pad name="2" x="10.16" y="0" drill="1.3" diameter="2.6" shape="round"/>
<circle x="5.08" y="0" radius="13.8" width="0.2" layer="21"/>
<text x="-1.6" y="1.4" size="1.2" layer="21" align="center">+</text>
<text x="5.08" y="14.4" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="5.08" y="-14.4" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="CPOL6">
<description>Electrolítico radial D6.3 mm, paso 2.54 mm; pad 1 = +</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<circle x="1.27" y="0" radius="3.3" width="0.2" layer="21"/>
<text x="-1.6" y="1.4" size="1.2" layer="21" align="center">+</text>
<text x="1.27" y="3.9" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="1.27" y="-3.9" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="CPOL5">
<description>Electrolítico radial D5 mm, paso 2.54 mm; pad 1 = +</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<circle x="1.27" y="0" radius="2.8" width="0.2" layer="21"/>
<text x="-1.6" y="1.4" size="1.2" layer="21" align="center">+</text>
<text x="1.27" y="3.4" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="1.27" y="-3.4" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="CTANT">
<description>Tántalo de gota, paso 2.54 mm; pad 1 = +</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-1.3" y1="-2.1" x2="3.84" y2="-2.1" width="0.2" layer="21"/>
<wire x1="3.84" y1="-2.1" x2="3.84" y2="2.1" width="0.2" layer="21"/>
<wire x1="3.84" y1="2.1" x2="-1.3" y2="2.1" width="0.2" layer="21"/>
<wire x1="-1.3" y1="2.1" x2="-1.3" y2="-2.1" width="0.2" layer="21"/>
<text x="1.27" y="2.8" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="1.27" y="-2.8" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="CAP">
<description>Cerámico/poliéster, paso 5.08 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="5.08" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-2.24" y1="-2.24" x2="7.32" y2="-2.24" width="0.2" layer="21"/>
<wire x1="7.32" y1="-2.24" x2="7.32" y2="2.24" width="0.2" layer="21"/>
<wire x1="7.32" y1="2.24" x2="-2.24" y2="2.24" width="0.2" layer="21"/>
<wire x1="-2.24" y1="2.24" x2="-2.24" y2="-2.24" width="0.2" layer="21"/>
<text x="2.54" y="2.94" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.54" y="-2.94" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="RES10">
<description>Resistencia 1/4 W, 10.16 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="10.16" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-2.24" y1="-2.24" x2="12.4" y2="-2.24" width="0.2" layer="21"/>
<wire x1="12.4" y1="-2.24" x2="12.4" y2="2.24" width="0.2" layer="21"/>
<wire x1="12.4" y1="2.24" x2="-2.24" y2="2.24" width="0.2" layer="21"/>
<wire x1="-2.24" y1="2.24" x2="-2.24" y2="-2.24" width="0.2" layer="21"/>
<text x="5.08" y="2.94" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="5.08" y="-2.94" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="RES1W">
<description>Resistencia 1 W, 15.24 mm</description>
<pad name="1" x="0" y="0" drill="1" diameter="2" shape="square"/>
<pad name="2" x="15.24" y="0" drill="1" diameter="2" shape="round"/>
<wire x1="-1.2" y1="-2.3" x2="16.4" y2="-2.3" width="0.2" layer="21"/>
<wire x1="16.4" y1="-2.3" x2="16.4" y2="2.3" width="0.2" layer="21"/>
<wire x1="16.4" y1="2.3" x2="-1.2" y2="2.3" width="0.2" layer="21"/>
<wire x1="-1.2" y1="2.3" x2="-1.2" y2="-2.3" width="0.2" layer="21"/>
<text x="7.6" y="3" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="7.6" y="-3" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="RES2W">
<description>Resistencia 2 W, 20.32 mm</description>
<pad name="1" x="0" y="0" drill="1" diameter="2" shape="square"/>
<pad name="2" x="20.32" y="0" drill="1" diameter="2" shape="round"/>
<wire x1="-1.2" y1="-2.7" x2="21.5" y2="-2.7" width="0.2" layer="21"/>
<wire x1="21.5" y1="-2.7" x2="21.5" y2="2.7" width="0.2" layer="21"/>
<wire x1="21.5" y1="2.7" x2="-1.2" y2="2.7" width="0.2" layer="21"/>
<wire x1="-1.2" y1="2.7" x2="-1.2" y2="-2.7" width="0.2" layer="21"/>
<text x="10.15" y="3.4" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="10.15" y="-3.4" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="RES3W">
<description>Resistencia 3 W, 25.4 mm</description>
<pad name="1" x="0" y="0" drill="1.1" diameter="2" shape="square"/>
<pad name="2" x="25.4" y="0" drill="1.1" diameter="2" shape="round"/>
<wire x1="-1.2" y1="-3.3" x2="26.6" y2="-3.3" width="0.2" layer="21"/>
<wire x1="26.6" y1="-3.3" x2="26.6" y2="3.3" width="0.2" layer="21"/>
<wire x1="26.6" y1="3.3" x2="-1.2" y2="3.3" width="0.2" layer="21"/>
<wire x1="-1.2" y1="3.3" x2="-1.2" y2="-3.3" width="0.2" layer="21"/>
<text x="12.7" y="4" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="12.7" y="-4" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="TO220">
<description>TO-220 vertical; aleta hacia la línea gruesa (borde de la placa, disipador)</description>
<pad name="1" x="0" y="0" drill="1" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="1" diameter="2" shape="round"/>
<pad name="3" x="5.08" y="0" drill="1" diameter="2" shape="round"/>
<wire x1="-2.7" y1="-3.7" x2="7.8" y2="-3.7" width="0.2" layer="21"/>
<wire x1="7.8" y1="-3.7" x2="7.8" y2="5.7" width="0.2" layer="21"/>
<wire x1="7.8" y1="5.7" x2="-2.7" y2="5.7" width="0.2" layer="21"/>
<wire x1="-2.7" y1="5.7" x2="-2.7" y2="-3.7" width="0.2" layer="21"/>
<wire x1="-2.7" y1="5.1" x2="7.8" y2="5.1" width="0.6" layer="21"/>
<text x="2.55" y="6.4" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.55" y="-4.4" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="TO92">
<description>TO-92 en línea, paso 2.54 mm (BC547/BC557: 1 C, 2 B, 3 E)</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<pad name="3" x="5.08" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-1.3" y1="-2.3" x2="6.4" y2="-2.3" width="0.2" layer="21"/>
<wire x1="6.4" y1="-2.3" x2="6.4" y2="1.7" width="0.2" layer="21"/>
<wire x1="6.4" y1="1.7" x2="-1.3" y2="1.7" width="0.2" layer="21"/>
<wire x1="-1.3" y1="1.7" x2="-1.3" y2="-2.3" width="0.2" layer="21"/>
<text x="2.55" y="2.4" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.55" y="-3" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="TRIM">
<description>Trimmer multivuelta 3296W, pines en línea 2.54 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<pad name="3" x="5.08" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-2" y1="-2.9" x2="7.1" y2="-2.9" width="0.2" layer="21"/>
<wire x1="7.1" y1="-2.9" x2="7.1" y2="1.9" width="0.2" layer="21"/>
<wire x1="7.1" y1="1.9" x2="-2" y2="1.9" width="0.2" layer="21"/>
<wire x1="-2" y1="1.9" x2="-2" y2="-2.9" width="0.2" layer="21"/>
<text x="2.55" y="2.6" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.55" y="-3.6" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="LED5">
<description>LED 5 mm; pad 1 = ánodo (pata larga)</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<circle x="1.27" y="0" radius="2.9" width="0.2" layer="21"/>
<text x="-1.6" y="1.4" size="1.2" layer="21" align="center">+</text>
<text x="1.27" y="3.5" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="1.27" y="-3.5" size="1" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="HDR3">
<description>Regleta 1x3, 2.54 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<pad name="3" x="5.08" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-2.24" y1="-2.24" x2="7.32" y2="-2.24" width="0.2" layer="21"/>
<wire x1="7.32" y1="-2.24" x2="7.32" y2="2.24" width="0.2" layer="21"/>
<wire x1="7.32" y1="2.24" x2="-2.24" y2="2.24" width="0.2" layer="21"/>
<wire x1="-2.24" y1="2.24" x2="-2.24" y2="-2.24" width="0.2" layer="21"/>
<text x="2.54" y="2.94" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.54" y="-2.94" size="1" layer="27" align="top-center">&gt;VALUE</text>
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
<symbol name="FUSE">
<wire x1="-2.54" y1="-0.8" x2="2.54" y2="-0.8" width="0.254" layer="94"/>
<wire x1="2.54" y1="-0.8" x2="2.54" y2="0.8" width="0.254" layer="94"/>
<wire x1="2.54" y1="0.8" x2="-2.54" y2="0.8" width="0.254" layer="94"/>
<wire x1="-2.54" y1="0.8" x2="-2.54" y2="-0.8" width="0.254" layer="94"/>
<wire x1="-2.54" y1="0" x2="2.54" y2="0" width="0.15" layer="94"/>
<text x="-3.81" y="2.4" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-4.2" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="5.08" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="C">
<wire x1="-0.6" y1="-2.54" x2="-0.6" y2="2.54" width="0.4" layer="94"/>
<wire x1="0.6" y1="-2.54" x2="0.6" y2="2.54" width="0.4" layer="94"/>
<text x="-3.81" y="2.4" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-4.2" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="5.08" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="CPOL">
<wire x1="-0.6" y1="-2.54" x2="-0.6" y2="2.54" width="0.4" layer="94"/>
<wire x1="0.6" y1="-2.54" x2="0.6" y2="2.54" width="0.9" layer="94"/>
<text x="-2.6" y="0.6" size="1.27" layer="94">+</text>
<text x="-3.81" y="2.4" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-4.2" size="1.778" layer="96">&gt;VALUE</text>
<pin name="+" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="-" x="5.08" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="D">
<wire x1="-1.27" y1="1.27" x2="-1.27" y2="-1.27" width="0.254" layer="94"/>
<wire x1="-1.27" y1="-1.27" x2="1.27" y2="0" width="0.254" layer="94"/>
<wire x1="1.27" y1="0" x2="-1.27" y2="1.27" width="0.254" layer="94"/>
<wire x1="1.27" y1="1.27" x2="1.27" y2="-1.27" width="0.254" layer="94"/>
<text x="-3.81" y="2.4" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-4.2" size="1.778" layer="96">&gt;VALUE</text>
<pin name="A" x="-3.81" y="0" length="short" direction="pas"/>
<pin name="K" x="3.81" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="LED">
<wire x1="-1.27" y1="1.27" x2="-1.27" y2="-1.27" width="0.254" layer="94"/>
<wire x1="-1.27" y1="-1.27" x2="1.27" y2="0" width="0.254" layer="94"/>
<wire x1="1.27" y1="0" x2="-1.27" y2="1.27" width="0.254" layer="94"/>
<wire x1="1.27" y1="1.27" x2="1.27" y2="-1.27" width="0.254" layer="94"/>
<wire x1="0" y1="1.6" x2="1.2" y2="2.8" width="0.15" layer="94"/>
<wire x1="0.8" y1="1.6" x2="2" y2="2.8" width="0.15" layer="94"/>
<text x="-3.81" y="2.4" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-4.2" size="1.778" layer="96">&gt;VALUE</text>
<pin name="A" x="-3.81" y="0" length="short" direction="pas"/>
<pin name="K" x="3.81" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="NPN">
<wire x1="0" y1="-2.54" x2="0" y2="2.54" width="0.4" layer="94"/>
<wire x1="0" y1="1.27" x2="2.54" y2="2.54" width="0.254" layer="94"/>
<wire x1="0" y1="-1.27" x2="2.54" y2="-2.54" width="0.254" layer="94"/>
<wire x1="-2.54" y1="0" x2="0" y2="0" width="0.254" layer="94"/>
<text x="3.8" y="1.0" size="1.778" layer="95">&gt;NAME</text>
<text x="3.8" y="-1.8" size="1.778" layer="96">&gt;VALUE</text>
<text x="1.2" y="-2.4" size="1.0" layer="94">E</text>
<pin name="B" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="C" x="2.54" y="5.08" length="short" direction="pas" rot="R270"/>
<pin name="E" x="2.54" y="-5.08" length="short" direction="pas" rot="R90"/>
</symbol>
<symbol name="PNP">
<wire x1="0" y1="-2.54" x2="0" y2="2.54" width="0.4" layer="94"/>
<wire x1="0" y1="1.27" x2="2.54" y2="2.54" width="0.254" layer="94"/>
<wire x1="0" y1="-1.27" x2="2.54" y2="-2.54" width="0.254" layer="94"/>
<wire x1="-2.54" y1="0" x2="0" y2="0" width="0.254" layer="94"/>
<text x="3.8" y="1.0" size="1.778" layer="95">&gt;NAME</text>
<text x="3.8" y="-1.8" size="1.778" layer="96">&gt;VALUE</text>
<text x="1.2" y="1.6" size="1.0" layer="94">E</text>
<pin name="B" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="E" x="2.54" y="5.08" length="short" direction="pas" rot="R270"/>
<pin name="C" x="2.54" y="-5.08" length="short" direction="pas" rot="R90"/>
</symbol>
<symbol name="REG">
<wire x1="-5.08" y1="-2.54" x2="5.08" y2="-2.54" width="0.254" layer="94"/>
<wire x1="5.08" y1="-2.54" x2="5.08" y2="2.54" width="0.254" layer="94"/>
<wire x1="5.08" y1="2.54" x2="-5.08" y2="2.54" width="0.254" layer="94"/>
<wire x1="-5.08" y1="2.54" x2="-5.08" y2="-2.54" width="0.254" layer="94"/>
<text x="-5.08" y="3.2" size="1.778" layer="95">&gt;NAME</text>
<text x="-5.08" y="-5.0" size="1.778" layer="96">&gt;VALUE</text>
<pin name="IN" x="-7.62" y="0" length="short" direction="pas"/>
<pin name="OUT" x="7.62" y="0" length="short" direction="pas" rot="R180"/>
<pin name="ADJ" x="0" y="-5.08" length="short" direction="pas" rot="R90"/>
</symbol>
<symbol name="POT">
<wire x1="-3.81" y1="-1.016" x2="3.81" y2="-1.016" width="0.254" layer="94"/>
<wire x1="3.81" y1="-1.016" x2="3.81" y2="1.016" width="0.254" layer="94"/>
<wire x1="3.81" y1="1.016" x2="-3.81" y2="1.016" width="0.254" layer="94"/>
<wire x1="-3.81" y1="1.016" x2="-3.81" y2="-1.016" width="0.254" layer="94"/>
<wire x1="0" y1="-2.54" x2="0" y2="-1.016" width="0.254" layer="94"/>
<text x="-3.81" y="2.4" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-4.2" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-7.62" y="0" length="short" direction="pas"/>
<pin name="3" x="7.62" y="0" length="short" direction="pas" rot="R180"/>
<pin name="2" x="0" y="-5.08" length="short" direction="pas" rot="R90"/>
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
<symbol name="HDR3">
<wire x1="-2.54" y1="-6.35" x2="2.54" y2="-6.35" width="0.254" layer="94"/>
<wire x1="2.54" y1="-6.35" x2="2.54" y2="1.27" width="0.254" layer="94"/>
<wire x1="2.54" y1="1.27" x2="-2.54" y2="1.27" width="0.254" layer="94"/>
<wire x1="-2.54" y1="1.27" x2="-2.54" y2="-6.35" width="0.254" layer="94"/>
<text x="-2.54" y="2.27" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="-5.08" y="-2.54" length="short" direction="pas"/>
<pin name="3" x="-5.08" y="-5.08" length="short" direction="pas"/>
</symbol>
<symbol name="HDR4">
<wire x1="-2.54" y1="-8.89" x2="2.54" y2="-8.89" width="0.254" layer="94"/>
<wire x1="2.54" y1="-8.89" x2="2.54" y2="1.27" width="0.254" layer="94"/>
<wire x1="2.54" y1="1.27" x2="-2.54" y2="1.27" width="0.254" layer="94"/>
<wire x1="-2.54" y1="1.27" x2="-2.54" y2="-8.89" width="0.254" layer="94"/>
<text x="-2.54" y="2.27" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="-5.08" y="-2.54" length="short" direction="pas"/>
<pin name="3" x="-5.08" y="-5.08" length="short" direction="pas"/>
<pin name="4" x="-5.08" y="-7.62" length="short" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="R10" prefix="R">
<gates>
<gate name="G$1" symbol="R" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="RES10">
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
<deviceset name="R5W" prefix="R">
<gates>
<gate name="G$1" symbol="R" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="RES5W">
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
<deviceset name="CPOL35" prefix="C">
<gates>
<gate name="G$1" symbol="CPOL" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="CPOL35">
<connects>
<connect gate="G$1" pin="+" pad="1"/>
<connect gate="G$1" pin="-" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="CPOL8" prefix="C">
<gates>
<gate name="G$1" symbol="CPOL" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="CPOL8">
<connects>
<connect gate="G$1" pin="+" pad="1"/>
<connect gate="G$1" pin="-" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="D201" prefix="D">
<gates>
<gate name="G$1" symbol="D" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="DIODE">
<connects>
<connect gate="G$1" pin="A" pad="1"/>
<connect gate="G$1" pin="K" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TERM3" prefix="J">
<gates>
<gate name="G$1" symbol="HDR3" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TERM3">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TIP41C" prefix="Q">
<gates>
<gate name="G$1" symbol="NPN" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO220">
<connects>
<connect gate="G$1" pin="B" pad="1"/>
<connect gate="G$1" pin="C" pad="2"/>
<connect gate="G$1" pin="E" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TIP42C" prefix="Q">
<gates>
<gate name="G$1" symbol="PNP" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO220">
<connects>
<connect gate="G$1" pin="B" pad="1"/>
<connect gate="G$1" pin="C" pad="2"/>
<connect gate="G$1" pin="E" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="BD139" prefix="Q">
<gates>
<gate name="G$1" symbol="NPN" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO126">
<connects>
<connect gate="G$1" pin="E" pad="1"/>
<connect gate="G$1" pin="C" pad="2"/>
<connect gate="G$1" pin="B" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="BD140" prefix="Q">
<gates>
<gate name="G$1" symbol="PNP" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO126">
<connects>
<connect gate="G$1" pin="E" pad="1"/>
<connect gate="G$1" pin="C" pad="2"/>
<connect gate="G$1" pin="B" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="R1W" prefix="R">
<gates>
<gate name="G$1" symbol="R" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="RES1W">
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
<deviceset name="R2W" prefix="R">
<gates>
<gate name="G$1" symbol="R" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="RES2W">
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
<deviceset name="R3W" prefix="R">
<gates>
<gate name="G$1" symbol="R" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="RES3W">
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
<deviceset name="C" prefix="C">
<gates>
<gate name="G$1" symbol="C" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="CAP">
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
<deviceset name="CPOL25" prefix="C">
<gates>
<gate name="G$1" symbol="CPOL" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="CPOL25">
<connects>
<connect gate="G$1" pin="+" pad="1"/>
<connect gate="G$1" pin="-" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="CPOL6" prefix="C">
<gates>
<gate name="G$1" symbol="CPOL" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="CPOL6">
<connects>
<connect gate="G$1" pin="+" pad="1"/>
<connect gate="G$1" pin="-" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="CPOL5" prefix="C">
<gates>
<gate name="G$1" symbol="CPOL" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="CPOL5">
<connects>
<connect gate="G$1" pin="+" pad="1"/>
<connect gate="G$1" pin="-" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="CTANT" prefix="C">
<gates>
<gate name="G$1" symbol="CPOL" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="CTANT">
<connects>
<connect gate="G$1" pin="+" pad="1"/>
<connect gate="G$1" pin="-" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="D41" prefix="D">
<gates>
<gate name="G$1" symbol="D" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="DO41">
<connects>
<connect gate="G$1" pin="A" pad="1"/>
<connect gate="G$1" pin="K" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="D35" prefix="D">
<gates>
<gate name="G$1" symbol="D" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="DO35">
<connects>
<connect gate="G$1" pin="A" pad="1"/>
<connect gate="G$1" pin="K" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="LED" prefix="LED">
<gates>
<gate name="G$1" symbol="LED" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="LED5">
<connects>
<connect gate="G$1" pin="A" pad="1"/>
<connect gate="G$1" pin="K" pad="2"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TIP31C" prefix="Q">
<gates>
<gate name="G$1" symbol="NPN" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO220">
<connects>
<connect gate="G$1" pin="B" pad="1"/>
<connect gate="G$1" pin="C" pad="2"/>
<connect gate="G$1" pin="E" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TIP32C" prefix="Q">
<gates>
<gate name="G$1" symbol="PNP" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO220">
<connects>
<connect gate="G$1" pin="B" pad="1"/>
<connect gate="G$1" pin="C" pad="2"/>
<connect gate="G$1" pin="E" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="BC547" prefix="Q">
<gates>
<gate name="G$1" symbol="NPN" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO92">
<connects>
<connect gate="G$1" pin="C" pad="1"/>
<connect gate="G$1" pin="B" pad="2"/>
<connect gate="G$1" pin="E" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="BC557" prefix="Q">
<gates>
<gate name="G$1" symbol="PNP" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO92">
<connects>
<connect gate="G$1" pin="C" pad="1"/>
<connect gate="G$1" pin="B" pad="2"/>
<connect gate="G$1" pin="E" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="LM317T" prefix="U">
<gates>
<gate name="G$1" symbol="REG" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO220">
<connects>
<connect gate="G$1" pin="ADJ" pad="1"/>
<connect gate="G$1" pin="OUT" pad="2"/>
<connect gate="G$1" pin="IN" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="LM337T" prefix="U">
<gates>
<gate name="G$1" symbol="REG" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TO220">
<connects>
<connect gate="G$1" pin="ADJ" pad="1"/>
<connect gate="G$1" pin="IN" pad="2"/>
<connect gate="G$1" pin="OUT" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="TRIM" prefix="RV">
<gates>
<gate name="G$1" symbol="POT" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TRIM">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="FUSE" prefix="F">
<gates>
<gate name="G$1" symbol="FUSE" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="FUSE">
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
<gate name="G$1" symbol="HDR2" x="0" y="0" addlevel="next"/>
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
<deviceset name="TERM4" prefix="J">
<gates>
<gate name="G$1" symbol="HDR4" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="TERM4">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="4" pad="4"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HDR3" prefix="J">
<gates>
<gate name="G$1" symbol="HDR3" x="0" y="0" addlevel="next"/>
</gates>
<devices>
<device name="" package="HDR3">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="3" pad="3"/>
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
<part name="J1" library="fuente16" deviceset="TERM3" device="" value="SEC 18-0-18"/>
<part name="F2" library="fuente16" deviceset="FUSE" device="" value="T3.15A"/>
<part name="F3" library="fuente16" deviceset="FUSE" device="" value="T3.15A"/>
<part name="D1" library="fuente16" deviceset="D201" device="" value="1N5408"/>
<part name="D2" library="fuente16" deviceset="D201" device="" value="1N5408"/>
<part name="D3" library="fuente16" deviceset="D201" device="" value="1N5408"/>
<part name="D4" library="fuente16" deviceset="D201" device="" value="1N5408"/>
<part name="C1" library="fuente16" deviceset="CPOL35" device="" value="15000u/50V"/>
<part name="C3" library="fuente16" deviceset="C" device="" value="100n"/>
<part name="C2A" library="fuente16" deviceset="CPOL25" device="" value="6800u/50V"/>
<part name="C2B" library="fuente16" deviceset="CPOL25" device="" value="6800u/50V"/>
<part name="C4" library="fuente16" deviceset="C" device="" value="100n"/>
<part name="J3" library="fuente16" deviceset="HDR3" device="" value="TP"/>
<part name="RSC1" library="fuente16" deviceset="R5W" device="" value="0R27 5W"/>
<part name="Q1" library="fuente16" deviceset="TIP42C" device="" value="TIP42C"/>
<part name="Q2" library="fuente16" deviceset="BD140" device="" value="BD140"/>
<part name="Q3" library="fuente16" deviceset="BC557" device="" value="BC557"/>
<part name="R3" library="fuente16" deviceset="R1W" device="" value="2k7 1W"/>
<part name="R4" library="fuente16" deviceset="R10" device="" value="1k"/>
<part name="R5" library="fuente16" deviceset="R10" device="" value="270"/>
<part name="R6" library="fuente16" deviceset="R10" device="" value="12k"/>
<part name="R7" library="fuente16" deviceset="R1W" device="" value="2R7 1W"/>
<part name="Q4" library="fuente16" deviceset="TIP42C" device="" value="TIP42C"/>
<part name="C5" library="fuente16" deviceset="C" device="" value="100n"/>
<part name="U1" library="fuente16" deviceset="LM317T" device="" value="LM317T"/>
<part name="R8" library="fuente16" deviceset="R10" device="" value="120 1%"/>
<part name="R9" library="fuente16" deviceset="R10" device="" value="1k3 1%"/>
<part name="RV1" library="fuente16" deviceset="TRIM" device="" value="200 3296W"/>
<part name="C6" library="fuente16" deviceset="CPOL5" device="" value="10u/25V"/>
<part name="D5" library="fuente16" deviceset="D41" device="" value="1N4007"/>
<part name="D6" library="fuente16" deviceset="D35" device="" value="1N4148"/>
<part name="C7" library="fuente16" deviceset="CTANT" device="" value="10u tant"/>
<part name="C8" library="fuente16" deviceset="C" device="" value="100n"/>
<part name="C9" library="fuente16" deviceset="CPOL8" device="" value="220u/25V"/>
<part name="D7" library="fuente16" deviceset="D201" device="" value="1N5408"/>
<part name="R10" library="fuente16" deviceset="R10" device="" value="2k2"/>
<part name="LED1" library="fuente16" deviceset="LED" device="" value="verde"/>
<part name="J4" library="fuente16" deviceset="TERM2" device="" value="RL +16"/>
<part name="RSC2" library="fuente16" deviceset="R5W" device="" value="0R27 5W"/>
<part name="Q5" library="fuente16" deviceset="TIP41C" device="" value="TIP41C"/>
<part name="Q6" library="fuente16" deviceset="BD139" device="" value="BD139"/>
<part name="Q7" library="fuente16" deviceset="BC547" device="" value="BC547"/>
<part name="R11" library="fuente16" deviceset="R1W" device="" value="2k7 1W"/>
<part name="R12" library="fuente16" deviceset="R10" device="" value="1k"/>
<part name="R13" library="fuente16" deviceset="R10" device="" value="270"/>
<part name="R14" library="fuente16" deviceset="R10" device="" value="12k"/>
<part name="R15" library="fuente16" deviceset="R1W" device="" value="2R7 1W"/>
<part name="Q8" library="fuente16" deviceset="TIP41C" device="" value="TIP41C"/>
<part name="C10" library="fuente16" deviceset="C" device="" value="100n"/>
<part name="U2" library="fuente16" deviceset="LM337T" device="" value="LM337T"/>
<part name="R16" library="fuente16" deviceset="R10" device="" value="120 1%"/>
<part name="R17" library="fuente16" deviceset="R10" device="" value="1k3 1%"/>
<part name="RV2" library="fuente16" deviceset="TRIM" device="" value="200 3296W"/>
<part name="C11" library="fuente16" deviceset="CPOL5" device="" value="10u/25V"/>
<part name="D8" library="fuente16" deviceset="D41" device="" value="1N4007"/>
<part name="D9" library="fuente16" deviceset="D35" device="" value="1N4148"/>
<part name="C12" library="fuente16" deviceset="CTANT" device="" value="10u tant"/>
<part name="C13" library="fuente16" deviceset="C" device="" value="100n"/>
<part name="C14" library="fuente16" deviceset="CPOL8" device="" value="220u/25V"/>
<part name="D10" library="fuente16" deviceset="D201" device="" value="1N5408"/>
<part name="R18" library="fuente16" deviceset="R10" device="" value="2k2"/>
<part name="LED2" library="fuente16" deviceset="LED" device="" value="verde"/>
<part name="J5" library="fuente16" deviceset="TERM2" device="" value="RL -16"/>
<part name="R19" library="fuente16" deviceset="R3W" device="" value="100 3W"/>
<part name="C15" library="fuente16" deviceset="CPOL6" device="" value="100u/25V"/>
<part name="C16" library="fuente16" deviceset="C" device="" value="100n"/>
<part name="U3" library="fuente16" deviceset="LM317T" device="" value="LM317T"/>
<part name="R20" library="fuente16" deviceset="R10" device="" value="120 1%"/>
<part name="R21" library="fuente16" deviceset="R10" device="" value="330 1%"/>
<part name="RV3" library="fuente16" deviceset="TRIM" device="" value="50 3296W"/>
<part name="C17" library="fuente16" deviceset="CPOL5" device="" value="10u/25V"/>
<part name="D11" library="fuente16" deviceset="D41" device="" value="1N4007"/>
<part name="D12" library="fuente16" deviceset="D35" device="" value="1N4148"/>
<part name="C18" library="fuente16" deviceset="CTANT" device="" value="10u tant"/>
<part name="C19" library="fuente16" deviceset="C" device="" value="100n"/>
<part name="D13" library="fuente16" deviceset="D41" device="" value="1N4007"/>
<part name="R22" library="fuente16" deviceset="R10" device="" value="470"/>
<part name="LED3" library="fuente16" deviceset="LED" device="" value="verde"/>
<part name="J2" library="fuente16" deviceset="TERM4" device="" value="SALIDA"/>
</parts>
<sheets>
<sheet>
<plain>
<text x="5.08" y="-3.81" size="2.54" layer="97">Entrada, puente y filtros</text>
<text x="5.08" y="-34.29" size="2.54" layer="97">Filtro -  y puntos de prueba</text>
<text x="5.08" y="-64.77" size="2.54" layer="97">Limitador +16 V (foldback)</text>
<text x="5.08" y="-95.25" size="2.54" layer="97">Ampliación y regulador +16 V</text>
<text x="5.08" y="-125.73" size="2.54" layer="97">Salida +16 V</text>
<text x="5.08" y="-156.21" size="2.54" layer="97">Limitador -16 V (foldback)</text>
<text x="5.08" y="-186.69" size="2.54" layer="97">Ampliación y regulador -16 V</text>
<text x="5.08" y="-217.17" size="2.54" layer="97">Salida -16 V</text>
<text x="5.08" y="-247.65" size="2.54" layer="97">Rama +5 V</text>
<text x="5.08" y="-278.13" size="2.54" layer="97">Salida +5 V</text>
<text x="5.08" y="12.7" size="3.81" layer="97">Fuente ±16 V / 1,5 A y +5 V, versión 2 (conexiones por etiquetas de red; ver esquematicos/ para el dibujo)</text>
</plain>
<instances>
<instance part="J1" gate="G$1" x="20.32" y="-15.24"/>
<instance part="F2" gate="G$1" x="60.96" y="-15.24"/>
<instance part="F3" gate="G$1" x="101.6" y="-15.24"/>
<instance part="D1" gate="G$1" x="142.24" y="-15.24"/>
<instance part="D2" gate="G$1" x="182.88" y="-15.24"/>
<instance part="D3" gate="G$1" x="223.52" y="-15.24"/>
<instance part="D4" gate="G$1" x="264.16" y="-15.24"/>
<instance part="C1" gate="G$1" x="304.8" y="-15.24"/>
<instance part="C3" gate="G$1" x="345.44" y="-15.24"/>
<instance part="C2A" gate="G$1" x="20.32" y="-45.72"/>
<instance part="C2B" gate="G$1" x="60.96" y="-45.72"/>
<instance part="C4" gate="G$1" x="101.6" y="-45.72"/>
<instance part="J3" gate="G$1" x="142.24" y="-45.72"/>
<instance part="J2" gate="G$1" x="182.88" y="-45.72"/>
<instance part="RSC1" gate="G$1" x="20.32" y="-76.2"/>
<instance part="Q1" gate="G$1" x="60.96" y="-76.2"/>
<instance part="Q2" gate="G$1" x="101.6" y="-76.2"/>
<instance part="Q3" gate="G$1" x="142.24" y="-76.2"/>
<instance part="R3" gate="G$1" x="182.88" y="-76.2"/>
<instance part="R4" gate="G$1" x="223.52" y="-76.2"/>
<instance part="R5" gate="G$1" x="264.16" y="-76.2"/>
<instance part="R6" gate="G$1" x="304.8" y="-76.2"/>
<instance part="R7" gate="G$1" x="20.32" y="-106.68"/>
<instance part="Q4" gate="G$1" x="60.96" y="-106.68"/>
<instance part="C5" gate="G$1" x="101.6" y="-106.68"/>
<instance part="U1" gate="G$1" x="142.24" y="-106.68"/>
<instance part="R8" gate="G$1" x="182.88" y="-106.68"/>
<instance part="R9" gate="G$1" x="223.52" y="-106.68"/>
<instance part="RV1" gate="G$1" x="264.16" y="-106.68"/>
<instance part="C6" gate="G$1" x="304.8" y="-106.68"/>
<instance part="D5" gate="G$1" x="345.44" y="-106.68"/>
<instance part="D6" gate="G$1" x="386.08" y="-106.68"/>
<instance part="C7" gate="G$1" x="20.32" y="-137.16"/>
<instance part="C8" gate="G$1" x="60.96" y="-137.16"/>
<instance part="C9" gate="G$1" x="101.6" y="-137.16"/>
<instance part="D7" gate="G$1" x="142.24" y="-137.16"/>
<instance part="R10" gate="G$1" x="182.88" y="-137.16"/>
<instance part="LED1" gate="G$1" x="223.52" y="-137.16"/>
<instance part="J4" gate="G$1" x="264.16" y="-137.16"/>
<instance part="RSC2" gate="G$1" x="20.32" y="-167.64"/>
<instance part="Q5" gate="G$1" x="60.96" y="-167.64"/>
<instance part="Q6" gate="G$1" x="101.6" y="-167.64"/>
<instance part="Q7" gate="G$1" x="142.24" y="-167.64"/>
<instance part="R11" gate="G$1" x="182.88" y="-167.64"/>
<instance part="R12" gate="G$1" x="223.52" y="-167.64"/>
<instance part="R13" gate="G$1" x="264.16" y="-167.64"/>
<instance part="R14" gate="G$1" x="304.8" y="-167.64"/>
<instance part="R15" gate="G$1" x="20.32" y="-198.12"/>
<instance part="Q8" gate="G$1" x="60.96" y="-198.12"/>
<instance part="C10" gate="G$1" x="101.6" y="-198.12"/>
<instance part="U2" gate="G$1" x="142.24" y="-198.12"/>
<instance part="R16" gate="G$1" x="182.88" y="-198.12"/>
<instance part="R17" gate="G$1" x="223.52" y="-198.12"/>
<instance part="RV2" gate="G$1" x="264.16" y="-198.12"/>
<instance part="C11" gate="G$1" x="304.8" y="-198.12"/>
<instance part="D8" gate="G$1" x="345.44" y="-198.12"/>
<instance part="D9" gate="G$1" x="386.08" y="-198.12"/>
<instance part="C12" gate="G$1" x="20.32" y="-228.6"/>
<instance part="C13" gate="G$1" x="60.96" y="-228.6"/>
<instance part="C14" gate="G$1" x="101.6" y="-228.6"/>
<instance part="D10" gate="G$1" x="142.24" y="-228.6"/>
<instance part="R18" gate="G$1" x="182.88" y="-228.6"/>
<instance part="LED2" gate="G$1" x="223.52" y="-228.6"/>
<instance part="J5" gate="G$1" x="264.16" y="-228.6"/>
<instance part="R19" gate="G$1" x="20.32" y="-259.08"/>
<instance part="C15" gate="G$1" x="60.96" y="-259.08"/>
<instance part="C16" gate="G$1" x="101.6" y="-259.08"/>
<instance part="U3" gate="G$1" x="142.24" y="-259.08"/>
<instance part="R20" gate="G$1" x="182.88" y="-259.08"/>
<instance part="R21" gate="G$1" x="223.52" y="-259.08"/>
<instance part="RV3" gate="G$1" x="264.16" y="-259.08"/>
<instance part="C17" gate="G$1" x="304.8" y="-259.08"/>
<instance part="D11" gate="G$1" x="20.32" y="-289.56"/>
<instance part="D12" gate="G$1" x="60.96" y="-289.56"/>
<instance part="C18" gate="G$1" x="101.6" y="-289.56"/>
<instance part="C19" gate="G$1" x="142.24" y="-289.56"/>
<instance part="D13" gate="G$1" x="182.88" y="-289.56"/>
<instance part="R22" gate="G$1" x="223.52" y="-289.56"/>
<instance part="LED3" gate="G$1" x="264.16" y="-289.56"/>
</instances>
<busses>
</busses>
<nets>
<net name="ACA" class="0">
<segment>
<pinref part="J1" gate="G$1" pin="1"/>
<wire x1="15.24" y1="-15.24" x2="5.08" y2="-15.24" width="0.1524" layer="91"/>
<label x="5.08" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="F2" gate="G$1" pin="1"/>
<wire x1="55.88" y1="-15.24" x2="45.72" y2="-15.24" width="0.1524" layer="91"/>
<label x="45.72" y="-15.24" size="1.27" layer="95"/>
</segment>
</net>
<net name="ACB" class="0">
<segment>
<pinref part="J1" gate="G$1" pin="3"/>
<wire x1="15.24" y1="-20.32" x2="5.08" y2="-20.32" width="0.1524" layer="91"/>
<label x="5.08" y="-20.32" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="F3" gate="G$1" pin="1"/>
<wire x1="96.52" y1="-15.24" x2="86.36" y2="-15.24" width="0.1524" layer="91"/>
<label x="86.36" y="-15.24" size="1.27" layer="95"/>
</segment>
</net>
<net name="AC1" class="0">
<segment>
<pinref part="F2" gate="G$1" pin="2"/>
<wire x1="66.04" y1="-15.24" x2="76.2" y2="-15.24" width="0.1524" layer="91"/>
<label x="67.31" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D1" gate="G$1" pin="A"/>
<wire x1="138.43" y1="-15.24" x2="128.27" y2="-15.24" width="0.1524" layer="91"/>
<label x="128.27" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D3" gate="G$1" pin="K"/>
<wire x1="227.33" y1="-15.24" x2="237.49" y2="-15.24" width="0.1524" layer="91"/>
<label x="228.6" y="-15.24" size="1.27" layer="95"/>
</segment>
</net>
<net name="AC2" class="0">
<segment>
<pinref part="F3" gate="G$1" pin="2"/>
<wire x1="106.68" y1="-15.24" x2="116.84" y2="-15.24" width="0.1524" layer="91"/>
<label x="107.95" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D2" gate="G$1" pin="A"/>
<wire x1="179.07" y1="-15.24" x2="168.91" y2="-15.24" width="0.1524" layer="91"/>
<label x="168.91" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D4" gate="G$1" pin="K"/>
<wire x1="267.97" y1="-15.24" x2="278.13" y2="-15.24" width="0.1524" layer="91"/>
<label x="269.24" y="-15.24" size="1.27" layer="95"/>
</segment>
</net>
<net name="VRAWP" class="0">
<segment>
<pinref part="D1" gate="G$1" pin="K"/>
<wire x1="146.05" y1="-15.24" x2="156.21" y2="-15.24" width="0.1524" layer="91"/>
<label x="147.32" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D2" gate="G$1" pin="K"/>
<wire x1="186.69" y1="-15.24" x2="196.85" y2="-15.24" width="0.1524" layer="91"/>
<label x="187.96" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C1" gate="G$1" pin="+"/>
<wire x1="299.72" y1="-15.24" x2="289.56" y2="-15.24" width="0.1524" layer="91"/>
<label x="289.56" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C3" gate="G$1" pin="1"/>
<wire x1="340.36" y1="-15.24" x2="330.2" y2="-15.24" width="0.1524" layer="91"/>
<label x="330.2" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="RSC1" gate="G$1" pin="1"/>
<wire x1="15.24" y1="-76.2" x2="5.08" y2="-76.2" width="0.1524" layer="91"/>
<label x="5.08" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q3" gate="G$1" pin="E"/>
<wire x1="144.78" y1="-71.12" x2="144.78" y2="-66.04" width="0.1524" layer="91"/>
<label x="144.78" y="-66.04" size="1.27" layer="95" rot="R90"/>
</segment>
<segment>
<pinref part="J3" gate="G$1" pin="1"/>
<wire x1="137.16" y1="-45.72" x2="127" y2="-45.72" width="0.1524" layer="91"/>
<label x="127" y="-45.72" size="1.27" layer="95"/>
</segment>
</net>
<net name="VRAWN" class="0">
<segment>
<pinref part="D3" gate="G$1" pin="A"/>
<wire x1="219.71" y1="-15.24" x2="209.55" y2="-15.24" width="0.1524" layer="91"/>
<label x="209.55" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D4" gate="G$1" pin="A"/>
<wire x1="260.35" y1="-15.24" x2="250.19" y2="-15.24" width="0.1524" layer="91"/>
<label x="250.19" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C2A" gate="G$1" pin="-"/>
<wire x1="25.4" y1="-45.72" x2="35.56" y2="-45.72" width="0.1524" layer="91"/>
<label x="26.67" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C2B" gate="G$1" pin="-"/>
<wire x1="66.04" y1="-45.72" x2="76.2" y2="-45.72" width="0.1524" layer="91"/>
<label x="67.31" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C4" gate="G$1" pin="2"/>
<wire x1="106.68" y1="-45.72" x2="116.84" y2="-45.72" width="0.1524" layer="91"/>
<label x="107.95" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="RSC2" gate="G$1" pin="1"/>
<wire x1="15.24" y1="-167.64" x2="5.08" y2="-167.64" width="0.1524" layer="91"/>
<label x="5.08" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q7" gate="G$1" pin="E"/>
<wire x1="144.78" y1="-172.72" x2="144.78" y2="-177.8" width="0.1524" layer="91"/>
<label x="144.78" y="-177.8" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="J3" gate="G$1" pin="3"/>
<wire x1="137.16" y1="-50.8" x2="127" y2="-50.8" width="0.1524" layer="91"/>
<label x="127" y="-50.8" size="1.27" layer="95"/>
</segment>
</net>
<net name="E1" class="0">
<segment>
<pinref part="RSC1" gate="G$1" pin="2"/>
<wire x1="25.4" y1="-76.2" x2="35.56" y2="-76.2" width="0.1524" layer="91"/>
<label x="26.67" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q1" gate="G$1" pin="E"/>
<wire x1="63.5" y1="-71.12" x2="63.5" y2="-66.04" width="0.1524" layer="91"/>
<label x="63.5" y="-66.04" size="1.27" layer="95" rot="R90"/>
</segment>
<segment>
<pinref part="R4" gate="G$1" pin="1"/>
<wire x1="218.44" y1="-76.2" x2="208.28" y2="-76.2" width="0.1524" layer="91"/>
<label x="208.28" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R5" gate="G$1" pin="2"/>
<wire x1="269.24" y1="-76.2" x2="279.4" y2="-76.2" width="0.1524" layer="91"/>
<label x="270.51" y="-76.2" size="1.27" layer="95"/>
</segment>
</net>
<net name="B1" class="0">
<segment>
<pinref part="Q1" gate="G$1" pin="B"/>
<wire x1="55.88" y1="-76.2" x2="45.72" y2="-76.2" width="0.1524" layer="91"/>
<label x="45.72" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q2" gate="G$1" pin="E"/>
<wire x1="104.14" y1="-71.12" x2="104.14" y2="-66.04" width="0.1524" layer="91"/>
<label x="104.14" y="-66.04" size="1.27" layer="95" rot="R90"/>
</segment>
<segment>
<pinref part="R4" gate="G$1" pin="2"/>
<wire x1="228.6" y1="-76.2" x2="238.76" y2="-76.2" width="0.1524" layer="91"/>
<label x="229.87" y="-76.2" size="1.27" layer="95"/>
</segment>
</net>
<net name="BD1" class="0">
<segment>
<pinref part="Q2" gate="G$1" pin="B"/>
<wire x1="96.52" y1="-76.2" x2="86.36" y2="-76.2" width="0.1524" layer="91"/>
<label x="86.36" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q3" gate="G$1" pin="C"/>
<wire x1="144.78" y1="-81.28" x2="144.78" y2="-86.36" width="0.1524" layer="91"/>
<label x="144.78" y="-86.36" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="R3" gate="G$1" pin="1"/>
<wire x1="177.8" y1="-76.2" x2="167.64" y2="-76.2" width="0.1524" layer="91"/>
<label x="167.64" y="-76.2" size="1.27" layer="95"/>
</segment>
</net>
<net name="BS1" class="0">
<segment>
<pinref part="Q3" gate="G$1" pin="B"/>
<wire x1="137.16" y1="-76.2" x2="127" y2="-76.2" width="0.1524" layer="91"/>
<label x="127" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R5" gate="G$1" pin="1"/>
<wire x1="259.08" y1="-76.2" x2="248.92" y2="-76.2" width="0.1524" layer="91"/>
<label x="248.92" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R6" gate="G$1" pin="1"/>
<wire x1="299.72" y1="-76.2" x2="289.56" y2="-76.2" width="0.1524" layer="91"/>
<label x="289.56" y="-76.2" size="1.27" layer="95"/>
</segment>
</net>
<net name="VA1" class="0">
<segment>
<pinref part="Q1" gate="G$1" pin="C"/>
<wire x1="63.5" y1="-81.28" x2="63.5" y2="-86.36" width="0.1524" layer="91"/>
<label x="63.5" y="-86.36" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="Q2" gate="G$1" pin="C"/>
<wire x1="104.14" y1="-81.28" x2="104.14" y2="-86.36" width="0.1524" layer="91"/>
<label x="104.14" y="-86.36" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="R6" gate="G$1" pin="2"/>
<wire x1="309.88" y1="-76.2" x2="320.04" y2="-76.2" width="0.1524" layer="91"/>
<label x="311.15" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R7" gate="G$1" pin="1"/>
<wire x1="15.24" y1="-106.68" x2="5.08" y2="-106.68" width="0.1524" layer="91"/>
<label x="5.08" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q4" gate="G$1" pin="E"/>
<wire x1="63.5" y1="-101.6" x2="63.5" y2="-96.52" width="0.1524" layer="91"/>
<label x="63.5" y="-96.52" size="1.27" layer="95" rot="R90"/>
</segment>
</net>
<net name="IN1" class="0">
<segment>
<pinref part="R7" gate="G$1" pin="2"/>
<wire x1="25.4" y1="-106.68" x2="35.56" y2="-106.68" width="0.1524" layer="91"/>
<label x="26.67" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q4" gate="G$1" pin="B"/>
<wire x1="55.88" y1="-106.68" x2="45.72" y2="-106.68" width="0.1524" layer="91"/>
<label x="45.72" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C5" gate="G$1" pin="1"/>
<wire x1="96.52" y1="-106.68" x2="86.36" y2="-106.68" width="0.1524" layer="91"/>
<label x="86.36" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="U1" gate="G$1" pin="IN"/>
<wire x1="134.62" y1="-106.68" x2="124.46" y2="-106.68" width="0.1524" layer="91"/>
<label x="124.46" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D5" gate="G$1" pin="K"/>
<wire x1="349.25" y1="-106.68" x2="359.41" y2="-106.68" width="0.1524" layer="91"/>
<label x="350.52" y="-106.68" size="1.27" layer="95"/>
</segment>
</net>
<net name="ADJ1" class="0">
<segment>
<pinref part="U1" gate="G$1" pin="ADJ"/>
<wire x1="142.24" y1="-111.76" x2="142.24" y2="-116.84" width="0.1524" layer="91"/>
<label x="142.24" y="-116.84" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="R8" gate="G$1" pin="2"/>
<wire x1="187.96" y1="-106.68" x2="198.12" y2="-106.68" width="0.1524" layer="91"/>
<label x="189.23" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R9" gate="G$1" pin="1"/>
<wire x1="218.44" y1="-106.68" x2="208.28" y2="-106.68" width="0.1524" layer="91"/>
<label x="208.28" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C6" gate="G$1" pin="+"/>
<wire x1="299.72" y1="-106.68" x2="289.56" y2="-106.68" width="0.1524" layer="91"/>
<label x="289.56" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D6" gate="G$1" pin="A"/>
<wire x1="382.27" y1="-106.68" x2="372.11" y2="-106.68" width="0.1524" layer="91"/>
<label x="372.11" y="-106.68" size="1.27" layer="95"/>
</segment>
</net>
<net name="RV1A" class="0">
<segment>
<pinref part="R9" gate="G$1" pin="2"/>
<wire x1="228.6" y1="-106.68" x2="238.76" y2="-106.68" width="0.1524" layer="91"/>
<label x="229.87" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="RV1" gate="G$1" pin="1"/>
<wire x1="256.54" y1="-106.68" x2="246.38" y2="-106.68" width="0.1524" layer="91"/>
<label x="246.38" y="-106.68" size="1.27" layer="95"/>
</segment>
</net>
<net name="+16V" class="0">
<segment>
<pinref part="Q4" gate="G$1" pin="C"/>
<wire x1="63.5" y1="-111.76" x2="63.5" y2="-116.84" width="0.1524" layer="91"/>
<label x="63.5" y="-116.84" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="U1" gate="G$1" pin="OUT"/>
<wire x1="149.86" y1="-106.68" x2="160.02" y2="-106.68" width="0.1524" layer="91"/>
<label x="151.13" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R8" gate="G$1" pin="1"/>
<wire x1="177.8" y1="-106.68" x2="167.64" y2="-106.68" width="0.1524" layer="91"/>
<label x="167.64" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D5" gate="G$1" pin="A"/>
<wire x1="341.63" y1="-106.68" x2="331.47" y2="-106.68" width="0.1524" layer="91"/>
<label x="331.47" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D6" gate="G$1" pin="K"/>
<wire x1="389.89" y1="-106.68" x2="400.05" y2="-106.68" width="0.1524" layer="91"/>
<label x="391.16" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C7" gate="G$1" pin="+"/>
<wire x1="15.24" y1="-137.16" x2="5.08" y2="-137.16" width="0.1524" layer="91"/>
<label x="5.08" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C8" gate="G$1" pin="1"/>
<wire x1="55.88" y1="-137.16" x2="45.72" y2="-137.16" width="0.1524" layer="91"/>
<label x="45.72" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C9" gate="G$1" pin="+"/>
<wire x1="96.52" y1="-137.16" x2="86.36" y2="-137.16" width="0.1524" layer="91"/>
<label x="86.36" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D7" gate="G$1" pin="K"/>
<wire x1="146.05" y1="-137.16" x2="156.21" y2="-137.16" width="0.1524" layer="91"/>
<label x="147.32" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R10" gate="G$1" pin="1"/>
<wire x1="177.8" y1="-137.16" x2="167.64" y2="-137.16" width="0.1524" layer="91"/>
<label x="167.64" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J4" gate="G$1" pin="1"/>
<wire x1="259.08" y1="-137.16" x2="248.92" y2="-137.16" width="0.1524" layer="91"/>
<label x="248.92" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R19" gate="G$1" pin="1"/>
<wire x1="15.24" y1="-259.08" x2="5.08" y2="-259.08" width="0.1524" layer="91"/>
<label x="5.08" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J2" gate="G$1" pin="1"/>
<wire x1="177.8" y1="-45.72" x2="167.64" y2="-45.72" width="0.1524" layer="91"/>
<label x="167.64" y="-45.72" size="1.27" layer="95"/>
</segment>
</net>
<net name="LED1A" class="0">
<segment>
<pinref part="R10" gate="G$1" pin="2"/>
<wire x1="187.96" y1="-137.16" x2="198.12" y2="-137.16" width="0.1524" layer="91"/>
<label x="189.23" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="LED1" gate="G$1" pin="A"/>
<wire x1="219.71" y1="-137.16" x2="209.55" y2="-137.16" width="0.1524" layer="91"/>
<label x="209.55" y="-137.16" size="1.27" layer="95"/>
</segment>
</net>
<net name="E2" class="0">
<segment>
<pinref part="RSC2" gate="G$1" pin="2"/>
<wire x1="25.4" y1="-167.64" x2="35.56" y2="-167.64" width="0.1524" layer="91"/>
<label x="26.67" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q5" gate="G$1" pin="E"/>
<wire x1="63.5" y1="-172.72" x2="63.5" y2="-177.8" width="0.1524" layer="91"/>
<label x="63.5" y="-177.8" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="R12" gate="G$1" pin="1"/>
<wire x1="218.44" y1="-167.64" x2="208.28" y2="-167.64" width="0.1524" layer="91"/>
<label x="208.28" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R13" gate="G$1" pin="2"/>
<wire x1="269.24" y1="-167.64" x2="279.4" y2="-167.64" width="0.1524" layer="91"/>
<label x="270.51" y="-167.64" size="1.27" layer="95"/>
</segment>
</net>
<net name="B2" class="0">
<segment>
<pinref part="Q5" gate="G$1" pin="B"/>
<wire x1="55.88" y1="-167.64" x2="45.72" y2="-167.64" width="0.1524" layer="91"/>
<label x="45.72" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q6" gate="G$1" pin="E"/>
<wire x1="104.14" y1="-172.72" x2="104.14" y2="-177.8" width="0.1524" layer="91"/>
<label x="104.14" y="-177.8" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="R12" gate="G$1" pin="2"/>
<wire x1="228.6" y1="-167.64" x2="238.76" y2="-167.64" width="0.1524" layer="91"/>
<label x="229.87" y="-167.64" size="1.27" layer="95"/>
</segment>
</net>
<net name="BD2" class="0">
<segment>
<pinref part="Q6" gate="G$1" pin="B"/>
<wire x1="96.52" y1="-167.64" x2="86.36" y2="-167.64" width="0.1524" layer="91"/>
<label x="86.36" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q7" gate="G$1" pin="C"/>
<wire x1="144.78" y1="-162.56" x2="144.78" y2="-157.48" width="0.1524" layer="91"/>
<label x="144.78" y="-157.48" size="1.27" layer="95" rot="R90"/>
</segment>
<segment>
<pinref part="R11" gate="G$1" pin="1"/>
<wire x1="177.8" y1="-167.64" x2="167.64" y2="-167.64" width="0.1524" layer="91"/>
<label x="167.64" y="-167.64" size="1.27" layer="95"/>
</segment>
</net>
<net name="BS2" class="0">
<segment>
<pinref part="Q7" gate="G$1" pin="B"/>
<wire x1="137.16" y1="-167.64" x2="127" y2="-167.64" width="0.1524" layer="91"/>
<label x="127" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R13" gate="G$1" pin="1"/>
<wire x1="259.08" y1="-167.64" x2="248.92" y2="-167.64" width="0.1524" layer="91"/>
<label x="248.92" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R14" gate="G$1" pin="1"/>
<wire x1="299.72" y1="-167.64" x2="289.56" y2="-167.64" width="0.1524" layer="91"/>
<label x="289.56" y="-167.64" size="1.27" layer="95"/>
</segment>
</net>
<net name="VA2" class="0">
<segment>
<pinref part="Q5" gate="G$1" pin="C"/>
<wire x1="63.5" y1="-162.56" x2="63.5" y2="-157.48" width="0.1524" layer="91"/>
<label x="63.5" y="-157.48" size="1.27" layer="95" rot="R90"/>
</segment>
<segment>
<pinref part="Q6" gate="G$1" pin="C"/>
<wire x1="104.14" y1="-162.56" x2="104.14" y2="-157.48" width="0.1524" layer="91"/>
<label x="104.14" y="-157.48" size="1.27" layer="95" rot="R90"/>
</segment>
<segment>
<pinref part="R14" gate="G$1" pin="2"/>
<wire x1="309.88" y1="-167.64" x2="320.04" y2="-167.64" width="0.1524" layer="91"/>
<label x="311.15" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R15" gate="G$1" pin="1"/>
<wire x1="15.24" y1="-198.12" x2="5.08" y2="-198.12" width="0.1524" layer="91"/>
<label x="5.08" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q8" gate="G$1" pin="E"/>
<wire x1="63.5" y1="-203.2" x2="63.5" y2="-208.28" width="0.1524" layer="91"/>
<label x="63.5" y="-208.28" size="1.27" layer="95" rot="R270"/>
</segment>
</net>
<net name="IN2" class="0">
<segment>
<pinref part="R15" gate="G$1" pin="2"/>
<wire x1="25.4" y1="-198.12" x2="35.56" y2="-198.12" width="0.1524" layer="91"/>
<label x="26.67" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="Q8" gate="G$1" pin="B"/>
<wire x1="55.88" y1="-198.12" x2="45.72" y2="-198.12" width="0.1524" layer="91"/>
<label x="45.72" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C10" gate="G$1" pin="2"/>
<wire x1="106.68" y1="-198.12" x2="116.84" y2="-198.12" width="0.1524" layer="91"/>
<label x="107.95" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="U2" gate="G$1" pin="IN"/>
<wire x1="134.62" y1="-198.12" x2="124.46" y2="-198.12" width="0.1524" layer="91"/>
<label x="124.46" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D8" gate="G$1" pin="A"/>
<wire x1="341.63" y1="-198.12" x2="331.47" y2="-198.12" width="0.1524" layer="91"/>
<label x="331.47" y="-198.12" size="1.27" layer="95"/>
</segment>
</net>
<net name="ADJ2" class="0">
<segment>
<pinref part="U2" gate="G$1" pin="ADJ"/>
<wire x1="142.24" y1="-203.2" x2="142.24" y2="-208.28" width="0.1524" layer="91"/>
<label x="142.24" y="-208.28" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="R16" gate="G$1" pin="2"/>
<wire x1="187.96" y1="-198.12" x2="198.12" y2="-198.12" width="0.1524" layer="91"/>
<label x="189.23" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R17" gate="G$1" pin="1"/>
<wire x1="218.44" y1="-198.12" x2="208.28" y2="-198.12" width="0.1524" layer="91"/>
<label x="208.28" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C11" gate="G$1" pin="-"/>
<wire x1="309.88" y1="-198.12" x2="320.04" y2="-198.12" width="0.1524" layer="91"/>
<label x="311.15" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D9" gate="G$1" pin="K"/>
<wire x1="389.89" y1="-198.12" x2="400.05" y2="-198.12" width="0.1524" layer="91"/>
<label x="391.16" y="-198.12" size="1.27" layer="95"/>
</segment>
</net>
<net name="RV2A" class="0">
<segment>
<pinref part="R17" gate="G$1" pin="2"/>
<wire x1="228.6" y1="-198.12" x2="238.76" y2="-198.12" width="0.1524" layer="91"/>
<label x="229.87" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="RV2" gate="G$1" pin="1"/>
<wire x1="256.54" y1="-198.12" x2="246.38" y2="-198.12" width="0.1524" layer="91"/>
<label x="246.38" y="-198.12" size="1.27" layer="95"/>
</segment>
</net>
<net name="-16V" class="0">
<segment>
<pinref part="Q8" gate="G$1" pin="C"/>
<wire x1="63.5" y1="-193.04" x2="63.5" y2="-187.96" width="0.1524" layer="91"/>
<label x="63.5" y="-187.96" size="1.27" layer="95" rot="R90"/>
</segment>
<segment>
<pinref part="U2" gate="G$1" pin="OUT"/>
<wire x1="149.86" y1="-198.12" x2="160.02" y2="-198.12" width="0.1524" layer="91"/>
<label x="151.13" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R16" gate="G$1" pin="1"/>
<wire x1="177.8" y1="-198.12" x2="167.64" y2="-198.12" width="0.1524" layer="91"/>
<label x="167.64" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D8" gate="G$1" pin="K"/>
<wire x1="349.25" y1="-198.12" x2="359.41" y2="-198.12" width="0.1524" layer="91"/>
<label x="350.52" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D9" gate="G$1" pin="A"/>
<wire x1="382.27" y1="-198.12" x2="372.11" y2="-198.12" width="0.1524" layer="91"/>
<label x="372.11" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C12" gate="G$1" pin="-"/>
<wire x1="25.4" y1="-228.6" x2="35.56" y2="-228.6" width="0.1524" layer="91"/>
<label x="26.67" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C13" gate="G$1" pin="2"/>
<wire x1="66.04" y1="-228.6" x2="76.2" y2="-228.6" width="0.1524" layer="91"/>
<label x="67.31" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C14" gate="G$1" pin="-"/>
<wire x1="106.68" y1="-228.6" x2="116.84" y2="-228.6" width="0.1524" layer="91"/>
<label x="107.95" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D10" gate="G$1" pin="A"/>
<wire x1="138.43" y1="-228.6" x2="128.27" y2="-228.6" width="0.1524" layer="91"/>
<label x="128.27" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R18" gate="G$1" pin="1"/>
<wire x1="177.8" y1="-228.6" x2="167.64" y2="-228.6" width="0.1524" layer="91"/>
<label x="167.64" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J5" gate="G$1" pin="1"/>
<wire x1="259.08" y1="-228.6" x2="248.92" y2="-228.6" width="0.1524" layer="91"/>
<label x="248.92" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J2" gate="G$1" pin="2"/>
<wire x1="177.8" y1="-48.26" x2="167.64" y2="-48.26" width="0.1524" layer="91"/>
<label x="167.64" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="LED2K" class="0">
<segment>
<pinref part="R18" gate="G$1" pin="2"/>
<wire x1="187.96" y1="-228.6" x2="198.12" y2="-228.6" width="0.1524" layer="91"/>
<label x="189.23" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="LED2" gate="G$1" pin="K"/>
<wire x1="227.33" y1="-228.6" x2="237.49" y2="-228.6" width="0.1524" layer="91"/>
<label x="228.6" y="-228.6" size="1.27" layer="95"/>
</segment>
</net>
<net name="VIN3" class="0">
<segment>
<pinref part="R19" gate="G$1" pin="2"/>
<wire x1="25.4" y1="-259.08" x2="35.56" y2="-259.08" width="0.1524" layer="91"/>
<label x="26.67" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C15" gate="G$1" pin="+"/>
<wire x1="55.88" y1="-259.08" x2="45.72" y2="-259.08" width="0.1524" layer="91"/>
<label x="45.72" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C16" gate="G$1" pin="1"/>
<wire x1="96.52" y1="-259.08" x2="86.36" y2="-259.08" width="0.1524" layer="91"/>
<label x="86.36" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="U3" gate="G$1" pin="IN"/>
<wire x1="134.62" y1="-259.08" x2="124.46" y2="-259.08" width="0.1524" layer="91"/>
<label x="124.46" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D11" gate="G$1" pin="K"/>
<wire x1="24.13" y1="-289.56" x2="34.29" y2="-289.56" width="0.1524" layer="91"/>
<label x="25.4" y="-289.56" size="1.27" layer="95"/>
</segment>
</net>
<net name="ADJ3" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="ADJ"/>
<wire x1="142.24" y1="-264.16" x2="142.24" y2="-269.24" width="0.1524" layer="91"/>
<label x="142.24" y="-269.24" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="R20" gate="G$1" pin="2"/>
<wire x1="187.96" y1="-259.08" x2="198.12" y2="-259.08" width="0.1524" layer="91"/>
<label x="189.23" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R21" gate="G$1" pin="1"/>
<wire x1="218.44" y1="-259.08" x2="208.28" y2="-259.08" width="0.1524" layer="91"/>
<label x="208.28" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C17" gate="G$1" pin="+"/>
<wire x1="299.72" y1="-259.08" x2="289.56" y2="-259.08" width="0.1524" layer="91"/>
<label x="289.56" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D12" gate="G$1" pin="A"/>
<wire x1="57.15" y1="-289.56" x2="46.99" y2="-289.56" width="0.1524" layer="91"/>
<label x="46.99" y="-289.56" size="1.27" layer="95"/>
</segment>
</net>
<net name="RV3A" class="0">
<segment>
<pinref part="R21" gate="G$1" pin="2"/>
<wire x1="228.6" y1="-259.08" x2="238.76" y2="-259.08" width="0.1524" layer="91"/>
<label x="229.87" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="RV3" gate="G$1" pin="1"/>
<wire x1="256.54" y1="-259.08" x2="246.38" y2="-259.08" width="0.1524" layer="91"/>
<label x="246.38" y="-259.08" size="1.27" layer="95"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<pinref part="U3" gate="G$1" pin="OUT"/>
<wire x1="149.86" y1="-259.08" x2="160.02" y2="-259.08" width="0.1524" layer="91"/>
<label x="151.13" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R20" gate="G$1" pin="1"/>
<wire x1="177.8" y1="-259.08" x2="167.64" y2="-259.08" width="0.1524" layer="91"/>
<label x="167.64" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D11" gate="G$1" pin="A"/>
<wire x1="16.51" y1="-289.56" x2="6.35" y2="-289.56" width="0.1524" layer="91"/>
<label x="6.35" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D12" gate="G$1" pin="K"/>
<wire x1="64.77" y1="-289.56" x2="74.93" y2="-289.56" width="0.1524" layer="91"/>
<label x="66.04" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C18" gate="G$1" pin="+"/>
<wire x1="96.52" y1="-289.56" x2="86.36" y2="-289.56" width="0.1524" layer="91"/>
<label x="86.36" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C19" gate="G$1" pin="1"/>
<wire x1="137.16" y1="-289.56" x2="127" y2="-289.56" width="0.1524" layer="91"/>
<label x="127" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D13" gate="G$1" pin="K"/>
<wire x1="186.69" y1="-289.56" x2="196.85" y2="-289.56" width="0.1524" layer="91"/>
<label x="187.96" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R22" gate="G$1" pin="1"/>
<wire x1="218.44" y1="-289.56" x2="208.28" y2="-289.56" width="0.1524" layer="91"/>
<label x="208.28" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J2" gate="G$1" pin="4"/>
<wire x1="177.8" y1="-53.34" x2="167.64" y2="-53.34" width="0.1524" layer="91"/>
<label x="167.64" y="-53.34" size="1.27" layer="95"/>
</segment>
</net>
<net name="LED3A" class="0">
<segment>
<pinref part="R22" gate="G$1" pin="2"/>
<wire x1="228.6" y1="-289.56" x2="238.76" y2="-289.56" width="0.1524" layer="91"/>
<label x="229.87" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="LED3" gate="G$1" pin="A"/>
<wire x1="260.35" y1="-289.56" x2="250.19" y2="-289.56" width="0.1524" layer="91"/>
<label x="250.19" y="-289.56" size="1.27" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="J1" gate="G$1" pin="2"/>
<wire x1="15.24" y1="-17.78" x2="5.08" y2="-17.78" width="0.1524" layer="91"/>
<label x="5.08" y="-17.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C1" gate="G$1" pin="-"/>
<wire x1="309.88" y1="-15.24" x2="320.04" y2="-15.24" width="0.1524" layer="91"/>
<label x="311.15" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C3" gate="G$1" pin="2"/>
<wire x1="350.52" y1="-15.24" x2="360.68" y2="-15.24" width="0.1524" layer="91"/>
<label x="351.79" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C2A" gate="G$1" pin="+"/>
<wire x1="15.24" y1="-45.72" x2="5.08" y2="-45.72" width="0.1524" layer="91"/>
<label x="5.08" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C2B" gate="G$1" pin="+"/>
<wire x1="55.88" y1="-45.72" x2="45.72" y2="-45.72" width="0.1524" layer="91"/>
<label x="45.72" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C4" gate="G$1" pin="1"/>
<wire x1="96.52" y1="-45.72" x2="86.36" y2="-45.72" width="0.1524" layer="91"/>
<label x="86.36" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J3" gate="G$1" pin="2"/>
<wire x1="137.16" y1="-48.26" x2="127" y2="-48.26" width="0.1524" layer="91"/>
<label x="127" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R3" gate="G$1" pin="2"/>
<wire x1="187.96" y1="-76.2" x2="198.12" y2="-76.2" width="0.1524" layer="91"/>
<label x="189.23" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C5" gate="G$1" pin="2"/>
<wire x1="106.68" y1="-106.68" x2="116.84" y2="-106.68" width="0.1524" layer="91"/>
<label x="107.95" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="RV1" gate="G$1" pin="2"/>
<wire x1="264.16" y1="-111.76" x2="264.16" y2="-116.84" width="0.1524" layer="91"/>
<label x="264.16" y="-116.84" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="RV1" gate="G$1" pin="3"/>
<wire x1="271.78" y1="-106.68" x2="281.94" y2="-106.68" width="0.1524" layer="91"/>
<label x="273.05" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C6" gate="G$1" pin="-"/>
<wire x1="309.88" y1="-106.68" x2="320.04" y2="-106.68" width="0.1524" layer="91"/>
<label x="311.15" y="-106.68" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C7" gate="G$1" pin="-"/>
<wire x1="25.4" y1="-137.16" x2="35.56" y2="-137.16" width="0.1524" layer="91"/>
<label x="26.67" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C8" gate="G$1" pin="2"/>
<wire x1="66.04" y1="-137.16" x2="76.2" y2="-137.16" width="0.1524" layer="91"/>
<label x="67.31" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C9" gate="G$1" pin="-"/>
<wire x1="106.68" y1="-137.16" x2="116.84" y2="-137.16" width="0.1524" layer="91"/>
<label x="107.95" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D7" gate="G$1" pin="A"/>
<wire x1="138.43" y1="-137.16" x2="128.27" y2="-137.16" width="0.1524" layer="91"/>
<label x="128.27" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="LED1" gate="G$1" pin="K"/>
<wire x1="227.33" y1="-137.16" x2="237.49" y2="-137.16" width="0.1524" layer="91"/>
<label x="228.6" y="-137.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J4" gate="G$1" pin="2"/>
<wire x1="259.08" y1="-139.7" x2="248.92" y2="-139.7" width="0.1524" layer="91"/>
<label x="248.92" y="-139.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="R11" gate="G$1" pin="2"/>
<wire x1="187.96" y1="-167.64" x2="198.12" y2="-167.64" width="0.1524" layer="91"/>
<label x="189.23" y="-167.64" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C10" gate="G$1" pin="1"/>
<wire x1="96.52" y1="-198.12" x2="86.36" y2="-198.12" width="0.1524" layer="91"/>
<label x="86.36" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="RV2" gate="G$1" pin="2"/>
<wire x1="264.16" y1="-203.2" x2="264.16" y2="-208.28" width="0.1524" layer="91"/>
<label x="264.16" y="-208.28" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="RV2" gate="G$1" pin="3"/>
<wire x1="271.78" y1="-198.12" x2="281.94" y2="-198.12" width="0.1524" layer="91"/>
<label x="273.05" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C11" gate="G$1" pin="+"/>
<wire x1="299.72" y1="-198.12" x2="289.56" y2="-198.12" width="0.1524" layer="91"/>
<label x="289.56" y="-198.12" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C12" gate="G$1" pin="+"/>
<wire x1="15.24" y1="-228.6" x2="5.08" y2="-228.6" width="0.1524" layer="91"/>
<label x="5.08" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C13" gate="G$1" pin="1"/>
<wire x1="55.88" y1="-228.6" x2="45.72" y2="-228.6" width="0.1524" layer="91"/>
<label x="45.72" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C14" gate="G$1" pin="+"/>
<wire x1="96.52" y1="-228.6" x2="86.36" y2="-228.6" width="0.1524" layer="91"/>
<label x="86.36" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D10" gate="G$1" pin="K"/>
<wire x1="146.05" y1="-228.6" x2="156.21" y2="-228.6" width="0.1524" layer="91"/>
<label x="147.32" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="LED2" gate="G$1" pin="A"/>
<wire x1="219.71" y1="-228.6" x2="209.55" y2="-228.6" width="0.1524" layer="91"/>
<label x="209.55" y="-228.6" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J5" gate="G$1" pin="2"/>
<wire x1="259.08" y1="-231.14" x2="248.92" y2="-231.14" width="0.1524" layer="91"/>
<label x="248.92" y="-231.14" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C15" gate="G$1" pin="-"/>
<wire x1="66.04" y1="-259.08" x2="76.2" y2="-259.08" width="0.1524" layer="91"/>
<label x="67.31" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C16" gate="G$1" pin="2"/>
<wire x1="106.68" y1="-259.08" x2="116.84" y2="-259.08" width="0.1524" layer="91"/>
<label x="107.95" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="RV3" gate="G$1" pin="2"/>
<wire x1="264.16" y1="-264.16" x2="264.16" y2="-269.24" width="0.1524" layer="91"/>
<label x="264.16" y="-269.24" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="RV3" gate="G$1" pin="3"/>
<wire x1="271.78" y1="-259.08" x2="281.94" y2="-259.08" width="0.1524" layer="91"/>
<label x="273.05" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C17" gate="G$1" pin="-"/>
<wire x1="309.88" y1="-259.08" x2="320.04" y2="-259.08" width="0.1524" layer="91"/>
<label x="311.15" y="-259.08" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C18" gate="G$1" pin="-"/>
<wire x1="106.68" y1="-289.56" x2="116.84" y2="-289.56" width="0.1524" layer="91"/>
<label x="107.95" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="C19" gate="G$1" pin="2"/>
<wire x1="147.32" y1="-289.56" x2="157.48" y2="-289.56" width="0.1524" layer="91"/>
<label x="148.59" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="D13" gate="G$1" pin="A"/>
<wire x1="179.07" y1="-289.56" x2="168.91" y2="-289.56" width="0.1524" layer="91"/>
<label x="168.91" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="LED3" gate="G$1" pin="K"/>
<wire x1="267.97" y1="-289.56" x2="278.13" y2="-289.56" width="0.1524" layer="91"/>
<label x="269.24" y="-289.56" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="J2" gate="G$1" pin="3"/>
<wire x1="177.8" y1="-50.8" x2="167.64" y2="-50.8" width="0.1524" layer="91"/>
<label x="167.64" y="-50.8" size="1.27" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
