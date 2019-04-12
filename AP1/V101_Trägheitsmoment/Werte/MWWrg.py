import numpy
import sympy
import math

#Winkelrichtgröße

#Werte
x1=0.00355615804844531
x2=0.02133694829067186
x3=0.023707720322968733
x4=0.024893106339117173
x5=0.021336948290671856
x6=0.020744255282597636
x7=0.021336948290671856
x8=0.021781468046727523
x9=0.0205466909465729
x10=0.020625716680982793

N=10
#Mittelwert
#mu= Summe aller Werte / Anzahl
mu=(x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10)/N
#mu=0.01998659605394277
print(mu)


#Standardabweichung
#sigma= Wurzel[ ( (mu-Wert1)^2 + (mu-Wert2)^2 + + )/Anzahl ]
sigma= math.sqrt( ( (mu-x1)**2 + (mu-x2)**2 + (mu-x3)**2 + (mu-x4)**2 + (mu-x5)**2 + (mu-x6)**2 + (mu-x7)**2 + (mu-x8)**2 + (mu-x9)**2 + (mu-x10)**2)/N )
#sigma=0.005637978804395922
print(sigma)

#Varianz
#V= sigma/ Wurzel [Anzahl]
V= sigma/math.sqrt(N)
#V= 0.0017828854421644052
print(V)
