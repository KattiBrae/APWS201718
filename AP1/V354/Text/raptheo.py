import numpy
import sympy
import math

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

print('rap')
rap= math.sqrt(4 * L / C )
print(rap)

#print('drdL')
#drdL = rap.diff(L)
#print(dtdL)
#
#print('drdC')
#drdC = rap.diff(C)
#print(dtdC)


print('drap')
drap= math.sqrt( ( math.sqrt(1/(L * C)) )**2 * dL**2 + ( - math.sqrt(L/C**3) )**2 * dC**2)
print(drap)
#=
