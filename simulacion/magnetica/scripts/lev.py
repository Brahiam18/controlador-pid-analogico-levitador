import numpy as np
from scipy.special import ellipk, ellipe
MU0=4e-7*np.pi
def loop_B(a,z0,rho,z,I=1.0):
    """Campo (Brho,Bz) de una espira de radio a en z0, corriente I, en (rho,z). Vectorizado."""
    rho=np.asarray(rho,float); dz=np.asarray(z,float)-z0
    rho=np.maximum(rho,1e-9)
    d1=(a+rho)**2+dz**2; d2=(a-rho)**2+dz**2
    m=4*a*rho/d1
    K=ellipk(m); E=ellipe(m)
    c=MU0*I/(2*np.pi)
    Bz=c/np.sqrt(d1)*(K+(a*a-rho**2-dz**2)/d2*E)
    Br=c*dz/(rho*np.sqrt(d1))*(-K+(a*a+rho**2+dz**2)/d2*E)
    return Br,Bz
def coil_loops(Ri,Ro,H,z_bot,NI,nr=8,nz=12):
    r=Ri+(np.arange(nr)+.5)*(Ro-Ri)/nr
    z=z_bot+(np.arange(nz)+.5)*H/nz
    R,Z=np.meshgrid(r,z); return R.ravel(),Z.ravel(),NI/(nr*nz)
def coil_Bz(coil,rho,z):
    R,Z,i=coil
    return sum(loop_B(a,z0,rho,z,i)[1] for a,z0 in zip(R,Z))
def magnet_points(Rm,L,z_bot,n_r=6,n_z=4,n_t=12):
    """dipolos que representan el disco imantado (uniforme). devuelve rho,z,volumen"""
    dr=Rm/n_r; dzm=L/n_z
    rs=(np.arange(n_r)+.5)*dr
    pts=[]
    for i,r in enumerate(rs):
        for k in range(n_z):
            for t in range(n_t):
                th=2*np.pi*(t+.5)/n_t
                vol=2*np.pi*r*dr*dzm/n_t
                pts.append((r*np.cos(th),r*np.sin(th),z_bot+(k+.5)*dzm,vol))
    return np.array(pts)
def force_z(coil,cx,cy,mx,my,mz_bot,Rm,L,Br):
    """Fuerza vertical (N) sobre el iman (momento -z: repulsion), bobina en (cx,cy)"""
    M=Br/MU0
    P=magnet_points(Rm,L,mz_bot)
    x=mx+P[:,0]-cx; y=my+P[:,1]-cy; z=P[:,2]; V=P[:,3]
    rho=np.hypot(x,y); h=1e-4
    dB=(coil_Bz(coil,rho,z+h)-coil_Bz(coil,rho,z-h))/(2*h)
    return float(np.sum(-M*V*dB))   # m=-z => Fz=-m dBz/dz
def magnet_Bz_axis(Rm,L,z_bot,z,Br,n=200):
    """Bz del iman (momento +z) sobre el eje, modelo de espiras de corriente superficial K=M"""
    M=Br/MU0; zs=z_bot+(np.arange(n)+.5)*L/n; dI=M*L/n
    return sum(loop_B(Rm,z0,1e-9,z,dI)[1] for z0 in zs)
if __name__=="__main__":
    # verificaciones
    Br=1.31;Rm=0.01;L=0.01
    for zz in (0.02,0.04):
        an=Br/2*((zz+L)/np.hypot(Rm,zz+L)-zz/np.hypot(Rm,zz))
        print("iman eje z=%.0f mm: numerico %.5f T, analitico %.5f T"%(zz*1e3,magnet_Bz_axis(Rm,L,0,-0+zz+0 if False else zz+0,Br) if False else magnet_Bz_axis(Rm,L,0,L+zz,Br),an))
    a=0.014;I=550;zz=0.05
    print("espira eje: %.6e vs %.6e"%(loop_B(a,0,1e-9,zz,I)[1][()],MU0*I*a*a/(2*(a*a+zz*zz)**1.5)))
