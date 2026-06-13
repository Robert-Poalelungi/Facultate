import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram
from seaborn import scatterplot

def plot_ierarhie(h:np.ndarray,etichete=None,color_threshold = 0,titlu="Plot Ierarhie"):
    f = plt.figure(titlu,figsize=(10,6))
    ax = f.add_subplot(1,1,1)
    ax.set_title(titlu,fontdict={"fontsize":16})
    dendrogram(h,color_threshold=color_threshold,labels=etichete,ax=ax)
    if color_threshold!=0:
        ax.axhline(color_threshold,c="r")

def plot_partitie(
        t_z:pd.DataFrame,
        t_gz:pd.DataFrame,
        p,
        scor_silh,
        titlu,
        etichete=True
):
    f = plt.figure(figsize=(9, 8))
    ax = f.add_subplot(1, 1, 1, aspect=1)
    ax.set_title(titlu+". Scor Silh:"+str(scor_silh), fontdict={"fontsize": 16})
    clase = np.unique(p)
    scatterplot(t_z,x="Z1",y="Z2",hue=p,hue_order=clase,ax=ax)
    scatterplot(t_gz,x="Z1",y="Z2",hue=clase,hue_order=clase,
                legend=False,marker="s",s = 150, ax=ax)
    if etichete:
        n = len(t_z)
        for i in range(n):
            ax.text(t_z["Z1"].iloc[i],t_z["Z2"].iloc[i],t_z.index[i])

def show():
    plt.show()