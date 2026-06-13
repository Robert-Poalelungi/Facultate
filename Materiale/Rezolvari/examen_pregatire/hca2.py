import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from seaborn import barplot,countplot,histplot

rawDiversitate=pd.read_csv('./dateIN/Diversitate.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/Coduri_Localitati.csv',index_col=0)

labels=list(rawDiversitate.columns.values[1:])

merged=rawDiversitate.merge(rawCoduri,left_index=True,right_index=True).drop('Localitate_y',axis=1).rename(columns={'Localitate_x':'Localitate'})[['Judet','Localitate'] + labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(merged)

# standardizare
x=StandardScaler().fit_transform(merged[labels])
# HCA = Hierarchy Clustering Analysis

# calcul ierarhie (matrice ierarhie)
HC=linkage(x,method='ward')
print(HC)

# calcul partitie optimala
n=HC.shape[0] # nr de jonctiuni
print(n)
dist_1=HC[1:n,2] # toate liniile, fara prima
dist_2=HC[0:n-1,2] # toate fara ultima
diff=dist_1-dist_2
j=np.argmax(diff) # cea mai mare diferenta intre toate distantele
t=(HC[j,2]+HC[j+1,2])/2

# k = nr optim de clustere  (cate clustere sunt formate daca taiem la acel prag)
k = n-j

cat = fcluster(HC,k,criterion='maxclust') # obtinem labels numerice adica 0,1, ..
merged['Clusters'] = ['C'+str(i+1) for i in cat] # transformam strict pt a une in csv si atat
merged.to_csv('./dateOUT/HCA_popt.csv')

# plot dendograma pt partitia optimala (adica pt HC)
plt.figure(figsize=(12,12))
plt.title("Dendograma")
dendrogram(HC,leaf_rotation=30,labels=merged.index.values) # adica valorile de la siruta care e indexul
plt.axhline(t,c='r')
# axhline horizontal, axvline vertical
plt.show()

# t (treshold) = media dintre cele 2 dist consec care au cea mai mare diferenta si asa trasam linia rosie
# esential pt a sti unde taiem dendograma si si cate clustere alegem

# calcul partitie oarecare (ex: k=5 clustere) => kmeans
l=5

kmeans=KMeans(n_clusters=k,n_init=10)
labels_kmeans=kmeans.fit_predict(x) # obtinem labels numerice adica 0,1, ..
merged['Kmeans_Clusters']=['C'+str(i+1) for i in labels_kmeans] # transformam strict pt a une in csv si atat

# plot dendograma partitie oarecare
plt.figure(figsize=(8,8))
plt.title('Dendograma partitie oarecare')
dendrogram(HC,leaf_rotation=30,labels=merged.index.values)
plt.axhline(HC[-(l-1),2],c='r')
plt.show()

# Calcul Silhouette Score pentru ambele partiții (optimala si oarecare)
silhouette_opt = silhouette_score(x, cat)
silhouette_fixed = silhouette_score(x, labels_kmeans)

# plot Silhouette pentru ambele partiții (optimala si oarecare)
plt.figure(figsize=(10, 5))
barplot(x=["Optimum", f"{k} Clustere"], y=[silhouette_opt, silhouette_fixed], palette="viridis")
plt.title("Scor Silhouette pentru Partiții")
plt.ylabel("Silhouette Score")
plt.show()


# Histograme clusteri pentru fiecare variabila observata ((partiție optimală și partiție-k)
# asa vedem distributia variabilei pe clusters
# alegem variabila pt exemplu
variabila='2015'

plt.figure(figsize=(8,8))
plt.title(f'Histograma clusteri pentru variabila {variabila}')
histplot(data=merged,x=variabila,hue='Kmeans_Clusters',kde=True,bins=30)
plt.xlabel(variabila)
plt.ylabel('Frecventa')
plt.show()

# Plot clusterizare în 2D folosind PCA - Trasare plot partiție în axe principale

# pt partiție optimală
pca = PCA(n_components=2)
pca_scores = pca.fit_transform(x)

plt.figure(figsize=(10, 8))
plt.title("Reprezentare 2D a Clusterelor folosind PCA")
scatter=plt.scatter(pca_scores[:, 0], pca_scores[:, 1], c=cat, cmap='viridis')
plt.colorbar(scatter,label="Cluster")
plt.xlabel("Componenta Principală 1")
plt.ylabel("Componenta Principală 2")
plt.show()

# pt partiție-k (oarecare)
pca=PCA(n_components=2)
C=pca.fit_transform(x)

kmeans=KMeans(n_clusters=5,n_init=10)
labels_kmeans=kmeans.fit_predict(C)

plt.figure(figsize=(8,8))
plt.title(f'Partitie a {k} clusteri pe cele 2 componente principale')
scatter=plt.scatter(C[:,0],C[:,1],c=labels_kmeans,cmap='viridis')
plt.colorbar(scatter,label="Cluster")
plt.xlabel("Componenta Principală 1")
plt.ylabel("Componenta Principală 2")
plt.show()




