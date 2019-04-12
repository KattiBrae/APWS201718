import numpy as np
import sympy
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Violett405')

x, y = np.loadtxt('Violett405.txt', unpack=True,delimiter=',')
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
plt.plot(x_new,f(x_new,*popt),'-', label='$\lambda = 405nm$')
plt.ylabel('$\sqrt{I}$ / $\sqrt{nA}$')
plt.xlabel('U / V')
plt.grid()
plt.legend()

#[-1.08433154  1.08174944]
#[[  3.05247754e-04  -9.47378022e-05]
# [ -9.47378022e-05   4.33247566e-05]]


plt.savefig('Violett405.pdf')
print ('Fertig')
