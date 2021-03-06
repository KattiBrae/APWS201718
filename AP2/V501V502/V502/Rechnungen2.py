
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show




print('Rechnung für e/m0')




print('######250#1#######')
D = 0.00635
B = 0.0204/1000
U_B = 250
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)


print('######250#2######')
D = 0.0127
B = 0.0408/1000
U_B = 250
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######250#3######')
D = 0.01905
B = 0.06377/1000
U_B = 250
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######250#4######')
D = 0.0254
B = 0.081624/1000
U_B = 250
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######250#5######')
D = 0.03175
B = 0.10203/1000
U_B = 250
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######250#6######')
D = 0.0381
B = 0.12243/1000
U_B = 250
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######250#7######')
D = 0.04445
B = 0.1453944/1000
U_B = 250
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######250#8######')
D = 0.0508
B = 0.1658/1000
U_B = 250
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)

print('_______________________________________________________________')

print('######300#1#######')
D = 0.00635
B = 0.0223/1000
U_B = 300
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)


print('######300#2######')
D = 0.0127
B = 0.0446/1000
U_B = 300
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######300#3######')
D = 0.01905
B = 0.066957/1000
U_B = 300
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######300#4######')
D = 0.0254
B = 0.089277/1000
U_B = 300
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######300#5######')
D = 0.03175
B = 0.114785/1000
U_B = 300
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######300#6######')
D = 0.0381
B = 0.133915/1000
U_B = 300
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######300#7######')
D = 0.04445
B = 0.15942/1000
U_B = 300
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######300#8######')
D = 0.0508
B = 0.1817434/1000
U_B = 300
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)

print('___________________________________________________________________')

print('######350#1#######')
D = 0.00635
B = 0.022319/1000
U_B = 350
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)


print('######350#2######')
D = 0.0127
B = 0.04655173/1000
U_B = 350
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######350#3######')
D = 0.01905
B = 0.07014644/1000
U_B = 350
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######350#4######')
D = 0.0254
B = 0.09565423/1000
U_B = 350
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######350#5######')
D = 0.03175
B = 0.1115966/1000
U_B = 350
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######350#6######')
D = 0.0381
B = 0.14411904/1000
U_B = 350
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######350#7######')
D = 0.04445
B = 0.16898914/1000
U_B = 350
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######350#8######')
D = 0.0508
B = 0.19322155/1000
U_B = 350
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)

print('_______________________________________________________________')

print('######400#1#######')
D = 0.00635
B = 0.02550779/1000
U_B = 400
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)


print('######400#2######')
D = 0.0127
B = 0.05101559/1000
U_B = 400
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######400#3######')
D = 0.01905
B = 0.07716108/1000
U_B = 400
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######400#4######')
D = 0.0254
B = 0.10330657/1000
U_B = 400
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######400#5######')
D = 0.03175
B = 0.12817667/1000
U_B = 400
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######400#6######')
D = 0.0381
B = 0.15623524/1000
U_B = 400
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######400#7######')
D = 0.04445
B = 0.18174304/1000
U_B = 400
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######400#8######')
D = 0.0508
B = 0.20725083/1000
U_B = 400
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)

print('___________________________________________________________________')

print('######440#1#######')
D = 0.00635
B = 0.02423241/1000
U_B = 440
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)


print('######440#2######')
D = 0.0127
B = 0.05101559/1000
U_B = 440
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######440#3######')
D = 0.01905
B = 0.07971186/1000
U_B = 440
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######440#4######')
D = 0.0254
B = 0.10840813/1000
U_B = 440
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######440#5######')
D = 0.03175
B = 0.13519131/1000
U_B = 440
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######440#6######')
D = 0.0381
B = 0.16516297/1000
U_B = 440
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('######440#7######')
D = 0.04445
B = 0.19449694/1000
U_B = 440
L = 0.1533
e_0 = ((D*((8*U_B)**(1/2)))/((L**2+D**2)*B))**2
print(e_0)



print('Mittel')
m=349670871696.1769+346104785252.9026+313406640062.1215+332176947900.1776+322412730298.32495+311082886099.75134+287999727352.45337+276008361438.9652+351148898948.49524+347567738979.3029+341138157675.83203+333201775944.0266+305688375216.2485+312014382275.39716+287463740437.627+275648250514.0725+408976507908.4486+372206810298.7022+362625042783.34326+338629596601.03394+377306306187.8136+314294754680.4061+298468071775.8785+284516988793.70447+357844303368.5272+354194722071.4837+342503027513.59937+331794617001.49274+326866165471.80566+305642542259.8103+294911590994.1194+282630298339.1472+436153379580.52905+389614194278.63196+353026908146.00696+331431818232.4522+323208720337.1057+300842451220.32367
print(m)
e=m/39
print(e)
a=1.75e11
print(a)
