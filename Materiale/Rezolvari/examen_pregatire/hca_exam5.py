import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage,fcluster,dendrogram
from seaborn import histplot, barplot
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

rawAlcohol=pd.read_csv('./dateIN/alcohol.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/CoduriTariExtins2.csv',index_col=0)
labels=list(rawAlcohol.columns.values[1:])

merged=rawAlcohol.merge(rawCoduri,right_index=True,left_index=True)[['Continent','Code']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(merged)

#B1
x=StandardScaler().fit_transform(merged[labels])
HC=linkage(x,method='ward')
print(HC)

#B2
cat=fcluster(HC,5,criterion='maxclust')
labels_clusters_k=['C'+str(i) for i in cat]
merged['Clusters']=labels_clusters_k
merged[['Code','Clusters']].to_csv('./dateOUT/p4.csv')

#B3
pca=PCA(n_components=2)
C=pca.fit_transform(x)
kmeans=KMeans(n_clusters=5,n_init=10)
labels_kmeans=kmeans.fit_predict(C)
plt.figure(figsize=(8,8))
plt.title("Partitie a 5 clusteri pe cele 2 componente principale")
plt.scatter(C[:,0],C[:,1],c=labels_kmeans,cmap='viridis')
plt.colorbar()
plt.xlabel("Componenta principla 1")
plt.ylabel("Componenta principala 2")
plt.show()

plt.figure(figsize=(8,8))
plt.title('Dendograma')
dendrogram(HC,leaf_rotation=30,labels=merged.index.values)
plt.axhline(5,c='r')
plt.show()

variabila='2015'

plt.figure(figsize=(8,8))
plt.title('histograma pentru o variabila')
histplot(data=merged,x=variabila,hue='Clusters',kde=True,bins=30)
plt.xlabel(variabila)
plt.ylabel('Frecventa')
plt.show()

plt.figure(figsize=(8,8))
plt.title('histograma pentru toate variabilele')
histplot(data=merged,x=labels_clusters_k,hue='Clusters',kde=True,bins=30)
plt.show()

n=HC.shape[0]
dist_1=HC[1:n,2]
dist_2=HC[0:n-1,2]
diff=dist_1-dist_2
j=np.argmax(diff)
t=(HC[j,2]+HC[j+1,2])/2

cat_optim=fcluster(HC,n-j,criterion='maxclust')
labels_clusters=['C'+str(i) for i in cat_optim]

silhouette_opt = silhouette_score(x, labels_clusters)  # Scor Silhouette pentru partiția optimă

plt.figure(figsize=(6, 5))
barplot(x=["Optim"], y=[silhouette_opt], palette="viridis")

plt.title("Scor Silhouette pentru Partiția Optimă")
plt.ylabel("Silhouette Score")
plt.ylim(0, 1)
plt.show()

silhouette_k=silhouette_score(x,labels_clusters_k)
plt.figure(figsize=(6, 5))
barplot(x=[f"{5} Clustere"], y=[silhouette_k], palette="viridis")

plt.title("Scor Silhouette pentru Partiția Optimă")
plt.ylabel("Silhouette Score")
plt.ylim(0, 1)
plt.show()

