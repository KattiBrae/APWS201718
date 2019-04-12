
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show



x, y = np.loadtxt('Gravitation.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)



mü = 9.81*0.0014*0.0791278
print(mü)



plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')


plt.ylabel('$R/cm$')
plt.xlabel('$B/mT$')
plt.grid()
plt.legend()




plt.savefig('Gravitation.pdf')
print ('Fertig')
