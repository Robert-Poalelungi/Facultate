import numpy as np
import pandas as pd


def inlocuire_na(X):
    medii = np.nanmean(X, axis=0)
    k_nan = np.where(np.isnan(X))
    X[k_nan] = medii[k_nan[1]]


def acp(X:np.ndarray,std=True,nlib=0):
    n,m = X.shape
    x_ = X - np.mean(X,axis=0)
    if std:
        x_ = x_/np.std(X,axis=0,ddof=nlib)
    R = (1/n-nlib)*x_.T@x_
    # calcul vector si valori proprii
    valp, vecp = np.linalg.eig(R)
    # sortare valori proprii si vectori proprii
    k_inv = [k for k in reversed(np.argsort(valp))]
    alpha = valp[k_inv]
    a = vecp[:, k_inv]
    # print(a)
    regularizare(a)
    # calcul corelatii factoriale
    Rxc = np.round(a * np.sqrt(alpha),2)
    # calcul componente
    # standardizare X
    C = x_ @ a
    return R, alpha, a, Rxc, C


# Regularizare vectori proprii
def regularizare(t, y=None):
    if type(t) is pd.DataFrame:
        for c in t.columns:
            minim = t[c].min()
            maxim = t[c].max()
            if abs(minim) > abs(maxim):
                t[c] = -t[c]
                if y is not None:
                    k = t.columns.get_loc(c)  # determina indexul coloanei
                    y[:, k] = -y[:, k]
    else:
        for i in range(np.shape(t)[1]):
            minim = np.min(t[:, i])
            maxim = np.max(t[:, i])
            if np.abs(minim) > np.abs(maxim):
                t[:, i] = -t[:, i]


def tabelare_varianta(alpha):
    m = len(alpha)
    varianta_cumulata = np.cumsum(alpha)
    procent_varianta = alpha * 100 / m
    procent_cumulat = np.cumsum(procent_varianta)
    tabel_varianta = pd.DataFrame(data={"Varianta": alpha,
                                        "Varianta Cumulata": varianta_cumulata,
                                        "Procent varianta": procent_varianta,
                                        "Procent cumulat": procent_cumulat
                                        })
    return tabel_varianta


def tabelare(x, nume_coloane=None, nume_instante=None, tabel=None):
    x_tab = pd.DataFrame(x)
    if nume_coloane is not None:
        x_tab.columns = nume_coloane
    if nume_instante is not None:
        x_tab.index = nume_instante
    if tabel is not None:
        x_tab.to_csv(tabel)
    return x_tab

