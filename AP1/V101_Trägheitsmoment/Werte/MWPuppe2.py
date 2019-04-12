import numpy
import sympy
import math

#Puppe2

#Werte


N=
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=(  +  +  +  +  +  +  +  )/N
#mu=
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu- )**2 + (mu- )**2 + (mu- )**2 + (mu- )**2 + (mu- )**2 )/N )
#sigma=
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V=
print(V)
