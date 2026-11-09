-- FEMM 4.2 (Windows) - magnetostatico axisimetrico. Bobina de aire + iman N42 encima.
-- NO probado en FEMM; ejecutar con File > Open Lua Script. Unidades: mm.
gap   = 40      -- distancia cara superior de la bobina - cara inferior del iman (mm)
Ri,Ro,H = 7.5,20,25      -- bobina: radio interior, exterior, altura
N,I   = 564,1.0          -- vueltas y corriente (A)
Rm,Lm = 10,10            -- iman: radio y espesor
Br    = 1.31             -- T (N42)
newdocument(0)
mi_probdef(0,"millimeters","axi",1e-8,0,30)
mi_addmaterial("Aire",1,1,0,0,0,0,0,1,0,0,0)
mi_addmaterial("Cobre",1,1,0,0,58,0,0,1,0,0,0)
mi_addmaterial("N42",1.05,1.05,(Br/(4e-7*pi*1.05)),0,0,0,0,1,0,0,0)  -- Hc [A/m]
mi_addcircprop("Bobina",I,1)
-- bobina
mi_drawrectangle(Ri,0,Ro,H)
mi_addblocklabel((Ri+Ro)/2,H/2); mi_selectlabel((Ri+Ro)/2,H/2)
mi_setblockprop("Cobre",1,0,"Bobina",0,1,N); mi_clearselected()
-- iman (magnetizado hacia -z: repulsion)
z0=H+gap
mi_drawrectangle(0,z0,Rm,z0+Lm)
mi_addblocklabel(Rm/2,z0+Lm/2); mi_selectlabel(Rm/2,z0+Lm/2)
mi_setblockprop("N42",1,0,"<None>",-90,2,0); mi_clearselected()
-- aire y frontera abierta
mi_drawrectangle(0,-150,150,z0+Lm+150)
mi_addblocklabel(100,100); mi_selectlabel(100,100)
mi_setblockprop("Aire",1,0,"<None>",0,0,0); mi_clearselected()
mi_makeABC(7,150,0,0,0)
mi_saveas("levitador_aire.fem")
mi_analyze(); mi_loadsolution()
mo_groupselectblock(2)
fz=mo_blockintegral(19)   -- fuerza en z por tensor de Maxwell ponderado [N]
print("Fuerza vertical sobre el iman: "..fz.." N = "..(fz/9.81*1000).." gf")
