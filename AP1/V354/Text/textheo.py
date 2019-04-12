import numpy
import sympy
import math

#R = sympy.var('R')
#L = sympy.var('L')

R=48.1
dR=0.1
#
L=10.11e-3
dL=0.03e-3
#
#mu=910.58084477
#dmu=672.13921200
#mu=sympy.var('mu')
print('tex')
tex= 2*L/R
print(tex)

print('dtdL')
dtdL= 2/R
print(dtdL)

print('dtdR')
dtdR= -2*L/R**2
print(dtdR)


print('dtex')
dtex= math.sqrt( (2/R)**2 * dL**2 + (-2*L/R**2)**2 * dR**2)
print(dtex)
#=
