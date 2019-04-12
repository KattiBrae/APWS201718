import numpy
import sympy
import math

#h= sympy.var('h')
#r= sympy.var('r')
#m= sympy.var('m')
#D= sympy.var('D')
#n= sympy.var('n')
#b= sympy.var('b')

h=0.0296 #m
r=0.1745 #m
m=0.2218 #kg
D= 0.01998659605394277
dD= 0.0017828854421644052

n= 753.53384036
dn=  9.11818729e+02
b= 4.64771862
db= 5.20015394e-01

#Eigenträgheitsmoment

#liegender Zyliner alleine
#Iz = m (r**2 / 4 + h**2 / 12)

#beide Zylinder mit Satz von Steiner
#IZ = ID + 2 * m * (r**2 / 4 + h**2 / 12) + 2 * m * a**2

#Schwingungsdauerformel
#T= 2 * math.pi * math.sqrt(IZ/D)
#T**2= 4 * (math.pi)**2 * ID/D + 8 * (math.pi)**2* m * (r**2 / 4 + h**2 / 12)/D + 8 * (math.pi)**2 * m * a**2 / D
#T**2= 8 * (math.pi)**2 * m/D * a**2 + 4 * (math.pi)**2 * ID/D + 8 * (math.pi)**2* m * (r**2 / 4 + h**2 / 12)/D
#y =         n    *               x  +                            b

#daraus folgt
#b= 4 * (math.pi)**2 * ID/D + 8 * (math.pi)**2* m * (r**2 / 4 + h**2 / 12)/D
#4 * (math.pi)**2 * ID/D = b - 8 * (math.pi)**2* m * (r**2 / 4 + h**2 / 12)/D

print('ID')
ID = b * D / (4 * (math.pi)**2) - 2 * m * (r**2 / 4 + h**2 / 12)
print(ID)
#ID=


#print('difb')
#difb= ID.diff(b)
#print(difb)
#difb= 0.0253302959105844*D

#print('difI')
#difI= ID.diff(D)
#print(difI)
#difI=0.0253302959105844*b

print('dID')
dID = math.sqrt((0.0253302959105844*b)**2 * dD**2 + (0.0253302959105844*D)**2 * db**2)
print(dID)
#dID=


#ID= -0.0033682541261903383 +- 3.6633709486164808e-06
