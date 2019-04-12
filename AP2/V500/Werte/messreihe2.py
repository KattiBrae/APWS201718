import numpy as np
import sympy
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('messreihe2')

x, y = np.loadtxt('messreihe2.txt', unpack=True,delimiter=',')
#def f(x,a,b):
#    return a*x+b
#popt, pcov = curve_fit(f, x, y)
#print(popt)
#print(pcov)

x_new = np.linspace(x[0], x[-1], 500)
#xyab
plt.figure(1)
plt.plot(x,y,'x')
#plt.plot(x_new,f(x_new,*popt),'-', label='$messreihe 2$')
plt.ylabel('I / nA')
plt.xlabel('U / V')
plt.grid()
plt.legend()

#[-0.1536525   0.37257411]
#[[ 0.00011768  0.00040729]
# [ 0.00040729  0.00457169]]



plt.savefig('messreihe2.pdf')
print ('Fertig')
