import numpy
import sympy
import math

L=10.11e-3
dL=0.03e-3
mu=910.58084477
dmu=672.13921200

print('dreff')
dreff= math.sqrt( (4 * math.pi * mu)**2 * dL**2 + (4 * math.pi * L)**2 * dmu**2 )
print(dreff)
#=85.39329297010516
