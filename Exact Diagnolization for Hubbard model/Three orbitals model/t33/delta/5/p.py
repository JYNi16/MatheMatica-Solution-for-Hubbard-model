import matplotlib.pyplot as plt 
import numpy as np
from scipy.interpolate import make_interp_spline 
import math 

t = []
J = []
K = []
B1 = []
B2 = []
t1 = []
t2 = []

k = 0 
pi = math.pi 
x = np.linspace(0,pi/2,1000)
y = -0.2*(np.tan(x))



with open('S.dat','r') as f1:
    l = f1.readlines()
    for i in l:
        i = i.split()
        t.append(np.float(i[0]))
        J.append(((np.float(i[3]))-(np.float(i[2])))*0.5)
        K.append((np.float(i[1]))/3 + (np.float(i[3]))/6 - (np.float(i[2]))/2)         
    

plt.figure(figsize=(7,6))
#p1 = plt.subplot(121)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(t,J,'-',color = '#008800',linewidth=4,label = '$J$')
plt.plot(t,K,'-',color='Red',linewidth=4,label='$K$')
#plt.text(0.0,-0.0565,'(a)',fontproperties = 'Times New Roman', size = 22)
legend = plt.legend(loc='best',  fontsize='xx-large',frameon=False)
legend.get_title().set_fontsize(fontsize = 20)
xticks = [0,0.5,1,1,1.5,2]
plt.xticks(xticks,fontproperties = 'Times New Roman', size = 14)
yticks = [-0.06,-0.04,-0.02,0,0.02]
plt.yticks(yticks,fontproperties = 'Times New Roman', size = 14)
plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
plt.ylabel('Energy(eV)',fontproperties = 'Times New Roman',size = 18)
plt.xlim(-0.1,2.1)
plt.ylim(-0.06,0.02)
legend = plt.legend(loc=1,  fontsize='x-large',frameon=False)
legend.get_title().set_fontsize(fontsize = 20)
#p2 = plt.subplot(122)
#plt.text(0.05,-3.8,'(b)',fontproperties = 'Times New Roman', size = 22)
#p2.plot(x,y,linewidth = 4,label=r'$t_{23}/t_{22}$')
#legend = plt.legend(loc=1,  fontsize='x-large',frameon=False)
#legend.get_title().set_fontsize(fontsize = 20)
#plt.rcParams['xtick.direction'] = 'in'
#plt.rcParams['ytick.direction'] = 'in'
#plt.xlim(0,pi/2)
#plt.ylim(-4,0.1)
#xticks  = [0.0,pi/6,pi/3,pi/2]
#xticks_label = ['$0$',r'$\pi/6$',r'$\pi/3$',r'$\pi/2$']
#plt.xticks(xticks,xticks_label, fontproperties = 'Times New Roman', size = 14)
#plt.xlabel(r'$\pi-\theta$',fontproperties = 'Times New Roman',size = 18)
#plt.ylabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
#yticks  = [-4,-3,-2,-1,0]
#plt.yticks(yticks,fontproperties = 'Times New Roman', size = 14)
plt.savefig('t23.jpg',dpi=500)