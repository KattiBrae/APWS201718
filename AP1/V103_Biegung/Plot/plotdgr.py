import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show



x, y = np.loadtxt('gvonxr.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)


plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='einseitig eingespannt, runder Stab')

plt.xlabel('$g_{r}(x)/m^3$')
plt.ylabel('$D_{r}(x)/m$')
plt.grid()
plt.legend()

plt.savefig('plotdgr.pdf')
