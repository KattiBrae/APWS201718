import numpy as np
import sympy
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Cyan492')

x, y = np.loadtxt('Cyan492.txt', unpack=True,delimiter=',')
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
plt.plot(x_new,f(x_new,*popt),'-', label='$\lambda = 492nm$')
plt.ylabel('$\sqrt{I}$ / $\sqrt{nA}$')
plt.xlabel('U / V')
plt.grid()
plt.legend()

#[-0.38439415  0.2909924 ]
#[[  3.04888360e-05  -8.67915523e-06]
# [ -8.67915523e-06   3.96556087e-06]]


plt.savefig('Cyan492.pdf')
print ('Fertig')
