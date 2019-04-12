import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show


print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('reichweite15.txt', unpack=True,delimiter=',')
T=np.sqrt(y)

plt.plot(x, y, "kx", label="Messwerte")
plt.errorbar(x, y, yerr=T, fmt="none", capsize=3, capthick=1, ms=9, markerfacecolor="red")

y=58601+0*x
plt.plot(y,label=r'$\frac{N_{0}}{2}$')


print('Erste Grade')
c, v = np.loadtxt('fit15.txt', unpack=True,delimiter=',')
def f(c,a,b):
    return a*c+b
popt, pcov = curve_fit(f, c, v)
print(popt)
print(np.diag(pcov))
c_new = np.linspace(x[15], x[-1], 500)
#
#
#
#print('Zweite Grade')
#q, w = np.loadtxt('beta3.txt', unpack=True,delimiter=',')
#def g(q,r,s):
#    return r*q+s
#pqpt, pcqv = curve_fit(g, q, w)
#print(pqpt)
#print(np.diag(pcqv))
#q_new = np.linspace(x[4], x[-1], 500)

plt.figure(1)
#plt.plot(x,y,'x')
plt.plot(c_new,f(c_new,*popt),'-', label='Lineare Regression')
#plt.plot(q_new,g(q_new,*pqpt),'-', label='Lineare Regression Hintergrundstrahlung')
plt.xlabel('Effektive Länge $x/ 10^{-3}m$')
plt.ylabel('Zählrate $N$')
plt.grid()
plt.legend()



plt.savefig('reichweite15.pdf')
print ('Fertig')
