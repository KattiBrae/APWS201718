
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('T_B')

x, y = np.loadtxt('tabel.txt', unpack=True,delimiter=',')

def f(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)






print('T_A')

z, u = np.loadtxt('tabel2.txt', unpack=True,delimiter=',')

def f(z,e,f,g,h):
    return e*z**3+f*z**2+g*z+h
popt2, pcov2 = curve_fit(f, z, u)
print(popt2)
print(pcov2)

z_new = np.linspace(z[0], z[-1], 500)




plt.figure(1)
plt.plot(x,y,'o')
plt.plot(z_new,f(z_new,*popt2),'-',label='$T_B$')
plt.plot(x_new,f(x_new,*popt),'-', label='$T_A$')
plt.plot(z,u,'o')

plt.xlabel('Zeit in min')
plt.ylabel('Temp in K')
plt.grid()
plt.legend()




plt.savefig('plot.pdf')
print ('Fertig')
