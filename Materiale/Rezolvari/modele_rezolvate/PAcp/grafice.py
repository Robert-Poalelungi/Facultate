import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.colors as color
import numpy as np
import scipy.cluster.hierarchy as hclust
import statsmodels.graphics.mosaicplot as smosaic
import pandas as pd


def plot_varianta(alpha, titlu='Plot varianta',procent_minimal=80):
    n = len(alpha)
    f = plt.figure(titlu, figsize=(10, 7))
    f1 = f.add_subplot(1, 1, 1)
    f1.set_title(titlu, fontsize=16, color='b', verticalalignment='bottom')
    f1.set_xticks(np.arange(1, n + 1))
    f1.set_xlabel('Componenta', fontsize=12, color='r', verticalalignment='top')
    f1.set_ylabel('Varianta', fontsize=12, color='r', verticalalignment='bottom')
    f1.plot(np.arange(1, n + 1), alpha, 'ro-')
    f1.axhline(1, c='g',label="Kaiser")
    j_Kaiser = np.where(alpha < 1)[0][0]
    eps = alpha[:n-1] - alpha[1:]
    d = eps[:n-2] - eps[1:]
    conditie = d < 0
    if (conditie.any()):
        j_Cattel = np.where(d < 0)[0][0]+2
        f1.axhline(alpha[j_Cattel - 1], c='m',label="Cattell")
    else:
        j_Cattel = None
    procent_cumulat = np.cumsum(alpha)*100/sum(alpha)
    j_Procent_Minimal = np.where(procent_cumulat>procent_minimal)[0][0]+1
    f1.axhline(alpha[j_Procent_Minimal-1],c="c",label = "Procent minimal (>"+str(procent_minimal)+")")
    f1.legend()
    return j_Kaiser,j_Cattel, j_Procent_Minimal


def corelograma(t, title=None, valmin=-1, valmax=1):
    f = plt.figure(figsize=(8, 7))
    f1 = f.add_subplot(1, 1, 1)
    f1.set_title(title, fontsize=16, color='b', verticalalignment='bottom')
    f1.tick_params(axis='x', rotation=30)
    sb.heatmap(np.round(t, 2), cmap='bwr', vmin=valmin, vmax=valmax, annot=True, ax=f1)


# Plot corelatii - Cercul corelatiilor
def plot_corelatii(r, k1=0, k2=1, nume_variabile=None):
    fig = plt.figure(figsize=(8, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title("Plot corelatii", fontsize=16)
    t = np.arange(0, np.pi * 2, 0.01)
    ax.plot(np.cos(t), np.sin(t))
    ax.axhline(0, c='k')
    ax.axvline(0, c='k')
    ax.set_xlabel("Componenta " + str(k1 + 1))
    ax.set_ylabel("Componenta " + str(k2 + 1))
    ax.scatter(r[:, k1], r[:, k2], c='r')
    if nume_variabile is not None:
        m = np.shape(r)[0]
        for i in range(m):
            ax.text(r[i, k1], r[i, k2], nume_variabile[i])


# Plot instante
def plot_instante(t, k1=0, k2=1, nume_instante=None):
    fig = plt.figure(figsize=(11, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title("Plot instante", fontsize=16)
    ax.set_xlabel("a" + str(k1 + 1))
    ax.set_ylabel("a" + str(k2 + 1))
    ax.scatter(t[:, k1], t[:, k2], c='r')
    if nume_instante is not None:
        m = np.shape(t)[0]
        for i in range(m):
            ax.text(t[i, k1], t[i, k2], nume_instante[i])


def show():
    plt.show()
