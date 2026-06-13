import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from seaborn import heatmap


def plot_varianta(alpha: np.ndarray, procent_minimal=80, scal=True):
    m = len(alpha)
    x = np.arange(1, m + 1)
    f = plt.figure(figsize=(8, 5))
    ax = f.add_subplot(1, 1, 1)
    ax.set_title("Plot varianta", color="b", fontsize=18)
    ax.set_xlabel("Componenta", fontsize=12)
    ax.set_ylabel("Varianta", fontsize=12)
    ax.set_xticks(x)
    ax.plot(x, alpha)
    ax.scatter(x, alpha, c="r", alpha=0.5)
    k1 = None
    if scal:
        k1 = len(np.where(alpha > 1)[0])
        ax.axhline(1, c="g", label="Criteriul Kaiser")
    procent_cumulat = np.cumsum(alpha * 100 / sum(alpha))
    k2 = np.where(procent_cumulat > procent_minimal)[0][0] + 1
    ax.axvline(k2, c="c", label="Procent minimal (" + str(procent_minimal) + ")")
    k3 = None
    eps = alpha[:m - 1] - alpha[1:]
    sigma = eps[:m - 2] - eps[1:]
    negative = sigma < 0
    if any(negative):
        k3 = np.where(negative)[0][0] + 2
        ax.axvline(k3, c="m", label="Criteriul Cattell (Elbow)")
    ax.legend()
    plt.savefig("graphics/PlotVarianta.png")
    return k1, k2, k3


def show():
    plt.show()


def corelograma(t: pd.DataFrame, titlu="Corelograma", vmin=-1, cmap="RdYlBu", annot=True):
    f = plt.figure(figsize=(8, 8))
    ax = f.add_subplot(1, 1, 1)
    ax.set_title(titlu, color="b", fontsize=18)
    heatmap(t, vmin=vmin, vmax=1, cmap=cmap, annot=annot, ax=ax)


def scatterplot(t: pd.DataFrame, x="C1", y="C2", titlu="Plot scoruri"):
    f = plt.figure(figsize=(9, 6))
    ax = f.add_subplot(1, 1, 1, aspect=1)
    ax.set_title(titlu, color="b", fontsize=18)
    ax.scatter(t[x], t[y], c="r")
