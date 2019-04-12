import numpy
import sympy
import math

#Arm

#Werte
0.0168
0.0126
0.0162
0.0135
0.0109
0.0146
0.0128
0.0111


N=8
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=( 0.0168 + 0.0126 + 0.0162 + 0.0135 + 0.0109 + 0.0146 + 0.0128 + 0.0111 )/N
#mu= 0.013562500000000002
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu-0.0168 )**2 + (mu-0.0126 )**2 + (mu-0.0162 )**2 + (mu-0.0135 )**2 + (mu-0.0109 )**2 + (mu-0.0146 )**2 + (mu-0.0128 )**2 + (mu-0.0111 )**2 )/N )
#sigma= 0.0020365028234696847
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V= 0.0007200124781904822
print(V)
