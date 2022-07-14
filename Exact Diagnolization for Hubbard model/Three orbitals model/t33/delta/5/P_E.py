import matplotlib.pyplot as plt 
import numpy as np
from scipy.interpolate import make_interp_spline 

t = []
J = []
K = []
E0 = []
E1 = []
E2 = []
E3 = []
K = []
B1 = []
B2 = []
t1 = []
t2 = []

k = 0 

with open('S.dat','r') as f1:
    l = f1.readlines()
    for i in l:
        i = i.split()
        t.append(np.float(i[0]))
        E0.append(np.float(i[1]))
        E1.append(np.float(i[2]))
        E2.append(np.float(i[3]))
        E3.append(np.float(i[4]))


       

with open('S1.dat','r') as f2:
    m = f2.readlines()
    for j in m:
        j = j.split()
        t1.append(np.float(j[0]))
        B1.append(-((np.float(j[1]))/3 + (np.float(j[3]))/6 - (np.float(j[2]))/2)/(((np.float(j[3]))-(np.float(j[2])))*0.5))
with open('S2.dat','r') as f3:
    w = f3.readlines()
    for k in w:
        k = k.split()
        t2.append(np.float(k[0]))
        B2.append(-((np.float(k[1]))/3 + (np.float(k[3]))/6 - (np.float(k[2]))/2)/(((np.float(k[3]))-(np.float(k[2])))*0.5))
       
       

plt.figure(figsize=(14,7))
p1 = plt.subplot(121)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.text(1.9,4.43,'(a)',fontproperties = 'Times New Roman', size = 22)
p1.plot(t, E0,Linewidth = 4, label='S=0')
p1.plot(t, E1,Linewidth = 4,label='S=1')
p1.plot(t, E2,Linewidth = 4, label='S=2')
p1.plot(t,E3, Linewidth = 4,Label = 'Next-one')
plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
plt.ylabel('Energy(eV)',fontproperties = 'Times New Roman',size = 18)
plt.legend(loc = 3)
p2 = plt.subplot(122)
plt.text(1.9,0.85,'(b)',fontproperties = 'Times New Roman', size = 22)
p2.plot(t1,B1,color ='red',linewidth=4)
p2.plot(t2,B2,color ='red',linewidth=4)
plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
plt.ylabel(r'$\beta$',fontproperties = 'Times New Roman',size = 18)
plt.xticks(fontproperties = 'Times New Roman', size = 14)
plt.yticks(fontproperties = 'Times New Roman', size = 14)
#plt.vlines(1,-1.5,1.5,color = 'black', linewidth = 1)
#plt.legend(loc=2)
plt.ylim(-1.0,1.0)
plt.savefig('beta_K.jpg',dpi=500)