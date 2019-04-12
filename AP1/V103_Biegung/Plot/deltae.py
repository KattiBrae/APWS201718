import numpy
import sympy
import math

Ie= sympy.var('Ie')
Ir= sympy.var('Ir')
a= sympy.var('a')
b= sympy.var('b')
c= sympy.var('c')
d= sympy.var('d')
g= sympy.var('g')
m= sympy.var('m')


Ee=(m*g)/(2*Ie)*1/a
print(Ee)
Er=(m*g)/(2*Ir)*1/b
print(Er)
Ebr=(m*g)/(48*Ie)*1/c
print(Ebr)
Ebl=(m*g)/(48*Ie)*1/d
print(Ebl)

print('diff Ee')
print('dei, dea')
dei=Ee.diff(Ie)
dea=Ee.diff(a)
print(dei)
print(dea)
#Ee nach Ie differenziert: -g*m/(2*Ie**2*a)
#Ee nach a differenziert: -g*m/(2*Ie*a**2)

print('diff Er')
print('dri, drb')
dri=Er.diff(Ir)
drb=Er.diff(b)
print(dri)
print(drb)
#Er nach Ir differenziert: -g*m/(2*Ir**2*b)
#Er nach b differenziert:  -g*m/(2*Ir*b**2)

print('diff Ebr')
print('dbri, dbrc')
dbri=Ebr.diff(Ie)
dbrc=Ebr.diff(c)
print(dbri)
print(dbrc)
#Ebr nach Ie differenziert: -g*m/(48*Ie**2*c)
#Ebr nach c differenziert:  -g*m/(48*Ie*c**2)

print('diff Ebl')
print('dbli, dbld')
dbli=Ebl.diff(Ie)
dbld=Ebl.diff(d)
print(dbli)
print(dbld)
#Ebl nach Ie differenziert: -g*m/(48*Ie**2*d)
#Ebl nach d differenziert:  -g*m/(48*Ie*d**2)
