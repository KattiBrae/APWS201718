
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
import math


x, y = np.loadtxt('Phasschib.txt', unpack=True,delimiter=',')
y = y*2*np.pi




plt.plot(x,y,'x', label ='Messwerte')
plt.xscale('log')

plt.ylabel('$[phi] rad $')
plt.xlabel('$[f] Hz$')
plt.grid()
plt.legend()




plt.savefig('Phasschib.pdf')
print ('Fertig')
