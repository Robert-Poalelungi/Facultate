import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hclust
import scipy.spatial.distance as distance
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans

df = pd.read_csv("ADN_Total.csv", index_col=0)

# replace na
for column in df.columns:
    if any(df[column].isna()):
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column] = np.mean(df[column], axis=0)

        else:
            df[column] = df[column].mode()[0]

n = len(df.index)

# ierarhie
ierarhie = hclust.linkage(df.values, method="ward")

# distanta intre puncte
matrice_distante = distance.squareform(distance.pdist(df.values, metric="euclidean"))

# dendograma
hclust.dendrogram(ierarhie, labels=df.index)
plt.title("Dendograma")
plt.show()
# plt.savefig("dendograma.png")
plt.clf()

# k-means - partitie cu k clusteri unici
k = 2
centroids, labels = kmeans(df.values, k)
df["Cluster"] = labels

plt.scatter(df.iloc[:, 3], df.iloc[:, 4], c=df['Cluster'], cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, linewidths=2, color='r')
plt.title('K-means Clustering')
plt.show()
# plt.savefig("kmeans.png")
plt.clf()

# partitie optima

p = n - 1
k_dif_max = np.argmax(ierarhie[1:, 2] - ierarhie[:(p - 1), 2])
nr_clusteri = p - k_dif_max

prag = (ierarhie[k_dif_max, 2] + ierarhie[k_dif_max + 1, 2]) / 2

hclust.dendrogram(ierarhie, labels=df.index, color_threshold=prag)
plt.title("Dendograma pratitie optima")
plt.show()
plt.clf()

# c[i] = clusterul din care face parte instanta i
c = np.arange(n)
for i in range(n - nr_clusteri):
    k1 = ierarhie[i, 0]
    k2 = ierarhie[i, 1]
    c[c == k1] = n + i
    c[c == k2] = n + i

coduri = pd.Categorical(c).codes
partitie_optima = np.array(["c" + str(cod + 1) for cod in coduri])
print(partitie_optima)
print(pd.DataFrame(data=partitie_optima, index=df.index.to_numpy(), columns=["Cluster"]))
