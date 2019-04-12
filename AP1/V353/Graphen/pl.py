
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
import math



x, y = np.loadtxt('pl.txt', unpack=True,delimiter=',')

a =  y *2 * math.pi
print(a)

def f(x,a,b):
    return np.tan(x)
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)
plt.polar(a,x,'x')

def H(x, c):
    return -np.sin(c)/x
x = np.linspace(0.000001, 2, 28)
plt.polar(x,H(-np.tan(x),x))

#z=np.linspace(10,10,28)

#plt.figure(1)
#plt.plot(x,y,'x', label ='Messwerte')
#plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
#plt.grid()
#f =  x *2 * math.pi

#plt.polar(np.arcsin(f*1.49))
plt.grid()
plt.grid()
#plt.ylabel('$ln( {U_c}/{U_0})$')
#plt.xlabel('$[T] s$')

#plt.legend()




plt.savefig('pl.pdf')
print ('Fertig')
