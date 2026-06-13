import numpy as np
import pandas as pd


def nan_replace(x:np.ndarray):
    is_nan = np.isnan(x)
    # print(is_nan)
    k = np.where(is_nan)
    # print(k)
    x[k] = np.nanmean(x[:,k[1]],axis=0)

def standardizare_centrare(x:np.ndarray,scal=True,nlib=0):
    x_ = x - np.mean(x,axis=0)
    if scal:
        x_ = x_ / np.std(x,axis=0,ddof=nlib)
    return x_

def tabelare_matrice(x:np.ndarray,nume_linii=None,
                     nume_coloane=None,nume_fisier="data_out/out.csv"):
    tmp = pd.DataFrame(np.round(x,3),nume_linii,nume_coloane)
    tmp.to_csv(nume_fisier)

def calcul_corelatii_covariante(x:np.ndarray,y:np.ndarray):
    g = np.unique(y)
    r_v = {}
    for v in g:
        x_ = x[y==v,:]
        r_v[v] = ( np.corrcoef(x_,rowvar=False), np.cov(x_,rowvar=False) )
    return r_v
