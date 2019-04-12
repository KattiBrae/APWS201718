
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
import math
import pylab



x, y = np.loadtxt('normkonspan.txt', unpack=True,delimiter=',')




plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')

#plt.xscale('log')

u = np.linspace(8.75,8.75,60000)
plt.plot(u)
#v = np.linspace(17.5,0,10)
#g = v
#plt.plot(g)
plt.ylabel('$Uc/u $')
plt.xlabel('$[f]  Hz$')
plt.grid()
plt.legend()




plt.savefig('normkonspan.pdf')
print ('Fertig')
