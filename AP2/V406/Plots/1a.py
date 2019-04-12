
import numpy as np
import sympy
import math as m
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
#plt.rcParams['figure.figsize'] = (20, 10)
#plt.rcParams['font.size'] = 15
#plt.rcParams['lines.linewidth'] = 3

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('1a.txt', unpack=True)#,delimiter=',')
d=x+1
b=0.022
#s=np.arctan(x/900000000)
#X=np.pi*np.sin(np.arctan(x/900000000))
#r=b**2*(63.5/(np.pi*np.sin(np.arctan(x/900))))**2#*(np.sin((np.pi*np.sin(np.arctan(x/900)))/63.5))**2
#t=(np.sin((np.pi*np.sin(np.arctan(x/900)))/63.5))**2
#p=r*t
#print(r)
#print(t)
#print(p)
#print(s)
#print(X)
def f(x,a,b):
    X=np.pi*np.sin(x)#np.arctan(x/900000))
    #print(X)
    #return a+b*np.arctan(x/900)
    #return a+b*s
    #return a**2*b**2*(63.5/(b*np.pi*np.sin(np.arctan(x/900))))**2*(np.sin((b*np.pi*np.sin(np.arctan(x/900)))/63.5))**2
    return a**2*b**2*(63.5/(b*X))**2*(np.sin((b*X)/63.5))**2
popt, pcov = curve_fit(f, x, y)
print(popt)
print(np.diag(pcov))

x_new = np.linspace(np.min(x), np.max(x), 1000)



plt.figure(1)
plt.plot(x,y,'x')
#plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.xlabel('Auslenkung /mm')
plt.ylabel('Intensität /nA')
plt.grid()
plt.legend()


plt.savefig('1a.pdf')
print ('Fertig')
