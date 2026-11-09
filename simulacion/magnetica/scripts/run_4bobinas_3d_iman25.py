import numpy as np, fem3d as f, json, sys
Rm=12.7; Lm=2.1; N=652; CC=18.5; Wgf=7.94
pos=[(CC,CC),(-CC,CC),(-CC,-CC),(CC,-CC)]
def case(gf,hc,ncoil=4):
    zb=26.0+gf; mag=(0,0,zb,zb+Lm,Rm); P=pos[:ncoil]
    cores=[(x,y,-11.0,34.0,3.0) for x,y in P]
    co,T,L=f.mesh_geom(cores,mag,hc=hc,hfar=15.0)
    coils=[(x,y,0.0) for x,y in P]
    r=lambda I,mur:f.run(co,T,L,coils,I,N,mur,1.31,mag,Rm=Rm)
    base=r(0.0,1.0);a=r(0.0,1000.0);b=r(1.0,1000.0)
    F0=(a-base)/9.81*1e3;F1=(b-a)/9.81*1e3;Ieq=(Wgf-F0)/F1
    print("gf %d hc %.2f n=%d tets %d: F0 %.2f gf F1 %.2f gf/A Ieq %.2f A"%(gf,hc,ncoil,len(T),F0,F1,Ieq),flush=True)
    return dict(gf=gf,hc=hc,n=ncoil,F0=F0,F1=F1,Ieq=Ieq)
out=[]
for gf,hc in ((30,1.0),(30,0.7),(25,1.0),(25,0.7),(35,1.0),(35,0.7),(20,1.0),(20,0.7)):
    out.append(case(gf,hc)); json.dump(out,open("res4coil_iman25.json","w"))
