"""Magnetostatica 3D con potencial escalar reducido: H = Hs - grad(phi);  div(mu H + M)=0.
Hs = campo de Biot-Savart de las bobinas (espiras filamentarias); hierro lineal (mur); iman por magnetizacion M.
Fuerza sobre el iman: Fz = Mz * (Int_cara_sup Bz dS - Int_cara_inf Bz dS)   (resta de la corrida solo-iman en aire)."""
import numpy as np, gmsh, sys
sys.path.insert(0,'.')
from lev import loop_B
from skfem import *
import pyamg, scipy.sparse.linalg as spl
MU0=4e-7*np.pi; mm=1e-3
def mesh_geom(cores, mag, box=(110,110,-70,150), hc=1.0, hm=2.0, hfar=18.0, fn="g.msh"):
    gmsh.initialize(); gmsh.option.setNumber("General.Terminal",0)
    gmsh.model.add("m"); oc=gmsh.model.occ
    x,y,z0,z1=box
    B=oc.addBox(-x,-y,z0,2*x,2*y,z1-z0)
    objs=[]
    for (cx,cy,za,zb,R) in cores: objs.append((3,oc.addCylinder(cx,cy,za,0,0,zb-za,R)))
    cx,cy,za,zb,R=mag; M=oc.addCylinder(cx,cy,za,0,0,zb-za,R)
    out,_=oc.fragment([(3,B)],objs+[(3,M)]); oc.synchronize()
    tags={}
    for d,t in out:
        c=gmsh.model.occ.getCenterOfMass(d,t); tags[t]=c
    # clasificar por centro de masa
    core_t=[];mag_t=None;air_t=None
    for t,c in tags.items():
        if abs(c[0]-mag[0])<1e-6 and abs(c[1]-mag[1])<1e-6 and abs(c[2]-(mag[2]+mag[3])/2)<1e-3: mag_t=t;continue
        isc=False
        for k in cores:
            if abs(c[0]-k[0])<1e-6 and abs(c[1]-k[1])<1e-6 and abs(c[2]-(k[2]+k[3])/2)<1e-3: isc=True
        if isc: core_t.append(t)
        else: air_t=t
    gmsh.model.addPhysicalGroup(3,[air_t],1);gmsh.model.addPhysicalGroup(3,core_t,2);gmsh.model.addPhysicalGroup(3,[mag_t],3)
    surf=[e for d,t in out if t in core_t+[mag_t] for e in [b[1] for b in gmsh.model.getBoundary([(3,t)],oriented=False)]]
    f=gmsh.model.mesh.field
    f.add("Distance",1);f.setNumbers(1,"FacesList",surf);f.setNumber(1,"Sampling",40)
    f.add("Threshold",2);f.setNumber(2,"InField",1);f.setNumber(2,"SizeMin",hc);f.setNumber(2,"SizeMax",hfar);f.setNumber(2,"DistMin",1.0);f.setNumber(2,"DistMax",60)
    f.setAsBackgroundMesh(2)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary",0);gmsh.option.setNumber("Mesh.MeshSizeFromPoints",0);gmsh.option.setNumber("Mesh.MeshSizeFromCurvature",0)
    gmsh.model.mesh.generate(3)
    nt,co,_=gmsh.model.mesh.getNodes(); co=co.reshape(-1,3); idx={int(t):i for i,t in enumerate(nt)}
    tag=np.zeros(0,int); T=[];L=[]
    for pg,lab in ((1,1),(2,2),(3,3)):
        for e in gmsh.model.getEntitiesForPhysicalGroup(3,pg):
            et,_,en=gmsh.model.mesh.getElements(3,e)
            for ty,nn in zip(et,en):
                if ty==4:
                    nn=nn.reshape(-1,4); T.append(np.vectorize(idx.get)(nn)); L+= [lab]*len(nn)
    gmsh.finalize()
    return co,np.vstack(T),np.array(L)
