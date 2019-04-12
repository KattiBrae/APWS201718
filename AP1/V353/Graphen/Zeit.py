
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show



x, y = np.loadtxt('Zeit.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)






plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')


plt.ylabel(r'$\ln{ \left( \frac{U_c}{U_0} \right) }$')
plt.xlabel('$t/s$')
plt.grid()
plt.legend()




plt.savefig('Zeit.pdf')
print ('Fertig')
