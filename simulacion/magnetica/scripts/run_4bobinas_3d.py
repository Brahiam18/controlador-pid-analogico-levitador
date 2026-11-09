import numpy as np, fem3d as f, time, json, sys
Rm=10.0; N=652; CC=18.5; W=np.pi*(Rm*1e-3)**2*4.2e-3*7.5e3*9.81
pos=[(CC,CC),(-CC,CC),(-CC,-CC),(CC,-CC)]
res={}
def case(gf,hc,ncoil,core=True):
    zb=26.0+gf; mag=(0,0,zb,zb+4.2,Rm)
    P=pos[:ncoil]
    cores=[(x,y,-11.0,34.0,3.0) for x,y in P]
    co,T,L=f.mesh_geom(cores,mag,hc=hc,hfar=15.0)
    coils=[(x,y,0.0) for x,y in P]
    base=f.run(co,T,L,coils,0.0,N,1.0,1.31,mag)
    mur=1000.0 if core else 1.0
    a=f.run(co,T,L,coils,0.0,N,mur,1.31,mag);b=f.run(co,T,L,coils,1.0,N,mur,1.31,mag)
    F0=(a-base)/9.81*1e3;F1=(b-a)/9.81*1e3
    Ieq=(W/9.81*1e3-F0)/F1
    print("gf %d hc %.2f n=%d core=%s tets %d: F0 %.2f gf, F1 %.2f gf/A (total), Ieq %.2f A"%(gf,hc,ncoil,core,len(T),F0,F1,Ieq),flush=True)
    return dict(gf=gf,hc=hc,n=ncoil,core=core,F0=F0,F1=F1,Ieq=Ieq)
out=[]
for gf in (20,25,30,35):
    for hc in (1.0,0.7):
        out.append(case(gf,hc,4))
json.dump(out,open("res4coil.json","w"))