def coil_Hs(P,coils,NI,Ri=3.0,Ro=16.5,H=23.0,nr=4,nz=8):
    """H de Biot-Savart (A/m) en puntos P (mm). coils: lista de (cx,cy,zbot) en mm."""
    Hx=np.zeros(len(P));Hy=np.zeros(len(P));Hz=np.zeros(len(P))
    rr=Ri+(np.arange(nr)+.5)*(Ro-Ri)/nr; zz=(np.arange(nz)+.5)*H/nz
    for (cx,cy,zb) in coils:
        dx=(P[:,0]-cx)*mm;dy=(P[:,1]-cy)*mm;rho=np.hypot(dx,dy);c=np.where(rho>1e-12,dx/np.maximum(rho,1e-12),0);s=np.where(rho>1e-12,dy/np.maximum(rho,1e-12),0)
        for a in rr:
            for z0 in zz:
                Br,Bz=loop_B(a*mm,(zb+z0)*mm,rho,P[:,2]*mm,NI/(nr*nz))
                Hx+=Br*c/MU0;Hy+=Br*s/MU0;Hz+=Bz/MU0
    return Hx,Hy,Hz

def run(co,T,L,coils,I,N,mur,Br,mag,sign=-1,Rm=10.0):
    """co en mm. devuelve Fz [N] (sin restar la linea base)."""
    mesh=MeshTet(co.T*mm,T.T.copy())
    cen=co[T].mean(axis=1)                    # mm
    Hx,Hy,Hz=coil_Hs(cen,coils,N*I) if I!=0 else (np.zeros(len(T)),)*3
    nu=np.where(L==2,mur,1.0)*MU0
    Mz=np.where(L==3,sign*Br/MU0,0.0)
    basis=Basis(mesh,ElementTetP1())
    def F(a): return np.repeat(a[:,None],basis.X.shape[1],axis=1)
    @BilinearForm
    def a(u,v,w): return w.mu*(u.grad[0]*v.grad[0]+u.grad[1]*v.grad[1]+u.grad[2]*v.grad[2])
    @LinearForm
    def l(v,w): return (w.mu*w.hx)*v.grad[0]+(w.mu*w.hy)*v.grad[1]+(w.mu*w.hz+MU0*w.mz)*v.grad[2]
    K=a.assemble(basis,mu=F(nu)); b=l.assemble(basis,mu=F(nu),hx=F(Hx),hy=F(Hy),hz=F(Hz),mz=F(Mz))
    D=basis.get_dofs().all()
    I_=basis.complement_dofs(D)
    Kc=K[I_][:,I_].tocsr(); bc=b[I_]
    ml=pyamg.smoothed_aggregation_solver(Kc)
    x=np.zeros(basis.N); x[I_]=ml.solve(bc,tol=1e-10,accel="cg",maxiter=300)
    g=basis.interpolate(x).grad            # (3,nel,nq)
    gz=g[2][:,0]
    Bz=MU0*(Hz-gz)*np.where(L==2,mur,1.0)+MU0*Mz     # B = mu(H)+mu0 M
    # caras del iman
    f2t=mesh.f2t; fp=mesh.p[:,mesh.facets]    # (3,3,nf)
    zt=mag[3]*mm; zb=mag[2]*mm; cxm,cym=mag[0]*mm,mag[1]*mm
    zc=fp[2].mean(axis=0); rc=np.hypot(fp[0].mean(axis=0)-cxm,fp[1].mean(axis=0)-cym)
    area=0.5*np.linalg.norm(np.cross(fp[:,1]-fp[:,0],fp[:,2]-fp[:,0],axis=0),axis=0)
    flat=(fp[2].max(axis=0)-fp[2].min(axis=0))<1e-9
    # recuperacion nodal de Bz usando solo elementos de aire (O(h^2))
    vol=np.abs(np.einsum('ij,ij->i',np.cross(co[T[:,1]]-co[T[:,0]],co[T[:,2]]-co[T[:,0]]),co[T[:,3]]-co[T[:,0]]))/6
    w=np.where(L==1,vol,0.0)
    num=np.zeros(len(co));den=np.zeros(len(co))
    for k in range(4):
        np.add.at(num,T[:,k],w*Bz);np.add.at(den,T[:,k],w)
    Bn=num/np.maximum(den,1e-30)
    out=0.0
    for zface,sg in ((zt,+1),(zb,-1)):
        sel=np.where(flat&(abs(zc-zface)<1e-7)&(rc<=Rm*mm+1e-6)&(f2t[1]>=0))[0]
        for f in sel:
            t0,t1=f2t[0,f],f2t[1,f]
            nodes=mesh.facets[:,f]
            out+=sg*Bn[nodes].mean()*area[f]
    return Mz[L==3][0]*out
