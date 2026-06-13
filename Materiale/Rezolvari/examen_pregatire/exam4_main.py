import numpy as np
import pandas as pd
from factor_analyzer import calculate_bartlett_sphericity
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from seaborn import heatmap


rawRata=pd.read_csv('./dateIN/Rata.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/CoduriTariExtins.csv',index_col=0)
labels=list(rawRata.columns.values[1:])
print(labels)

merged=rawRata.merge(rawCoduri,right_index=True,left_index=True).drop(['Country_Name'],axis=1)[['Continent','Country']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(merged)

#1
merged[merged['RS']<np.average(merged['RS'])][['Country','RS']].sort_values('RS',ascending=False).reset_index().rename(columns={'index':'Three_Letter_Country_Code'}).to_csv('./dateOUT/Cerinta1_4.csv',index=False)
#2
merged.groupby(['Continent']).apply(lambda df:pd.Series({ind:df[ind].idxmax() for ind in labels})).to_csv('./dateOUT/Cerinta2_4.csv')

#B1 PCA- Analiza componentelor principale

x=StandardScaler().fit_transform(merged[labels])


pca=PCA()
C=pca.fit_transform(x)#componente principale
alpha=pca.explained_variance_ #varianta componentelor
pve=pca.explained_variance_ratio_ #varianta explicata
a=pca.components_.T
components=pca.components_
rxc=a*np.sqrt(alpha) #factors loadings
C2=C*C
#scores = pca.transform(x) scoruri brute faca modelul e antrenat
#scores=pca.fit_transform(x) scoruri brute daca modelul nu e antrenat
scores=C/np.sqrt(alpha) #scoruri standardizate
quality=np.transpose(C2.T/np.sum(C2,axis=1))
communalities=np.cumsum(rxc*rxc,axis=1)
contributions=C2/(x.shape[0]*alpha)
print(pve)

alpha_cum=np.cumsum(alpha)
pve_cum=np.cumsum(pve)
pd.DataFrame(data={
    'Variatia componentelor':alpha,
    'Variatia cumulata':alpha_cum,
    'Procent din variatia explicata':pve,
    'Procent din variatia cumulata':pve_cum
}).to_csv('./dateOUT/pca_variatie',index=False)

#B2

plt.figure(figsize=(8,8))
plt.title('Plot de varianta a criteriilor componentelor')
Xindex=['C'+str(k+1) for k in range(len(alpha))]
plt.plot(Xindex,alpha,'bo-')
# 🔹 Criteriul Kaiser (valoare de referință 1)
plt.axhline(1,c='r',label='Kaiser')

# 🔹 Criteriul Cattell (Punctul unde diferențele scad drastic)
eps=np.diff(alpha)
d=np.diff(eps)
if(d<0).any():
    j_Cattel=np.where(d<0)[0][0] + 2
    plt.axhline(alpha[j_Cattel-1],c='m',label='Cattell')

# 🔹 Criteriul Procent Minimal (ex: 80%)
procent_cumulat=np.cumsum(alpha)*100 / np.sum(alpha)
j_procent_Minimal=np.where(procent_cumulat>80)[0][0]+1
plt.axhline(alpha[j_procent_Minimal-1],c='c',label='Procent minimal > 80%')
plt.legend()
plt.xlabel('Componenta')
plt.ylabel('Varianta')
plt.show()

#B3
communalities_df=pd.DataFrame(data=communalities,index=labels,columns=['C'+str(i+1) for i in range(communalities.shape[1])])
plt.figure(figsize=(8,8))
plt.title("Corelograma ")
heatmap(communalities_df,vmin=-1,vmax=1,cmap='bwr',annot=True)
plt.show()

#corelograma corelatii factoriale
print(rxc)
rxc_df=pd.DataFrame(data=rxc,index=labels,columns=['C'+str(i+1) for i in range(rxc.shape[1])])
plt.figure(figsize=(8,8))
plt.title("Corelograma ")
heatmap(rxc_df,vmin=-1,vmax=1,cmap='bwr',annot=True)
plt.show()

#cercul de corelatie pentru corelatii
plt.figure(figsize=(12, 12))
plt.title('Correlation circle')
T = [t for t in np.arange(0, np.pi * 2, 0.01)]
X = [np.cos(t) for t in T]
Y = [np.sin(t) for t in T]
plt.plot(X, Y)
plt.axhline(0, c='g')
plt.axvline(0, c='g')
plt.scatter(rxc[:, 0], rxc[:, 1])
for i in range(rxc.shape[0]):
    plt.text(rxc[i,0],rxc[i,1],labels[i],fontsize=12,ha='right')

plt.show()

plt.figure(figsize=(8,8))
plt.title('Plot scoruri')
plt.scatter(scores[:,0],scores[:,1])
plt.xlabel('Score 1')
plt.ylabel('Score 2')
plt.show()


