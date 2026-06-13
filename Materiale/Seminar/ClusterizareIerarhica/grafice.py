import matplotlib.pyplot as plt
import pandas as pd
from geopandas import GeoDataFrame
from seaborn import kdeplot, scatterplot
from scipy.cluster.hierarchy import dendrogram,set_link_color_palette
from scikitplot.metrics import plot_silhouette
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm
from matplotlib.colors import rgb2hex


# Crearea unei liste de culori in functie de numarul de clusteri
# in hexazecimal string (#rrggbb)
def generare_rampa(denumire,nr_clusteri):
    cmap = cm.get_cmap(denumire, nr_clusteri)
    culori = [rgb2hex(cmap(i)) for i in range(nr_clusteri)]
    return culori


def plot_scoruri(t, v1, v2, y, clase=None, titlu="Plot partitie",
                 etichete=False, culori=None):
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 14, "color": "b"})
    scatterplot(t, x=v1, y=v2, hue=y, hue_order=clase, ax=ax, palette=culori)
    if etichete:
        for j in range(len(t)):
            ax.text(t[v1].iloc[j], t[v2].iloc[j], t.index[j])
    plt.savefig("out/plot_instante_" + v1 + "_" + v2)


def plot_ierarhie(h, threshold, titlu, k, etichete,culori=None):
    fig = plt.figure(titlu, figsize=(9, 7))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    if culori is not None:
        set_link_color_palette(culori)
    r_dendr = dendrogram(h, ax=ax, color_threshold=threshold,
               labels=etichete)
    plt.savefig("out/dendr_"+str(k))
    

def histograme(t, variabila, partitie, culori):
    fig = plt.figure(figsize=(9, 7))
    fig.suptitle("Histograme pentru variabila " + variabila)
    assert isinstance(fig, plt.Figure)
    clase = np.unique(partitie)
    q = len(clase)
    min_max = (t[variabila].min(), t[variabila].max())
    ax = fig.subplots(1, q, sharey=True)
    for i in range(q):
        axe = ax[i]
        assert isinstance(axe, plt.Axes)
        axe.set_xlabel(str(clase[i]))
        axe.hist(t[partitie == clase[i]][variabila], range=min_max, color=culori[i], rwidth=0.9)
    plt.savefig("out/hist_"+variabila+"_"+str(q))


def plot_indecsi_silhouette(x, partitia, titlu, k, culori):
    fig = plt.figure(titlu, figsize=(10, 7))
    ax = fig.add_subplot(1, 1, 1)
    # Creare rampa de culori din lista de culori primita
    cmap = LinearSegmentedColormap.from_list("cmap", culori, len(culori))
    plot_silhouette(x, partitia, titlu, ax=ax, cmap=cmap)
    plt.savefig("out/Silhouette_" + str(k))


def show():
    plt.show()

def harta(shp, camp_legatura, t, camp_harta, titlu, culori):
    shp1 = pd.merge(shp, t, left_on=camp_legatura, right_index=True)
    f = plt.figure(titlu + "-" + camp_harta, figsize=(9, 7))
    ax = f.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    cmap = LinearSegmentedColormap.from_list("cmap", culori, len(culori))
    shp1.plot(camp_harta, cmap=cmap, ax=ax, legend=True,edgecolor='black')
    # shp1.boundary.plot(ax=ax)
    plt.savefig("out/Harta_P_" + str(len(culori)))