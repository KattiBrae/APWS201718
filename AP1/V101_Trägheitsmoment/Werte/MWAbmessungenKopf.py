import numpy
import sympy
import math

#Kopf

#Werte
0.0221
0.0259
0.0308
0.0309
0.0236


N=5
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=( 0.0221 + 0.0259 + 0.0308 + 0.0309 + 0.0236)/N
#mu= 0.02666
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu-0.0221)**2 + (mu-0.0259)**2 + (mu-0.0308)**2 + (mu-0.0309)**2 + (mu-0.0236)**2 )/N )
#sigma= 0.0036291045727562055
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V= 0.0016229849044276413
print(V)
