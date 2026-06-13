import numpy as np
import pandas as pd
from factor_analyzer import calculate_bartlett_sphericity,calculate_kmo,FactorAnalyzer
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from seaborn import heatmap, kdeplot
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split

rawAlcohol = pd.read_csv('./dateIN/alcohol.csv', index_col=0)
rawCoduri = pd.read_csv('./dateIN/CoduriTariExtins2.csv', index_col=0)
labels = list(rawAlcohol.columns.values[1:])

merged = rawAlcohol.merge(rawCoduri, right_index=True, left_index=True)[['Continent', 'Code'] + labels]
merged.fillna(np.mean(merged[labels], axis=0),inplace=True)
print(merged)

# 1
merged['Consum mediu'] = merged[labels].mean(axis=1)
merged[['Code', 'Consum mediu']].sort_values('Consum mediu', ascending=False).to_csv('./dateOUT/Cerinta1_consum.csv')

# 2

merged[['Continent'] + labels] \
    .groupby('Continent') \
    .mean() \
    .idxmax(axis=1) \
    .reset_index() \
    .rename(columns={0: 'Anul'}) \
    .to_csv('./dateOUT/Cerinta2.csv', index=False)
print(merged)

# B1

x = StandardScaler().fit_transform(merged[labels])
HC = linkage(x, method='ward')
print(HC)

n=HC.shape[0]
dist_1=HC[1:n,2]
dist_2=HC[0:n-1,2]
diff=dist_1-dist_2
j=np.argmax(diff)
t=(HC[j,2]+HC[j+1,2])/2

plt.figure(figsize=(12,12))
plt.title('Dendogram')
dendrogram(HC,leaf_rotation=30,labels=merged.index.values)
plt.axhline(t,c='r')
plt.show()

# cat=fcluster(HC,n-j,criterion='maxclust')
# labels_clusters=['C'+str(i) for i in cat]
# merged['Clusters']=labels_clusters
# merged.to_csv('./dateOUT/popt2.csv')

#B2
kmeans=KMeans(n_clusters=5,n_init=10)
k_labels=['C'+str(i+1) for i in kmeans.fit_predict(x)]
# print((k_labels))
# cat=fcluster(HC,5,criterion='maxclust')
# clusters=['C'+str(i) for i in cat]
merged['Clusters']=k_labels
merged[['Code','Clusters']].to_csv('./dateOUT/p4.csv')

#B3
pca=PCA()
C=pca.fit_transform(x)#componentele principale
print(C)


labels_kmeans=kmeans.fit_predict(C)
plt.figure(figsize=(8,8))
plt.title("Kmeans clustering on PCA data")
plt.scatter(C[:,0],C[:,1],c=labels_kmeans,cmap='viridis')
plt.show()



plt.figure(figsize=(8,8))
plt.title('Dendograma')
dendrogram(HC,leaf_rotation=30,labels=merged.index.values)
plt.axhline(HC[-(5-1), 2],c='r')
plt.show()
#EFA
bartlett_stat,bartlett_p=calculate_bartlett_sphericity(x)
if bartlett_p>0.001:
    print(bartlett_p)
    print('Nu exista factori comuni semnificativ')
    exit(0)

kmo_all,kmo_p=calculate_kmo(x)
if kmo_p<0.6:
    print('Analiza factoriala nu este recomandata')
    exit(0)

efa=FactorAnalyzer(n_factors=x.shape[1]-1,rotation=None)
scores=efa.fit_transform(x)
factorLoadings=efa.loadings_
plt.figure(figsize=(8,8))
plt.title('Corelograma corelatii factoriale')
factorLoadings_df=pd.DataFrame(data=factorLoadings,index=labels,columns=['F'+str(i+1) for i in range(factorLoadings.shape[1])])
print(factorLoadings_df)
heatmap(factorLoadings_df,vmin=-1,vmax=1,cmap='bwr',annot=True)
plt.show()

plt.figure(figsize=(8,8))
plt.title('Cercul pentru corelatiile factoriale')
T=np.arange(0,np.pi*2,0.01)
X=np.cos(T)
Y=np.sin(T)
plt.plot(X,Y)
plt.axhline(0,c='g')
plt.axvline(0,c='g')
plt.scatter(factorLoadings[:,0],factorLoadings[:,1])
for i in range(factorLoadings.shape[0]):
    plt.annotate(labels[i],(factorLoadings[i,0],factorLoadings[i,1]))
plt.show()
print(factorLoadings)
communalities=efa.get_communalities()
specificFactors=efa.get_uniquenesses()
comm_spec=pd.DataFrame(data={
    'Comunalitati':communalities,
    'Factori specifici': specificFactors
},index=labels)
plt.figure(figsize=(8,8))
plt.title('Corelogarama intre comunalitati si factori specifici')
heatmap(comm_spec,vmax=1,vmin=-1,cmap='bwr',annot=True)
plt.show()


#LDA
x_lda=pd.read_csv('./dateIN/ProiectB.csv',index_col=0)
x_applied=pd.read_csv('./dateIN/ProiectB_apply.csv',index_col=0)
tinta='VULNERAB'
labels_lda=list(x_lda.columns.values[:-1])
dict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7}
x_lda[tinta]=x_lda[tinta].map(dict)

lda=LinearDiscriminantAnalysis()
x_test,x_train,y_test,y_train=train_test_split(x_lda[labels_lda],x_lda[tinta],train_size=0.4)
lda.fit(x_train,y_train)

scores=lda.transform(x_test)

predict_test=lda.predict(x_test)
predict_applied=lda.predict(x_applied)

cm=confusion_matrix(y_test,predict_test)
accuracy=accuracy_score(y_test,predict_test)

#plot instante

plt.figure(figsize=(8,8))
plt.title('Plot instante pe axe discriminante')
plt.scatter(scores[:,0],scores[:,1])
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.show()

#plot distributii
plt.figure(figsize=(8,8))
plt.title('Plot distributii pe axe discriminante')
kdeplot(scores[y_test == 0, 1], label='Clasa 0')  # Distribuția scorurilor pentru clasa 0 pe LD1
kdeplot(scores[y_test == 1, 1], label='Clasa 1')
plt.legend()
plt.show()

gn=GaussianNB()
gn.fit(x_train,y_train)
prediction_bayesian=gn.predict(x_test)