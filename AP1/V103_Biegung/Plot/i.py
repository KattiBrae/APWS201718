import numpy
import sympy
import math

#a = sympy.var('a')
#da= sympy.var('da')
#r = sympy.var('r')
#dr= sympy.var('dr')


#a= (1.012 ± 1.3267√10 ⋅ 10−3) ⋅ 10−2m.
#r=(4.9975 ± 7.5√10 ⋅ 10−4) ⋅ 10−3m

a=0.0101210
da=0.000013267 * math.sqrt(10)
#
r=0.0049975
dr=0.00000075 * math.sqrt(10)

#print('Ie')
Ie= a**4 /12
#print(Ie)
#Ie=8.744046397332399e-10

#print('Ir')
Ir= math.pi * r**4 /4
#print(Ir)
#Ir= 4.898928404845304e-10 

#print('IeA')
IeA= a**3/3
#print(IeA)

#print('IrR')
IrR= math.pi*r**3
#print(IrR)

print('dIe')
dIe= math.sqrt( (IeA)**2 * (da)**2)
print(dIe)

print('dIr')
dIr= math.sqrt( (IrR)**2 * (dr)**2 )
print(dIr)
