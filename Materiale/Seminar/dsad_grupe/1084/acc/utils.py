import numpy as np
import pandas as pd
import scipy.stats as stts
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype


def nan_replace(t):
    nume_variabile = list(t.columns)
    for each in nume_variabile:
        if any(t[each].isna()):
            if is_numeric_dtype(t[each]):
                t[each].fillna(t[each].mean(), inplace=True)
            else:
                t[each].filnna(t[each].mode()[0], inplace=True)


def to_dataframe(x, nume_linii=None, nume_coloane=None, fisier=None):
    df = pd.DataFrame(x, nume_linii, nume_coloane)
    if fisier is not None:
        df.to_csv(fisier)

    return df


def test_bartlett(r2, n, p, q, m):
    v = 1 - r2

    chi2 = (-n + 1 + (p + q + 1) / 2) * np.log(np.flip(np.cumprod(np.flip(v))))
    nlib = [(p - k + 1) * (q - k + 1) for k in range(1, m + 1)]

    p_values = 1 - stts.chi2.cdf(chi2, nlib)
    return p_values


def plot_corelatii(t_z, var_z1, var_z2, t_u, var_u1, var_u2, titlu="Plot corelatii"):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title(titlu)
    ax.set_xlabel(var_z1 + "/" + var_z2)
    ax.set_ylabel(var_u1 + "/" + var_u2)

    theta = np.arange(0, 2 * np.pi, 0.01)
    ax.plot(np.cos(theta), np.sin(theta))
    ax.plot(0.7 * np.cos(theta), 0.7 * np.sin(theta), color='orange')

    ax.axhline(0)
    ax.axvline(0)

    ax.scatter(t_z[var_z1], t_z[var_z2], color="red", label="Spatiul X")
    ax.scatter(t_u[var_u1], t_u[var_u2], color="green", label="Spatiul Y")

    for i in range(len(t_z)):
        ax.text(t_z[var_z1].iloc[i], t_z[var_z2].iloc[i], t_z.index[i])
    for i in range(len(t_u)):
        ax.text(t_u[var_u1].iloc[i], t_u[var_u2].iloc[i], t_u.index[i])

    ax.legend()


def scatter_2d(t_z, var_z1, var_z2, t_u, var_u1, var_u2):
    fig = plt.figure(figsize=(9, 9))
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title("Plot scoruri")
    ax.set_xlabel(var_z1 + "/" + var_z2)
    ax.set_ylabel(var_u1 + "/" + var_u2)

    ax.axhline(0)
    ax.axvline(0)

    ax.scatter(t_z[var_z1], t_z[var_z2], color="red", label="Spatiul X")
    ax.scatter(t_u[var_u1], t_u[var_u2], color="green", label="Spatiul Y")

    for i in range(len(t_z)):
        ax.text(t_z[var_z1].iloc[i], t_z[var_z2].iloc[i], t_z.index[i])
    for i in range(len(t_u)):
        ax.text(t_u[var_u1].iloc[i], t_u[var_u2].iloc[i], t_u.index[i])

    ax.legend()


def show():
    plt.show()
