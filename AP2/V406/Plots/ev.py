#!/usr/local/bin/python
# -*- coding: iso-8859-15 -*-

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import scipy as sp
import scipy.optimize as opt
import scipy.constants as const
import scipy.stats as stats

from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Times New Roman'], 'size': 12})


lamb=635e-9 #Laser-Wellenlänge
L=0.9 # Abstand Spalt, Photozelle

def Mittelwert (x) : #Funktionsdefinition: def Name(argumente): Blocks mit tab
    mw=sp.mean(x)
    N=len(x)
    f_mw=sp.sqrt((sp.sum((x-mw)**2))/(N*(N-1)))
    return mw,f_mw

def cos (x, a, b) :
    return a*sp.cos(x+b)

def _1_r2(x, a,b):
    return a/(x+b)**2
def _1_r (x, a, b):
    return a/(x+b)


def LinReg (x,y) : #Lineare Regression
    m = ((sp.mean(x*y))-(sp.mean(x)*sp.mean(y)))/(sp.mean(x*x)-sp.mean(x)*sp.mean(x))
    b = sp.mean(y)-m*sp.mean(x)
    N=len(y)
    Delta= N * sp.sum(x**2) - (sp.sum(x))**2
    sigma_y=sp.sqrt(sp.sum((y-(m*x+b))**2)/(N-2))
    f_m=sigma_y*sp.sqrt(N/Delta)
    f_b=sigma_y*sp.sqrt(sum(x**2)/Delta)
    return m,b,f_m,f_b

def I_phi1(x, A, b, c):
    return ((A*lamb)/(const.pi*sp.sin((x-c)/L+0.000001)))**2 *(sp.sin((const.pi*b*sp.sin((x-c)/L+0.000001))/(lamb)))**2

def I_phi2(x, A, b, c, s):
    return 4*A*(sp.cos((const.pi*s*sp.sin((x-c)/L+0.000001))/(lamb)))**2 * ((lamb)/(const.pi*b*sp.sin((x-c)/L+0.000001)))**2*(sp.sin((const.pi*b*sp.sin((x-c)/L+0.000001))/(lamb)))**2

x1,I1 = np.loadtxt("1a.txt", unpack=True) # loadtxt liest Daten aus Tabellen-datei ein, unpack = True damit die Arrays richtig zugordnet werden
x2,I2 = np.loadtxt("1b.txt", unpack=True)
x3,I3 = np.loadtxt("2.txt", unpack=True)


x1=x1/1000
x2=x2/1000
x3=x3/1000

I1=I1/100000000
i2=I2/1
I_2=i2/13000000000
i3=I3/1000000000
I_3=i3/15

var1, f_var1=opt.curve_fit(I_phi1, x1, I1, [1, 160e-6, 25e-3], maxfev=10000)
var2, f_var2=opt.curve_fit(I_phi1, x2, i2, [1, 160e-6, 25e-3], maxfev=10000)
var3, f_var3=opt.curve_fit(I_phi2, x3, I_3, [1, 40e-6 , 25e-3 , 0.25e-3], maxfev=10000)

x_werte=np.linspace(-0.03 ,0.03, 10000) # linspace(a,b, N) erstellt Array mit N Werten von a bis b

phi1=sp.arctan((x1)/L)#-var1[2])/L)
phi2=sp.arctan((x2)/L)#-var2[2])/L)
phi3=sp.arctan((x3)/L)#-var3[2])/L)

plt.plot(phi1,I1/(650e-9),'x',label="Messwerte")
plt.plot(x_werte,I_phi1((x_werte+var1[2]), var1[0], var1[1], var1[2])/(650e-9), 'r-', label=r"$\mathrm{Einfachspalt}$")
plt.xlabel("Winkel in rad")
plt.ylabel("Normierte Intesität")
plt.legend()
plt.grid()
plt.savefig('1_a.pdf')
plt.show()

#plt.plot(phi2,I_2/(480e-9),"x",label="Messwerte")
#plt.plot(x_werte,I_phi1((x_werte+var2[2]), var2[0], var2[1], var2[2])/(480e-9), 'r-', label=r"$\mathrm{Fit}$")
#plt.xlabel("Winkel in rad")
#plt.ylabel("Normierte Intesität")
#plt.legend()
#plt.grid()
#plt.savefig('1b')
#plt.show()

#plt.plot(phi3,i3/(100e-9),"x",label="Messwerte")
#plt.plot(x_werte,I_phi2((x_werte+var3[2]), var3[0], var3[1], var3[2], var3[3])/(100e-9), 'r-', label=r"$\mathrm{Doppelspalt}$")
#plt.xlabel("Winkel in rad")
#plt.ylabel('Normierte Intesität')
#plt.legend()
#plt.grid()
#plt.savefig('2.pdf')
#plt.show()
