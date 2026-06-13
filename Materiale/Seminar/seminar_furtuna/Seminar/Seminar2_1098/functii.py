import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


def nan_replace_df(t: pd.DataFrame):
    for c in t.columns:
        if any(t[c].isna()):
            if is_numeric_dtype(t[c]):
                t.fillna({c: t[c].mean()}, inplace=True)
            else:
                t.fillna({c: t[c].mode()[0]}, inplace=True)


def f_categorie(t: pd.Series):
    k = t.argmax()
    j = t.argmin()
    return pd.Series([t.index[k], t.index[j]],
                     ["Categorie_Max", "Categorie_Min"])


def f_disparitate(t: pd.DataFrame):
    x = t.values
    tx = np.sum(x, axis=0)
    tx[tx == 0] = 1
    p = x / tx
    p[p == 0] = 1
    return pd.Series(-np.sum(p * np.log(p), axis=0), t.columns)
