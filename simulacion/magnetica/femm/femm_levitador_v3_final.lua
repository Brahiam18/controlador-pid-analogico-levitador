-- FEMM 4.2 (Windows) - magnetostatico axisimetrico. UNA bobina con nucleo + iman N42 encima (repulsion).
-- Medidas finales del proyecto. NO probado en FEMM (el mismo modelo se resolvio con un solver propio).
-- Uso: File > Open Lua Script... > elegir este archivo. Resultado: ventana con F0, F1 y la corriente de equilibrio.
-- Unidades: mm. Eje z hacia arriba; z = 0 es la cara inferior del devanado.
gap   = 30             -- altura del iman sobre la PESTAÑA superior (mm); cambiar a 20, 25, 35...
fl    = 3              -- espesor de la pestaña (mm)
Ri,Ro,H = 3,16.5,23    -- radio interior (agujero Ø6), radio exterior del devanado (Ø33), largo del devanado
N     = 652            -- espiras
Rc    = 3              -- nucleo Ø6
zc0,zc1 = -11,34       -- nucleo de 45 mm: 8 mm sobre la pestaña superior y 8 mm bajo la inferior
mur   = 1000           -- permeabilidad relativa (200 a 1500 da casi lo mismo)
Rm,Lm = 10,4.2         -- iman N42 Ø20 x 4,2 mm
Br    = 1.31
peso_gf = 9.9          -- peso del iman en gf
newdocument(0)
mi_probdef(0,"millimeters","axi",1e-8,0,30)
mi_addmaterial("Aire",1,1,0,0,0,0,0,1,0,0,0)
mi_addmaterial("Cobre",1,1,0,0,58,0,0,1,0,0,0)
mi_addmaterial("Hierro",mur,mur,0,0,0,0,0,1,0,0,0)
mi_addmaterial("N42",1.05,1.05,(Br/(4e-7*pi*1.05)),0,0,0,0,1,0,0,0)
mi_addcircprop("Bobina",1,1)
-- GEOMETRIA: todos los segmentos se parten en los mismos puntos de corte para que no se superpongan
z0=H+fl+gap
ztop=z0+Lm+150
rb={0,Rc,Rm,Ro,150}
zb={-150,zc0,0,H,zc1,z0,z0+Lm,ztop}
visto={}
function seg(x1,y1,x2,y2)
  local k=format("%g_%g_%g_%g",x1,y1,x2,y2)
  if visto[k]==nil then
    visto[k]=1
    mi_addsegment(x1,y1,x2,y2)
  end
end
function vlinea(x,ya,yb)
  local i
  for i=1,getn(zb)-1 do
    if zb[i]>=ya and zb[i+1]<=yb then seg(x,zb[i],x,zb[i+1]) end
  end
end
function hlinea(y,xa,xb)
  local i
  for i=1,getn(rb)-1 do
    if rb[i]>=xa and rb[i+1]<=xb then seg(rb[i],y,rb[i+1],y) end
  end
end
-- caja de aire y eje
vlinea(0,-150,ztop); vlinea(150,-150,ztop); hlinea(-150,0,150); hlinea(ztop,0,150)
-- nucleo
vlinea(Rc,zc0,zc1); hlinea(zc0,0,Rc); hlinea(zc1,0,Rc)
-- devanado
vlinea(Ro,0,H); hlinea(0,Rc,Ro); hlinea(H,Rc,Ro)
-- iman
vlinea(Rm,z0,z0+Lm); hlinea(z0,0,Rm); hlinea(z0+Lm,0,Rm)
-- etiquetas de material
mi_addblocklabel((Rc+Ro)/2,H/2); mi_selectlabel((Rc+Ro)/2,H/2)
mi_setblockprop("Cobre",1,0,"Bobina",0,1,N); mi_clearselected()
mi_addblocklabel(Rc/2,(zc0+zc1)/2); mi_selectlabel(Rc/2,(zc0+zc1)/2)
mi_setblockprop("Hierro",1,0,"<None>",0,3,0); mi_clearselected()
mi_addblocklabel(Rm/2,z0+Lm/2); mi_selectlabel(Rm/2,z0+Lm/2)
mi_setblockprop("N42",1,0,"<None>",-90,2,0); mi_clearselected()
mi_addblocklabel(100,100); mi_selectlabel(100,100)
mi_setblockprop("Aire",1,0,"<None>",0,0,0); mi_clearselected()
mi_makeABC(7,150,0,0,0)
mi_saveas("levitador_nucleo_final.fem")
function fuerza(I)
  mi_modifycircprop("Bobina",1,I)
  mi_analyze(1); mi_loadsolution()
  mo_groupselectblock(2)
  local f=mo_blockintegral(19)      -- fuerza z en N
  mo_clearblock()
  return f/9.81*1000                -- gf
end
F0=fuerza(0); F1=fuerza(1)-F0
Ieq=(peso_gf-F0)/F1
mo_showdensityplot(0,0,0.4,0,"bmag")
showconsole()
print("Altura "..gap.." mm sobre la pestaña")
print("F con I=0: "..F0.." gf  (negativa = el nucleo atrae al iman)")
print("F1: "..F1.." gf por amperio")
print("Corriente de equilibrio: "..Ieq.." A")
