import numpy
import sympy
import math

#Puppe1

#Werte
0.41
0.43
0.39
0.41
0.42


N=5
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=( 0.41 + 0.43 + 0.39 + 0.41 + 0.42)/N
#mu= 0.41200000000000003
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu-0.41)**2 + (mu-0.43)**2 + (mu-0.39)**2 + (mu-0.41)**2 + (mu-0.42)**2 )/N )
#sigma= 0.013266499161421592
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V= 0.005932958789676527
print(V)
