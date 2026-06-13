import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd

#graficul corelograma
def corelograma(R2, dec=2, titlu='Corelograma', valMin=-1, valMax=1): #R2 e matricea primita, merge si cu matrice si cu dataframe
    plt.figure(titlu, figsize=(15, 11))
    plt.title(titlu, fontsize=12, color='blue', verticalalignment="bottom")
    sb.heatmap(np.round(a=R2, decimals=dec), vmin=valMin, vmax=valMax, cmap='bwr', annot=True)

def cerculCorelatiilor(R2, V1=0, V2=1, titlu='Cercul corelatiilor', dec= 2): #R2 e matricea primita, V1 si V2 sunt indicii matricii
    plt.figure(titlu, figsize=(8, 8))
    plt.title(titlu, fontsize=12, color='blue', verticalalignment="bottom")
    theta = [t for t in np.arange(0, 2 * np.pi, 0.01)]
    X = [np.cos(t) for t in theta]
    Y = [np.sin(t) for t in theta]
    plt.plot(X, Y)
    plt.axhline(y=0, color="green")
    plt.axvline(x=0, color='green')

    #aici e diferit in functie de daca e matrice sau dataframe
    if isinstance(R2, np.ndarray):
        plt.xlabel(xlabel='Variabila ' + str(V1 + 1), fontsize='10', color='blue', verticalalignment='top')
        plt.ylabel(ylabel='Variabila ' + str(V2 + 1), fontsize='10', color='blue', verticalalignment='bottom')
        plt.scatter(x=R2[:, V1], y=R2[:, V2], c='red')
        for i in range(R2.shape[0]):
            plt.text(x=R2[i, V1],y=R2[i, V2],s='(' + str(np.round(R2[i, V1], decimals=dec)) + ', ' + str(np.round(R2[i, V2], decimals=dec)) + ')' )

    if isinstance(R2, pd.DataFrame):
        plt.xlabel(xlabel='Variabila ' + R2.index.values[V1], fontsize='10', color='blue', verticalalignment='top')
        plt.ylabel(ylabel='Variabila ' + R2.index.values[V2], fontsize='10', color='blue', verticalalignment='bottom')
        plt.scatter(x=R2.iloc[:].iloc[V1], y=R2.iloc[:].iloc[V2], c='purple')
        for i in range(R2.index.values.shape[0]):
            plt.text(x=R2.iloc[i].iloc[V1], y=R2.iloc[i].iloc[V2], s=R2.index.values[i])



def afisare():
    plt.show()