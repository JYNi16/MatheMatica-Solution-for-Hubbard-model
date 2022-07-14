import matplotlib.pyplot as plt 
import numpy as np 

t = []
J1 = []
K1 = []
J2 = []
K2 = []

with open('5.dat','r') as f1:
    l = f1.readlines()
    for i in l:
        i = i.split()
        t.append(np.float(i[0]))
        J1.append(((np.float(i[3]))-(np.float(i[2])))*0.5)
        K1.append((np.float(i[1]))/3 + (np.float(i[3]))/6 - (np.float(i[2]))/2)
        
with open('6.dat','r') as f2:
    l = f2.readlines()
    for j in l:
        j = j.split()
        J2.append(((np.float(j[3]))-(np.float(j[2])))*0.5)
        K2.append((np.float(j[1]))/3 + (np.float(j[3]))/6 - (np.float(j[2]))/2)

plt.figure(figsize=(12,6))
p1 = plt.subplot(121)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
p1.text(0.0,-0.03,'(a)',fontproperties = 'Times New Roman', size = 20)
p1.plot(t,J1,'-',color='#008800',linewidth =4,label = 'J')
p1.plot(t,K1,'-',color='Red',linewidth =4,label='K')
plt.xticks(fontproperties = 'Times New Roman', size = 14)
plt.yticks(fontproperties = 'Times New Roman', size = 14)
plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
plt.ylabel('Energy($eV$)',fontproperties = 'Times New Roman',size = 18)
plt.xlim(-0.1,2.1)
#plt.ylim(-0.06,0.02)
plt.legend(loc=1)
p2 = plt.subplot(122)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
p2.text(0.0,-0.03,'(b)',fontproperties = 'Times New Roman', size = 20)
p2.plot(t,J2,'-',color = '#008800',linewidth =4,label = 'J')
p2.plot(t,K2,'-',color='Red',linewidth =4,label='K')
plt.xticks(fontproperties = 'Times New Roman', size = 14)
plt.yticks(fontproperties = 'Times New Roman', size = 14)
plt.xlabel('$t_{23}$/$t_{22}$',fontproperties = 'Times New Roman',size = 18)
#plt.ylabel('Energy($eV$)',fontproperties = 'Times New Roman',size = 18)
plt.xlim(-0.1,2.1)
#plt.ylim(-0.06,0.02)
plt.legend(loc=1)
plt.savefig("U.jpg",dpi=300)
