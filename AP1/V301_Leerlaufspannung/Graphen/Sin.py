
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show



x, y = np.loadtxt('Sin.txt', unpack=True,delimiter=',')



def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 50000)

plt.plot(x_new,f(x_new,*popt),'-', label='Ausgleichsrechnug')




plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')


plt.xlabel('$I/mA$')
plt.ylabel('$U/Vs$')
plt.grid()
plt.legend()




plt.savefig('Sin.pdf')
print ('Fertig')