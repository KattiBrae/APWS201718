import numpy as np
import sympy
import math as ma

m = 3

c = 4190




L = 18504.36215629483
#dT_A/dt   aus Tabelle DGMTab
Q1 =      1.35381120237
Q2 = 1.7115253413199998
Q3 =      1.70713937768
Q4 = 1.2296883990799998

R = 8.314472




a = (1/L)*(m*c+660)*Q1
print(a)
b = (1/L)*(m*c+660)*Q2
print(b)
c = (1/L)*(m*c+660)*Q3
print(c)
d = (1/L)*(m*c+660)*Q4
print(d)

print('Fehler')
#L        = sympy.var('L')
Q  = sympy.var('Q')
f = (1/L)*(m*c+660)*Q
df =  sympy.sqrt((f.diff(Q)*0.01285)**2)
print(df)
df =  sympy.sqrt((f.diff(Q)*0.01304)**2)
print(df)
df =  sympy.sqrt((f.diff(Q)*0.01361)**2)
print(df)
df =  sympy.sqrt((f.diff(Q)*0.01450)**2)
print(df)







#p*V=R*T*m
0.96792972684347
1.2236833712185382
1.2205475539195096
0.04410295345510843
