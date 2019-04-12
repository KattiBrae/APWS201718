import numpy
import sympy
import math

N=
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=( + + + )/N

#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu- )**2 + (mu- )**2 + (mu- )**2 ...)/N )

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
