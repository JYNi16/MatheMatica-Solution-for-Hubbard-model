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

with open('7.dat','r') as f1:
    l = f1.readlines()
    for i in l:
        i = i.split()
        t.append(np.float(i[0]))
        J.append(((np.float(i[3]))-(np.float(i[2])))*0.5)
        K.append((np.float(i[1]))/3 + (np.float(i[3]))/6 - (np.float(i[2]))/2)
       
    

plt.figure(figsize=(7,6))
#plt.rcParams['xtick.direction'] = 'in'
#plt.rcParams['ytick.direction'] = 'in'

#plt.text(0.0,-0.12,'(a)',fontproperties = 'Times New Roman', size = 22)
plt.plot(t,J,'-',color='#008800',linewidth=4,label = '$J$')
plt.plot(t,K,'-',color='red',linewidth=4,label='$K$')
xticks = [0,0.5,1,1.5,2,2.5,3,3.5,4]
plt.xticks(xticks,fontproperties = 'Times New Roman', size = 14)
yticks = [-0.12,-0.06,-0.0,0,0.05]
plt.yticks(yticks,fontproperties = 'Times New Roman', size = 14)
plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
plt.ylabel('Energy($eV$)',fontproperties = 'Times New Roman',size = 18)
legend = plt.legend(loc=1,  fontsize='x-large',frameon=False)
legend.get_title().set_fontsize(fontsize = 20)
plt.ylim(-0.13,0.05)
#plt.hlines(0,-0.2,2.2,color = 'black', linewidth = 1)
#plt.legend(loc=1)
#plt.vlines(1,-1.5,1.5,color = 'black', linewidth = 1)
#plt.legend(loc=2)
plt.savefig('JK.jpg',dpi=500)