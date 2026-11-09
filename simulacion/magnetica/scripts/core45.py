import numpy as np, fem
Ri,Ro,H,N=3e-3,16.5e-3,23e-3,652
Rm,L=10e-3,4.2e-3;W=np.pi*Rm**2*L*7.5e3*9.81;mm=1e-3
fl=3*mm   # espesor supuesto de cada pestaña
def run(p,tot=45*mm,gap_flange=30*mm,mur=1000.0):
    z1=H+fl+p; z0=z1-tot      # el nucleo mide 'tot'; p = lo que sobresale sobre la pestaña superior
    g=gap_flange+fl           # distancia desde la cara superior del devanado
    r=[]
    for I in (0.0,1.0):
        m,b,A,geo=fem.solve(g,I,core_z=(z0,z1),Rc=3*mm,Ri=Ri,Ro=Ro,H=H,Rm=Rm,L=L,N=N,mur=mur,core=True)
        r.append(fem.force_z(m,b,A,geo))
    m,b,A,geo=fem.solve(g,0.0,Rc=3*mm,Ri=Ri,Ro=Ro,H=H,Rm=Rm,L=L,N=N,mur=1.0,core=False);base=fem.force_z(m,b,A,geo)
    F0=r[0]-base;F1=r[1]-r[0]
    print("sobresale %2d mm arriba y %2d mm abajo de las pestañas: F0=%5.1f gf F1=%5.1f gf/A I(10 g, 30 mm sobre la pestaña)=%.2f A | punta del nucleo a %.0f mm del iman"%(p/mm,(tot-(H+2*fl)-p)/mm,F0/9.81*1e3,F1/9.81*1e3,(W-F0)/F1,(gap_flange-p)/mm))
for p in (0,4,8,12,16): run(p*mm)
print("\n-- nucleo 45 mm con 9 mm arriba/8 abajo: corriente de despegue y de trabajo segun altura sobre la pestaña")
for gf in (15,20,25,30,35,40):
    run(8*mm,gap_flange=gf*mm)
