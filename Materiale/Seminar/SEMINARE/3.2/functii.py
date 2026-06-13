import numpy as np
import pandas as pd
from scipy.stats import shapiro, kstest, norm, chi2


def nan_replace(x):
    k = np.where(np.isnan(x))
    x[k] = np.nanmean(x[:, k[1]], axis=0)


def calcul_corelatii_covariante(x, macroregiuni):
    v_macroregiuni = np.unique(macroregiuni)
    corelatii = {}
    covariante = {}
    # n = len(v_macroregiuni)
    # m = np.shape(x)[1]
    # m_corelatii = np.zeros(shape=(n, m, m))
    # i=0
    for v in v_macroregiuni:
        k = np.where(macroregiuni == v)
        y = x[k[0], :]
        r = np.corrcoef(y, rowvar=False) #iti transpune matricea, unde judetele sunt observatii si variabilele sunt somaj etc
        # m_corelatii[i,:,:] = r
        # i+=1
        cov = np.cov(y, rowvar=False)
        corelatii[v] = r
        covariante[v] = cov
    return corelatii, covariante


def salvare(x, nume_linii=None, nume_coloane=None, out="out.csv"):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    t.to_csv(out)


def teste_c(x, prag=0.1):
    m = np.shape(x)[1]
    t_pvalues = np.zeros(shape=(m, 3))
    t_test = np.empty(shape=(m, 3), dtype=bool)
    for j in range(m):
        t_pvalues[j, 0] = shapiro(x[:, j])[1] #shapiro iti returneaza de fapt (shapiro,p-value), de asta se ia shapiro[1]
        t_pvalues[j, 1] = kstest(x[:, j], "norm")[1]
        t_pvalues[j, 2] = f_chi2(x[:, j])[1]
    t_test[:, 0] = t_pvalues[:, 0] > prag
    t_test[:, 1] = t_pvalues[:, 1] > prag
    t_test[:, 2] = t_pvalues[:, 2] < prag
    return t_pvalues,t_test


def f_chi2(x):
    media = np.mean(x)
    std = np.std(x)
    f, l = np.histogram(x, bins="sturges")
    m = len(f)
    n = len(x)
    fe = (norm.cdf(l[1:], media, std) - norm.cdf(l[:m], media, std)) * n
    stts = sum((f - fe) ** 2 / fe)
    p_value = chi2.cdf(stts, m - 1)
    return stts, p_value
