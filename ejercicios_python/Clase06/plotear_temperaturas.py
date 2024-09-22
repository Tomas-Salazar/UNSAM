import numpy as np
import matplotlib.pyplot as plt


def plotear_temperaturas():
    temperaturas = np.load('ejercicios_python/Data/temperaturas.npy')
    plt.hist(temperaturas,bins=10)
    plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.

plotear_temperaturas()