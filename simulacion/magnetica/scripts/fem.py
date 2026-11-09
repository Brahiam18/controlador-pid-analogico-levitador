import numpy as np
from skfem import *
from skfem.helpers import dot
MU0=4e-7*np.pi
def lines(feats,lo,hi,fine_lo,fine_hi,h=0.5e-3,grow=1.12):
    pts=set(feats)|{lo,hi}
    pts|=set(np.arange(fine_lo,fine_hi+1e-12,h))
    x=fine_hi
    while x<hi: h*=grow; x+=h; pts.add(min(x,hi))
    x=fine_lo;hh=h
    h2=h
    h2=0.5e-3
    while x>lo: h2*=grow; x-=h2; pts.add(max(x,lo))
    a=np.array(sorted(pts));keep=[a[0]]
    for v in a[1:]:
        if v-keep[-1]>0.12e-3 or v in feats: keep.append(v)
    # asegurar que las caracteristicas exactas esten
    a=np.array(sorted(set(keep)|set(feats)))
    out=[a[0]]
    for v in a[1:]:
        if v-out[-1]>0.05e-3: out.append(v)
        elif v in feats: out[-1]=v
    return np.array(out)
def solve(g,I,core_z=None,cap=None,Rc=2.5e-3,Ri=3e-3,Ro=17e-3,H=20e-3,Rm=7.5e-3,L=7.5e-3,N=581,mur=1000.0,Br=1.31,sign=-1,core=True,Rs_d=3e-3,corelen=None,probe=None):
    zb=H+g; zt=zb+L
    corelen=H if corelen is None else corelen
    rf=[Rc,Ri,Ro,Rm,Rm+Rs_d]
    zf=[0.0,H,zb,zt,zb-Rs_d,zt+Rs_d,H-corelen if corelen<H else 0.0]
    if core_z: zf+=list(core_z)
    if cap: rf.append(cap[0]); zf+=[core_z[1]+cap[1]]
    rs=lines(set(rf),0.0,0.25,0.0,0.035)
    zs=lines(set(zf),-0.25,zt+0.25,-0.02,zt+0.02)
    mesh=MeshTri.init_tensor(rs,zs)
    basis=Basis(mesh,ElementTriP1(),intorder=2)
    cx=mesh.p[0][mesh.t].mean(axis=0); cz=mesh.p[1][mesh.t].mean(axis=0)
    in_coil=(cx>Ri)&(cx<Ro)&(cz>0)&(cz<H)
    in_core=core&(cx<Rc)&(cz>H-corelen)&(cz<H)
    if core_z: in_core=core&(cx<Rc)&(cz>core_z[0])&(cz<core_z[1])
    if core_z and cap: in_core=in_core|(core&(cx<cap[0])&(cz>core_z[1])&(cz<core_z[1]+cap[1]))
    in_mag=(cx<Rm)&(cz>zb)&(cz<zt)
    nu=np.ones(mesh.t.shape[1]); nu[in_core]=1/mur
    J=np.zeros_like(nu); J[in_coil]=N*I/((Ro-Ri)*H)
    M=np.zeros_like(nu); M[in_mag]=sign*Br/MU0
    nq=basis.X.shape[1]
    F=lambda a:np.repeat(a[:,None],nq,axis=1)
    @BilinearForm
    def a(u,v,w):
        r=w.x[0]
        return w.nu*(u.grad[1]*v.grad[1]*r+(u.grad[0]+u/r)*(v.grad[0]+v/r)*r)/MU0
    @LinearForm
    def l(v,w):
        r=w.x[0]
        return w.J*v*r+w.M*(v.grad[0]+v/r)*r
    K=a.assemble(basis,nu=F(nu)); b=l.assemble(basis,J=F(J),M=F(M))
    D=basis.get_dofs().all()
    A=solve_(K,b,D)
    return mesh,basis,A,dict(zb=zb,zt=zt,Rs=Rm+Rs_d,Rm=Rm,H=H)
def solve_(K,b,D):
    from skfem import condense, solve as sk
    return sk(*condense(K,b,D=D))
def make_B(mesh,basis,A):
    ig=basis.interpolate(A).grad
    gr=ig[0][:,0];gz=ig[1][:,0]
    finder=mesh.element_finder()
    def B(r,z):
        r=np.atleast_1d(np.asarray(r,float));z=np.atleast_1d(np.asarray(z,float))
        e=finder(x=r,y=z)
        Ap=basis.probes(np.vstack([r,z]))@A
        rr=np.maximum(r,1e-9)
        return -gz[e], gr[e]+Ap/rr     # Br, Bz
    return B
def force_z(mesh,basis,A,geo,n=200):
    B=make_B(mesh,basis,A); Rs=geo['Rs'];zb=geo['zb']-3e-3;zt=geo['zt']+3e-3
    eps=1e-5
    def avg(r,z):
        b1=B(r-eps*0,z+eps);b2=B(r-eps*0,z-eps);return (b1[0]+b2[0])/2,(b1[1]+b2[1])/2
    r=(np.arange(n)+.5)/n*Rs
    Brt,Bzt=avg(r,np.full(n,zt)); Brb,Bzb=avg(r,np.full(n,zb))
    top=np.sum((Bzt**2-Brt**2)/(2*MU0)*2*np.pi*r*(Rs/n))
    bot=np.sum((Bzb**2-Brb**2)/(2*MU0)*2*np.pi*r*(Rs/n))
    z=zb+(np.arange(n)+.5)/n*(zt-zb)
    e=1e-5
    b1=B(np.full(n,Rs-e),z);b2=B(np.full(n,Rs+e),z)
    Brs=(b1[0]+b2[0])/2;Bzs=(b1[1]+b2[1])/2
    side=np.sum(Bzs*Brs/MU0*2*np.pi*Rs*((zt-zb)/n))
    return top-bot+side
if __name__=="__main__":
    # validacion con aire (mur=1) contra Biot-Savart: iman 15x7.5, bobina Ri=4 Ro=17 H=20, N=581, gap 20 mm -> 12.0 gf/A
    for g in (0.010,0.020):
        res=[]
        for I in (0.0,1.0):
            m,b,A,geo=solve(g,I,Rc=2.5e-3,Ri=4e-3,mur=1.0,core=False)
            res.append(force_z(m,b,A,geo))
        print("aire g=%d mm: F(1A)-F(0)= %.2f gf (esperado %s)"%(g*1e3,(res[1]-res[0])/9.81*1e3,"12.0" if g==0.02 else "39.0"))
