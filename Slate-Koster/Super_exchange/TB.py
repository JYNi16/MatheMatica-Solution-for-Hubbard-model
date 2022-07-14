import matplotlib.pyplot as plt 
import numpy as np 
import math 

pi = math.pi 
x = np.linspace(0,pi/2,1000)
y = -0.2*(np.tan(x))


plt.figure(figsize=(7,6))
plt.text(0.05,-3.8,'(b)',fontproperties = 'Times New Roman', size = 22)
plt.plot(x,y,linewidth = 4,label=r'$t_{23}/t_{22}$')
#legend = plt.legend(loc=1,  fontsize='x-large',frameon=False)
#legend.get_title().set_fontsize(fontsize = 20)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.xlim(0,pi/2)
plt.ylim(-4,0.1)
xticks  = [0.0,pi/6,pi/3,pi/2]
xticks_label = ['$0$',r'$\pi/6$',r'$\pi/3$',r'$\pi/2$']
plt.xticks(xticks,xticks_label, fontproperties = 'Times New Roman', size = 14)
plt.xlabel(r'$\theta$',fontproperties = 'Times New Roman',size = 18)
plt.ylabel(r'$\alpha(t_{23}/t_{22})$',fontproperties = 'Times New Roman',size = 18)
yticks  = [-4,-3,-2,-1,0]
plt.yticks(yticks,fontproperties = 'Times New Roman', size = 14)
plt.savefig("beta.jpg",dpi=300)