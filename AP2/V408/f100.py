
import numpy as np
import sympy as s
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x=(0.15 , 0     )
y=(0    , 0.294 )
def f(x,a,b):
    return a*x+b
opt, cov = curve_fit(f, x, y)
print(opt)
print(np.diag(cov**(1/2)))
x_new = np.linspace(x[0], x[1], 500)

x2=( 0.12 ,     0 )
y2=(    0 , 0.620 )
def f2(x2,a2,b2):
    return a2*x2+b2
opt2, cov2 = curve_fit(f2, x2, y2)
print(opt2)
print(np.diag(cov2**(1/2)))
x2_new = np.linspace(x2[0], x2[1], 500)

x3=( 0.18 ,     0 )
y3=(    0 , 0.224 )
def f3(x3,a3,b3):
    return a3*x3+b3
opt3, cov3 = curve_fit(f3, x3, y3)
print(opt3)
print(np.diag(cov3**(1/2)))
x3_new = np.linspace(x3[0], x3[1], 500)

x4=( 0.20 ,     0 )
y4=(    0 , 0.195 )
def f4(x4,a4,b4):
    return a4*x4+b4
opt4, cov4 = curve_fit(f4, x4, y4)
print(opt4)
print(np.diag(cov4**(1/2)))
x4_new = np.linspace(x4[0], x4[1], 500)

x5=( 0.22 ,     0 )
y5=(    0 , 0.180 )
def f5(x5,a5,b5):
    return a5*x5+b5
opt5, cov5 = curve_fit(f5, x5, y5)
print(opt5)
print(np.diag(cov5**(1/2)))
x5_new = np.linspace(x5[0], x5[1], 500)

x6=( 0.25 ,     0 )
y6=(    0 , 0.163 )
def f6(x6,a6,b6):
    return a6*x6+b6
opt6, cov6 = curve_fit(f6, x6, y6)
print(opt6)
print(np.diag(cov6**(1/2)))
x6_new = np.linspace(x6[0], x6[1], 500)

x7=( 0.28 ,     0 )
y7=(    0 , 0.153 )
def f7(x7,a7,b7):
    return a7*x7+b7
opt7, cov7 = curve_fit(f7, x7, y7)
print(opt7)
print(np.diag(cov7**(1/2)))
x7_new = np.linspace(x7[0], x7[1], 500)

x8=( 0.30 ,     0 )
y8=(    0 , 0.145 )
def f8(x8,a8,b8):
    return a8*x8+b8
opt8, cov8 = curve_fit(f8, x8, y8)
print(opt8)
print(np.diag(cov8**(1/2)))
x8_new = np.linspace(x8[0], x8[1], 500)

x9=( 0.32 ,     0 )
y9=(    0 , 0.142 )
def f9(x9,a9,b9):
    return a9*x9+b9
opt9, cov9 = curve_fit(f9, x9, y9)
print(opt9)
print(np.diag(cov9**(1/2)))
x9_new = np.linspace(x9[0], x9[1], 500)

x10=( 0.35 ,    0 )
y10=(    0 , 0.137)
def f10(x10,a10,b10):
    return a10*x10+b10
opt10, cov10 = curve_fit(f10, x10, y10)
print(opt10)
print(np.diag(cov10**(1/2)))
x10_new = np.linspace(x10[0], x10[1], 500)

plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x2,y2,'x')
plt.plot(x3,y3,'x')
plt.plot(x4,y4,'x')
plt.plot(x5,y5,'x')
plt.plot(x6,y6,'x')
plt.plot(x7,y7,'x')
plt.plot(x8,y8,'x')
plt.plot(x9,y9,'x')
#plt.plot(x10,y10,'x')
plt.plot(x_new,f(x_new,*opt),'-')
plt.plot(x2_new,f2(x2_new,*opt2),'-')
plt.plot(x3_new,f3(x3_new,*opt3),'-')
plt.plot(x4_new,f4(x4_new,*opt4),'-')
plt.plot(x5_new,f5(x5_new,*opt5),'-')
plt.plot(x6_new,f6(x6_new,*opt6),'-')
plt.plot(x7_new,f7(x7_new,*opt7),'-')
plt.plot(x8_new,f8(x8_new,*opt8),'-')
plt.plot(x9_new,f9(x9_new,*opt9),'-')
#plt.plot(x10_new,f10(x10_new,*opt10),'-')
plt.xlabel('g /m')
plt.ylabel('b /m')
plt.grid()
plt.legend()




plt.savefig('f100.pdf')
print ('Fertig')
