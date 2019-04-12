import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show



x, y = np.loadtxt('ETM.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)


plt.figure(1)
plt.plot(x,y,'x', label = 'Messwerte')
plt.plot(x_new,f(x_new,*popt),'-', label='Eigenträgheitsmoment')

plt.xlabel('$a^2 [m^2]$')
plt.ylabel('$T^2 [s^{-2}]$')
plt.grid()
plt.legend()

#[ 753.53384036    4.64771862]
#[[  9.11818729e+02  -1.72106150e+01]
# [ -1.72106150e+01   5.20015394e-01]]

plt.savefig('plotETM.pdf')
