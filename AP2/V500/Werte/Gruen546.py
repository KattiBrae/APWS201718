import numpy as np
import sympy
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Gruen546')

x, y = np.loadtxt('Gruen546.txt', unpack=True,delimiter=',')
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
plt.plot(x_new,f(x_new,*popt),'-', label='$\lambda = 546nm$')
plt.ylabel('$\sqrt{I}$ / $\sqrt{nA}$')
plt.xlabel('U / V')
plt.grid()
plt.legend()

#[-1.16100461  0.83029471]
#[[ 0.00224458 -0.00077371]
# [-0.00077371  0.00034232]]


plt.savefig('Gruen546.pdf')
print ('Fertig')
