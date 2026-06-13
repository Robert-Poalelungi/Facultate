import numpy as np
import pandas as pd
from geopandas import GeoDataFrame
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from seaborn import scatterplot, kdeplot


def plot_ierarhie(h:np.ndarray,etichete=None,color_threshold=0,
                  titlu="Plot ierarhie"):
    fig = plt.figure(titlu,figsize=(12, 7))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16})
    dendrogram(h,labels=etichete,color_threshold=color_threshold,ax=ax)
    plt.savefig("graphics/"+titlu+".png")

def show():
    plt.show()

def plot_partitie(
        t_z:pd.DataFrame,
        t_gz:pd.DataFrame,
        clase,
        p,
        scor_silh,
        axa_x="Z1",
        axa_y="Z2",
        titlu="Plot partitie in axele principale",
        etichete=True
):
    fig = plt.figure(figsize=(9,7))
    ax = fig.add_subplot(1,1,1,aspect=1)
    titlu = titlu + " Scor Silhouette " + str(scor_silh)
    ax.set_title(titlu,
                 fontdict={"fontsize":16})
    scatterplot(t_z, x=axa_x, y=axa_y, hue=p,
                hue_order=clase, ax=ax)
    scatterplot(t_gz,x=axa_x,y=axa_y,
                hue=clase,hue_order=clase,legend=False,
                marker = "s",s=100,ax=ax
                )
    if etichete:
        n = len(t_z)
        for i in range(n):
            ax.text(t_z[axa_x].iloc[i],t_z[axa_y].iloc[i],t_z.index[i])
    plt.savefig("graphics/" + titlu + ".png")

def f_distributie(t_z:pd.DataFrame, p, clase, variabila,
                  titlu="Plot distributii pe clase"):
    titlu = titlu+"_"+variabila
    fig = plt.figure(titlu,figsize=(9, 7))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16})
    kdeplot(t_z, x=variabila, hue=p, hue_order=clase,
            ax=ax, warn_singular=False, fill=True)
    plt.savefig("graphics/" + titlu + ".png")

def histograme(t:pd.DataFrame,variabila,p,clase,titlu="Plot histograme"):
    titlu = titlu+"_"+variabila
    fig = plt.figure(titlu,figsize=(12, 7))
    q = len(clase)
    ax = fig.subplots(1,q,sharey=True)
    fig.suptitle(titlu, fontdict={"fontsize": 16})
    x = t[variabila].values
    for i in range(q):
        axa = ax[i]
        y = x[p==clase[i]]
        assert isinstance(axa,plt.Axes)
        axa.hist(y,10,rwidth=0.9,range=(min(x),max(x)))
        axa.set_xlabel(clase[i])
    plt.savefig("graphics/" + titlu + ".png")

def plot_harta(gdf:GeoDataFrame,
               camp_legatura,
               t:pd.DataFrame,
               camp_harta,
               cmap="Reds",
               titlu="Harta scoruri"
               ):
    gdf_ = gdf.merge(t,left_on=camp_legatura,right_index=True)
    f = plt.figure(titlu, figsize=(9, 8))
    ax = f.add_subplot(1, 1, 1, aspect=1)
    ax.set_title(titlu, color="b", fontsize=16)
    gdf_.plot(column=camp_harta,cmap=cmap,legend=True,ax=ax)
    plt.savefig("graphics/" + titlu + ".png")

def f_plot_silhouette(partitie, scoruri_silh, scor_silh, titlu="Plot Silhouette"):
    fig = plt.figure(titlu,figsize=(10, 6))
    ax = fig.add_subplot(1,1,1)

    ax.set_title(titlu, fontsize=16)
    clusteri = np.unique(partitie)
    y_lower = 10
    for cluster in clusteri:
        coeficienti = scoruri_silh[partitie == cluster]
        coeficienti.sort()
        size = coeficienti.shape[0]
        y_upper = y_lower + size

        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0, coeficienti,
            alpha=0.7
        )
        ax.text(-0.05, y_lower + size / 2, cluster)
        y_lower = y_upper + 10
    ax.axvline(
        scor_silh,
        color="red",
        linestyle="--",
        label="Coeficient mediu"
    )
    ax.set_xlabel("Coeficienti Silhouette")
    ax.set_ylabel("Cluster")
    ax.legend()
    plt.savefig("graphics/" + titlu + ".png")
