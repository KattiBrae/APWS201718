import numpy as np
import sympy
#
#T1A=  295.75
#T6A=  289.65
#T12A= 279.75
#T18A= 272.85
#
#T1B=  296.65
#T6B=  304.05
#T12B= 314.55
#T18B= 323.85
#
#
#v1= T1B/(T1B-T1A)
#print (v1)
#
#v6= T6B/(T6B-T6A)
#print (v6)
#
#v12= T12B/(T12B-T12A)
#print (v12)
#
#v18= T18B/(T18B-T18A)
#print (v18)
TB = sympy.var('TB')
TA = sympy.var('TA')
#
#v= TB/(TB-TA)
#
#print(TB)
#print(v.diff(TB))
#print(TA)
#print(v.diff(TA))
#
#
#
#t=1
#TA=295.75
#dA=0.0666
#TB=296.65
#dB=0.0822
#
#db=-TB/(-TA + TB)**2 + 1/(-TA + TB)
#da=TB/(-TA + TB)**2
#
#print(sympy.sqrt((db*dB)**2+((da*dA)**2)))
#
#Fehler f+r t=1 ist 38.6745495546705
#
#
#t=6
#TA=289.65
#dA=0.1013
#TB=304.05
#dB=0.1250
#
#db=-TB/(-TA + TB)**2 + 1/(-TA + TB)
#da=TB/(-TA + TB)**2
#
#print(sympy.sqrt((db*dB)**2+((da*dA)**2)))
#Fehler f+r t=6 ist 0.229237616664457
#
#
#t=12
#TA=279.75
#dA=0.1696
#TB=314.55
#dB=0.2093
#
#db=-TB/(-TA + TB)**2 + 1/(-TA + TB)
#da=TB/(-TA + TB)**2
#
#print(sympy.sqrt((db*dB)**2+((da*dA)**2)))
##Fehler f+r t=12 ist 0.0654068507251193
#
#
t=18
TA=272.85
dA=0.2478
TB=323.85
dB=0.3059

db=-TB/(-TA + TB)**2 + 1/(-TA + TB)
da=TB/(-TA + TB)**2

print(sympy.sqrt((db*dB)**2+((da*dA)**2)))
#Fehler f+r t=18 ist 0.0445160298838363
