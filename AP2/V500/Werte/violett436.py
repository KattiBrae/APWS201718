import numpy as np
import sympy
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Violett436')

x, y = np.loadtxt('Violett436.txt', unpack=True,delimiter=',')
h= y**(0.5)
def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, h)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)
#xyab
plt.figure(1)
plt.plot(x,h,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='$\lambda = 436nm$')
plt.ylabel('$\sqrt{I}$ / $\sqrt{nA}$')
plt.xlabel('U / V')
plt.grid()
plt.legend()

#[-0.53740846  0.61868258]
#[[ 0.00216784 -0.00084567]
# [-0.00084567  0.00049762]]




plt.savefig('Violett436.pdf')
print ('Fertig')
