# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:52:34 2015

@author: Luca Urpi
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def out_arr( outfile,list):
 filename=outfile
 f = open(filename, 'w')
 print >> f, "\n".join(list)
 f.close()
 return;
 
dip=np.radians(65)  
r0="taskB-3d_time_INJ_POINT_03.tec"
r1="taskB-3d_time_MP_18above.tec"
r3="taskB-3d_time_MONITORING2.tec"
r2="taskB-3d_time_MP_18below.tec"


column_hist1 = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)"," Effective_Strain")
column_hist0 = ("TIME","STRAIN_PLS","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","p_(1st_Invariant)","q_(2nd_Invariant)","Effective_Strain")
column_hist3 = ("TIME","STRAIN_PLS","VELOCITY_X1","VELOCITY_Y1","VELOCITY_Z1","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","PRESSURE1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","p_(1st_Invariant)","q_(2nd_Invariant)"," Effective_Strain")

p0 = pd.read_csv(r0, skiprows=2, header=0, names=column_hist0, delimiter=r"\s+")  

p1 = pd.read_csv(r1, skiprows=2, header=0, names=column_hist3, delimiter=r"\s+")  
p2 = pd.read_csv(r2, skiprows=2 ,header=0, names=column_hist3, delimiter=r"\s+")  
p3 = pd.read_csv(r3, skiprows=2, header=0, names=column_hist1, delimiter=r"\s+") 
X= p0["TIME"].values
X1= p1["TIME"].values
X2= p2["TIME"].values
P= p0["PRESSURE1"].values
P3= p3["PRESSURE1"].values
#v_x1_0= p0["VELOCITY_X1"].values
v_x1_1= p1["VELOCITY_X1"].values
v_x1_2= p2["VELOCITY_X1"].values
#v_y1_0= p0["VELOCITY_Y1"].values
v_y1_1= p1["VELOCITY_Y1"].values
v_y1_2= p2["VELOCITY_Y1"].values
#v_z1_0= p0["VELOCITY_Z1"].values
v_z1_1= p1["VELOCITY_Z1"].values
v_z1_2= p2["VELOCITY_Z1"].values

v_yavg=[]
v_zavg=[]
v_inj=[]
flow=[] #l/min
for i in range(len(v_y1_1)):
    v_yavg.append((v_y1_1[i]-v_y1_2[i])/2)
    v_zavg.append((v_z1_1[i]-v_z1_2[i])/2)
    v_inj.append(np.cos(dip)*v_yavg[i]+np.sin(dip)*v_zavg[i])
    flow.append(v_inj[i]*0.025*2*np.pi*0.18*1000*60)

"""
fig3 = plt.figure(figsize=(12,6))
ax1 = fig3.add_subplot(111)

#ax1.plot(X[0:-6], Dy[0:-6]*1e6, 'b-', lw=2.5,label='Dy')
#ax1.plot(X[0:-6], Dz[0:-6]*1e6, 'g-', lw=2.5,label='Dz')
#ax1.plot(X[0:-6], Dy2[0:-6]*1e6, 'b-.',lw=2.5, label='Dy bottom anchor')
#ax1.plot(X[0:-6], Dz2[0:-6]*1e6, 'g-.',lw=2.5, label='Dz bottom anchor')

#ax2 = ax1.twinx()
#ax1.plot(-1000, 5, 'b-', lw=2.5,label='Dy')
#ax2.plot(-1000, 5, 'g-', lw=2.5,label='Dz')
ax1.plot(X, flow, 'r--', lw=1.5,label='Injection pressure')
ax1.set_xlabel('Time (s)', fontsize=28)
ax1.set_ylabel('Flow rate (l/min)', fontsize=28)
ax1.tick_params(axis='y', labelsize=24)
#ax2.tick_params(axis='y', labelsize=28)
ax1.tick_params(axis='x', labelsize=24)
#ax1.set_ylim(0,7)
max_X=1.5*(min(np.amax(X),440))
ax1.set_xlim(0,max_X)
#ax2.set_xlim(0,800)
#ax2 = ax1.twinx()
#ax2.plot(X_st/86400, lake_level, 'k--', label='water level')
#ax2.set_ylabel('Lake level', fontsize=20)
plt.tight_layout()
plt.legend()
plt.grid()
plt.show()
"""
beta = dip-np.radians(90) #= -25 
#d0="taskB-3d_DEFORMATION_P3.tec"

#column_hist1 = ("TIME","STRAIN_PLS","DISPLACEMENT_X1","DISPLACEMENT_Y1","DISPLACEMENT_Z1","STRESS_XX","STRESS_YY","STRESS_ZZ","STRESS_XY","STRESS_XZ","STRESS_YZ","p_(1st_Invariant)","q_(2nd_Invariant)")

#e0 = pd.read_csv(d0, skiprows=2, header=0, names=column_hist1, delimiter=r"\s+")  

sxx0= p3["STRESS_XX"].values
syy0= p3["STRESS_YY"].values
szz0= p3["STRESS_ZZ"].values
sxz0= p3["STRESS_XZ"].values
syz0= p3["STRESS_YZ"].values
dxt = p3["DISPLACEMENT_X1"].values
dyt = p3["DISPLACEMENT_Y1"].values
dzt = p3["DISPLACEMENT_Z1"].values
dx0 = p3["DISPLACEMENT_X1"].values-dxt[1]
dy0 = p3["DISPLACEMENT_Y1"].values-dyt[1]
dz0 = p3["DISPLACEMENT_Z1"].values-dzt[1]

"""
fracture normal displacement and shear and normal stresses 
normal stress = sxx_z1*(cos(beta)^2)+(2*sxz*sin(beta)*cos(beta))+(szz*((sin(beta)^2))
shear stress =  -((0.5*(szz - sxx )*sin(2*beta))+(sxz *cos(2*beta)))
"""

n_stress=[]
s_stress=[]
n_displ=[]
ratio=[]

cb=np.cos(beta)
sb=np.sin(beta)
c2b=np.cos(beta)*np.cos(beta)
s2b=np.sin(beta)*np.sin(beta)
cb2=np.cos(2*beta)
sb2=np.sin(2*beta)
for i in range(len(sxx0)):
    n_stress.append(syy0[i]*c2b+(2*syz0[i]*sb*cb)+(szz0[i]*s2b))
    s_stress.append(-(0.5*(szz0[i] - syy0[i])*sb2)+(syz0[i]*cb2))
    ratio.append(np.abs(s_stress[i]/n_stress[i]))
    n_displ.append(np.cos(dip)*dz0[i]-np.sin(dip)*dy0[i])

n_displ[0]=0.0

point_out=[]
point_out.append("Output P3 point")
point_out.append("time (s) Pressure(Pa) flowrate(l/min) normal_displ(m) normal_stress(Pa) shear_stress(Pa)")
for jjj in range(len(X)):
   txt0=str(X[jjj])   
   txt=txt0
   txt1=str(P3[jjj])
   txt=txt+" "+txt1
   txt2=str(flow[jjj])
   txt=txt+" "+txt2
   txt3=str(n_displ[jjj])
   txt=txt+" "+txt3
   txt4=str(n_stress[jjj])
   txt=txt+" "+txt4
   txt5=str(s_stress[jjj])
   txt=txt+" "+txt5
   point_out.append(txt)

out_filename="P3_output.dat"
print "\nWriting P3 output"
out_arr(out_filename,point_out)
#X_st= X_st[0:-5]

