import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from seaborn import barplot, countplot, kdeplot, histplot

rawDiversitate=pd.read_csv('./dateIN/Diversitate.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/Coduri_Localitati.csv',index_col=0)
labels=list(rawDiversitate.columns.values[1:])

merged=rawDiversitate.merge(rawCoduri,right_index=True,left_index=True)\
    .drop({'Localitate_y'},axis=1)\
    .rename(columns={'Localitate_x':'Localitate'})\
    [['Judet','Localitate']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(merged)

#a1
merged['Diversitate medie']=merged[labels].mean(axis=1)
print(merged)
merged[['Localitate','Diversitate medie']].sort_values('Diversitate medie',ascending=False).to_csv('./dateOUT/Cerinta1_seria_e.csv')

#a2
merged.groupby('Judet')[labels].apply(lambda df: (df==0).sum()).to_csv('./dateOUT/Cerinta2_seria_e.csv')

#b1
x=StandardScaler().fit_transform(merged[labels])
HC=linkage(x,method='ward')
print(HC)

#b2

n=HC.shape[0]
dist_1=HC[1:n,2]
dist_2=HC[0:n-1,2]
diff=dist_1-dist_2
j=np.argmax(diff)
t=(HC[j,2]+HC[j+1,2])/2

plt.figure(figsize=(12,12))
plt.title("Dendograma")
dendrogram(HC,leaf_rotation=30,labels=merged.index.values)
plt.axhline(t,c='r')
plt.show()



#b3
cat=fcluster(HC,n-j,criterion='maxclust')
cat_fixed=fcluster(HC,5,criterion='maxclust')
labels_clusters=['C'+str(i) for i in cat]
labels_clusters_fixed=['C'+str(i) for i in cat_fixed]
merged['Clusters']=labels_clusters
merged.to_csv('./dateOUT/popt.csv')

silhouette_avg = silhouette_score(x, labels_clusters)
print(silhouette_avg)

silhouette_opt = silhouette_score(x, labels_clusters)
silhouette_fixed = silhouette_score(x, labels_clusters_fixed)

plt.figure(figsize=(10, 5))
barplot(x=["Optimum", f"{5} Clustere"], y=[silhouette_opt, silhouette_fixed], palette="viridis")
plt.title("Scor Silhouette pentru Partiții")
plt.ylabel("Silhouette Score")
plt.show()

#histograma
plt.figure(figsize=(10, 5))
countplot(x=labels_clusters_fixed, palette='viridis')
plt.title("Distribuția Localităților în Clustere (5 clustere)")
plt.xlabel("Cluster")
plt.ylabel("Număr de Localități")
plt.show()

#plot partitie axe principale
pca = PCA(n_components=2)
pca_scores = pca.fit_transform(x)

plt.figure(figsize=(10, 8))
scatter = plt.scatter(pca_scores[:, 0], pca_scores[:, 1], c=labels_clusters_fixed, cmap='viridis', edgecolors='k')
plt.colorbar(scatter, label="Cluster")
plt.xlabel("Componenta Principală 1")
plt.ylabel("Componenta Principală 2")
plt.title("Reprezentare 2D a Clusterelor folosind PCA")
plt.show()

# Cerința: Histograma/distribuția pentru o variabilă (la alegere)
variabila_aleasa = 'Diversitate medie'  # Alege variabila care te interesează

# Partiția optimă
plt.figure(figsize=(10, 5))
for cluster in np.unique(labels_clusters):
    cluster_data = merged[merged['Clusters'] == cluster][variabila_aleasa]
    #plt.hist(cluster_data, alpha=0.5, label=f'Cluster {cluster}') #histograma
    #sau
    kdeplot(cluster_data, fill=True, label=f'Cluster {cluster}') #grafic de distributie
plt.title(f'Distribuția {variabila_aleasa} (Partiția Optimală)')
plt.xlabel(variabila_aleasa)
plt.ylabel('Frecvență')
plt.legend()
plt.show()

variabila_aleasa = "2008"

plt.figure(figsize=(10, 6))

histplot(data=merged, x=variabila_aleasa, hue="Clusters",bins=30)

plt.title(f"Distribuția variabilei {variabila_aleasa} pe clustere")
plt.xlabel(variabila_aleasa)
plt.ylabel("Frecvență")
plt.legend(title="Cluster")
plt.show()