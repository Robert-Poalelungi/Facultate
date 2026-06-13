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


def calcul_ponderi(t: pd.Series):
    return t / t.sum()


def diversitate(t: pd.Series):
    p = t.values
    p[p == 0] = 1
    log2 = np.log2(p)
    shannon = -np.sum(p * log2)
    s = np.sum(p * p)
    simpson = 1 - s
    inv_simpson = 1 / s
    return pd.Series([shannon,simpson, inv_simpson], ["Shannon","Simpson", "InvSimpson"])
