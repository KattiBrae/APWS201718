import numpy
import sympy
import math

#Bein

#Werte
0.0124
0.0202
0.0173
0.0156
0.0112
0.0159
0.0154
0.0117


N=8
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=( 0.0124 + 0.0202 + 0.0173 + 0.0156 + 0.0112 + 0.0159 + 0.0154 + 0.0117 )/N
#mu= 0.0149625
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu-0.0124 )**2 + (mu-0.0202 )**2 + (mu-0.0173 )**2 + (mu-0.0156 )**2 + (mu-0.0112 )**2 + (mu-0.0159 )**2 + (mu-0.0154 )**2 + (mu-0.0117 )**2 )/N )
#sigma= 0.0028665909631476897
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V= 0.001013492954464904
print(V)
