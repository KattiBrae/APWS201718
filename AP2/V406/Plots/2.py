
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
#plt.rcParams['figure.figsize'] = (20, 10)
#plt.rcParams['font.size'] = 15
#plt.rcParams['lines.linewidth'] = 3

print('Graphik1')

x, y = np.loadtxt('2.txt', unpack=True)#,delimiter=',')

#def f(x,a,b):
#    return a*x+b
#popt, pcov = curve_fit(f, x, y)
#print(popt)
#print(pcov)
#
#x_new = np.linspace(x[0], x[-1], 500)





plt.figure(1)
plt.plot(x,y,'x')
#plt.plot(x_new,f(x_new,*popt),'-', label='Messung1')

plt.xlabel('Auslenkung /mm')
plt.ylabel('Intensität /$\mu$m')
plt.grid()
#plt.legend()




plt.savefig('2.pdf')
print ('Fertig')
