
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Empfindlichkeit auf 1/U_B')
x, y = np.loadtxt('Ergebniss.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.ylabel('$D/U_d$ / cm/V')
plt.xlabel('$1/U_{B}$ /  1/V')
plt.grid()
plt.legend()


plt.savefig('Ergebniss.pdf')
print ('Fertig')
