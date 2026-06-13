import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hclust

from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import fcluster

def nan_replace(tabel):
    for col in tabel.columns:
        if tabel[col].isna().any():
            if is_numeric_dtype(tabel[col]):
                tabel[col].fillna(tabel[col].mean(), inplace=True)
            else:
                tabel[col].fillna(tabel[col].mode()[0], inplace=True)


def partitie(h, nr_clusteri, p, instante):
    """
    Extragem clusteri sectionand dendrograma in dreptul pragului corespunzator lui nr_clusteri

    :param h: matrice de legaturi (linkage matrix)
    :param nr_clusteri:
    :param p: numar maxim de clusteri
    :param instante: observatii: tari, judete, localitati, etc.
    :return:
    """
    # matricea de legaturi H are n-1 randuri de forma [C1   C2  var_intre_C1_C2 size(C1+C2)]

    # pozitia pragului de sectionare in interiorul matricii de legaturi
    k_diff = p -nr_clusteri

    # pragul de sectionare
    prag = ( h[k_diff, 2] + h[k_diff + 1, 2] ) / 2

    # desenare
    fig, ax = plt.subplots(figsize=(9,6))
    ax.set_title(f"Clusterizare ierarhica (Ward) - {nr_clusteri} clusteri")
    hclust.dendrogram(h, labels=instante, ax=ax, color_threshold=prag)

    # numar observatii
    n = p + 1

    # simulare algoritm de merge intre clusteri
    c = np.arange(n)

    for i in range(n - nr_clusteri):
        k1 = int(h[i, 0])
        k2 = int(h[i, 1])
        c[c == k1] = n+i
        c[c == k2] = n+i

    coduri = pd.Categorical(c).codes
    return np.array([f"C{cod+1}" for cod in coduri])


def histograma(x, variabila, partitia):
    fig, axs = plt.subplots(1, len(np.unique(partitia)),
                            figsize=(10,6), sharey=True)
    fig.suptitle(f"Histograme pentru variabila: {variabila}")
    for ax, cluster in zip(axs, np.unique(partitia)):
        ax.hist(x[partitia == cluster], bins=10, rwidth=0.9)
        ax.set_title(cluster)


def execute():
    tabel = pd.read_csv("ADN_Tari.csv", index_col=0)
    instante = list(tabel.index)
    variabile = list(tabel.columns[1:])

    nan_replace(tabel)

    x = tabel[variabile].values

    # standardizare
    scaler = StandardScaler()
    x_std = scaler.fit_transform(x)

    # construirea ierarhiei de clusteri (folosind metoda Ward)
    h = hclust.linkage(x_std, method='ward')
    print(f"Linakge matrix:", h)
    n = len(instante)
    p = n-1

    # generare ierarhie de clusteri cu numar definit
    clusteri = [2,3,4,5]

    for k in clusteri:
        print(f"\nPartitionare cu {k} clusteri")

        part_k = partitie(h, k, p, instante)
        print(part_k)

        part_k_df = pd.DataFrame(data={"Cluster": part_k}, index=instante)
        part_k_df.to_csv(f"Partitie_{k}_clusteri.csv")

    # determinarea numarului optim de clusteri
    k_diff_max = np.argmax(h[1:, 2] - h[:-1, 2])
    nr_clusteri = p - k_diff_max
    print(f"Numar optim de clusteri: {nr_clusteri}")

    partitie_optima = partitie(h, nr_clusteri, p, instante)

    # varianta alternativa de extractie automata
    auto = fcluster(h, nr_clusteri, criterion='maxclust')
    print("Auto:\n", auto)

    # grafice
    for i in range(min(3, x.shape[1])):
        histograma(x[:, i], variabile[i], partitie_optima)

    # strict facultativ, cu rol de comparatie
    h_complete = hclust.linkage(x_std, method='complete')
    plt.figure(figsize=(9,6))
    plt.title("Dendrograma - Linkage complete")
    hclust.dendrogram(h_complete, labels=instante)

    plt.show()

if __name__ == '__main__':
    execute()





