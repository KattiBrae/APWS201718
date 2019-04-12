import numpy
import sympy
import math

#Rumpf

#Werte
0.0398
0.0341
0.0253
0.0252
0.0364
0.0391
0.0402
0.0415


N=8
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=( 0.0398 + 0.0341 + 0.0253 + 0.0252 + 0.0364 + 0.0391 + 0.0402 + 0.0415 )/N
#mu= 0.035199999999999995
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu-0.0398 )**2 + (mu-0.0341 )**2 + (mu-0.0253 )**2 + (mu-0.0252 )**2 + (mu-0.0364 )**2 + (mu-0.0391 )**2 + (mu-0.0402 )**2 + (mu-0.0415 )**2 )/N )
#sigma= 0.006141253943617705
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V= 0.002171261154260353
print(V)
