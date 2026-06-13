import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.dtypes.common import is_numeric_dtype
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_samples

set_date = pd.read_csv('./ConsumAlimentar.csv', index_col=1)
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
    nan_replace(set_date) #functie custom in functii.py

variabile=set_date.copy()
variabile = variabile.drop(columns=['Country'])

# Calcul ierarhie (matricea ierarhie)
linkage_matrix = linkage(variabile, method='ward')

# Calcul partiție optimă prin metoda Elbow
distances = linkage_matrix[:, 2]
differences = np.diff(distances, 2)
elbow_point = np.argmax(differences) + 1
optimal_partition = fcluster(linkage_matrix, t=distances[elbow_point - 1], criterion='distance')

# Calcul partiție oarecare cu un număr prestabilit de clusteri
#num_clusters = int(input("Introduceți numărul de clusteri dorit: ")) #citire de la tastatura
num_clusters = 4
custom_partition = fcluster(linkage_matrix, t=num_clusters, criterion='maxclust')

# Calcul indecși Silhouette
silhouette_optimal = silhouette_score(variabile, optimal_partition)
silhouette_custom = silhouette_score(variabile, custom_partition)


