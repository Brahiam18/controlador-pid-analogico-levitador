-- FEMM 4.2 (Windows) - magnetostatico axisimetrico. Bobina con nucleo de hierro + iman N42 encima (repulsion).
-- NO probado en FEMM (se valido el mismo modelo con un solver propio). File > Open Lua Script.
-- Unidades: mm. Eje z hacia arriba; la cara superior de la bobina esta en z = H.
gap   = 30             -- distancia cara superior de la bobina - cara inferior del iman (mm)
Ri,Ro,H = 3,17,20      -- carrete: radio interior (agujero 6 mm), radio exterior del devanado (SUPUESTO, medir), alto
N,I   = 618,1.0        -- vueltas (de 4 ohm con este devanado) y corriente de prueba (A)
Rc    = 3              -- nucleo: radio (varilla de 6 mm)
zc0,zc1 = -10,30       -- nucleo: de 10 mm debajo de la bobina a 10 mm sobre ella
mur   = 1000           -- permeabilidad relativa del hierro (200 a 1500 da casi lo mismo)
Rm,Lm = 10,4.2         -- iman: radio y espesor (disco 20 x 4,2 mm, ~10 g)
Br    = 1.31           -- T (N42)
newdocument(0)
mi_probdef(0,"millimeters","axi",1e-8,0,30)
mi_addmaterial("Aire",1,1,0,0,0,0,0,1,0,0,0)
mi_addmaterial("Cobre",1,1,0,0,58,0,0,1,0,0,0)
mi_addmaterial("Hierro",mur,mur,0,0,0,0,0,1,0,0,0)
mi_addmaterial("N42",1.05,1.05,(Br/(4e-7*pi*1.05)),0,0,0,0,1,0,0,0)
mi_addcircprop("Bobina",I,1)
-- bobina
mi_drawrectangle(Ri,0,Ro,H)
mi_addblocklabel((Ri+Ro)/2,H/2); mi_selectlabel((Ri+Ro)/2,H/2)
mi_setblockprop("Cobre",1,0,"Bobina",0,1,N); mi_clearselected()
-- nucleo
mi_drawrectangle(0,zc0,Rc,zc1)
mi_addblocklabel(Rc/2,(zc0+zc1)/2); mi_selectlabel(Rc/2,(zc0+zc1)/2)
mi_setblockprop("Hierro",1,0,"<None>",0,3,0); mi_clearselected()
-- iman (magnetizado hacia -z: repulsion cuando I > 0)
z0=H+gap
mi_drawrectangle(0,z0,Rm,z0+Lm)
mi_addblocklabel(Rm/2,z0+Lm/2); mi_selectlabel(Rm/2,z0+Lm/2)
mi_setblockprop("N42",1,0,"<None>",-90,2,0); mi_clearselected()
-- aire y frontera abierta
mi_drawrectangle(0,-150,150,z0+Lm+150)
mi_addblocklabel(100,100); mi_selectlabel(100,100)
mi_setblockprop("Aire",1,0,"<None>",0,0,0); mi_clearselected()
mi_makeABC(7,150,0,0,0)
mi_saveas("levitador_nucleo.fem")
mi_analyze(); mi_loadsolution()
mo_groupselectblock(2)
fz=mo_blockintegral(19)
print("Fuerza vertical sobre el iman con I="..I.." A: "..fz.." N = "..(fz/9.81*1000).." gf")
print("Repite con I = 0 para obtener la atraccion del hierro sin corriente; la corriente de equilibrio es I = (peso - F(0)) / (F(1) - F(0)).")
