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

def salvare(x, nume_linii=None, nume_coloane=None, out="out.csv"):
    t = pd.DataFrame(x, nume_linii, nume_coloane)
    t.to_csv(out)

#adaugare valori lipsa
valori_lipsa = set_date.isna().any().any()
if valori_lipsa:
    nan_replace(set_date)

def standardizare(A):
    media=np.mean(A,axis=0)
    std=np.std(A,axis=0)
    return A-media/std

x_col=set_date.columns[:4].values
y_col=set_date.columns[4:].values
X=set_date[x_col].values
Y=set_date[y_col].values
Xstd=standardizare(X)
Ystd=standardizare(Y)

cca=CCA(n_components=2)
cca.fit(Xstd,Ystd)
x_scores,y_scores=cca.transform(Xstd,Ystd)
corr_canonice=np.corrcoef(x_scores.T,y_scores.T)
test,p_value=bartlett(*corr_canonice)

corr_observate=np.corrcoef(Xstd.T,x_scores.T)

varianta_explicata=np.var(x_scores,axis=0)/np.sum(np.var(X,axis=0))
redundanta = np.sum(varianta_explicata)











