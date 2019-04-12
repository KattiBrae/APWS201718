
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('rausch.txt', unpack=True,delimiter=',')

def f(x,a,b,c,d):
    return a*np.cos(b*x+c)+d
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label= r'$\cos{(\varphi)}$')
plt.xlabel(r'$\varphi/rad$')
plt.ylabel('A/V')
plt.grid()
plt.legend()




plt.savefig('rausch.pdf')
print ('Fertig')
