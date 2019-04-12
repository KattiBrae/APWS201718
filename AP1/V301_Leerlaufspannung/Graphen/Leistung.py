
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
x, y = np.loadtxt('Leistung.txt', unpack=True,delimiter=',')

U0 = 1.4
Ri = 5.05722

t = np.linspace(0, x[-1], 5000)
N = U0**2/(t+Ri)**2 * t

plt.plot(t, N, '-', label='Theoriekurve')


#plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')


plt.xlabel('$R_{a}/ \Omega$')
plt.ylabel('$N=I U_{K}/VA$')
plt.grid()
plt.legend()




plt.savefig('Leistung.pdf')
print ('Fertig')
