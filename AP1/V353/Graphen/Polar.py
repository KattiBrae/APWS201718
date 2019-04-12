
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
import math
import pylab



x, y = np.loadtxt('Polar.txt', unpack=True,delimiter=',')
y = y*2 *math.pi

#print('hz')
#print(x)
#print('a/b')
#print(y)


def f(x,a,b):
    return a*np.arctan(b*(x))
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 50000)


##x = np.linspace(0, 10, 500)



plt.figure(1)
plt.plot(x,y,'x', label ='Messwerte')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.xscale('log')

#plt.polar(a,x)
#plt.yscale('log')


plt.ylabel(r'$\phi$/rad')
plt.xlabel(r'$f$/Hz')
plt.grid()
#plt.legend()




plt.savefig('Polar.pdf')
print ('Fertig')




#
#a=2.08333333333333e-05    *2*math.pi
#print(a)
#a=3.33333333333333e-05    *2*math.pi
#print(a)
#a=0.00005 *2*math.pi
#print(a)
#a=0.00005 *2*math.pi
#print(a)
#a=4.16666666666667e-05    *2*math.pi
#print(a)
#a=0.000075    *2*math.pi
#print(a)
#a=8.82352941176471e-05    *2*math.pi
#print(a)
#a=0.0001  *2*math.pi
#print(a)
#a=0.0001111111    *2*math.pi
#print(a)
#a=0.0001041667    *2*math.pi
#print(a)
#a=0.00015 *2*math.pi
#print(a)
#a=0.000175    *2*math.pi
#print(a)
#a=0.0001967213    *2*math.pi
#print(a)
#a=0.0002040816    *2*math.pi
#print(a)
#a=0.0002195122    *2*math.pi
#print(a)
#a=0.0002285714    *2*math.pi
#print(a)
#a=0.0002295082    *2*math.pi
#print(a)
#a=0.0002407407    *2*math.pi
#print(a)
#a=0.000244898 *2*math.pi
#print(a)
#a=0.0002786885    *2*math.pi
#print(a)
#a=0.000025    *2*math.pi
#print(a)
#a=0.0002333333    *2*math.pi
#print(a)
#a=0.0002244898    *2*math.pi
#print(a)
#a=0.000225    *2*math.pi
#print(a)
#a=0.0002428571    *2*math.pi
#print(a)
#a=0.0002622951    *2*math.pi
#print(a)
#a=0.0002407407    *2*math.pi
#print(a)
#a=0.000244898 *2*math.pi
#print(a)
