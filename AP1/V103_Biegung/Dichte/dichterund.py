import numpy
import sympy
import math


a=0.5*10**(-2)
b=0.4975*10**(-2)
c=0.5*10**(-2)
d=0.5*10**(-2)
e=0.5*10**(-2)
f=0.5*10**(-2)
g=0.5*10**(-2)
h=0.5*10**(-2)
i=0.5*10**(-2)
j=0.5*10**(-2)


print('Mittelwert')
mu=(a+b+c+d+e+f+g+h+i+j)/10
print(mu)
#mu=0.0049975

print('Standardabweichung')
sigma= sympy.sqrt(((a-mu)**2 +(b-mu)**2 +(c-mu)**2 +(d-mu)**2 +(e-mu)**2 +(f-mu)**2 +(g-mu)**2 +(h-mu)**2 +(i-mu)**2 +(j-mu)**2 )/10)
print(sigma)
#sigma=7.49999999999996e-6

print('Varianz')
V=sigma/sympy.sqrt(10)
print(V)
#V=7.49999999999996e-7*sqrt(10)

#Volumen: (Mittelwert+-Varianz)*Länge
print('Volumen')
Vol=mu**2*math.pi*0.55
print(Vol)
#Vol= 4.315371288709755e-05 m^3

print('Fehler')
dVol=V**2*math.pi*0.55
print(dVol)
#dVol= 9.71930227204331e-12 m^3

print('Dichte')
#Dichte=Masse/Volumen
rho=0.3605/Vol
print(rho)
#rho= 8353.858240267089 kg/m^3

print('Fehler')
#Fehler=Masse* (1/(Vol+dVolplus) - 1/(Vol-dVolminus))/2
drho=0.3605/2*(-1/(Vol+dVol)+1/(Vol-dVol))
print(drho)
#drho= 0.00188149913294365 kg/m^3
