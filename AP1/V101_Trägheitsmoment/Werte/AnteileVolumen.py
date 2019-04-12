import numpy
import sympy
import math

#VG = sympy.var('VG')
#VR = sympy.var('VR')

VG = 0.0007992530781681555
dVG= 5.5789460104753834e-05

VR = 0.00035967244804296
dVR= 4.4371750834852516e-05
VA = 6.489468539455908e-05
dVA= 6.890320110942402e-06
VB = 0.0001046552768102381
dVB= 1.417776249888061e-05
VK = 0.00010048070571560125
dVK= 1.2233958631857244e-05

#print('AR')
#AR =VR/VG
#print(AR)
##anteil des rumpfes am gesamtvolumen
#
#print('AA')
#AA =VA/VG
#print(AA)
##anteil eines armes am gesamtvolumen
#
#print('AB')
#AB =VB/VG
#print(AB)
##anteil eines beines am gesamtvolumen
#
#print('AK')
#AK =VK/VG
#print(AK)
##anteil des kopfs am gesamtvolumen
#

#print('A')
#A = VR/VG
#print(A)
#
#print('dAVR')
dAVR = 1/VG
#print(dAVR)
#
#print('dAVG')
dAVG = -VR/VG**2
#print(dAVG)

print('dAR')
dAR = math.sqrt( (dAVR)**2 * (dVR)**2 + (dAVG)**2 * (dVG)**2 )
print(dAR)

dAVA = 1/VG
dAVG = -VA/VG**2
print('dAA')
dAA = math.sqrt( (dAVA)**2 * (dVA)**2 + (dAVG)**2 * (dVG)**2 )
print(dAA)

dAVB = 1/VG
dAVG = -VB/VG**2
print('dAB')
dAB = math.sqrt( (dAVB)**2 * (dVB)**2 + (dAVG)**2 * (dVG)**2 )
print(dAB)

dAVK = 1/VG
dAVG = -VK/VG**2
print('dAK')
dAK = math.sqrt( (dAVK)**2 * (dVK)**2 + (dAVG)**2 * (dVG)**2 )
print(dAK)
