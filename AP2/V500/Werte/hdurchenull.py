import numpy as np
import sympy
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('h/e')

x, y = np.loadtxt('hdurchenull.txt', unpack=True,delimiter=',')
def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)
#xyab
plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='kinetische Energie')
plt.ylabel('$U_g$ / V')
plt.xlabel('$f $ / $10^{15}$ Hz')
plt.grid()
plt.legend()

#[  2.22256933e-06  -5.40851235e-01]
#[[  4.26150911e-13  -2.64631399e-07]
# [ -2.64631399e-07   1.67265542e-01]]



plt.savefig('hdurchenull.pdf')
print ('Fertig')
