import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import scipy.stats as sts


def nan_replace(t:pd.DataFrame):
    for coloana in t.columns:
        if t[coloana].isna().any():
            if is_numeric_dtype(t[coloana]):
                t.fillna({coloana:t[coloana].mean()},inplace=True)
            else:
                t.fillna({coloana:t[coloana].mode()[0]},inplace=True)


def tabelare_matrice(x, nume_linii=None, nume_coloane=None, out=None):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    if out is not None:
        t.to_csv(out)
    return t


def bartlett_test(n, l, x, e):
    m, q = np.shape(l)
    v = np.corrcoef(x, rowvar=False)
    psi = np.diag(e)
    v_ = l @ np.transpose(l) + psi
    I_ = np.linalg.inv(v_) @ v
    det_v_ = np.linalg.det(I_)
    urma = np.trace(I_)
    chi2 = (n - 1 - (2 * m + 4 * q - 5) / 2) * (urma - np.log(det_v_) - m)
    g_lib = ((m - q) * (m - q) - m - q) / 2
    p_value = sts.chi2.cdf(chi2, g_lib)
    return chi2, p_value

def ncomp_estim(alpha,pondere=None,limita=None):
    nrcomp_k =  len(np.where(alpha>1)[0])
    if pondere is None:
        pondere = np.cumsum(alpha/sum(alpha))
    if limita is not None:
        v = np.where(pondere>=limita)[0]
        if len(v)!=0:
            nrcomp_p = v[0] + 1
        else:
            nrcomp_p = np.NaN
    else:
        nrcomp_p = np.NaN
    m = len(alpha)
    eps = alpha[:(m-1)] - alpha[1:]
    sigma = eps[:(m-2)] - eps[1:]
    negative = sigma<0
    if any(negative):
        nrcomp_c = np.where(negative)[0][0] + 2
    else:
        nrcomp_c = np.NaN
    return [nrcomp_k,nrcomp_p,nrcomp_c]