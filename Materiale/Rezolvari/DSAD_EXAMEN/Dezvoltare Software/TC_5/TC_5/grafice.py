import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


def corelograma(matrice=None, dec=1, titlu='Corelograma', valMin=-1, valMax=1):
    plt.figure(titlu, figsize=(15, 11))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    sb.heatmap(data=np.round(matrice, dec), cmap='bwr', vmin=valMin, vmax=valMax, annot=True)


def cerculCorelatiilor(matrice=None, V1=0, V2=1, dec=2, titlu='Cercul corelatiilor',
                       valMin=-1, valMax=1,
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
        if isinstance(matrice, pd.DataFrame):
            plt.xlabel(xlabel=matrice.columns[V1], fontsize=12, color='r', verticalalignment='top')
            plt.ylabel(ylabel=matrice.columns[V2], fontsize=12, color='r', verticalalignment='bottom')
        else:
            plt.xlabel(xlabel='Var '+str(V1+1), fontsize=12, color='r', verticalalignment='top')
            plt.ylabel(ylabel='Var '+str(V2+1), fontsize=12, color='r', verticalalignment='bottom')
    else:
        plt.xlabel(xlabel=etichetaX, fontsize=12, color='r', verticalalignment='top')
        plt.ylabel(ylabel=etichetaY, fontsize=12, color='r', verticalalignment='bottom')

    if isinstance(matrice, np.ndarray):
        plt.scatter(x=matrice[:, V1], y=matrice[:, V2], c='r', vmin=valMin, vmax=valMax)
        # for i in range(len(matrice)):
        for i in range(matrice.shape[0]):
            # plt.text(x=0.25, y=0.25, s='un string')
            plt.text(x=matrice[i, V1], y=matrice[i, V2], s='(' +
                     str(np.round(matrice[i, V1], dec)) + ', ' +
                    str(np.round(matrice[i, V2], dec)) + ')')

    if isinstance(matrice, pd.DataFrame):
        plt.scatter(x=matrice.iloc[:, V1], y=matrice.iloc[:, V2], c='r', vmin=valMin, vmax=valMax)
        # plt.text(x=0.25, y=0.25, s='avem un pandas.DataFrame')
        for i in range(matrice.shape[0]):
            # plt.text(x=matrice.iloc[i, V1], y=matrice.iloc[i, V2], s='(' +
            #            str(np.round(matrice.iloc[i, V1], dec)) + ', ' +
            #            str(np.round(matrice.iloc[i, V2], dec)) + ')')
            plt.text(x=matrice.iloc[i, V1], y=matrice.iloc[i, V2], s=matrice.index[i])


def componentePrincipale(valoriProprii=None, titlu='Varianta explicata de componentele principale',
                         etichetaX='Componente principale', etichetaY='Varianta explicata - valori proprii'):
    plt.figure(titlu, figsize=(11, 8))
    plt.title(titlu, fontsize=14, color='k', verticalalignment='bottom')
    plt.xlabel(xlabel=etichetaX, fontsize=12, color='k', verticalalignment='top')
    plt.ylabel(ylabel=etichetaY, fontsize=12, color='k', verticalalignment='bottom')
    componente = ['C'+str(i+1) for i in range(0, len(valoriProprii), 1)]
    plt.plot(componente, valoriProprii, 'bo-')
    plt.axhline(y=1, color='r')


def norPuncte(matrice=None):
    for j in range(matrice.shape[1]):
        plt.scatter(x=matrice[:, j], y=matrice[:, 1])


def afisare():
    plt.show()