import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
from scipy.stats import entropy


def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if t[v].isna().any():
            if is_numeric_dtype(t[v]):
                t[v].fillna(value=t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0])


def selectie(t):
    k = np.argmax(t.values[2:]) + 2
    return pd.Series([t.iloc[0], t.iloc[1], t.index[k]], [t.index[0], t.index[1], "Categorie"])


def shannon(t):
    x = t.iloc[:, :-1].values
    # p = x / np.sum(x, axis=0)
    p = (x.T / np.sum(x,axis=1)).T
    h = entropy(p, base=2, axis=0)
    return pd.Series(h, t.columns[:-1])
