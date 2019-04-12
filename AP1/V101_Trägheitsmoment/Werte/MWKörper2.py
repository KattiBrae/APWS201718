import numpy
import sympy
import math

#Körper2

#Werte
1.14
1.16
1.20
1.15
1.21

N=5
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=( 1.14 + 1.16 + 1.20 + 1.15 + 1.21)/N
#mu= 1.1720000000000002
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu-1.14)**2 + (mu-1.16)**2 + (mu-1.20)**2 + (mu-1.15)**2 + (mu-1.21)**2 )/N )
#sigma= 0.027856776554368263
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V= 0.01245792920191796
print(V)
