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
<description>Cuatro controladores PID analógicos (levitador magnético) - Brahiam Alberto Campiño Romero</description>
<libraries>
<library name="pid4">
<packages>
<package name="DIL08">
<description>DIL8 (LM741), separación entre filas 7.62 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="0" y="-2.54" drill="0.9" diameter="2" shape="round"/>
<pad name="3" x="0" y="-5.08" drill="0.9" diameter="2" shape="round"/>
<pad name="4" x="0" y="-7.62" drill="0.9" diameter="2" shape="round"/>
<pad name="5" x="7.62" y="-7.62" drill="0.9" diameter="2" shape="round"/>
<pad name="6" x="7.62" y="-5.08" drill="0.9" diameter="2" shape="round"/>
<pad name="7" x="7.62" y="-2.54" drill="0.9" diameter="2" shape="round"/>
<pad name="8" x="7.62" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="1.4" y1="-8.9" x2="6.2" y2="-8.9" width="0.2" layer="21"/>
<wire x1="6.2" y1="-8.9" x2="6.2" y2="1.3" width="0.2" layer="21"/>
<wire x1="6.2" y1="1.3" x2="1.4" y2="1.3" width="0.2" layer="21"/>
<wire x1="1.4" y1="1.3" x2="1.4" y2="-8.9" width="0.2" layer="21"/>
<wire x1="3.2" y1="1.3" x2="4.4" y2="1.3" width="0.2" layer="21" curve="180"/>
<text x="3.81" y="-3.81" size="1.27" layer="25" rot="R90" align="center">&gt;NAME</text>
<text x="3.81" y="-6.6" size="1.0" layer="27" rot="R90" align="center">&gt;VALUE</text>
</package>
<package name="RES">
<description>Resistencia axial 1/4 W, 7.62 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="7.62" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="1.3" y1="-1.1" x2="6.3" y2="-1.1" width="0.2" layer="21"/>
<wire x1="6.3" y1="-1.1" x2="6.3" y2="1.1" width="0.2" layer="21"/>
<wire x1="6.3" y1="1.1" x2="1.3" y2="1.1" width="0.2" layer="21"/>
<wire x1="1.3" y1="1.1" x2="1.3" y2="-1.1" width="0.2" layer="21"/>
<wire x1="0" y1="0" x2="1.3" y2="0" width="0.2" layer="21"/>
<wire x1="6.3" y1="0" x2="7.62" y2="0" width="0.2" layer="21"/>
<text x="3.81" y="1.9" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="3.81" y="-1.9" size="1.0" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="CAP">
<description>Capacitor no polarizado, separación 5.08 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="5.08" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-1.5" y1="-2.5" x2="6.58" y2="-2.5" width="0.2" layer="21"/>
<wire x1="6.58" y1="-2.5" x2="6.58" y2="2.5" width="0.2" layer="21"/>
<wire x1="6.58" y1="2.5" x2="-1.5" y2="2.5" width="0.2" layer="21"/>
<wire x1="-1.5" y1="2.5" x2="-1.5" y2="-2.5" width="0.2" layer="21"/>
<text x="2.54" y="3.2" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="2.54" y="-3.2" size="1.0" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="POT">
<description>Potenciómetro 3 pines, separación 5.08 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="5.08" y="0" drill="0.9" diameter="2" shape="round"/>
<pad name="3" x="10.16" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-2.6" y1="-4.6" x2="12.76" y2="-4.6" width="0.2" layer="21"/>
<wire x1="12.76" y1="-4.6" x2="12.76" y2="4.6" width="0.2" layer="21"/>
<wire x1="12.76" y1="4.6" x2="-2.6" y2="4.6" width="0.2" layer="21"/>
<wire x1="-2.6" y1="4.6" x2="-2.6" y2="-4.6" width="0.2" layer="21"/>
<text x="5.08" y="5.3" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
<text x="5.08" y="-5.3" size="1.0" layer="27" align="top-center">&gt;VALUE</text>
</package>
<package name="HDR1">
<description>Regleta de 1 pines, 2.54 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<wire x1="-1.4" y1="-1.4" x2="1.4" y2="-1.4" width="0.2" layer="21"/>
<wire x1="1.4" y1="-1.4" x2="1.4" y2="1.4" width="0.2" layer="21"/>
<wire x1="1.4" y1="1.4" x2="-1.4" y2="1.4" width="0.2" layer="21"/>
<wire x1="-1.4" y1="1.4" x2="-1.4" y2="-1.4" width="0.2" layer="21"/>
<text x="0" y="2.1" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
</package>
<package name="HDR2">
<description>Regleta de 2 pines, 2.54 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-1.4" y1="-1.4" x2="3.94" y2="-1.4" width="0.2" layer="21"/>
<wire x1="3.94" y1="-1.4" x2="3.94" y2="1.4" width="0.2" layer="21"/>
<wire x1="3.94" y1="1.4" x2="-1.4" y2="1.4" width="0.2" layer="21"/>
<wire x1="-1.4" y1="1.4" x2="-1.4" y2="-1.4" width="0.2" layer="21"/>
<text x="1.27" y="2.1" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
</package>
<package name="HDR4">
<description>Regleta de 4 pines, 2.54 mm</description>
<pad name="1" x="0" y="0" drill="0.9" diameter="2" shape="square"/>
<pad name="2" x="2.54" y="0" drill="0.9" diameter="2" shape="round"/>
<pad name="3" x="5.08" y="0" drill="0.9" diameter="2" shape="round"/>
<pad name="4" x="7.62" y="0" drill="0.9" diameter="2" shape="round"/>
<wire x1="-1.4" y1="-1.4" x2="9.02" y2="-1.4" width="0.2" layer="21"/>
<wire x1="9.02" y1="-1.4" x2="9.02" y2="1.4" width="0.2" layer="21"/>
<wire x1="9.02" y1="1.4" x2="-1.4" y2="1.4" width="0.2" layer="21"/>
<wire x1="-1.4" y1="1.4" x2="-1.4" y2="-1.4" width="0.2" layer="21"/>
<text x="3.81" y="2.1" size="1.27" layer="25" align="bottom-center">&gt;NAME</text>
</package>
</packages>
<symbols>
<symbol name="LM741">
<wire x1="-7.62" y1="-7.62" x2="7.62" y2="-7.62" width="0.254" layer="94"/>
<wire x1="7.62" y1="-7.62" x2="7.62" y2="7.62" width="0.254" layer="94"/>
<wire x1="7.62" y1="7.62" x2="-7.62" y2="7.62" width="0.254" layer="94"/>
<wire x1="-7.62" y1="7.62" x2="-7.62" y2="-7.62" width="0.254" layer="94"/>
<text x="-7.62" y="8.5" size="1.778" layer="95">&gt;NAME</text>
<text x="-7.62" y="-10.2" size="1.778" layer="96">&gt;VALUE</text>
<text x="-6.8" y="1.1" size="1.27" layer="94">LM741</text>
<pin name="OFFSET1" x="-10.16" y="5.08" length="short" direction="pas"/>
<pin name="IN-" x="-10.16" y="2.54" length="short" direction="pas"/>
<pin name="IN+" x="-10.16" y="0" length="short" direction="pas"/>
<pin name="V-" x="-10.16" y="-2.54" length="short" direction="pas"/>
<pin name="V+" x="10.16" y="5.08" length="short" direction="pas" rot="R180"/>
<pin name="OUT" x="10.16" y="2.54" length="short" direction="pas" rot="R180"/>
<pin name="OFFSET2" x="10.16" y="0" length="short" direction="pas" rot="R180"/>
<pin name="NC" x="10.16" y="-2.54" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="R">
<wire x1="-2.54" y1="-1.016" x2="2.54" y2="-1.016" width="0.254" layer="94"/>
<wire x1="2.54" y1="-1.016" x2="2.54" y2="1.016" width="0.254" layer="94"/>
<wire x1="2.54" y1="1.016" x2="-2.54" y2="1.016" width="0.254" layer="94"/>
<wire x1="-2.54" y1="1.016" x2="-2.54" y2="-1.016" width="0.254" layer="94"/>
<text x="-3.81" y="2.2" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-3.9" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="5.08" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="C">
<wire x1="-0.6" y1="-2.54" x2="-0.6" y2="2.54" width="0.4" layer="94"/>
<wire x1="0.6" y1="-2.54" x2="0.6" y2="2.54" width="0.4" layer="94"/>
<text x="-3.81" y="3.2" size="1.778" layer="95">&gt;NAME</text>
<text x="-3.81" y="-5.4" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
<pin name="2" x="5.08" y="0" length="short" direction="pas" rot="R180"/>
</symbol>
<symbol name="POT">
<wire x1="-3.81" y1="-1.016" x2="3.81" y2="-1.016" width="0.254" layer="94"/>
<wire x1="3.81" y1="-1.016" x2="3.81" y2="1.016" width="0.254" layer="94"/>
<wire x1="3.81" y1="1.016" x2="-3.81" y2="1.016" width="0.254" layer="94"/>
<wire x1="-3.81" y1="1.016" x2="-3.81" y2="-1.016" width="0.254" layer="94"/>
<wire x1="0" y1="-2.54" x2="0" y2="-1.016" width="0.254" layer="94"/>
<text x="-5.08" y="2.2" size="1.778" layer="95">&gt;NAME</text>
<text x="-5.08" y="-7.4" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-7.62" y="0" length="short" direction="pas"/>
<pin name="3" x="7.62" y="0" length="short" direction="pas" rot="R180"/>
<pin name="2" x="0" y="-5.08" length="short" direction="pas" rot="R90"/>
</symbol>
<symbol name="HDR1">
<wire x1="-2.54" y1="-1.27" x2="2.54" y2="-1.27" width="0.254" layer="94"/>
<wire x1="2.54" y1="-1.27" x2="2.54" y2="1.27" width="0.254" layer="94"/>
<wire x1="2.54" y1="1.27" x2="-2.54" y2="1.27" width="0.254" layer="94"/>
<wire x1="-2.54" y1="1.27" x2="-2.54" y2="-1.27" width="0.254" layer="94"/>
<text x="-2.54" y="2.27" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="-5.08" y="0" length="short" direction="pas"/>
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
<deviceset name="LM741" prefix="U">
<gates>
<gate name="G$1" symbol="LM741" x="0" y="0"/>
</gates>
<devices>
<device name="" package="DIL08">
<connects>
<connect gate="G$1" pin="OFFSET1" pad="1"/>
<connect gate="G$1" pin="IN-" pad="2"/>
<connect gate="G$1" pin="IN+" pad="3"/>
<connect gate="G$1" pin="V-" pad="4"/>
<connect gate="G$1" pin="OFFSET2" pad="5"/>
<connect gate="G$1" pin="OUT" pad="6"/>
<connect gate="G$1" pin="V+" pad="7"/>
<connect gate="G$1" pin="NC" pad="8"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="R" prefix="R">
<gates>
<gate name="G$1" symbol="R" x="0" y="0"/>
</gates>
<devices>
<device name="" package="RES">
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
<gate name="G$1" symbol="C" x="0" y="0"/>
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
<deviceset name="POT" prefix="RV">
<gates>
<gate name="G$1" symbol="POT" x="0" y="0"/>
</gates>
<devices>
<device name="" package="POT">
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
<deviceset name="HDR1" prefix="J">
<gates>
<gate name="G$1" symbol="HDR1" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR1">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="HDR2" prefix="J">
<gates>
<gate name="G$1" symbol="HDR2" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR2">
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
<deviceset name="HDR4" prefix="J">
<gates>
<gate name="G$1" symbol="HDR4" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDR4">
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
<part name="P1_U1" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P1_U2" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P1_U3" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P1_U4" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P1_U5" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P1_U6" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P1_U7" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P1_R1" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_R2" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_R3" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_R4" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_R5" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_R6" library="pid4" deviceset="R" device="" value="1k"/>
<part name="P1_R7" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_R8" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_R9" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_ROFFSET" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P1_R10" library="pid4" deviceset="R" device="" value="1k"/>
<part name="P1_RBIAS" library="pid4" deviceset="R" device="" value="4.4k"/>
<part name="P1_R11" library="pid4" deviceset="R" device="" value="1M"/>
<part name="P1_R12" library="pid4" deviceset="R" device="" value="160k"/>
<part name="P1_R13" library="pid4" deviceset="R" device="" value="240k"/>
<part name="P1_R14" library="pid4" deviceset="R" device="" value="96k"/>
<part name="P1_R15" library="pid4" deviceset="R" device="" value="160k"/>
<part name="P1_POT1" library="pid4" deviceset="POT" device="" value="22k"/>
<part name="P1_POT2" library="pid4" deviceset="POT" device="" value="220k"/>
<part name="P1_POT3" library="pid4" deviceset="POT" device="" value="22k"/>
<part name="P1_C1" library="pid4" deviceset="C" device="" value="1u"/>
<part name="P1_C2" library="pid4" deviceset="C" device="" value="1u"/>
<part name="P1_J_IN" library="pid4" deviceset="HDR1" device="" value="VSENSOR"/>
<part name="P1_J_OUT" library="pid4" deviceset="HDR1" device="" value="VPID"/>
<part name="P1_J_PWR" library="pid4" deviceset="HDR4" device="" value="PWR"/>
<part name="P2_U1" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P2_U2" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P2_U3" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P2_U4" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P2_U5" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P2_U6" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P2_U7" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P2_R1" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_R2" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_R3" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_R4" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_R5" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_R6" library="pid4" deviceset="R" device="" value="1k"/>
<part name="P2_R7" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_R8" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_R9" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_ROFFSET" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P2_R10" library="pid4" deviceset="R" device="" value="1k"/>
<part name="P2_RBIAS" library="pid4" deviceset="R" device="" value="4.4k"/>
<part name="P2_R11" library="pid4" deviceset="R" device="" value="1M"/>
<part name="P2_R12" library="pid4" deviceset="R" device="" value="160k"/>
<part name="P2_R13" library="pid4" deviceset="R" device="" value="240k"/>
<part name="P2_R14" library="pid4" deviceset="R" device="" value="96k"/>
<part name="P2_R15" library="pid4" deviceset="R" device="" value="160k"/>
<part name="P2_POT1" library="pid4" deviceset="POT" device="" value="22k"/>
<part name="P2_POT2" library="pid4" deviceset="POT" device="" value="220k"/>
<part name="P2_POT3" library="pid4" deviceset="POT" device="" value="22k"/>
<part name="P2_C1" library="pid4" deviceset="C" device="" value="1u"/>
<part name="P2_C2" library="pid4" deviceset="C" device="" value="1u"/>
<part name="P2_J_IN" library="pid4" deviceset="HDR1" device="" value="VSENSOR"/>
<part name="P2_J_OUT" library="pid4" deviceset="HDR1" device="" value="VPID"/>
<part name="P2_J_PWR" library="pid4" deviceset="HDR4" device="" value="PWR"/>
<part name="P3_U1" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P3_U2" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P3_U3" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P3_U4" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P3_U5" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P3_U6" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P3_U7" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P3_R1" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_R2" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_R3" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_R4" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_R5" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_R6" library="pid4" deviceset="R" device="" value="1k"/>
<part name="P3_R7" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_R8" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_R9" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_ROFFSET" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P3_R10" library="pid4" deviceset="R" device="" value="1k"/>
<part name="P3_RBIAS" library="pid4" deviceset="R" device="" value="4.4k"/>
<part name="P3_R11" library="pid4" deviceset="R" device="" value="1M"/>
<part name="P3_R12" library="pid4" deviceset="R" device="" value="160k"/>
<part name="P3_R13" library="pid4" deviceset="R" device="" value="240k"/>
<part name="P3_R14" library="pid4" deviceset="R" device="" value="96k"/>
<part name="P3_R15" library="pid4" deviceset="R" device="" value="160k"/>
<part name="P3_POT1" library="pid4" deviceset="POT" device="" value="22k"/>
<part name="P3_POT2" library="pid4" deviceset="POT" device="" value="220k"/>
<part name="P3_POT3" library="pid4" deviceset="POT" device="" value="22k"/>
<part name="P3_C1" library="pid4" deviceset="C" device="" value="1u"/>
<part name="P3_C2" library="pid4" deviceset="C" device="" value="1u"/>
<part name="P3_J_IN" library="pid4" deviceset="HDR1" device="" value="VSENSOR"/>
<part name="P3_J_OUT" library="pid4" deviceset="HDR1" device="" value="VPID"/>
<part name="P3_J_PWR" library="pid4" deviceset="HDR4" device="" value="PWR"/>
<part name="P4_U1" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P4_U2" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P4_U3" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P4_U4" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P4_U5" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P4_U6" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P4_U7" library="pid4" deviceset="LM741" device="" value="LM741"/>
<part name="P4_R1" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_R2" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_R3" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_R4" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_R5" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_R6" library="pid4" deviceset="R" device="" value="1k"/>
<part name="P4_R7" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_R8" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_R9" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_ROFFSET" library="pid4" deviceset="R" device="" value="10k"/>
<part name="P4_R10" library="pid4" deviceset="R" device="" value="1k"/>
<part name="P4_RBIAS" library="pid4" deviceset="R" device="" value="4.4k"/>
<part name="P4_R11" library="pid4" deviceset="R" device="" value="1M"/>
<part name="P4_R12" library="pid4" deviceset="R" device="" value="160k"/>
<part name="P4_R13" library="pid4" deviceset="R" device="" value="240k"/>
<part name="P4_R14" library="pid4" deviceset="R" device="" value="96k"/>
<part name="P4_R15" library="pid4" deviceset="R" device="" value="160k"/>
<part name="P4_POT1" library="pid4" deviceset="POT" device="" value="22k"/>
<part name="P4_POT2" library="pid4" deviceset="POT" device="" value="220k"/>
<part name="P4_POT3" library="pid4" deviceset="POT" device="" value="22k"/>
<part name="P4_C1" library="pid4" deviceset="C" device="" value="1u"/>
<part name="P4_C2" library="pid4" deviceset="C" device="" value="1u"/>
<part name="P4_J_IN" library="pid4" deviceset="HDR1" device="" value="VSENSOR"/>
<part name="P4_J_OUT" library="pid4" deviceset="HDR1" device="" value="VPID"/>
<part name="P4_J_PWR" library="pid4" deviceset="HDR4" device="" value="PWR"/>
</parts>
<sheets>
<sheet>
<plain>
<text x="20" y="8" size="3.81" layer="97">Módulo PID 1: controlador PID analógico (7 x LM741)</text>
</plain>
<instances>
<instance part="P1_U6" gate="G$1" x="20.32" y="-15.24"/>
<instance part="P1_R12" gate="G$1" x="93.98" y="-15.24"/>
<instance part="P1_R13" gate="G$1" x="154.94" y="-15.24"/>
<instance part="P1_U1" gate="G$1" x="20.32" y="-48.26"/>
<instance part="P1_R1" gate="G$1" x="93.98" y="-48.26"/>
<instance part="P1_R2" gate="G$1" x="154.94" y="-48.26"/>
<instance part="P1_R3" gate="G$1" x="218.44" y="-48.26"/>
<instance part="P1_R4" gate="G$1" x="279.4" y="-48.26"/>
<instance part="P1_U2" gate="G$1" x="20.32" y="-81.28"/>
<instance part="P1_R5" gate="G$1" x="93.98" y="-81.28"/>
<instance part="P1_POT1" gate="G$1" x="154.94" y="-81.28"/>
<instance part="P1_R7" gate="G$1" x="218.44" y="-81.28"/>
<instance part="P1_U3" gate="G$1" x="20.32" y="-116.84"/>
<instance part="P1_POT2" gate="G$1" x="93.98" y="-116.84"/>
<instance part="P1_C1" gate="G$1" x="154.94" y="-116.84"/>
<instance part="P1_R11" gate="G$1" x="218.44" y="-116.84"/>
<instance part="P1_R8" gate="G$1" x="279.4" y="-116.84"/>
<instance part="P1_U4" gate="G$1" x="20.32" y="-149.86"/>
<instance part="P1_R6" gate="G$1" x="93.98" y="-149.86"/>
<instance part="P1_C2" gate="G$1" x="154.94" y="-149.86"/>
<instance part="P1_POT3" gate="G$1" x="218.44" y="-149.86"/>
<instance part="P1_R9" gate="G$1" x="279.4" y="-149.86"/>
<instance part="P1_U5" gate="G$1" x="20.32" y="-182.88"/>
<instance part="P1_ROFFSET" gate="G$1" x="93.98" y="-182.88"/>
<instance part="P1_R10" gate="G$1" x="154.94" y="-182.88"/>
<instance part="P1_RBIAS" gate="G$1" x="218.44" y="-182.88"/>
<instance part="P1_U7" gate="G$1" x="20.32" y="-218.44"/>
<instance part="P1_R14" gate="G$1" x="93.98" y="-218.44"/>
<instance part="P1_R15" gate="G$1" x="154.94" y="-218.44"/>
<instance part="P1_J_IN" gate="G$1" x="33.02" y="-251.46"/>
<instance part="P1_J_OUT" gate="G$1" x="93.98" y="-251.46"/>
<instance part="P1_J_PWR" gate="G$1" x="154.94" y="-251.46"/>
</instances>
<busses>
</busses>
<nets>
<net name="+16V" class="0">
<segment>
<pinref part="P1_U1" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-43.18" x2="43.18" y2="-43.18" width="0.1524" layer="91"/>
<label x="30.48" y="-43.18" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U2" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-76.2" x2="43.18" y2="-76.2" width="0.1524" layer="91"/>
<label x="30.48" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U3" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-111.76" x2="43.18" y2="-111.76" width="0.1524" layer="91"/>
<label x="30.48" y="-111.76" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U4" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-144.78" x2="43.18" y2="-144.78" width="0.1524" layer="91"/>
<label x="30.48" y="-144.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U5" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-177.8" x2="43.18" y2="-177.8" width="0.1524" layer="91"/>
<label x="30.48" y="-177.8" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U6" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-10.16" x2="43.18" y2="-10.16" width="0.1524" layer="91"/>
<label x="30.48" y="-10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U7" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-213.36" x2="43.18" y2="-213.36" width="0.1524" layer="91"/>
<label x="30.48" y="-213.36" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_J_PWR" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-251.46" x2="137.16" y2="-251.46" width="0.1524" layer="91"/>
<label x="137.16" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="-16V" class="0">
<segment>
<pinref part="P1_U1" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-50.8" x2="-2.54" y2="-50.8" width="0.1524" layer="91"/>
<label x="-2.54" y="-50.8" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U2" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-83.82" x2="-2.54" y2="-83.82" width="0.1524" layer="91"/>
<label x="-2.54" y="-83.82" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U3" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-119.38" x2="-2.54" y2="-119.38" width="0.1524" layer="91"/>
<label x="-2.54" y="-119.38" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U4" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-152.4" x2="-2.54" y2="-152.4" width="0.1524" layer="91"/>
<label x="-2.54" y="-152.4" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U5" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-185.42" x2="-2.54" y2="-185.42" width="0.1524" layer="91"/>
<label x="-2.54" y="-185.42" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U6" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-17.78" x2="-2.54" y2="-17.78" width="0.1524" layer="91"/>
<label x="-2.54" y="-17.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U7" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-220.98" x2="-2.54" y2="-220.98" width="0.1524" layer="91"/>
<label x="-2.54" y="-220.98" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R14" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-218.44" x2="76.2" y2="-218.44" width="0.1524" layer="91"/>
<label x="76.2" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_J_PWR" gate="G$1" pin="2"/>
<wire x1="149.86" y1="-254" x2="137.16" y2="-254" width="0.1524" layer="91"/>
<label x="137.16" y="-254" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VREFD" class="0">
<segment>
<pinref part="P1_R12" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-15.24" x2="76.2" y2="-15.24" width="0.1524" layer="91"/>
<label x="76.2" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R13" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-15.24" x2="137.16" y2="-15.24" width="0.1524" layer="91"/>
<label x="137.16" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U6" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-15.24" x2="-2.54" y2="-15.24" width="0.1524" layer="91"/>
<label x="-2.54" y="-15.24" size="1.27" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="P1_R12" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-15.24" x2="111.76" y2="-15.24" width="0.1524" layer="91"/>
<label x="99.06" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R4" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-48.26" x2="297.18" y2="-48.26" width="0.1524" layer="91"/>
<label x="284.48" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U2" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-81.28" x2="-2.54" y2="-81.28" width="0.1524" layer="91"/>
<label x="-2.54" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U3" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-116.84" x2="-2.54" y2="-116.84" width="0.1524" layer="91"/>
<label x="-2.54" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U4" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-149.86" x2="-2.54" y2="-149.86" width="0.1524" layer="91"/>
<label x="-2.54" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_RBIAS" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-182.88" x2="236.22" y2="-182.88" width="0.1524" layer="91"/>
<label x="223.52" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R15" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-218.44" x2="172.72" y2="-218.44" width="0.1524" layer="91"/>
<label x="160.02" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_J_PWR" gate="G$1" pin="3"/>
<wire x1="149.86" y1="-256.54" x2="137.16" y2="-256.54" width="0.1524" layer="91"/>
<label x="137.16" y="-256.54" size="1.27" layer="95"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<pinref part="P1_R13" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-15.24" x2="172.72" y2="-15.24" width="0.1524" layer="91"/>
<label x="160.02" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_J_PWR" gate="G$1" pin="4"/>
<wire x1="149.86" y1="-259.08" x2="137.16" y2="-259.08" width="0.1524" layer="91"/>
<label x="137.16" y="-259.08" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VREF" class="0">
<segment>
<pinref part="P1_U6" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-12.7" x2="43.18" y2="-12.7" width="0.1524" layer="91"/>
<label x="30.48" y="-12.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U6" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-12.7" x2="-2.54" y2="-12.7" width="0.1524" layer="91"/>
<label x="-2.54" y="-12.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R1" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-48.26" x2="76.2" y2="-48.26" width="0.1524" layer="91"/>
<label x="76.2" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_U1N" class="0">
<segment>
<pinref part="P1_R1" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-48.26" x2="111.76" y2="-48.26" width="0.1524" layer="91"/>
<label x="99.06" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R2" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-48.26" x2="137.16" y2="-48.26" width="0.1524" layer="91"/>
<label x="137.16" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U1" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-45.72" x2="-2.54" y2="-45.72" width="0.1524" layer="91"/>
<label x="-2.54" y="-45.72" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VSEN" class="0">
<segment>
<pinref part="P1_R3" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-48.26" x2="200.66" y2="-48.26" width="0.1524" layer="91"/>
<label x="200.66" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_J_IN" gate="G$1" pin="1"/>
<wire x1="27.94" y1="-251.46" x2="15.24" y2="-251.46" width="0.1524" layer="91"/>
<label x="15.24" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_U1P" class="0">
<segment>
<pinref part="P1_R3" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-48.26" x2="236.22" y2="-48.26" width="0.1524" layer="91"/>
<label x="223.52" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R4" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-48.26" x2="261.62" y2="-48.26" width="0.1524" layer="91"/>
<label x="261.62" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U1" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-48.26" x2="-2.54" y2="-48.26" width="0.1524" layer="91"/>
<label x="-2.54" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VE" class="0">
<segment>
<pinref part="P1_U1" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-45.72" x2="43.18" y2="-45.72" width="0.1524" layer="91"/>
<label x="30.48" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R2" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-48.26" x2="172.72" y2="-48.26" width="0.1524" layer="91"/>
<label x="160.02" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R5" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-81.28" x2="76.2" y2="-81.28" width="0.1524" layer="91"/>
<label x="76.2" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_POT2" gate="G$1" pin="1"/>
<wire x1="86.36" y1="-116.84" x2="73.66" y2="-116.84" width="0.1524" layer="91"/>
<label x="73.66" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R6" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-149.86" x2="76.2" y2="-149.86" width="0.1524" layer="91"/>
<label x="76.2" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_U2N" class="0">
<segment>
<pinref part="P1_R5" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-81.28" x2="111.76" y2="-81.28" width="0.1524" layer="91"/>
<label x="99.06" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_POT1" gate="G$1" pin="1"/>
<wire x1="147.32" y1="-81.28" x2="134.62" y2="-81.28" width="0.1524" layer="91"/>
<label x="134.62" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U2" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-78.74" x2="-2.54" y2="-78.74" width="0.1524" layer="91"/>
<label x="-2.54" y="-78.74" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VP" class="0">
<segment>
<pinref part="P1_U2" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-78.74" x2="43.18" y2="-78.74" width="0.1524" layer="91"/>
<label x="30.48" y="-78.74" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_POT1" gate="G$1" pin="2"/>
<wire x1="154.94" y1="-86.36" x2="154.94" y2="-91.44" width="0.1524" layer="91"/>
<label x="154.94" y="-91.44" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P1_POT1" gate="G$1" pin="3"/>
<wire x1="162.56" y1="-81.28" x2="175.26" y2="-81.28" width="0.1524" layer="91"/>
<label x="162.56" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R7" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-81.28" x2="200.66" y2="-81.28" width="0.1524" layer="91"/>
<label x="200.66" y="-81.28" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_U3N" class="0">
<segment>
<pinref part="P1_POT2" gate="G$1" pin="2"/>
<wire x1="93.98" y1="-121.92" x2="93.98" y2="-127" width="0.1524" layer="91"/>
<label x="93.98" y="-127" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P1_POT2" gate="G$1" pin="3"/>
<wire x1="101.6" y1="-116.84" x2="114.3" y2="-116.84" width="0.1524" layer="91"/>
<label x="101.6" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_C1" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-116.84" x2="137.16" y2="-116.84" width="0.1524" layer="91"/>
<label x="137.16" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R11" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-116.84" x2="200.66" y2="-116.84" width="0.1524" layer="91"/>
<label x="200.66" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U3" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-114.3" x2="-2.54" y2="-114.3" width="0.1524" layer="91"/>
<label x="-2.54" y="-114.3" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VI" class="0">
<segment>
<pinref part="P1_U3" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-114.3" x2="43.18" y2="-114.3" width="0.1524" layer="91"/>
<label x="30.48" y="-114.3" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_C1" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-116.84" x2="172.72" y2="-116.84" width="0.1524" layer="91"/>
<label x="160.02" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R11" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-116.84" x2="236.22" y2="-116.84" width="0.1524" layer="91"/>
<label x="223.52" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R8" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-116.84" x2="261.62" y2="-116.84" width="0.1524" layer="91"/>
<label x="261.62" y="-116.84" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_R6C2" class="0">
<segment>
<pinref part="P1_R6" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-149.86" x2="111.76" y2="-149.86" width="0.1524" layer="91"/>
<label x="99.06" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_C2" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-149.86" x2="137.16" y2="-149.86" width="0.1524" layer="91"/>
<label x="137.16" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_U4N" class="0">
<segment>
<pinref part="P1_C2" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-149.86" x2="172.72" y2="-149.86" width="0.1524" layer="91"/>
<label x="160.02" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_POT3" gate="G$1" pin="1"/>
<wire x1="210.82" y1="-149.86" x2="198.12" y2="-149.86" width="0.1524" layer="91"/>
<label x="198.12" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U4" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-147.32" x2="-2.54" y2="-147.32" width="0.1524" layer="91"/>
<label x="-2.54" y="-147.32" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VD" class="0">
<segment>
<pinref part="P1_U4" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-147.32" x2="43.18" y2="-147.32" width="0.1524" layer="91"/>
<label x="30.48" y="-147.32" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_POT3" gate="G$1" pin="2"/>
<wire x1="218.44" y1="-154.94" x2="218.44" y2="-160.02" width="0.1524" layer="91"/>
<label x="218.44" y="-160.02" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P1_POT3" gate="G$1" pin="3"/>
<wire x1="226.06" y1="-149.86" x2="238.76" y2="-149.86" width="0.1524" layer="91"/>
<label x="226.06" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R9" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-149.86" x2="261.62" y2="-149.86" width="0.1524" layer="91"/>
<label x="261.62" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_SUMN" class="0">
<segment>
<pinref part="P1_R7" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-81.28" x2="236.22" y2="-81.28" width="0.1524" layer="91"/>
<label x="223.52" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R8" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-116.84" x2="297.18" y2="-116.84" width="0.1524" layer="91"/>
<label x="284.48" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R9" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-149.86" x2="297.18" y2="-149.86" width="0.1524" layer="91"/>
<label x="284.48" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_ROFFSET" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-182.88" x2="111.76" y2="-182.88" width="0.1524" layer="91"/>
<label x="99.06" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R10" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-182.88" x2="137.16" y2="-182.88" width="0.1524" layer="91"/>
<label x="137.16" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U5" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-180.34" x2="-2.54" y2="-180.34" width="0.1524" layer="91"/>
<label x="-2.54" y="-180.34" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_U5P" class="0">
<segment>
<pinref part="P1_U5" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-182.88" x2="-2.54" y2="-182.88" width="0.1524" layer="91"/>
<label x="-2.54" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_RBIAS" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-182.88" x2="200.66" y2="-182.88" width="0.1524" layer="91"/>
<label x="200.66" y="-182.88" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VPID" class="0">
<segment>
<pinref part="P1_U5" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-180.34" x2="43.18" y2="-180.34" width="0.1524" layer="91"/>
<label x="30.48" y="-180.34" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R10" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-182.88" x2="172.72" y2="-182.88" width="0.1524" layer="91"/>
<label x="160.02" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_J_OUT" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-251.46" x2="76.2" y2="-251.46" width="0.1524" layer="91"/>
<label x="76.2" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VOFFD" class="0">
<segment>
<pinref part="P1_R14" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-218.44" x2="111.76" y2="-218.44" width="0.1524" layer="91"/>
<label x="99.06" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_R15" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-218.44" x2="137.16" y2="-218.44" width="0.1524" layer="91"/>
<label x="137.16" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U7" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-218.44" x2="-2.54" y2="-218.44" width="0.1524" layer="91"/>
<label x="-2.54" y="-218.44" size="1.27" layer="95"/>
</segment>
</net>
<net name="P1_VOFF" class="0">
<segment>
<pinref part="P1_U7" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-215.9" x2="43.18" y2="-215.9" width="0.1524" layer="91"/>
<label x="30.48" y="-215.9" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_U7" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-215.9" x2="-2.54" y2="-215.9" width="0.1524" layer="91"/>
<label x="-2.54" y="-215.9" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P1_ROFFSET" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-182.88" x2="76.2" y2="-182.88" width="0.1524" layer="91"/>
<label x="76.2" y="-182.88" size="1.27" layer="95"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<plain>
<text x="20" y="8" size="3.81" layer="97">Módulo PID 2: controlador PID analógico (7 x LM741)</text>
</plain>
<instances>
<instance part="P2_U6" gate="G$1" x="20.32" y="-15.24"/>
<instance part="P2_R12" gate="G$1" x="93.98" y="-15.24"/>
<instance part="P2_R13" gate="G$1" x="154.94" y="-15.24"/>
<instance part="P2_U1" gate="G$1" x="20.32" y="-48.26"/>
<instance part="P2_R1" gate="G$1" x="93.98" y="-48.26"/>
<instance part="P2_R2" gate="G$1" x="154.94" y="-48.26"/>
<instance part="P2_R3" gate="G$1" x="218.44" y="-48.26"/>
<instance part="P2_R4" gate="G$1" x="279.4" y="-48.26"/>
<instance part="P2_U2" gate="G$1" x="20.32" y="-81.28"/>
<instance part="P2_R5" gate="G$1" x="93.98" y="-81.28"/>
<instance part="P2_POT1" gate="G$1" x="154.94" y="-81.28"/>
<instance part="P2_R7" gate="G$1" x="218.44" y="-81.28"/>
<instance part="P2_U3" gate="G$1" x="20.32" y="-116.84"/>
<instance part="P2_POT2" gate="G$1" x="93.98" y="-116.84"/>
<instance part="P2_C1" gate="G$1" x="154.94" y="-116.84"/>
<instance part="P2_R11" gate="G$1" x="218.44" y="-116.84"/>
<instance part="P2_R8" gate="G$1" x="279.4" y="-116.84"/>
<instance part="P2_U4" gate="G$1" x="20.32" y="-149.86"/>
<instance part="P2_R6" gate="G$1" x="93.98" y="-149.86"/>
<instance part="P2_C2" gate="G$1" x="154.94" y="-149.86"/>
<instance part="P2_POT3" gate="G$1" x="218.44" y="-149.86"/>
<instance part="P2_R9" gate="G$1" x="279.4" y="-149.86"/>
<instance part="P2_U5" gate="G$1" x="20.32" y="-182.88"/>
<instance part="P2_ROFFSET" gate="G$1" x="93.98" y="-182.88"/>
<instance part="P2_R10" gate="G$1" x="154.94" y="-182.88"/>
<instance part="P2_RBIAS" gate="G$1" x="218.44" y="-182.88"/>
<instance part="P2_U7" gate="G$1" x="20.32" y="-218.44"/>
<instance part="P2_R14" gate="G$1" x="93.98" y="-218.44"/>
<instance part="P2_R15" gate="G$1" x="154.94" y="-218.44"/>
<instance part="P2_J_IN" gate="G$1" x="33.02" y="-251.46"/>
<instance part="P2_J_OUT" gate="G$1" x="93.98" y="-251.46"/>
<instance part="P2_J_PWR" gate="G$1" x="154.94" y="-251.46"/>
</instances>
<busses>
</busses>
<nets>
<net name="+16V" class="0">
<segment>
<pinref part="P2_U1" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-43.18" x2="43.18" y2="-43.18" width="0.1524" layer="91"/>
<label x="30.48" y="-43.18" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U2" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-76.2" x2="43.18" y2="-76.2" width="0.1524" layer="91"/>
<label x="30.48" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U3" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-111.76" x2="43.18" y2="-111.76" width="0.1524" layer="91"/>
<label x="30.48" y="-111.76" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U4" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-144.78" x2="43.18" y2="-144.78" width="0.1524" layer="91"/>
<label x="30.48" y="-144.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U5" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-177.8" x2="43.18" y2="-177.8" width="0.1524" layer="91"/>
<label x="30.48" y="-177.8" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U6" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-10.16" x2="43.18" y2="-10.16" width="0.1524" layer="91"/>
<label x="30.48" y="-10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U7" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-213.36" x2="43.18" y2="-213.36" width="0.1524" layer="91"/>
<label x="30.48" y="-213.36" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_J_PWR" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-251.46" x2="137.16" y2="-251.46" width="0.1524" layer="91"/>
<label x="137.16" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="-16V" class="0">
<segment>
<pinref part="P2_U1" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-50.8" x2="-2.54" y2="-50.8" width="0.1524" layer="91"/>
<label x="-2.54" y="-50.8" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U2" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-83.82" x2="-2.54" y2="-83.82" width="0.1524" layer="91"/>
<label x="-2.54" y="-83.82" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U3" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-119.38" x2="-2.54" y2="-119.38" width="0.1524" layer="91"/>
<label x="-2.54" y="-119.38" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U4" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-152.4" x2="-2.54" y2="-152.4" width="0.1524" layer="91"/>
<label x="-2.54" y="-152.4" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U5" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-185.42" x2="-2.54" y2="-185.42" width="0.1524" layer="91"/>
<label x="-2.54" y="-185.42" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U6" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-17.78" x2="-2.54" y2="-17.78" width="0.1524" layer="91"/>
<label x="-2.54" y="-17.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U7" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-220.98" x2="-2.54" y2="-220.98" width="0.1524" layer="91"/>
<label x="-2.54" y="-220.98" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R14" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-218.44" x2="76.2" y2="-218.44" width="0.1524" layer="91"/>
<label x="76.2" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_J_PWR" gate="G$1" pin="2"/>
<wire x1="149.86" y1="-254" x2="137.16" y2="-254" width="0.1524" layer="91"/>
<label x="137.16" y="-254" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VREFD" class="0">
<segment>
<pinref part="P2_R12" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-15.24" x2="76.2" y2="-15.24" width="0.1524" layer="91"/>
<label x="76.2" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R13" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-15.24" x2="137.16" y2="-15.24" width="0.1524" layer="91"/>
<label x="137.16" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U6" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-15.24" x2="-2.54" y2="-15.24" width="0.1524" layer="91"/>
<label x="-2.54" y="-15.24" size="1.27" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="P2_R12" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-15.24" x2="111.76" y2="-15.24" width="0.1524" layer="91"/>
<label x="99.06" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R4" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-48.26" x2="297.18" y2="-48.26" width="0.1524" layer="91"/>
<label x="284.48" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U2" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-81.28" x2="-2.54" y2="-81.28" width="0.1524" layer="91"/>
<label x="-2.54" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U3" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-116.84" x2="-2.54" y2="-116.84" width="0.1524" layer="91"/>
<label x="-2.54" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U4" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-149.86" x2="-2.54" y2="-149.86" width="0.1524" layer="91"/>
<label x="-2.54" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_RBIAS" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-182.88" x2="236.22" y2="-182.88" width="0.1524" layer="91"/>
<label x="223.52" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R15" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-218.44" x2="172.72" y2="-218.44" width="0.1524" layer="91"/>
<label x="160.02" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_J_PWR" gate="G$1" pin="3"/>
<wire x1="149.86" y1="-256.54" x2="137.16" y2="-256.54" width="0.1524" layer="91"/>
<label x="137.16" y="-256.54" size="1.27" layer="95"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<pinref part="P2_R13" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-15.24" x2="172.72" y2="-15.24" width="0.1524" layer="91"/>
<label x="160.02" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_J_PWR" gate="G$1" pin="4"/>
<wire x1="149.86" y1="-259.08" x2="137.16" y2="-259.08" width="0.1524" layer="91"/>
<label x="137.16" y="-259.08" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VREF" class="0">
<segment>
<pinref part="P2_U6" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-12.7" x2="43.18" y2="-12.7" width="0.1524" layer="91"/>
<label x="30.48" y="-12.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U6" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-12.7" x2="-2.54" y2="-12.7" width="0.1524" layer="91"/>
<label x="-2.54" y="-12.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R1" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-48.26" x2="76.2" y2="-48.26" width="0.1524" layer="91"/>
<label x="76.2" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_U1N" class="0">
<segment>
<pinref part="P2_R1" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-48.26" x2="111.76" y2="-48.26" width="0.1524" layer="91"/>
<label x="99.06" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R2" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-48.26" x2="137.16" y2="-48.26" width="0.1524" layer="91"/>
<label x="137.16" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U1" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-45.72" x2="-2.54" y2="-45.72" width="0.1524" layer="91"/>
<label x="-2.54" y="-45.72" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VSEN" class="0">
<segment>
<pinref part="P2_R3" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-48.26" x2="200.66" y2="-48.26" width="0.1524" layer="91"/>
<label x="200.66" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_J_IN" gate="G$1" pin="1"/>
<wire x1="27.94" y1="-251.46" x2="15.24" y2="-251.46" width="0.1524" layer="91"/>
<label x="15.24" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_U1P" class="0">
<segment>
<pinref part="P2_R3" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-48.26" x2="236.22" y2="-48.26" width="0.1524" layer="91"/>
<label x="223.52" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R4" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-48.26" x2="261.62" y2="-48.26" width="0.1524" layer="91"/>
<label x="261.62" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U1" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-48.26" x2="-2.54" y2="-48.26" width="0.1524" layer="91"/>
<label x="-2.54" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VE" class="0">
<segment>
<pinref part="P2_U1" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-45.72" x2="43.18" y2="-45.72" width="0.1524" layer="91"/>
<label x="30.48" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R2" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-48.26" x2="172.72" y2="-48.26" width="0.1524" layer="91"/>
<label x="160.02" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R5" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-81.28" x2="76.2" y2="-81.28" width="0.1524" layer="91"/>
<label x="76.2" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_POT2" gate="G$1" pin="1"/>
<wire x1="86.36" y1="-116.84" x2="73.66" y2="-116.84" width="0.1524" layer="91"/>
<label x="73.66" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R6" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-149.86" x2="76.2" y2="-149.86" width="0.1524" layer="91"/>
<label x="76.2" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_U2N" class="0">
<segment>
<pinref part="P2_R5" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-81.28" x2="111.76" y2="-81.28" width="0.1524" layer="91"/>
<label x="99.06" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_POT1" gate="G$1" pin="1"/>
<wire x1="147.32" y1="-81.28" x2="134.62" y2="-81.28" width="0.1524" layer="91"/>
<label x="134.62" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U2" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-78.74" x2="-2.54" y2="-78.74" width="0.1524" layer="91"/>
<label x="-2.54" y="-78.74" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VP" class="0">
<segment>
<pinref part="P2_U2" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-78.74" x2="43.18" y2="-78.74" width="0.1524" layer="91"/>
<label x="30.48" y="-78.74" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_POT1" gate="G$1" pin="2"/>
<wire x1="154.94" y1="-86.36" x2="154.94" y2="-91.44" width="0.1524" layer="91"/>
<label x="154.94" y="-91.44" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P2_POT1" gate="G$1" pin="3"/>
<wire x1="162.56" y1="-81.28" x2="175.26" y2="-81.28" width="0.1524" layer="91"/>
<label x="162.56" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R7" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-81.28" x2="200.66" y2="-81.28" width="0.1524" layer="91"/>
<label x="200.66" y="-81.28" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_U3N" class="0">
<segment>
<pinref part="P2_POT2" gate="G$1" pin="2"/>
<wire x1="93.98" y1="-121.92" x2="93.98" y2="-127" width="0.1524" layer="91"/>
<label x="93.98" y="-127" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P2_POT2" gate="G$1" pin="3"/>
<wire x1="101.6" y1="-116.84" x2="114.3" y2="-116.84" width="0.1524" layer="91"/>
<label x="101.6" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_C1" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-116.84" x2="137.16" y2="-116.84" width="0.1524" layer="91"/>
<label x="137.16" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R11" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-116.84" x2="200.66" y2="-116.84" width="0.1524" layer="91"/>
<label x="200.66" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U3" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-114.3" x2="-2.54" y2="-114.3" width="0.1524" layer="91"/>
<label x="-2.54" y="-114.3" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VI" class="0">
<segment>
<pinref part="P2_U3" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-114.3" x2="43.18" y2="-114.3" width="0.1524" layer="91"/>
<label x="30.48" y="-114.3" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_C1" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-116.84" x2="172.72" y2="-116.84" width="0.1524" layer="91"/>
<label x="160.02" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R11" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-116.84" x2="236.22" y2="-116.84" width="0.1524" layer="91"/>
<label x="223.52" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R8" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-116.84" x2="261.62" y2="-116.84" width="0.1524" layer="91"/>
<label x="261.62" y="-116.84" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_R6C2" class="0">
<segment>
<pinref part="P2_R6" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-149.86" x2="111.76" y2="-149.86" width="0.1524" layer="91"/>
<label x="99.06" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_C2" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-149.86" x2="137.16" y2="-149.86" width="0.1524" layer="91"/>
<label x="137.16" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_U4N" class="0">
<segment>
<pinref part="P2_C2" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-149.86" x2="172.72" y2="-149.86" width="0.1524" layer="91"/>
<label x="160.02" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_POT3" gate="G$1" pin="1"/>
<wire x1="210.82" y1="-149.86" x2="198.12" y2="-149.86" width="0.1524" layer="91"/>
<label x="198.12" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U4" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-147.32" x2="-2.54" y2="-147.32" width="0.1524" layer="91"/>
<label x="-2.54" y="-147.32" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VD" class="0">
<segment>
<pinref part="P2_U4" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-147.32" x2="43.18" y2="-147.32" width="0.1524" layer="91"/>
<label x="30.48" y="-147.32" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_POT3" gate="G$1" pin="2"/>
<wire x1="218.44" y1="-154.94" x2="218.44" y2="-160.02" width="0.1524" layer="91"/>
<label x="218.44" y="-160.02" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P2_POT3" gate="G$1" pin="3"/>
<wire x1="226.06" y1="-149.86" x2="238.76" y2="-149.86" width="0.1524" layer="91"/>
<label x="226.06" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R9" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-149.86" x2="261.62" y2="-149.86" width="0.1524" layer="91"/>
<label x="261.62" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_SUMN" class="0">
<segment>
<pinref part="P2_R7" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-81.28" x2="236.22" y2="-81.28" width="0.1524" layer="91"/>
<label x="223.52" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R8" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-116.84" x2="297.18" y2="-116.84" width="0.1524" layer="91"/>
<label x="284.48" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R9" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-149.86" x2="297.18" y2="-149.86" width="0.1524" layer="91"/>
<label x="284.48" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_ROFFSET" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-182.88" x2="111.76" y2="-182.88" width="0.1524" layer="91"/>
<label x="99.06" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R10" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-182.88" x2="137.16" y2="-182.88" width="0.1524" layer="91"/>
<label x="137.16" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U5" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-180.34" x2="-2.54" y2="-180.34" width="0.1524" layer="91"/>
<label x="-2.54" y="-180.34" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_U5P" class="0">
<segment>
<pinref part="P2_U5" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-182.88" x2="-2.54" y2="-182.88" width="0.1524" layer="91"/>
<label x="-2.54" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_RBIAS" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-182.88" x2="200.66" y2="-182.88" width="0.1524" layer="91"/>
<label x="200.66" y="-182.88" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VPID" class="0">
<segment>
<pinref part="P2_U5" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-180.34" x2="43.18" y2="-180.34" width="0.1524" layer="91"/>
<label x="30.48" y="-180.34" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R10" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-182.88" x2="172.72" y2="-182.88" width="0.1524" layer="91"/>
<label x="160.02" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_J_OUT" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-251.46" x2="76.2" y2="-251.46" width="0.1524" layer="91"/>
<label x="76.2" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VOFFD" class="0">
<segment>
<pinref part="P2_R14" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-218.44" x2="111.76" y2="-218.44" width="0.1524" layer="91"/>
<label x="99.06" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_R15" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-218.44" x2="137.16" y2="-218.44" width="0.1524" layer="91"/>
<label x="137.16" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U7" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-218.44" x2="-2.54" y2="-218.44" width="0.1524" layer="91"/>
<label x="-2.54" y="-218.44" size="1.27" layer="95"/>
</segment>
</net>
<net name="P2_VOFF" class="0">
<segment>
<pinref part="P2_U7" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-215.9" x2="43.18" y2="-215.9" width="0.1524" layer="91"/>
<label x="30.48" y="-215.9" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_U7" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-215.9" x2="-2.54" y2="-215.9" width="0.1524" layer="91"/>
<label x="-2.54" y="-215.9" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P2_ROFFSET" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-182.88" x2="76.2" y2="-182.88" width="0.1524" layer="91"/>
<label x="76.2" y="-182.88" size="1.27" layer="95"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<plain>
<text x="20" y="8" size="3.81" layer="97">Módulo PID 3: controlador PID analógico (7 x LM741)</text>
</plain>
<instances>
<instance part="P3_U6" gate="G$1" x="20.32" y="-15.24"/>
<instance part="P3_R12" gate="G$1" x="93.98" y="-15.24"/>
<instance part="P3_R13" gate="G$1" x="154.94" y="-15.24"/>
<instance part="P3_U1" gate="G$1" x="20.32" y="-48.26"/>
<instance part="P3_R1" gate="G$1" x="93.98" y="-48.26"/>
<instance part="P3_R2" gate="G$1" x="154.94" y="-48.26"/>
<instance part="P3_R3" gate="G$1" x="218.44" y="-48.26"/>
<instance part="P3_R4" gate="G$1" x="279.4" y="-48.26"/>
<instance part="P3_U2" gate="G$1" x="20.32" y="-81.28"/>
<instance part="P3_R5" gate="G$1" x="93.98" y="-81.28"/>
<instance part="P3_POT1" gate="G$1" x="154.94" y="-81.28"/>
<instance part="P3_R7" gate="G$1" x="218.44" y="-81.28"/>
<instance part="P3_U3" gate="G$1" x="20.32" y="-116.84"/>
<instance part="P3_POT2" gate="G$1" x="93.98" y="-116.84"/>
<instance part="P3_C1" gate="G$1" x="154.94" y="-116.84"/>
<instance part="P3_R11" gate="G$1" x="218.44" y="-116.84"/>
<instance part="P3_R8" gate="G$1" x="279.4" y="-116.84"/>
<instance part="P3_U4" gate="G$1" x="20.32" y="-149.86"/>
<instance part="P3_R6" gate="G$1" x="93.98" y="-149.86"/>
<instance part="P3_C2" gate="G$1" x="154.94" y="-149.86"/>
<instance part="P3_POT3" gate="G$1" x="218.44" y="-149.86"/>
<instance part="P3_R9" gate="G$1" x="279.4" y="-149.86"/>
<instance part="P3_U5" gate="G$1" x="20.32" y="-182.88"/>
<instance part="P3_ROFFSET" gate="G$1" x="93.98" y="-182.88"/>
<instance part="P3_R10" gate="G$1" x="154.94" y="-182.88"/>
<instance part="P3_RBIAS" gate="G$1" x="218.44" y="-182.88"/>
<instance part="P3_U7" gate="G$1" x="20.32" y="-218.44"/>
<instance part="P3_R14" gate="G$1" x="93.98" y="-218.44"/>
<instance part="P3_R15" gate="G$1" x="154.94" y="-218.44"/>
<instance part="P3_J_IN" gate="G$1" x="33.02" y="-251.46"/>
<instance part="P3_J_OUT" gate="G$1" x="93.98" y="-251.46"/>
<instance part="P3_J_PWR" gate="G$1" x="154.94" y="-251.46"/>
</instances>
<busses>
</busses>
<nets>
<net name="+16V" class="0">
<segment>
<pinref part="P3_U1" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-43.18" x2="43.18" y2="-43.18" width="0.1524" layer="91"/>
<label x="30.48" y="-43.18" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U2" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-76.2" x2="43.18" y2="-76.2" width="0.1524" layer="91"/>
<label x="30.48" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U3" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-111.76" x2="43.18" y2="-111.76" width="0.1524" layer="91"/>
<label x="30.48" y="-111.76" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U4" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-144.78" x2="43.18" y2="-144.78" width="0.1524" layer="91"/>
<label x="30.48" y="-144.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U5" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-177.8" x2="43.18" y2="-177.8" width="0.1524" layer="91"/>
<label x="30.48" y="-177.8" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U6" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-10.16" x2="43.18" y2="-10.16" width="0.1524" layer="91"/>
<label x="30.48" y="-10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U7" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-213.36" x2="43.18" y2="-213.36" width="0.1524" layer="91"/>
<label x="30.48" y="-213.36" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_J_PWR" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-251.46" x2="137.16" y2="-251.46" width="0.1524" layer="91"/>
<label x="137.16" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="-16V" class="0">
<segment>
<pinref part="P3_U1" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-50.8" x2="-2.54" y2="-50.8" width="0.1524" layer="91"/>
<label x="-2.54" y="-50.8" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U2" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-83.82" x2="-2.54" y2="-83.82" width="0.1524" layer="91"/>
<label x="-2.54" y="-83.82" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U3" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-119.38" x2="-2.54" y2="-119.38" width="0.1524" layer="91"/>
<label x="-2.54" y="-119.38" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U4" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-152.4" x2="-2.54" y2="-152.4" width="0.1524" layer="91"/>
<label x="-2.54" y="-152.4" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U5" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-185.42" x2="-2.54" y2="-185.42" width="0.1524" layer="91"/>
<label x="-2.54" y="-185.42" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U6" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-17.78" x2="-2.54" y2="-17.78" width="0.1524" layer="91"/>
<label x="-2.54" y="-17.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U7" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-220.98" x2="-2.54" y2="-220.98" width="0.1524" layer="91"/>
<label x="-2.54" y="-220.98" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R14" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-218.44" x2="76.2" y2="-218.44" width="0.1524" layer="91"/>
<label x="76.2" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_J_PWR" gate="G$1" pin="2"/>
<wire x1="149.86" y1="-254" x2="137.16" y2="-254" width="0.1524" layer="91"/>
<label x="137.16" y="-254" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VREFD" class="0">
<segment>
<pinref part="P3_R12" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-15.24" x2="76.2" y2="-15.24" width="0.1524" layer="91"/>
<label x="76.2" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R13" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-15.24" x2="137.16" y2="-15.24" width="0.1524" layer="91"/>
<label x="137.16" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U6" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-15.24" x2="-2.54" y2="-15.24" width="0.1524" layer="91"/>
<label x="-2.54" y="-15.24" size="1.27" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="P3_R12" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-15.24" x2="111.76" y2="-15.24" width="0.1524" layer="91"/>
<label x="99.06" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R4" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-48.26" x2="297.18" y2="-48.26" width="0.1524" layer="91"/>
<label x="284.48" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U2" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-81.28" x2="-2.54" y2="-81.28" width="0.1524" layer="91"/>
<label x="-2.54" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U3" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-116.84" x2="-2.54" y2="-116.84" width="0.1524" layer="91"/>
<label x="-2.54" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U4" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-149.86" x2="-2.54" y2="-149.86" width="0.1524" layer="91"/>
<label x="-2.54" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_RBIAS" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-182.88" x2="236.22" y2="-182.88" width="0.1524" layer="91"/>
<label x="223.52" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R15" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-218.44" x2="172.72" y2="-218.44" width="0.1524" layer="91"/>
<label x="160.02" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_J_PWR" gate="G$1" pin="3"/>
<wire x1="149.86" y1="-256.54" x2="137.16" y2="-256.54" width="0.1524" layer="91"/>
<label x="137.16" y="-256.54" size="1.27" layer="95"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<pinref part="P3_R13" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-15.24" x2="172.72" y2="-15.24" width="0.1524" layer="91"/>
<label x="160.02" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_J_PWR" gate="G$1" pin="4"/>
<wire x1="149.86" y1="-259.08" x2="137.16" y2="-259.08" width="0.1524" layer="91"/>
<label x="137.16" y="-259.08" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VREF" class="0">
<segment>
<pinref part="P3_U6" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-12.7" x2="43.18" y2="-12.7" width="0.1524" layer="91"/>
<label x="30.48" y="-12.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U6" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-12.7" x2="-2.54" y2="-12.7" width="0.1524" layer="91"/>
<label x="-2.54" y="-12.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R1" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-48.26" x2="76.2" y2="-48.26" width="0.1524" layer="91"/>
<label x="76.2" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_U1N" class="0">
<segment>
<pinref part="P3_R1" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-48.26" x2="111.76" y2="-48.26" width="0.1524" layer="91"/>
<label x="99.06" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R2" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-48.26" x2="137.16" y2="-48.26" width="0.1524" layer="91"/>
<label x="137.16" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U1" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-45.72" x2="-2.54" y2="-45.72" width="0.1524" layer="91"/>
<label x="-2.54" y="-45.72" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VSEN" class="0">
<segment>
<pinref part="P3_R3" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-48.26" x2="200.66" y2="-48.26" width="0.1524" layer="91"/>
<label x="200.66" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_J_IN" gate="G$1" pin="1"/>
<wire x1="27.94" y1="-251.46" x2="15.24" y2="-251.46" width="0.1524" layer="91"/>
<label x="15.24" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_U1P" class="0">
<segment>
<pinref part="P3_R3" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-48.26" x2="236.22" y2="-48.26" width="0.1524" layer="91"/>
<label x="223.52" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R4" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-48.26" x2="261.62" y2="-48.26" width="0.1524" layer="91"/>
<label x="261.62" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U1" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-48.26" x2="-2.54" y2="-48.26" width="0.1524" layer="91"/>
<label x="-2.54" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VE" class="0">
<segment>
<pinref part="P3_U1" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-45.72" x2="43.18" y2="-45.72" width="0.1524" layer="91"/>
<label x="30.48" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R2" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-48.26" x2="172.72" y2="-48.26" width="0.1524" layer="91"/>
<label x="160.02" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R5" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-81.28" x2="76.2" y2="-81.28" width="0.1524" layer="91"/>
<label x="76.2" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_POT2" gate="G$1" pin="1"/>
<wire x1="86.36" y1="-116.84" x2="73.66" y2="-116.84" width="0.1524" layer="91"/>
<label x="73.66" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R6" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-149.86" x2="76.2" y2="-149.86" width="0.1524" layer="91"/>
<label x="76.2" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_U2N" class="0">
<segment>
<pinref part="P3_R5" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-81.28" x2="111.76" y2="-81.28" width="0.1524" layer="91"/>
<label x="99.06" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_POT1" gate="G$1" pin="1"/>
<wire x1="147.32" y1="-81.28" x2="134.62" y2="-81.28" width="0.1524" layer="91"/>
<label x="134.62" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U2" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-78.74" x2="-2.54" y2="-78.74" width="0.1524" layer="91"/>
<label x="-2.54" y="-78.74" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VP" class="0">
<segment>
<pinref part="P3_U2" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-78.74" x2="43.18" y2="-78.74" width="0.1524" layer="91"/>
<label x="30.48" y="-78.74" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_POT1" gate="G$1" pin="2"/>
<wire x1="154.94" y1="-86.36" x2="154.94" y2="-91.44" width="0.1524" layer="91"/>
<label x="154.94" y="-91.44" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P3_POT1" gate="G$1" pin="3"/>
<wire x1="162.56" y1="-81.28" x2="175.26" y2="-81.28" width="0.1524" layer="91"/>
<label x="162.56" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R7" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-81.28" x2="200.66" y2="-81.28" width="0.1524" layer="91"/>
<label x="200.66" y="-81.28" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_U3N" class="0">
<segment>
<pinref part="P3_POT2" gate="G$1" pin="2"/>
<wire x1="93.98" y1="-121.92" x2="93.98" y2="-127" width="0.1524" layer="91"/>
<label x="93.98" y="-127" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P3_POT2" gate="G$1" pin="3"/>
<wire x1="101.6" y1="-116.84" x2="114.3" y2="-116.84" width="0.1524" layer="91"/>
<label x="101.6" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_C1" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-116.84" x2="137.16" y2="-116.84" width="0.1524" layer="91"/>
<label x="137.16" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R11" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-116.84" x2="200.66" y2="-116.84" width="0.1524" layer="91"/>
<label x="200.66" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U3" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-114.3" x2="-2.54" y2="-114.3" width="0.1524" layer="91"/>
<label x="-2.54" y="-114.3" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VI" class="0">
<segment>
<pinref part="P3_U3" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-114.3" x2="43.18" y2="-114.3" width="0.1524" layer="91"/>
<label x="30.48" y="-114.3" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_C1" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-116.84" x2="172.72" y2="-116.84" width="0.1524" layer="91"/>
<label x="160.02" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R11" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-116.84" x2="236.22" y2="-116.84" width="0.1524" layer="91"/>
<label x="223.52" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R8" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-116.84" x2="261.62" y2="-116.84" width="0.1524" layer="91"/>
<label x="261.62" y="-116.84" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_R6C2" class="0">
<segment>
<pinref part="P3_R6" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-149.86" x2="111.76" y2="-149.86" width="0.1524" layer="91"/>
<label x="99.06" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_C2" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-149.86" x2="137.16" y2="-149.86" width="0.1524" layer="91"/>
<label x="137.16" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_U4N" class="0">
<segment>
<pinref part="P3_C2" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-149.86" x2="172.72" y2="-149.86" width="0.1524" layer="91"/>
<label x="160.02" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_POT3" gate="G$1" pin="1"/>
<wire x1="210.82" y1="-149.86" x2="198.12" y2="-149.86" width="0.1524" layer="91"/>
<label x="198.12" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U4" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-147.32" x2="-2.54" y2="-147.32" width="0.1524" layer="91"/>
<label x="-2.54" y="-147.32" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VD" class="0">
<segment>
<pinref part="P3_U4" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-147.32" x2="43.18" y2="-147.32" width="0.1524" layer="91"/>
<label x="30.48" y="-147.32" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_POT3" gate="G$1" pin="2"/>
<wire x1="218.44" y1="-154.94" x2="218.44" y2="-160.02" width="0.1524" layer="91"/>
<label x="218.44" y="-160.02" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P3_POT3" gate="G$1" pin="3"/>
<wire x1="226.06" y1="-149.86" x2="238.76" y2="-149.86" width="0.1524" layer="91"/>
<label x="226.06" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R9" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-149.86" x2="261.62" y2="-149.86" width="0.1524" layer="91"/>
<label x="261.62" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_SUMN" class="0">
<segment>
<pinref part="P3_R7" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-81.28" x2="236.22" y2="-81.28" width="0.1524" layer="91"/>
<label x="223.52" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R8" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-116.84" x2="297.18" y2="-116.84" width="0.1524" layer="91"/>
<label x="284.48" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R9" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-149.86" x2="297.18" y2="-149.86" width="0.1524" layer="91"/>
<label x="284.48" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_ROFFSET" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-182.88" x2="111.76" y2="-182.88" width="0.1524" layer="91"/>
<label x="99.06" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R10" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-182.88" x2="137.16" y2="-182.88" width="0.1524" layer="91"/>
<label x="137.16" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U5" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-180.34" x2="-2.54" y2="-180.34" width="0.1524" layer="91"/>
<label x="-2.54" y="-180.34" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_U5P" class="0">
<segment>
<pinref part="P3_U5" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-182.88" x2="-2.54" y2="-182.88" width="0.1524" layer="91"/>
<label x="-2.54" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_RBIAS" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-182.88" x2="200.66" y2="-182.88" width="0.1524" layer="91"/>
<label x="200.66" y="-182.88" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VPID" class="0">
<segment>
<pinref part="P3_U5" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-180.34" x2="43.18" y2="-180.34" width="0.1524" layer="91"/>
<label x="30.48" y="-180.34" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R10" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-182.88" x2="172.72" y2="-182.88" width="0.1524" layer="91"/>
<label x="160.02" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_J_OUT" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-251.46" x2="76.2" y2="-251.46" width="0.1524" layer="91"/>
<label x="76.2" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VOFFD" class="0">
<segment>
<pinref part="P3_R14" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-218.44" x2="111.76" y2="-218.44" width="0.1524" layer="91"/>
<label x="99.06" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_R15" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-218.44" x2="137.16" y2="-218.44" width="0.1524" layer="91"/>
<label x="137.16" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U7" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-218.44" x2="-2.54" y2="-218.44" width="0.1524" layer="91"/>
<label x="-2.54" y="-218.44" size="1.27" layer="95"/>
</segment>
</net>
<net name="P3_VOFF" class="0">
<segment>
<pinref part="P3_U7" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-215.9" x2="43.18" y2="-215.9" width="0.1524" layer="91"/>
<label x="30.48" y="-215.9" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_U7" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-215.9" x2="-2.54" y2="-215.9" width="0.1524" layer="91"/>
<label x="-2.54" y="-215.9" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P3_ROFFSET" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-182.88" x2="76.2" y2="-182.88" width="0.1524" layer="91"/>
<label x="76.2" y="-182.88" size="1.27" layer="95"/>
</segment>
</net>
</nets>
</sheet>
<sheet>
<plain>
<text x="20" y="8" size="3.81" layer="97">Módulo PID 4: controlador PID analógico (7 x LM741)</text>
</plain>
<instances>
<instance part="P4_U6" gate="G$1" x="20.32" y="-15.24"/>
<instance part="P4_R12" gate="G$1" x="93.98" y="-15.24"/>
<instance part="P4_R13" gate="G$1" x="154.94" y="-15.24"/>
<instance part="P4_U1" gate="G$1" x="20.32" y="-48.26"/>
<instance part="P4_R1" gate="G$1" x="93.98" y="-48.26"/>
<instance part="P4_R2" gate="G$1" x="154.94" y="-48.26"/>
<instance part="P4_R3" gate="G$1" x="218.44" y="-48.26"/>
<instance part="P4_R4" gate="G$1" x="279.4" y="-48.26"/>
<instance part="P4_U2" gate="G$1" x="20.32" y="-81.28"/>
<instance part="P4_R5" gate="G$1" x="93.98" y="-81.28"/>
<instance part="P4_POT1" gate="G$1" x="154.94" y="-81.28"/>
<instance part="P4_R7" gate="G$1" x="218.44" y="-81.28"/>
<instance part="P4_U3" gate="G$1" x="20.32" y="-116.84"/>
<instance part="P4_POT2" gate="G$1" x="93.98" y="-116.84"/>
<instance part="P4_C1" gate="G$1" x="154.94" y="-116.84"/>
<instance part="P4_R11" gate="G$1" x="218.44" y="-116.84"/>
<instance part="P4_R8" gate="G$1" x="279.4" y="-116.84"/>
<instance part="P4_U4" gate="G$1" x="20.32" y="-149.86"/>
<instance part="P4_R6" gate="G$1" x="93.98" y="-149.86"/>
<instance part="P4_C2" gate="G$1" x="154.94" y="-149.86"/>
<instance part="P4_POT3" gate="G$1" x="218.44" y="-149.86"/>
<instance part="P4_R9" gate="G$1" x="279.4" y="-149.86"/>
<instance part="P4_U5" gate="G$1" x="20.32" y="-182.88"/>
<instance part="P4_ROFFSET" gate="G$1" x="93.98" y="-182.88"/>
<instance part="P4_R10" gate="G$1" x="154.94" y="-182.88"/>
<instance part="P4_RBIAS" gate="G$1" x="218.44" y="-182.88"/>
<instance part="P4_U7" gate="G$1" x="20.32" y="-218.44"/>
<instance part="P4_R14" gate="G$1" x="93.98" y="-218.44"/>
<instance part="P4_R15" gate="G$1" x="154.94" y="-218.44"/>
<instance part="P4_J_IN" gate="G$1" x="33.02" y="-251.46"/>
<instance part="P4_J_OUT" gate="G$1" x="93.98" y="-251.46"/>
<instance part="P4_J_PWR" gate="G$1" x="154.94" y="-251.46"/>
</instances>
<busses>
</busses>
<nets>
<net name="+16V" class="0">
<segment>
<pinref part="P4_U1" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-43.18" x2="43.18" y2="-43.18" width="0.1524" layer="91"/>
<label x="30.48" y="-43.18" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U2" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-76.2" x2="43.18" y2="-76.2" width="0.1524" layer="91"/>
<label x="30.48" y="-76.2" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U3" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-111.76" x2="43.18" y2="-111.76" width="0.1524" layer="91"/>
<label x="30.48" y="-111.76" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U4" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-144.78" x2="43.18" y2="-144.78" width="0.1524" layer="91"/>
<label x="30.48" y="-144.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U5" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-177.8" x2="43.18" y2="-177.8" width="0.1524" layer="91"/>
<label x="30.48" y="-177.8" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U6" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-10.16" x2="43.18" y2="-10.16" width="0.1524" layer="91"/>
<label x="30.48" y="-10.16" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U7" gate="G$1" pin="V+"/>
<wire x1="30.48" y1="-213.36" x2="43.18" y2="-213.36" width="0.1524" layer="91"/>
<label x="30.48" y="-213.36" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_J_PWR" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-251.46" x2="137.16" y2="-251.46" width="0.1524" layer="91"/>
<label x="137.16" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="-16V" class="0">
<segment>
<pinref part="P4_U1" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-50.8" x2="-2.54" y2="-50.8" width="0.1524" layer="91"/>
<label x="-2.54" y="-50.8" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U2" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-83.82" x2="-2.54" y2="-83.82" width="0.1524" layer="91"/>
<label x="-2.54" y="-83.82" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U3" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-119.38" x2="-2.54" y2="-119.38" width="0.1524" layer="91"/>
<label x="-2.54" y="-119.38" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U4" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-152.4" x2="-2.54" y2="-152.4" width="0.1524" layer="91"/>
<label x="-2.54" y="-152.4" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U5" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-185.42" x2="-2.54" y2="-185.42" width="0.1524" layer="91"/>
<label x="-2.54" y="-185.42" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U6" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-17.78" x2="-2.54" y2="-17.78" width="0.1524" layer="91"/>
<label x="-2.54" y="-17.78" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U7" gate="G$1" pin="V-"/>
<wire x1="10.16" y1="-220.98" x2="-2.54" y2="-220.98" width="0.1524" layer="91"/>
<label x="-2.54" y="-220.98" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R14" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-218.44" x2="76.2" y2="-218.44" width="0.1524" layer="91"/>
<label x="76.2" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_J_PWR" gate="G$1" pin="2"/>
<wire x1="149.86" y1="-254" x2="137.16" y2="-254" width="0.1524" layer="91"/>
<label x="137.16" y="-254" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VREFD" class="0">
<segment>
<pinref part="P4_R12" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-15.24" x2="76.2" y2="-15.24" width="0.1524" layer="91"/>
<label x="76.2" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R13" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-15.24" x2="137.16" y2="-15.24" width="0.1524" layer="91"/>
<label x="137.16" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U6" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-15.24" x2="-2.54" y2="-15.24" width="0.1524" layer="91"/>
<label x="-2.54" y="-15.24" size="1.27" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="P4_R12" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-15.24" x2="111.76" y2="-15.24" width="0.1524" layer="91"/>
<label x="99.06" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R4" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-48.26" x2="297.18" y2="-48.26" width="0.1524" layer="91"/>
<label x="284.48" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U2" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-81.28" x2="-2.54" y2="-81.28" width="0.1524" layer="91"/>
<label x="-2.54" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U3" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-116.84" x2="-2.54" y2="-116.84" width="0.1524" layer="91"/>
<label x="-2.54" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U4" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-149.86" x2="-2.54" y2="-149.86" width="0.1524" layer="91"/>
<label x="-2.54" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_RBIAS" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-182.88" x2="236.22" y2="-182.88" width="0.1524" layer="91"/>
<label x="223.52" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R15" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-218.44" x2="172.72" y2="-218.44" width="0.1524" layer="91"/>
<label x="160.02" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_J_PWR" gate="G$1" pin="3"/>
<wire x1="149.86" y1="-256.54" x2="137.16" y2="-256.54" width="0.1524" layer="91"/>
<label x="137.16" y="-256.54" size="1.27" layer="95"/>
</segment>
</net>
<net name="+5V" class="0">
<segment>
<pinref part="P4_R13" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-15.24" x2="172.72" y2="-15.24" width="0.1524" layer="91"/>
<label x="160.02" y="-15.24" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_J_PWR" gate="G$1" pin="4"/>
<wire x1="149.86" y1="-259.08" x2="137.16" y2="-259.08" width="0.1524" layer="91"/>
<label x="137.16" y="-259.08" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VREF" class="0">
<segment>
<pinref part="P4_U6" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-12.7" x2="43.18" y2="-12.7" width="0.1524" layer="91"/>
<label x="30.48" y="-12.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U6" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-12.7" x2="-2.54" y2="-12.7" width="0.1524" layer="91"/>
<label x="-2.54" y="-12.7" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R1" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-48.26" x2="76.2" y2="-48.26" width="0.1524" layer="91"/>
<label x="76.2" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_U1N" class="0">
<segment>
<pinref part="P4_R1" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-48.26" x2="111.76" y2="-48.26" width="0.1524" layer="91"/>
<label x="99.06" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R2" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-48.26" x2="137.16" y2="-48.26" width="0.1524" layer="91"/>
<label x="137.16" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U1" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-45.72" x2="-2.54" y2="-45.72" width="0.1524" layer="91"/>
<label x="-2.54" y="-45.72" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VSEN" class="0">
<segment>
<pinref part="P4_R3" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-48.26" x2="200.66" y2="-48.26" width="0.1524" layer="91"/>
<label x="200.66" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_J_IN" gate="G$1" pin="1"/>
<wire x1="27.94" y1="-251.46" x2="15.24" y2="-251.46" width="0.1524" layer="91"/>
<label x="15.24" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_U1P" class="0">
<segment>
<pinref part="P4_R3" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-48.26" x2="236.22" y2="-48.26" width="0.1524" layer="91"/>
<label x="223.52" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R4" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-48.26" x2="261.62" y2="-48.26" width="0.1524" layer="91"/>
<label x="261.62" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U1" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-48.26" x2="-2.54" y2="-48.26" width="0.1524" layer="91"/>
<label x="-2.54" y="-48.26" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VE" class="0">
<segment>
<pinref part="P4_U1" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-45.72" x2="43.18" y2="-45.72" width="0.1524" layer="91"/>
<label x="30.48" y="-45.72" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R2" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-48.26" x2="172.72" y2="-48.26" width="0.1524" layer="91"/>
<label x="160.02" y="-48.26" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R5" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-81.28" x2="76.2" y2="-81.28" width="0.1524" layer="91"/>
<label x="76.2" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_POT2" gate="G$1" pin="1"/>
<wire x1="86.36" y1="-116.84" x2="73.66" y2="-116.84" width="0.1524" layer="91"/>
<label x="73.66" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R6" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-149.86" x2="76.2" y2="-149.86" width="0.1524" layer="91"/>
<label x="76.2" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_U2N" class="0">
<segment>
<pinref part="P4_R5" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-81.28" x2="111.76" y2="-81.28" width="0.1524" layer="91"/>
<label x="99.06" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_POT1" gate="G$1" pin="1"/>
<wire x1="147.32" y1="-81.28" x2="134.62" y2="-81.28" width="0.1524" layer="91"/>
<label x="134.62" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U2" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-78.74" x2="-2.54" y2="-78.74" width="0.1524" layer="91"/>
<label x="-2.54" y="-78.74" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VP" class="0">
<segment>
<pinref part="P4_U2" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-78.74" x2="43.18" y2="-78.74" width="0.1524" layer="91"/>
<label x="30.48" y="-78.74" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_POT1" gate="G$1" pin="2"/>
<wire x1="154.94" y1="-86.36" x2="154.94" y2="-91.44" width="0.1524" layer="91"/>
<label x="154.94" y="-91.44" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P4_POT1" gate="G$1" pin="3"/>
<wire x1="162.56" y1="-81.28" x2="175.26" y2="-81.28" width="0.1524" layer="91"/>
<label x="162.56" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R7" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-81.28" x2="200.66" y2="-81.28" width="0.1524" layer="91"/>
<label x="200.66" y="-81.28" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_U3N" class="0">
<segment>
<pinref part="P4_POT2" gate="G$1" pin="2"/>
<wire x1="93.98" y1="-121.92" x2="93.98" y2="-127" width="0.1524" layer="91"/>
<label x="93.98" y="-127" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P4_POT2" gate="G$1" pin="3"/>
<wire x1="101.6" y1="-116.84" x2="114.3" y2="-116.84" width="0.1524" layer="91"/>
<label x="101.6" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_C1" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-116.84" x2="137.16" y2="-116.84" width="0.1524" layer="91"/>
<label x="137.16" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R11" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-116.84" x2="200.66" y2="-116.84" width="0.1524" layer="91"/>
<label x="200.66" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U3" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-114.3" x2="-2.54" y2="-114.3" width="0.1524" layer="91"/>
<label x="-2.54" y="-114.3" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VI" class="0">
<segment>
<pinref part="P4_U3" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-114.3" x2="43.18" y2="-114.3" width="0.1524" layer="91"/>
<label x="30.48" y="-114.3" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_C1" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-116.84" x2="172.72" y2="-116.84" width="0.1524" layer="91"/>
<label x="160.02" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R11" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-116.84" x2="236.22" y2="-116.84" width="0.1524" layer="91"/>
<label x="223.52" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R8" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-116.84" x2="261.62" y2="-116.84" width="0.1524" layer="91"/>
<label x="261.62" y="-116.84" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_R6C2" class="0">
<segment>
<pinref part="P4_R6" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-149.86" x2="111.76" y2="-149.86" width="0.1524" layer="91"/>
<label x="99.06" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_C2" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-149.86" x2="137.16" y2="-149.86" width="0.1524" layer="91"/>
<label x="137.16" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_U4N" class="0">
<segment>
<pinref part="P4_C2" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-149.86" x2="172.72" y2="-149.86" width="0.1524" layer="91"/>
<label x="160.02" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_POT3" gate="G$1" pin="1"/>
<wire x1="210.82" y1="-149.86" x2="198.12" y2="-149.86" width="0.1524" layer="91"/>
<label x="198.12" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U4" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-147.32" x2="-2.54" y2="-147.32" width="0.1524" layer="91"/>
<label x="-2.54" y="-147.32" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VD" class="0">
<segment>
<pinref part="P4_U4" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-147.32" x2="43.18" y2="-147.32" width="0.1524" layer="91"/>
<label x="30.48" y="-147.32" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_POT3" gate="G$1" pin="2"/>
<wire x1="218.44" y1="-154.94" x2="218.44" y2="-160.02" width="0.1524" layer="91"/>
<label x="218.44" y="-160.02" size="1.27" layer="95" rot="R270"/>
</segment>
<segment>
<pinref part="P4_POT3" gate="G$1" pin="3"/>
<wire x1="226.06" y1="-149.86" x2="238.76" y2="-149.86" width="0.1524" layer="91"/>
<label x="226.06" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R9" gate="G$1" pin="1"/>
<wire x1="274.32" y1="-149.86" x2="261.62" y2="-149.86" width="0.1524" layer="91"/>
<label x="261.62" y="-149.86" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_SUMN" class="0">
<segment>
<pinref part="P4_R7" gate="G$1" pin="2"/>
<wire x1="223.52" y1="-81.28" x2="236.22" y2="-81.28" width="0.1524" layer="91"/>
<label x="223.52" y="-81.28" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R8" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-116.84" x2="297.18" y2="-116.84" width="0.1524" layer="91"/>
<label x="284.48" y="-116.84" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R9" gate="G$1" pin="2"/>
<wire x1="284.48" y1="-149.86" x2="297.18" y2="-149.86" width="0.1524" layer="91"/>
<label x="284.48" y="-149.86" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_ROFFSET" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-182.88" x2="111.76" y2="-182.88" width="0.1524" layer="91"/>
<label x="99.06" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R10" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-182.88" x2="137.16" y2="-182.88" width="0.1524" layer="91"/>
<label x="137.16" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U5" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-180.34" x2="-2.54" y2="-180.34" width="0.1524" layer="91"/>
<label x="-2.54" y="-180.34" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_U5P" class="0">
<segment>
<pinref part="P4_U5" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-182.88" x2="-2.54" y2="-182.88" width="0.1524" layer="91"/>
<label x="-2.54" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_RBIAS" gate="G$1" pin="1"/>
<wire x1="213.36" y1="-182.88" x2="200.66" y2="-182.88" width="0.1524" layer="91"/>
<label x="200.66" y="-182.88" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VPID" class="0">
<segment>
<pinref part="P4_U5" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-180.34" x2="43.18" y2="-180.34" width="0.1524" layer="91"/>
<label x="30.48" y="-180.34" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R10" gate="G$1" pin="2"/>
<wire x1="160.02" y1="-182.88" x2="172.72" y2="-182.88" width="0.1524" layer="91"/>
<label x="160.02" y="-182.88" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_J_OUT" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-251.46" x2="76.2" y2="-251.46" width="0.1524" layer="91"/>
<label x="76.2" y="-251.46" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VOFFD" class="0">
<segment>
<pinref part="P4_R14" gate="G$1" pin="2"/>
<wire x1="99.06" y1="-218.44" x2="111.76" y2="-218.44" width="0.1524" layer="91"/>
<label x="99.06" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_R15" gate="G$1" pin="1"/>
<wire x1="149.86" y1="-218.44" x2="137.16" y2="-218.44" width="0.1524" layer="91"/>
<label x="137.16" y="-218.44" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U7" gate="G$1" pin="IN+"/>
<wire x1="10.16" y1="-218.44" x2="-2.54" y2="-218.44" width="0.1524" layer="91"/>
<label x="-2.54" y="-218.44" size="1.27" layer="95"/>
</segment>
</net>
<net name="P4_VOFF" class="0">
<segment>
<pinref part="P4_U7" gate="G$1" pin="OUT"/>
<wire x1="30.48" y1="-215.9" x2="43.18" y2="-215.9" width="0.1524" layer="91"/>
<label x="30.48" y="-215.9" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_U7" gate="G$1" pin="IN-"/>
<wire x1="10.16" y1="-215.9" x2="-2.54" y2="-215.9" width="0.1524" layer="91"/>
<label x="-2.54" y="-215.9" size="1.27" layer="95"/>
</segment>
<segment>
<pinref part="P4_ROFFSET" gate="G$1" pin="1"/>
<wire x1="88.9" y1="-182.88" x2="76.2" y2="-182.88" width="0.1524" layer="91"/>
<label x="76.2" y="-182.88" size="1.27" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
