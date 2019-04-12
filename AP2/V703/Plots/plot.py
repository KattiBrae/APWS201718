
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('tab2.txt', unpack=True,delimiter=',')
T=np.sqrt(y)



plt.plot(x, y, "kx", label="Messwerte")
plt.errorbar(x, y, yerr=T, fmt="none", capsize=5, capthick=2, ms=9, markerfacecolor="red")

c, v = np.loadtxt('tab2.txt', unpack=True,delimiter=',')
def f(c,a,b):
    return a*c+b
popt, pcov = curve_fit(f, c, v)
print(popt)
print(np.diag(pcov))
print(np.sqrt(np.diag(pcov)))
c_new = np.linspace(x[1], x[-1], 500)

plt.figure(1)
#plt.plot(x,y,'x')
plt.plot(c_new,f(c_new,*popt),'-', label='Lineare Regression')
plt.xlabel('Spannung U / V')
plt.ylabel('N/t $/$ 1/min')
plt.grid()
plt.legend()



plt.savefig('Graphik1.pdf')
print ('Fertig')
