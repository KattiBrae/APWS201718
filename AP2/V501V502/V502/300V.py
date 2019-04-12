
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Messreihe2  300V')
x, y = np.loadtxt('300V.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(x,y,'o')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.ylabel('Höhe / cm')
plt.xlabel('B-Feld / mT')
plt.grid()
plt.legend()




plt.savefig('300V.pdf')
print ('Fertig')
