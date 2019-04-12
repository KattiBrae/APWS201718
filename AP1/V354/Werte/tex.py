import numpy
import sympy
import math

mu=910.58084477
dmu=672.13921200
#mu=sympy.var('mu')

tex= 1/(2 * math.pi * mu)

dtmu= -0.159154943091895/mu**2

print('dtex')
dtex= math.sqrt( (-0.159154943091895/mu**2)**2 * dmu**2 )
print(dtex)
#=0.00012901563488104507
