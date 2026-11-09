import numpy as np, fem, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
mm=1e-3; Ri,Ro,H,N=3*mm,16.5*mm,23*mm,652; Rm,L=10*mm,4.2*mm
W=np.pi*Rm**2*L*7.5e3*9.81; fl=3*mm
def sol(gf,I,mur=1000.):
    z1=H+fl+8*mm; z0=z1-45*mm
    return fem.solve(gf*mm+fl,I,core_z=(z0,z1),Rc=3*mm,Ri=Ri,Ro=Ro,H=H,Rm=Rm,L=L,N=N,mur=mur,core=True),(z0,z1)
def base(gf):
    m,b,A,g=fem.solve(gf*mm+fl,0.,Rc=3*mm,Ri=Ri,Ro=Ro,H=H,Rm=Rm,L=L,N=N,mur=1.,core=False);return fem.force_z(m,b,A,g)
def force(gf,I):
    (m,b,A,g),_=sol(gf,I); return (fem.force_z(m,b,A,g)-base(gf))/9.81*1e3
# 1) mapa de campo, h=30 mm, I=0.75 A
gf=30;I=0.75
(m,b,A,g),(z0,z1)=sol(gf,I)
B=fem.make_B(m,b,A)
r=np.linspace(0.05e-3,45e-3,260);z=np.linspace(-20e-3,g['zt']+12e-3,300)
R,Z=np.meshgrid(r,z)
def ch(f,x,y,n=1500):
    return np.concatenate([f(x[i:i+n],y[i:i+n]) for i in range(0,len(x),n)])
Bs=[B(R.ravel()[i:i+1500],Z.ravel()[i:i+1500]) for i in range(0,R.size,1500)]
Br=np.concatenate([a[0] for a in Bs]);Bz=np.concatenate([a[1] for a in Bs]);Bm=np.hypot(Br,Bz).reshape(R.shape)
fig,ax=plt.subplots(figsize=(7.5,8))
im=ax.pcolormesh(R/mm,Z/mm,Bm*1e3,cmap="inferno",vmax=400,shading="auto")
px,pz=m.p[0],m.p[1];ok=(px<45e-3)&(pz>-20e-3)&(pz<g['zt']+12e-3)
import matplotlib.tri as mtri
tri=mtri.Triangulation(px/mm,pz/mm,m.t.T);msk=~ok[m.t].all(axis=0);tri.set_mask(msk)
ax.tricontour(tri,A*px,levels=26,colors="w",linewidths=.6)
for s in(-1,1):pass
ax.add_patch(Rectangle((Ri/mm,0),(Ro-Ri)/mm,H/mm,fill=False,ec="c",lw=1.2))
ax.add_patch(Rectangle((0,z0/mm),3,(z1-z0)/mm,fill=False,ec="lime",lw=1.2))
ax.add_patch(Rectangle((0,g['zb']/mm),Rm/mm,L/mm,fill=False,ec="red",lw=1.5))
ax.set_xlabel("r [mm] (eje de simetria en r = 0)");ax.set_ylabel("z [mm]");ax.set_aspect("equal")
ax.set_title("Densidad de flujo |B| [mT] y lineas de flujo\nI = %.2f A, iman a %d mm sobre la bobina (cian: devanado, verde: nucleo, rojo: iman)"%(I,gf),fontsize=9)
plt.colorbar(im,label="|B| [mT]",shrink=.7);plt.tight_layout();plt.savefig("../figuras/fem_1_mapa_campo.png",dpi=170);plt.close()
# 2) fuerza vs corriente a varias alturas
fig,ax=plt.subplots(figsize=(7,4.5));Is=np.linspace(0,1.6,5)
for gf in(20,25,30,35):
    F0=force(gf,0.);F1=force(gf,1.)-F0
    ax.plot(Is,F0+F1*Is,"o-",label="%d mm"%gf)
ax.axhline(W/9.81*1e3,c="r",ls="--",label="peso del iman (%.1f gf)"%(W/9.81*1e3))
ax.set_xlabel("Corriente I [A]");ax.set_ylabel("Fuerza vertical sobre el iman [gf]");ax.grid(alpha=.3);ax.legend(title="altura sobre la pestaña")
ax.set_title("Fuerza vs corriente (bobina con nucleo Ø6x45 mm, 652 espiras)",fontsize=10);plt.tight_layout();plt.savefig("../figuras/fem_2_fuerza_vs_corriente.png",dpi=170);plt.close()
# 3) corriente de equilibrio vs altura
hs=[15,20,25,30,35,40];Ieq=[];F0s=[];F1s=[]
for gf in hs:
    F0=force(gf,0.);F1=force(gf,1.)-F0;F0s.append(F0);F1s.append(F1);Ieq.append((W/9.81*1e3-F0)/F1)
print(hs,Ieq,F0s,F1s)
fig,(a1,a2)=plt.subplots(1,2,figsize=(10,4))
a1.plot(hs,Ieq,"o-");a1.set_xlabel("Altura del iman sobre la pestaña [mm]");a1.set_ylabel("Corriente de equilibrio [A]");a1.grid(alpha=.3);a1.set_title("Corriente necesaria para sostener 10 g",fontsize=10)
a2.plot(hs,F0s,"s-",c="C1");a2.set_xlabel("Altura [mm]");a2.set_ylabel("Fuerza con I = 0 [gf] (negativa = atrae hacia abajo)");a2.grid(alpha=.3);a2.set_title("Atraccion del nucleo de hierro sin corriente",fontsize=10)
plt.tight_layout();plt.savefig("../figuras/fem_3_corriente_equilibrio.png",dpi=170)
