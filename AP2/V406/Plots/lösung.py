import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.optimize import curve_fit
from scipy.stats import stats
import scipy.constants as const
plt.rcParams['figure.figsize'] = (20, 10)
plt.rcParams['font.size'] = 15
plt.rcParams['lines.linewidth'] = 3

#text_file = open("build/values.txt", "w")

# einlesen der Messwerte

x1, y1 = np.genfromtxt('1a.txt', unpack=True,delimiter=',') # Einzelspalt 1
l = 633e-9 # Wellenlänge
y=y1*10**(-9)
psi=np.arctan(x1/0.9)
x=(2*np.pi)/(360)*psi

# Theoriefunktion Einzelspalt
def g(x1, A0_1, b):
	return A0_1**2 * (l/(np.pi*b*np.sin(x1)))**2 * np.sin((np.pi*b*np.sin(x1))/l)**2
##
popt, pcov = curve_fit(g, x1, y1)
print(popt)
print(np.diag(pcov))
##### Einzelspalt 1

## Umrechnen in richtige Einheiten und abziehen des Dunktelstroms
#x = A_1*1e-07 # Winkel in rad
#I_1 += 0.0025
#I_1 -= 0.025
#
#
#x[25] = 0.00001 # Maximum bei x=0, wird manuell verändert, damit nicht durch 0 geteilt wird
#
#guess = (9000, 0.15e-3) # Schätzwerte für Datensatz 1
#params, covariance= curve_fit(g, x, I_1, guess)
#errors = np.sqrt(np.diag(covariance))
#print(errors)
#
## Werte aus Regression werden abgespeichert (Mittelwert, Standardabweichung), damit man sie später noch benutzen kann
#A0_1 = ufloat(params[0], errors[0])
#b_1 =  ufloat(params[1], errors[1])
#
## Werte werden in txt geschrieben
#text_file.write(' Parameter des Fits:' + '\n')
#text_file.write('         A0_1 =' + str(A0_1) + '\n')
#text_file.write('         b_1 =' + str(b_1) + '\n')

# Plot des ersten Einzelspalts
x_plot = np.linspace(np.min(x1), np.max(x1), 94)
plt.figure(1)
plt.grid()
plt.plot(x1, y1, 'x')
#plt.plot(x, I_1, 'b+', label='Messwerte Einzelspalt')
plt.plot(x_plot, g(x_plot, *popt), 'r', label='Einzelspalt')#, linewidth=3)
#plt.legend(loc="best")
plt.ylabel('Intensität')
plt.xlabel('Auslenkung/nm')
plt.savefig('bla.pdf')
#plt.close()
#



#A_2, I_2 = np.genfromtxt('tab2.txt', unpack=True) #  Einzelspalt 2
#A_DS, I_DS = np.genfromtxt('tab3.txt', unpack=True) # DS - Doppelspalt
# Theoriefunktion Doppelspalt
#def f(phi, A0_3, b, s):
#    return A0_3 *4*np.cos(np.pi*s*np.sin(phi)/l)**2*(l/(np.pi*b*np.sin(phi)))**2*np.sin(np.pi*b*np.sin(phi)/l)**2

# Es ist egal, wie du Variablen in Funktionen nennst. Sie sind nur Platzhalter innerhalb der Funktion und auch nur in dieser definiert. A0_1 und A0_3 kännen auch gleich und einfacher als A benannt werden.
# Funktioniert aber auch so












##### Einzelspalt 2

## Umrechnen in richtige Einheiten und abziehen des Dunktelstroms
#x = A_2*1e-07 # Winkel in rad
#I_2 += 0.0025
#I_2 -= 0.025
#
#x[28] = 0.00011 # Maximum bei x=0, wird manuell verändert, damit nicht durch 0 geteilt wird
#
#guess = (9000, 0.4e-3) # Schätzwerte
#params, covariance = curve_fit(g, x, I_2, guess)
#errors = np.sqrt(np.diag(covariance))
#
## Werte aus Regression werden abgespeichert (Mittelwert, Standardabweichung), damit man sie später noch benutzen kann
#A0_2 = ufloat(params[0], errors[0])
#b_2 =  ufloat(params[1], errors[1])
#
## Werte werden in txt geschrieben
#text_file.write('         A0_2 =' + str(A0_2) + '\n')
#text_file.write('         b_2 =' + str(b_2) + '\n')
#
#x_plot = np.linspace(np.min(x), np.max(x), 10000)
#plt.figure()
#plt.grid()
#plt.plot(x, I_2, 'b+', label='Messwertes')
#plt.plot(x_plot, g(x_plot, *params), 'r-', label='Ausgleichskurve', linewidth=3)
#plt.legend(loc="best")
#plt.ylabel('$I/\mu A$')
#plt.xlabel(r'$\phi/rad}$')
#plt.savefig('build/plot2.pdf')
#plt.close()
#





###### Doppelspalt
#
#x = A_DS*1e-07 # Winkel in rad
#I_DS += 0.0025
#I_DS -= 0.025
#
#x[49] = 0.000001 # Maximum bei x=0
#
## unwichtige Messwerte werden abgeschnitten
#x = x[12:-1]
#I = I_DS[12:-1]
#
#
#guess = (1, 0.1e-3, 0.4e-3) # Schätzwerte für Doppelspalt
#params, covariance = curve_fit(f, x, I, guess)
#errors = np.sqrt(np.diag(covariance))
#
#
## Werte aus Regression werden abgespeichert (Mittelwert, Standardabweichung), damit man sie später noch benutzen kann
#A0_DS = ufloat(params[0], errors[0])
#b_DS =  ufloat(params[1], errors[1])
#s_DS =  ufloat(params[2], errors[2])
#
#text_file.write(' Parameter des Fits:' + '\n')
#text_file.write('         A0_3 =' + str(A0_DS)  + '\n')
#text_file.write('         b_3 =' + str(b_DS) + '\n')
#text_file.write('         s =' + str(s_DS) + '\n')

#x_plot = np.linspace(np.min(x), np.max(x), 10000)
#plt.figure()
#plt.grid()
#plt.plot(x_plot, f(x_plot, noms(A0_DS), noms(b_DS), 0), 'g-', label='einhüllender Einzelspalt', linewidth=3) #Mittelwerte(noms(x)) der Parameter werden für den Plot verwendet
#plt.plot(x, I, 'b+', label='Messwerte Doppelspalt')
#plt.plot(x_plot, f(x_plot, *params), 'r-', label='Doppelspalt', linewidth=3)
#plt.legend(loc="best")
#plt.ylabel('$I/\mu A$')
#plt.xlabel(r'$\phi/rad}$')
#plt.savefig('build/plotDS.pdf')
#plt.close()
