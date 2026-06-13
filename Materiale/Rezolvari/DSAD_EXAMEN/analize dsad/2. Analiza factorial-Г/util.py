import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb


def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    nume_variabile = list(t.columns)

    for each in nume_variabile:
        if any(t[each].isna()):
            if pd.api.types.is_numeric_dtype(t[each]):
                t[each].fillna(t[each].mean(), inplace=True)
            else:
                modul = t[each].mode()[0]
                t[each].fillna(modul, inplace=True)


def tabelare_matrice(x, nume_linii=None, nume_coloane=None, out=None):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    if out is not None:
        t.to_csv(out)

    return t


def corelograma(x, valMin=-1, valMax=1, titlu="Corelatii factoriale"):
    fig = plt.figure(titlu, figsize=(9, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})

    ax_ = sb.heatmap(data=x,
                     vmin=valMin, vmax=valMax,
                     cmap='RdYlBu', annot=True, ax=ax)
    ax_.set_xticklabels(x.columns, ha="right", rotation=30)


def plot_corelatii(x, var_x, var_y, titlu="Plot corelatii", aspect="auto"):
    fig = plt.figure(titlu, figsize=(9, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlabel(var_x, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var_y, fontdict={"fontsize": 12, "color": "b"})

    ax.set_aspect(aspect)

    theta = np.arange(0, 2 * np.pi, 0.01)
    ax.plot(np.cos(theta), np.sin(theta), color="b")

    ax.axhline(0)
    ax.axvline(0)

    ax.scatter(x[var_x], x[var_y], color="r")

    for i in range(len(x)):
        ax.text(x[var_x].iloc[i], x[var_y].iloc[i], x.index[i])

    # plt.show()


def plot_componente(x, var_x, var_y, titlu="Plot componente", aspect="auto"):
    fig = plt.figure(titlu, figsize=(9, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_xlabel(var_x, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var_y, fontdict={"fontsize": 12, "color": "b"})

    ax.set_aspect(aspect)
    ax.scatter(x[var_x], x[var_y], color="r")

    for i in range(len(x)):
        ax.text(x[var_x].iloc[i], x[var_y].iloc[i], x.index[i])


def tabelare_varianta(alpha, etichete_componente):
    procent = alpha * 100 / sum(alpha)
    tabel_varianta = pd.DataFrame(data={
        "Varianta": alpha,
        "Varianta cumulata": np.cumsum(alpha),
        "Procent varianta": procent,
        "Procent cumulat": np.cumsum(procent)
    },
        index=etichete_componente)

    return tabel_varianta


def harta(shape, x, camp_legatura, nume_instante, titlu="Harta scoruri"):
    n, m = x.shape

    tabel = pd.DataFrame(data={"Coduri": nume_instante})
    for i in range(m):
        tabel["v" + str(i+1)] = x[:, i]

    shape_ = pd.merge(shape, tabel, left_on=camp_legatura, right_on="Coduri")

    for i in range(m):
        fig = plt.figure(titlu + " - " + str(i+1), figsize=(9, 9))
        ax = fig.add_subplot(1, 1, 1)

        shape_.plot("v" + str(i+1), cmap="Reds", ax=ax, legend=True)


def show():
    plt.show()
