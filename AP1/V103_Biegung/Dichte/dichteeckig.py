import numpy
import sympy
import math

a=0.01010
b=0.01005
c=0.01000
d=0.01005
e=0.01035
f=0.01030
g=0.01030
h=0.01000
i=0.01000
j=0.01005


print('Mittelwert')
mu=(a+b+c+d+e+f+g+h+i+j)/10
print(mu)
#mu=0.01012

print('Standardabweichung')
sigma= sympy.sqrt(((a-mu)**2 +(b-mu)**2 +(c-mu)**2 +(d-mu)**2 +(e-mu)**2 +(f-mu)**2 +(g-mu)**2 +(h-mu)**2 +(i-mu)**2 +(j-mu)**2 )/10)
print(sigma)
#sigma=0.000132664991614216

print('Varianz')
V=sigma/sympy.sqrt(10)
print(V)
#V=1.32664991614216e-5*sqrt(10)

#Dichte=Masse/Volumen
#Volumen: (Mittelwert+-Varianz)*Länge
print('Volumen')
Vol=mu*mu*0.60
print(Vol)
#Vol= 6.144864e-05 m^3

print('Fehler')
dVol=V*V*0.60
print(dVol)
#dVol= 1.05600000000000e-9 m^3

print('Dichte')
#Dichte=Masse/Volumen
rho=0.5024/Vol
print(rho)
#rho=8175.933592671863 kg/m^3

print('Fehler')
#Fehler=Masse* (1/(Vol+dVolplus) - 1/(Vol-dVolminus))/2
drho=0.5024/2*(-1/(Vol+dVol)+1/(Vol-dVol))
print(drho)
#drho=0.140504100275805 kg/m^3
