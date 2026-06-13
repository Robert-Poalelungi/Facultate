import numpy as np
import pandas as pd
from scipy.stats import shapiro, kstest, norm, chi2


def nan_replace(x):
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean(x[:, k[1]], axis=0)

def standardize(x, std=True, ddof=0):
    x_ = x - np.mean(x, axis=0)
    if std:
        x_ = x_ / np.std(x, axis=0, ddof=ddof)
    return x_

def salvare(x, nume_linii=None, nume_coloane=None, out="out.csv"):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    t.to_csv(out)


def teste_c(x, prag=0.1):
    assert isinstance(x, np.ndarray)
    m = x.shape[1] #stocheaza nr
    t_pvalues = np.zeros(shape=(m, 3)) #conntine valorile lui p-value
    t_test = np.empty(shape=(m, 3), dtype=bool) #contine doar true sau false
    for j in range(m):
        t_pvalues[j, 0] = shapiro(x[:, j])[1]
        t_pvalues[j, 1] = kstest(x[:, j], "norm")[1]
        t_pvalues[j, 2] = f_chi2(x[:, j])[1]
    t_test[:, 0] = t_pvalues[:, 0] > prag
    t_test[:, 1] = t_pvalues[:, 1] > prag
    t_test[:, 2] = t_pvalues[:, 2] < prag
    return t_pvalues,t_test


def f_chi2(x):
    n = len(x)
    f, l = np.histogram(x, bins="sturges")
    m = len(f)
    media = np.mean(x)
    std = np.std(x)
    fe = (norm.cdf(l[1:], media, std) - norm.cdf(l[:m], media, std)) * n
    stts = sum((f - fe) ** 2 / fe)
    p_value = chi2.cdf(stts, m - 1)
    return stts, p_value
