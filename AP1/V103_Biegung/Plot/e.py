import numpy
import sympy
import math

a= sympy.var('a')
b= sympy.var('b')
c= sympy.var('c')
d= sympy.var('d')

m=1.1994
M= 2.370
g=9.81


##eckigerStab
Ie=8.74405e-10
dIe=1.4498455802873657e-11
#
##runder Stab
Ir=4.89893e-10
dIr=9.299712968528236e-13
#
###Steigung einseitig eingespannt eckig
#a=48.22455
#da=1.46510
##
###Steigung einseitig eingespannt rund
#b=118.36623
#db=0.86521
##
###beidseitig eingespannt eckig rechts
#c=5.05407
#dc=0.00753
##
###beidseitig eingespannt eckig links
#d=-2.29541
#dd=0.07490

##Steigung einseitig eingespannt eckig
a=0.04822455
da=1.46510033e-06
#
##Steigung einseitig eingespannt rund
b=0.11836623
db=8.65208768e-07
#
##beidseitig eingespannt eckig rechts
c=5.05406944e-03
dc=7.52445183e-09
#
##beidseitig eingespannt eckig links
d=-0.00229541
dd=7.48994852e-08


print('Ee')
Ee=(m*g)/(2*Ie)*1/a
print(Ee)

ei =-g*m/(2*Ie**2*a)
ea =-g*m/(2*Ie*a**2)
dEe= math.sqrt(ei**2 *dIe**2 + ea**2 *da**2)
print('dEe')
print(dEe)
#Ee=  139.51543 10^9
#dEe=  81.14634 10^9



print('Er')
Er=(m*g)/(2*Ir)*1/b
print(Er)

ri =-g*m/(2*Ir**2*b)
rb =-g*m/(2*Ir*b**2)
dEr = math.sqrt(ri**2 *dIr**2 + rb**2 *db**2)
print('dEr')
print(dEr)
#Er=101.45513 10^9
#dEr=1.30440 10^9



print('Ebr')
Ebr=(M*g)/(48*Ie)*1/c
print(Ebr)

bri =-g*M/(48*Ie**2*c)
brc =-g*M/(48*Ie*c**2)
dEbr = math.sqrt(bri**2 *dIe**2 + brc**2 *dc**2)
print('dEbr')
print(dEbr)
#Ebr=109.60296 10^9
#dEbr=63.71674 10^9



print('Ebl')
Ebl=(M*g)/(48*Ie)*1/d
print(Ebl)

bli =-g*M/(48*Ie**2*d)
bld =-g*M/(48*Ie*d**2)
dEbl = math.sqrt(bli**2 *dIe**2 + bld**2 *dd**2)
print('dEbl')
print(dEbl)
#Ebl=241.32550 10^9
#dEbl=143.15275 10^9
