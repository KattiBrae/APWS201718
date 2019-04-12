import numpy
import sympy
import math

#Körper1

#Werte


N=5
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=( 0.85 + 0.85 + 0.845 + 0.87 + 0.87)/N
#mu= 0.857
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu-0.85)**2 + (mu-0.85)**2 + (mu-0.845)**2 + (mu-0.87)**2 + (mu-0.87)**2 )/N )
#sigma= 0.010770329614269018
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V= 0.0048166378315169225
print(V)
