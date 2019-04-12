
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show



x, y = np.loadtxt('Freq.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return np.exp(-a*x+b)
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 50000)







plt.figure(1)

plt.plot(x,y,'x', label ='Messwerte')
plt.plot(x_new,f(x_new,*popt),'-', label='Ausgleichsrechnug')
plt.xscale('log')

plt.ylabel('$U_c$/ V ')
plt.xlabel('$f$/Hz')
plt.grid()
plt.legend()




plt.savefig('Freq.pdf')
print ('Fertig')
