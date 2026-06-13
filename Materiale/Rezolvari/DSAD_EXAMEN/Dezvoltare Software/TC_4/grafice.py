import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np


def corelograma(matrice=None, dec=1, titlu='Corelograma', valMin=-1, valMax=1):
    plt.figure(titlu, figsize=(15, 11))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    sb.heatmap(data=np.round(matrice, dec), cmap='bwr', vmin=valMin, vmax=valMax, annot=True)

def cerculCorelatiilor(matrice=None, V1=0, V2=1, titlu='Cercul corelatiilor',
                       etichetaX=None, etichetaY=None):
    plt.figure(titlu, figsize=(8, 8))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    T = [t for t in np.arange(0, np.pi*2, 0.01)]
    X = [np.cos(t) for t in T]
    Y = [np.sin(t) for t in T]
    plt.plot(X, Y)
    plt.axhline(y=0, color='g')
    plt.axvline(x=0, color='g')
    if etichetaX==None or etichetaY==None:
        plt.xlabel(xlabel='Var '+str(V1+1), fontsize=12, color='r', verticalalignment='top')
        plt.ylabel(ylabel='Var '+str(V2+1), fontsize=12, color='r', verticalalignment='bottom')
    else:
        plt.xlabel(xlabel=etichetaX, fontsize=12, color='r', verticalalignment='top')
        plt.ylabel(ylabel=etichetaY, fontsize=12, color='r', verticalalignment='bottom')
    plt.scatter(x=matrice[:, V1], y=matrice[:, V2])


def afisare():
    plt.show()