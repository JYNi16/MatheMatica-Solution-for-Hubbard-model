import matplotlib.pyplot as plt 
import numpy as np
from scipy.interpolate import make_interp_spline 

t = []
J = []
K = []
B1 = []
B2 = []
t1 = []
t2 = []

k = 0 

       

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
                
    

plt.figure(figsize=(7,6))
#plt.plot(t, E0,Linewidth = 3, label='S=0')
#plt.plot(t, E1,Linewidth = 3,label='S=1')
#plt.plot(t, E2,Linewidth = 3, label='S=2')
#plt.plot(t,E3, Linewidth = 3,Label = 'Next-one')
#plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
#plt.ylabel('E(eV)',fontproperties = 'Times New Roman',size = 18)
#plt.ylim(4.4,5.0)
#plt.legend(loc = 3)
#p2 = plt.subplot(121)
#plt.rcParams['xtick.direction'] = 'in'
#plt.rcParams['ytick.direction'] = 'in'
#legend = plt.legend(loc='best',  fontsize='xx-large',frameon=False)
#legend.get_title().set_fontsize(fontsize = 20)
#plt.text(0.0,-0.056,'(a)',fontproperties = 'Times New Roman', size = 22)
#plt.plot(t,J,'-',color='#008B8B',linewidth=4,label = '$J$')
#plt.plot(t,K,'-',color='#FA8072',linewidth=4,label='$K$')
#xticks = [0,0.5,1,1,1.5,2]
#plt.xticks(xticks,fontproperties = 'Times New Roman', size = 14)
#yticks = [-0.06,-0.04,-0.02,0,0.02]
#plt.yticks(yticks,fontproperties = 'Times New Roman', size = 14)
#plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
#plt.ylabel('Energy($eV$)',fontproperties = 'Times New Roman',size = 18)
#plt.xlim(-0.1,2.1)
#plt.ylim(-0.06,0.02)
#legend = plt.legend(loc=1,  fontsize='x-large',frameon=False)
#legend.get_title().set_fontsize(fontsize = 20)
#plt.hlines(0,-0.2,2.2,color = 'black', linewidth = 1)
#plt.legend(loc=1)
#p3 = plt.subplot(122)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#plt.text(0.0,-1.33,'(a)',fontproperties = 'Times New Roman', size = 22)
plt.plot(t1,B1,color ='red',linewidth=4)
plt.plot(t2,B2,color ='red',linewidth=4)
plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
plt.ylabel(r'$\beta$',fontproperties = 'Times New Roman',size = 18)
plt.xticks(fontproperties = 'Times New Roman', size = 14)
plt.yticks(fontproperties = 'Times New Roman', size = 14)
#plt.vlines(1,-1.5,1.5,color = 'black', linewidth = 1)
#plt.legend(loc=2)
plt.ylim(-1.0,1.0)
plt.savefig('beta.jpg',dpi=500)