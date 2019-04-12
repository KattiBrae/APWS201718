
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('150V')

x, y = np.loadtxt('150V.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)
#xyab

print('250V')

z, u = np.loadtxt('250V.txt', unpack=True,delimiter=',')

def f(z,e,f):
    return e*z+f
popt2, pcov2 = curve_fit(f, z, u)
print(popt2)
print(pcov2)

z_new = np.linspace(z[0], z[-1], 500)
#zuef
print('350V')

q, t = np.loadtxt('350V.txt', unpack=True,delimiter=',')

def f(q,w,r):
    return w*q+r
popt3, pcov3 = curve_fit(f, q, t)
print(popt3)
print(pcov3)

q_new = np.linspace(q[0], q[-1], 500)
#qtwr

print('450V')

i, o = np.loadtxt('450V.txt', unpack=True,delimiter=',')

def f(i,p,v):
    return p*i+v
popt4, pcov4 = curve_fit(f, i, o)
print(popt4)
print(pcov4)

i_new = np.linspace(i[0], i[-1], 500)


#xyab
#zuef
#qtwr
#iopv

print('480V')

s, d = np.loadtxt('480V.txt', unpack=True,delimiter=',')

def f(s,g,h):
    return g*s+h
popt5, pcov5 = curve_fit(f, s, d)
print(popt5)
print(pcov5)

s_new = np.linspace(s[0], s[-1], 500)

plt.figure(1)
plt.plot(x,y,'x')
plt.plot(z,u,'x')
plt.plot(q,t,'x')
plt.plot(i,o,'x')
plt.plot(s,d,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='$150V$')
plt.plot(z_new,f(z_new,*popt2),'-',label='$250V$')
plt.plot(q_new,f(q_new,*popt3),'-', label='$350V$')
plt.plot(i_new,f(i_new,*popt4),'-', label='$450V$')
plt.plot(s_new,f(s_new,*popt5),'-', label='$480V$')

plt.ylabel('Höhe / cm')
plt.xlabel('U / V')
plt.grid()
plt.legend()




plt.savefig('V501.pdf')
print ('Fertig')
