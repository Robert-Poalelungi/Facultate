import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hclust


def nan_replace(x):
    # identificare pozitii elemente lipsa
    is_nan = np.isnan(x)

    # identificare indecsi de poziti pt elementele lipsa
    k_nan = np.where(is_nan)

    x[k_nan] = np.nanmean(x[:, k_nan[1]], axis=0)


def partitie(h, nr_clusteri, p, instante, metoda):
    k_dif_max = p - nr_clusteri
    prag = (h[k_dif_max, 2] + h[k_dif_max + 1, 2]) / 2

    plot_ierarhie(h, instante, "Partitia cu " + str(nr_clusteri) + " clusteri. Metoda: " + metoda, prag)

    n = p + 1

    # c[i] = clusterul din care face parte instanta i
    c = np.arange(n)
    for i in range(n - nr_clusteri):
        k1 = h[i, 0]
        k2 = h[i, 1]
        c[c == k1] = n + i
        c[c == k2] = n + i

    coduri = pd.Categorical(c).codes
    return np.array(["c" + str(cod + 1) for cod in coduri])


def plot_ierarhie(h, instante, titlu, prag=None):
    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontsize=18, color='b')
    hclust.dendrogram(h, labels=instante, ax=ax, color_threshold=prag)


def histograma(x, variabila, partitia):
    fig = plt.figure(figsize=(14, 8))

    fig.suptitle("Histograme pt variabila " + variabila, fontsize=18, color='b')

    clusteri = list(set(partitia))
    size = len(clusteri)

    axs = fig.subplots(1, size, sharey=True)
    for i in range(size):
        ax = axs[i]
        ax.set_xlabel(clusteri[i])
        ax.hist(x[partitia == clusteri[i]], bins=10, rwidth=0.9, range=(min(x), max(x)))


def show():
    plt.show()
