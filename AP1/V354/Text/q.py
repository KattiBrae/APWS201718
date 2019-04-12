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
#print('q')
#q= math.sqrt(L) /(R * math.sqrt(C))
#print(q)
#
#print('dqdR')
#dqdR= q.diff(R)
#print(dqdR)
#
#print('dqdL')
#dqdL= q.diff(L)
#print(dqdL)
#
#print('dqdC')
#dqdC= q.diff(C)
#print(dqdC)


print('dq')
dq= math.sqrt( ( - math.sqrt(L)/(R**2 * math.sqrt(C)) )**2 * dR**2 + ( 1/(2 * R * math.sqrt(L * C)) )**2 * dL**2 + ( - math.sqrt(L)/(2 * R * math.sqrt(C**3)) )**2 * dC**2)
print(dq)
#=
