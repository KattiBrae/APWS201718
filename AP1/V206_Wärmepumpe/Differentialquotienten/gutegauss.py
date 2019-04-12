import numpy as np
import sympy
import math as ma

x = sympy.var('x')
a = sympy.var('a')
b = sympy.var('b')
c = sympy.var('c')
d = sympy.var('d')
e = sympy.var('e')
f = sympy.var('f')
g = sympy.var('g')
h = sympy.var('h')



fB=3*a*x**2+2*b*x+c
fA=3*e*x**2+2*f*x+g

#dfB =  sympy.sqrt((fB.diff(a)*2.76984976e-07)**2 + (fB.diff(b)*2.30590006e-04)**2 + (fB.diff(c)*1.58569823e-02)**2)
#dfA =  sympy.sqrt((fA.diff(e)*2.24432126e-07)**2 + (fA.diff(f)*1.86839762e-04)**2 + (fA.diff(g)*1.28484067e-02)**2)
#print(dfB)
#print(dfA)

dfB=sympy.sqrt(6.90486092367485e-13*x**4 + 2.1268700346832e-7*x**2 + 0.000251443887662513)
dfA=sympy.sqrt(4.53328012627919e-13*x**4 + 1.39636386656867e-7*x**2 + 0.000165081554728605)

print('1')
x=1
dfB=sympy.sqrt(6.90486092367485e-13*x**4 + 2.1268700346832e-7*x**2 + 0.000251443887662513)
dfA=sympy.sqrt(4.53328012627919e-13*x**4 + 1.39636386656867e-7*x**2 + 0.000165081554728605)
print(dfB)
print(dfA)

print('6')
x=6
dfB=sympy.sqrt(6.90486092367485e-13*x**4 + 2.1268700346832e-7*x**2 + 0.000251443887662513)
dfA=sympy.sqrt(4.53328012627919e-13*x**4 + 1.39636386656867e-7*x**2 + 0.000165081554728605)
print(dfB)
print(dfA)

print('12')
x=12
dfB=sympy.sqrt(6.90486092367485e-13*x**4 + 2.1268700346832e-7*x**2 + 0.000251443887662513)
dfA=sympy.sqrt(4.53328012627919e-13*x**4 + 1.39636386656867e-7*x**2 + 0.000165081554728605)
print(dfB)
print(dfA)

print('18')
x=18
dfB=sympy.sqrt(6.90486092367485e-13*x**4 + 2.1268700346832e-7*x**2 + 0.000251443887662513)
dfA=sympy.sqrt(4.53328012627919e-13*x**4 + 1.39636386656867e-7*x**2 + 0.000165081554728605)
print(dfB)
print(dfA)
