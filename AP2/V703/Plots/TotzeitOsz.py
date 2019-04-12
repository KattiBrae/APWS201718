
#import numpy as np
#import sympy
#import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
#from pylab import figure, axes, pie, title, show
#
#print('Totzeit Oszilloskop')
#print('Steigung','Y-Achsenabschnitt')
#x, y = np.loadtxt('Totzeit.txt', unpack=True,delimiter=',')
#
#
#plt.figure(1)
#plt.plot(x,y,'x', label='Messwerte')
#plt.xlabel('Spannung U in V')
#plt.ylabel('N/t in 1/min')
#plt.grid()
#plt.legend()
#plt.savefig('Totzeit.pdf')
#print ('Fertig')
#


import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
#x, y = np.loadtxt('Totzeit.txt', unpack=True,delimiter=',')
#T=np.sqrt(y)
#
#plt.plot(x, y, "kx", label="Messwerte")
#plt.errorbar(x, y, yerr=T, fmt="none", capsize=5, capthick=2, ms=9, markerfacecolor="red")
#
c, v = np.loadtxt('Totzeit.txt', unpack=True,delimiter=',')
def f(c,a,b):
    return a*c+b
popt, pcov = curve_fit(f, c, v)
print(popt)
print(np.diag(pcov))
print(np.sqrt(np.diag(pcov)))
c_new = np.linspace(c[0], c[-1], 500)

plt.figure(1)
plt.plot(c,v,'x', label='Messwerte')
plt.plot(c_new,f(c_new,*popt),'-', label='Lineare Regression')
plt.xlabel('Spannung U $/$ V')
plt.ylabel('t $/$ min$\cdot 10^{-6}$')
plt.grid()
plt.legend()



plt.savefig('Totzeit2.pdf')
print ('Fertig')
