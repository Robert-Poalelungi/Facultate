import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st


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


def test_bartlett(r2, n, p, q, m):
    v = 1 - r2

    chi2 = (-n + 1 + (p + q + 1) / 2) * np.log(np.flip(np.cumprod(np.flip(v))))
    # in codul initial din seminar aveam range(m+1), corect este range(1, m+1)
    nlib = [(p - k + 1) * (q - k + 1) for k in range(1, m + 1)]

    p_values = 1 - st.chi2.cdf(chi2, nlib)
    return p_values


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


def scatter(tabel_z, var_z1, var_z2, tabel_u, var_u1, var_u2, titlu="Plot scoruri"):
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "r"})
    ax.set_xlabel(var_z1 + "/" + var_z2, fontdict={"fontsize": 12, "color": "r"})
    ax.set_ylabel(var_u1 + "/" + var_u2, fontdict={"fontsize": 12, "color": "r"})

    ax.axhline(0)
    ax.axvline(0)

    ax.scatter(tabel_z[var_z1], tabel_z[var_z2], color="r", label="Spatiul X")
    ax.scatter(tabel_u[var_u1], tabel_u[var_u2], color="green", label="Spatiul U")

    for i in range(len(tabel_z)):
        ax.text(tabel_z[var_z1].iloc[i], tabel_z[var_z2].iloc[i], tabel_z.index[i])
    for i in range(len(tabel_u)):
        ax.text(tabel_u[var_u1].iloc[i], tabel_u[var_u2].iloc[i], tabel_u.index[i])


def show():
    plt.show()
