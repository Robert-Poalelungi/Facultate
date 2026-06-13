import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.dtypes.common import is_numeric_dtype
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_samples

set_date = pd.read_csv('ConsumAlimentar.csv', index_col=1)
def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if t[v].isna().any():
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

#adaugare valori lipsa
valori_lipsa = set_date.isna().any().any()
if valori_lipsa:
    nan_replace(set_date)

variabile=set_date.copy()
variabile=variabile.drop(columns=["Country"])



