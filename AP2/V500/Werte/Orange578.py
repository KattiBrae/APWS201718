import numpy as np
import sympy
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Orange578')

x, y = np.loadtxt('Orange578.txt', unpack=True,delimiter=',')
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
plt.plot(x_new,f(x_new,*popt),'-', label='$\lambda = 578nm$')
plt.ylabel('$\sqrt{I}$ / $\sqrt{nA}$')
plt.xlabel('U / V')
plt.grid()
plt.legend()

#[-1.00920485  0.58087581]
#[[ 0.0013733  -0.00045685]
# [-0.00045685  0.00017846]]


plt.savefig('Orange578.pdf')
print ('Fertig')
