
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show



x, y = np.loadtxt('Schwingung.txt', unpack=True,delimiter=',')








plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')


plt.ylabel('$ln( {U_c}/{U_0})$')
plt.xlabel('$[t] s$')
plt.grid()
plt.legend()




plt.savefig('Schwingung.pdf')
print ('Fertig')
