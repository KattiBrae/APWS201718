import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('L')





z, u = np.loadtxt('TP2.txt', unpack=True,delimiter=',')

def f(z,e,f,):
    return e*z+f
popt2, pcov2 = curve_fit(f, z, u)
print(popt2)
print(pcov2)

z_new = np.linspace(z[0], z[-1], 500)

plt.figure(1)
plt.plot(z, u,'o')
plt.plot(z_new,f(z_new,*popt2),'-',label='$L$')

plt.xlabel('1/T')
plt.ylabel('ln(p/p0)')
plt.grid()
plt.legend()


R = 8.314472
m = -2225.56070383
L =-m*R
print(L)

plt.savefig('p.pdf')
print ('Fertig')
