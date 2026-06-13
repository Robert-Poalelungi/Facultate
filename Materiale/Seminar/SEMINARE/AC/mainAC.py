import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.dtypes.common import is_numeric_dtype
from sklearn.cross_decomposition import CCA
from sklearn.datasets import make_multilabel_classification
from scipy.stats import bartlett
from sklearn.preprocessing import StandardScaler

set_date = pd.read_csv('DataSet_34.csv', index_col=0)
obs = set_date.index.values

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
def standardizare(A):
    medie_col = np.mean(a=A, axis=0) #medii pe coloane
    std_col = np.std(a=A, axis=0)
    return (A - medie_col)/std_col

x_col = set_date.columns[:4].values
print(x_col)
X = set_date[x_col].values
Xstd = standardizare(X)
print(X)
Xstd_df = pd.DataFrame(data=Xstd, index=obs, columns=x_col)
Xstd_df.to_csv('Xstd.csv')

y_col = set_date.columns[4:].values
print(y_col)
Y = set_date[y_col].values
Ystd = standardizare(Y)
print(Y)
Ystd_df = pd.DataFrame(data=Ystd, index=obs, columns=y_col)
Ystd_df.to_csv('Ystd.csv')

# Analiză canonică folosind sklearn.cross_decomposition.CCA
cca = CCA(n_components=2)
cca.fit(Xstd, Ystd)

# Calcul scoruri canonice (variabile canonice)
U_c, V_c = cca.transform(Xstd, Ystd)

# Calcul corelații canonice
corrs = np.corrcoef(U_c.T, V_c.T)

# Determinare relevanță rădăcini canonice (Test Bartlett)
test_statistic, p_value = bartlett(*corrs)
print(f"Test Bartlett - Statistică: {test_statistic}, p-value: {p_value}")

# Calcul corelații variabile observate - variabile canonice
corrs_observed = np.corrcoef(Xstd.T, U_c.T)

# Calcul varianță explicată și redundanță informațională
explained_variance_ratio = np.var(U_c, axis=0) / np.sum(np.var(X, axis=0))
redundancy = np.sum(explained_variance_ratio)
print("Varianță Explicată:", explained_variance_ratio)
print("Redundanță Informațională:", redundancy)
