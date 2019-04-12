import numpy
import sympy
import math

#r = sympy.var('r')
#L= sympy.var('L')


#rR = sympy.var('rR')
#drR= sympy.var('drR')
#rA = sympy.var('rA')
#drA= sympy.var('drA')
#rB = sympy.var('rB')
#drB= sympy.var('drB')
#rK = sympy.var('rK')
#drK= sympy.var('drK')

rR=  0.035199999999999995 #m
drR= 0.002171261154260353 #m
rA=  0.013562500000000002 #m
drA= 0.0007200124781904822 #m
rB=  0.0149625 #m
drB= 0.001013492954464904 #
rK=  0.02666 #m
drK= 0.0016229849044276413 #m
#
LR= 0.0924 #m
LA= 0.1123 #m
LB= 0.1488 #m
LK= 0.045 #m

#print('Rumpf')
#VolR= math.pi * rR**2 * LR
#print(VolR)
VolR=0.00035967244804296
#
#print('Arm')
#VolA= math.pi * rA**2 * LA
#print(VolA)
VolA= 6.489468539455908e-05
#
#print('Bein')
#VolB= math.pi * rB**2 * LB
#print(VolB)
VolB= 0.0001046552768102381
#
#print('Kopf')
#VolK= math.pi * rK**2 * LK
#print(VolK)
VolK= 0.00010048070571560125

GVol= VolR + 2*VolA + 2*VolB + VolK
print(GVol)

#Vol= math.pi * r**2 * L
#print('diffr')
#dR = 2 * math.pi * L * r
#print(dR)

#print('dR')
#dR= math.sqrt( (2 * math.pi * LR * rR)**2 * (drR)**2)
#print(dR)
dR= 4.4371750834852516e-05
#
#print('dA')
#dA= math.sqrt( (2 * math.pi * LA * rA)**2 * (drA)**2)
#print(dA)
dA= 6.890320110942402e-06
#
#print('dB')
#dB= math.sqrt( (2 * math.pi * LB * rB)**2 * (drB)**2)
#print(dB)
dB= 1.417776249888061e-05
#
#print('dK')
#dK= math.sqrt( (2 * math.pi * LK * rK)**2 * (drK)**2)
#print(dK)
dK= 1.2233958631857244e-05
#

dGVol= math.sqrt( (1)**2*(dR)**2 + (2)**2*(dA)**2 + (2)**2*(dB)**2 + (1)**2*(dK)**2 )
print(dGVol)
