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
    Extract clusters by cutting the dendrogram
    at a threshold corresponding to nr_clusteri
    """
    # position of cut in linkage matrix
    k_diff = p - nr_clusteri

    # dendrogram cut threshold
    prag = (h[k_diff, 2] + h[k_diff + 1, 2]) / 2

    # plot dendrogram
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_title(f"Hierarchical clustering (Ward) - {nr_clusteri} clusters")
    hclust.dendrogram(h, labels=instante, ax=ax,
                      color_threshold=prag)

    # number of observations
    n = p + 1

    # cluster assignment vector
    c = np.arange(n)

    # simulate merges
    for i in range(n - nr_clusteri):
        k1, k2 = int(h[i, 0]), int(h[i, 1])
        c[c == k1] = n + i
        c[c == k2] = n + i

    # recode cluster labels
    coduri = pd.Categorical(c).codes
    return np.array([f"C{cod + 1}" for cod in coduri])

def histograma(x, variabila, partitia):
    fig, axs = plt.subplots(1, len(np.unique(partitia)),
                            figsize=(10, 4), sharey=True)
    fig.suptitle(f"Histograms for variable: {variabila}")

    for ax, cluster in zip(axs, np.unique(partitia)):
        ax.hist(x[partitia == cluster], bins=10, rwidth=0.9)
        ax.set_title(cluster)

def execute():
    tabel = pd.read_csv("T:\\dsad\\ADN_Tari.csv", index_col=0)
    instante = list(tabel.index)
    variabile = list(tabel.columns)[1:]

    # 2. Handle missing values
    nan_replace(tabel)

    # 3. Extract numeric data matrix
    x = tabel[variabile].values
    # 4. Standardization (VERY IMPORTANT for Ward + Euclidean distance)
    #    Without scaling, variables with large variance dominate the clustering
    scaler = StandardScaler()
    x_std = scaler.fit_transform(x)

    # 5. Build hierarchical clustering (Ward method)
    h = hclust.linkage(x_std, method='ward')
    n = len(instante)
    p = n - 1

    # Generate and export multiple partitions
    # List of cluster numbers we want to illustrate
    cluster_numbers = [2, 3, 4, 5]

    for k in cluster_numbers:
        print(f"\nPartition with {k} clusters")

        # extract partition by cutting the dendrogram
        part_k = partitie(h, k, p, instante)

        # display cluster labels
        print(part_k)

        # save partition to CSV
        part_k_df = pd.DataFrame(
            data={"Cluster": part_k},
            index=instante
        )

        part_k_df.to_csv(f"T:\\dsad\\Partitie_{k}_clusteri.csv")

    # 6. Choose optimal number of clusters
    #    Largest jump in linkage distances
    k_diff_max = np.argmax(h[1:, 2] - h[:-1, 2])
    nr_clusteri = p - k_diff_max
    print("Optimal number of clusters:", nr_clusteri)

    # 7. Extract optimal partition (manual, didactic)
    partitie_optima = partitie(h, nr_clusteri, p, instante)

    # 8. Alternative: automatic extraction (practical usage)
    #    This is how it is usually done in real applications
    labels_auto = fcluster(h, nr_clusteri, criterion='maxclust')

    # 9. Visualize variable distributions per cluster
    for i in range(min(3, x.shape[1])):
        histograma(x[:, i], variabile[i], partitie_optima)

    # 10. Compare linkage methods (optional, quick demo)
    h_complete = hclust.linkage(x_std, method='complete')
    plt.figure(figsize=(9, 6))
    plt.title("Dendrogram – Complete linkage")
    hclust.dendrogram(h_complete, labels=instante)

    plt.show()

if __name__ == '__main__':
    execute()
