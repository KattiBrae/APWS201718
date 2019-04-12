import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show, array

N=np.sqrt(1.22826104e-05)
print(N)
N=np.sqrt(2.57508760e-05)
print(N)

#N=(0.101, 0.102, 0.103, 0.102, 0.103)
#mu= np.mean(N)
#print(mu)
#std= sp.std(N, ddof=1)
#print(std)

#dabw=[0.007, 0.009, 0.007, 0.009, 0.006]
#edat=[0.800, 0.850, 0.900, 0.950, 1.000]
#ddat=[0.563, 0.614, 0.663, 0.718, 0.768]
#for dd, e, d in zip(dabw, edat, ddat):
#    f=(e**2-d**2)/(4*e)
#    print(f)
#print('gauss')
#for dd, e, d in zip(dabw, edat, ddat):
#    df=np.sqrt( (-dd*d/(2*e))**2 )
#    print(df)



#f=np.loadtxt('besselcalc.txt', unpack=True,delimiter=',')
#mu=np.mean(f)
#print(mu)
#sigma= sp.std(f, ddof=1)
#print(sigma)
