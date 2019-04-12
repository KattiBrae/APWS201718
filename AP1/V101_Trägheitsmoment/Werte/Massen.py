import numpy
import sympy
import math

AR = 0.45001071358687744
dAR= 0.06378695542679592
AA = 0.08119416386020578
dAA= 0.010317048334251943
AB = 0.1309413497037788
dAB= 0.019955019151809517
AK = 0.1257182592851535
dAK= 0.017643799541805345

M = 0.1628

print('mR')
mR = M * AR
print(mR)

print('dmR')
dmR = M * dAR
print(dmR)

print('mA')
mA = M * AA
print(mA)

print('dmA')
dmA = M * dAA
print(dmA)

print('mB')
mB = M * AB
print(mB)

print('dmB')
dmB = M * dAB
print(dmB)

print('mK')
mK = M * AK
print(mK)

print('dmK')
dmK = M * dAK
print(dmK)
