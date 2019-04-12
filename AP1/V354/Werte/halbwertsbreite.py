import numpy
import sympy
import math

#q = sympy.var('q')
#R = sympy.var('R')
#L = sympy.var('L')
#C = sympy.var('C')

R=48.1
dR=0.1
#
L=10.11e-3
dL=0.03e-3
#
C=2.098e-9
dC=0.006e-9
#
print('hw')
hw= R / L
print(hw)

print('dhwdR')
dhwdR= 1/L
print(dhwdR)

print('dhwdL')
dhwdL= -R/L**2
print(dhwdL)

#print('dqdC')
#dqdC= q.diff(C)
#print(dqdC)


print('dhw')
dhw= math.sqrt( ( 1/L)**2 * dR**2 + ( -R/L**2 )**2 * dL**2 )
print(dhw)
#=
