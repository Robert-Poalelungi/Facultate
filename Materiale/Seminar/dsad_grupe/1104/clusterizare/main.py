"""
ACP - red. dim. si opereaza cu 1 singur set de date
    - constructia de comb. liniare din variabilele initiale pe modelul:
        C1 = a11 * V1 + a12 * V2 + ... + a1n * Vn
    - criterii de selectie ale unui numar optim de comp. principale: Kaiser, Cattel, %
    - conteaza foarte mult dispersia dintre var. initiale (variance)

AF  - red. dim. si opereaza cu 1 singur set de date
    - consideram ca in spatele var. initiale se afla un set de factori latenti care le influenteaza
       V1 = a11 * F1 + a12 * F2 + ... + a12 * Fn + E1
    - conteaza foarte mult covarianta (variatia comuna a variabilelor)

ACC - red. dim. si opereaza cu 2 seturi de date
    - construim comb. liniare specifice fiecarui set de date Z si U, alese astfel incat Var(Z, U) sa fie cat mai mari

AD  - clasificare si red. lim.
    - BDA Bayesian Disc. Analysis - Bayes: face exclusiv clasificarea elementelor
    - LDA Linear Disc. Analysis: face clasificarea elementelor + red. dim.
    - forma de invatare automata supervizata

HC  - clasificare
    - forma de invatare automata nesupervizata
"""
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
    Extragem clusteri sectionand dendrograma in dreptul unui prag corespunzator lui nr_clusteri.

    :param h: matricea de legaturi (linkage matrix)
    :param nr_clusteri: in cate categorii doresc sa grupez instantele
    :param p: numarul maxim de operatii de merge (n-1, unde n = nr de instante)
    :param instante: randurile din data frame (sau observatii) si de obicei repr. tari, localitati, persoane, etc
    :return:

    matricea de legaturi este o matrice cu p randuri, care descrie secvential (pas cu pas) procesul de clusterizare -
        adica modul in care sunt grupate din aproape in aproape instantele noastre
        fiecare rand din matricea de legaturi este de forma:
        [Ci     Cj      var_dintre_Ci_Cj        size(Ci+Cj)]
    """

    # pozitia pragului de sectionare in interiorul matricii de legaturi
    k_diff = p - nr_clusteri

    # pragul de sectionare al dendrogramei
    prag = ( h[k_diff, 2] + h[k_diff + 1, 2] ) / 2

    # desenare dendrograma
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_title(f"Clusterizare ierarhica folosind metoda Ward - {nr_clusteri} clusteri")
    hclust.dendrogram(h, labels=instante, ax=ax, color_threshold=prag)

    # numar instante
    n = p + 1  # len(instante)

    # reproducerea vizuala a algoritmului de clusterizare
    c = np.arange(n)

    for i in range(n - nr_clusteri):
        k1 = int(h[i, 0])
        k2 = int(h[i, 1])
        c[c == k1] = n+i
        c[c == k2] = n+i

    coduri = pd.Categorical(c).codes
    return np.array([f"C{cod+1}" for cod in coduri])


# partitie e un array de forma [C1, C2, C2, C3, C1, C2, C2, C1, C3 ...]
def histograma(x, variabila, partitie):
    fig, axs = plt.subplots(1, len(np.unique(partitie)), figsize=(10, 4), sharey=True)

    fig.suptitle(f"Histograme pentru variabila: {variabila}")

    for ax, cluster in zip(axs, np.unique(partitie)):
        ax.hist(x[partitie == cluster], bins=10, rwidth=0.9)
        ax.set_title(cluster)


def execute():
    tabel = pd.read_csv("ADN_Tari.csv", index_col=0)
    instante = list(tabel.index)
    variabile = list(tabel.columns[1:])

    nan_replace(tabel)

    x = tabel[variabile].values

    # standardizarea - foarte important cand facem clusterizare folosind metoda Ward
    scaler = StandardScaler()
    x_std = scaler.fit_transform(x)

    # construim ierarhia de clusteri
    h = hclust.linkage(x_std, method='ward')
    print("Matricea de legaturi\n", h)

    n = len(instante)
    p = n-1

    # partitionare cu un numar cunoscut de clusteri
    clusteri = [2,3,4,5]

    for k in clusteri:
        print(f"Partitionare cu {k} clusteri")

        part_k = partitie(h, k, p, instante)
        print(part_k)

        part_k_df = pd.DataFrame(data={"Cluster": part_k}, index=instante)
        part_k_df.to_csv(f"Partitie_{k}_clusteri.csv")

    # determinam numarul optim de clusteri
    k_diff_max = np.argmax(h[1:, 2] - h[:-1, 2])
    nr_clusteri = p - k_diff_max
    print(f"Numar optim de clusteri: {nr_clusteri}")

    partitie_optima = partitie(h, nr_clusteri, p, instante)

    # varianta alternativa de extractie automata a clusterilor, dar care intoarce alte rezultate
    auto = fcluster(h, nr_clusteri, criterion='maxclust')
    print("Auto\n", auto)

    # desenare grafice
    for i in range(3):
        histograma(x[:, i], variabile[i], partitie_optima)

    # pur facultativ, ca si comparatie intre ward si complete
    h_complete = hclust.linkage(x_std, method='complete')
    plt.figure(figsize=(9,6))
    plt.title("Dendrograma - complete linkage")
    hclust.dendrogram(h_complete, labels=instante)

    plt.show()



if __name__ == "__main__":
    execute()