
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('60geschw.txt', unpack=True,delimiter=',')

#def f(x,a,b):
#    return a*x+b
#popt, pcov = curve_fit(f, x, y)
#print(popt)
#print(pcov)

#x_new = np.linspace(x[0], x[-1], 500)



#plt.figure(1)
plt.plot(x,y,'x')
#plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.xlabel(r'$\frac{\Delta \nu}{\cos{\alpha}}$ /  Hz')
plt.ylabel('Strömungsgeschwindigkeit $v$' r'/$\frac{m}{s}$')
plt.grid()
plt.legend()




plt.savefig('60geschw.pdf')
print ('Fertig')
