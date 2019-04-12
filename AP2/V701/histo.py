import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show, array


#klappt, meine Daten <3
N = np.loadtxt('stat.txt', unpack=True,delimiter=',')
mu= np.mean(N)
print(mu)
##Standardabweichung der Messwerte
#sigma= np.std(N)
#Standardabweichung der Population
sigma= sp.std(N, ddof=1)
print(sigma)

#gaussverteilung
G = np.random.normal(mu, sigma/10, 10000)

#poisson
P = np.random.poisson(mu, 10000)

min=8600
max=9900
#plot
plt.hist([G], density=True, bins=50, range=(min, max), alpha=0.6, label=['Gaußverteilung'])
plt.hist([P], density=True, bins=50, range=(min, max), alpha=0.6, label=['Poissonverteilung'])
plt.hist([N], density=True, bins=50, range=(min, max), alpha=0.6, label=['Messdaten'])




#alles weitere: nicht wichtig?
#klappt
#rng = np.random.RandomState(10)  # deterministic random data
#a = np.hstack((rng.normal(size=1000),
#               rng.normal(loc=5, scale=2, size=1000)))
#plt.hist(a, bins='auto')  # arguments are passed to np.histogram
#plt.title("Histogram with 'auto' bins")

#kein Bild, aber auch kein Fehler
#import matplotlib.pyplot as plt
#import numpy as np
#gaussian_numbers = np.random.normal(size=10000)
#plt.hist(gaussian_numbers)
#plt.title("Gaussian Histogram")
#plt.xlabel("Value")
#plt.ylabel("Frequency")
#plt.show()

#kein Bild, aber auch kein Fehler
#a = np.arange(5)
#hist, bin_edges = np.histogram(a, density=True)
#hist
#array([ 0.5,  0. ,  0.5,  0. ,  0. ,  0.5,  0. ,  0.5,  0. ,  0.5])
#hist.sum()
#2.4999999999999996
#np.sum(hist * np.diff(bin_edges))
#1.0

#kein Bild, aber auch kein Fehler
#np.histogram([1, 2, 1], bins=[0, 1, 2, 3])
#(array([0, 2, 1]), array([0, 1, 2, 3]))
#np.histogram(np.arange(4), bins=np.arange(5), density=True)
#(array([ 0.25,  0.25,  0.25,  0.25]), array([0, 1, 2, 3, 4]))
#np.histogram([[1, 2, 1], [1, 0, 1]], bins=[0,1,2,3])
#(array([1, 4, 1]), array([0, 1, 2, 3]))

#klappt nicht, Fehlermeldung
#rng = np.random.RandomState(10)  # deterministic random data
#a = np.hstack((rng(size=10000),
#               rng(loc=5, scale=2, size=1000)))
#x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#plt.hist(a, bins='auto')  # arguments are passed to np.histogram

#klappt nicht, Fehlermeldung
#import random
#import numpy
#import matplotlib.pyplot as plt
#import plotly.plotly as py  # tools to communicate with Plotly's server
#histogram=plt.figure()
#x = [random.gauss(3,1) for _ in range(400)]
#y = [random.gauss(4,2) for _ in range(400)]
#bins = numpy.linspace(-10, 10, 100)
#pyplot.hist(x, bins, alpha=0.5)
#pyplot.hist(y, bins, alpha=0.5)
#pyplot.show()
#plot_url = py.plot_mpl(histogram, filename='docs/histogram-mpl-same')


plt.xlabel("Zählrate $N$")
plt.ylabel("Häufigkeit")

plt.grid()
plt.legend()




plt.savefig('Graphik1.pdf')
print ('Fertig')
