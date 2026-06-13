import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from seaborn import heatmap
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

rawRata=pd.read_csv('./dateIN/Rata.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/CoduriTariExtins.csv',index_col=0)
labels=list(rawRata.columns.values[1:])

merged=rawRata.merge(rawCoduri,left_index=True,right_index=True).drop('Country_Name',axis=1)[['Continent','Country']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)

# standardizare
x=StandardScaler().fit_transform(merged[labels])

# PCA
pca=PCA()
C=pca.fit_transform(x)

# Tabelul variantei
alpha=pca.explained_variance_ # varianta componentelor
pve=pca.explained_variance_ratio_ # procentul de varianta explicata
alpha_cum=np.cumsum(alpha) # varianta cumulata
pve_cum=np.cumsum(pve) # procentul cumulat

pd.DataFrame({'varianta componentelor':alpha,
              'procentul de varianta explicata':pve,
              'varianta cumulata':alpha_cum,
              'procentul cumulat': pve_cum
              }).to_csv('./dateOUT/PCA_Varianta_componente.csv',index=False)

# plot varianta componente cu evidentierea criteriilor de relevanta (Kaiser, Cattell, procent min)
plt.figure(figsize=(8,8))
plt.title('Plot varianta componente')
Xindex=['C'+str(i+1) for i in range(len(alpha))]
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

# calcul corelatii factoriale (variabile obs - componente)
a=pca.components_.T # matricea componentelor principale
rxc=a * np.sqrt(alpha)

# corelograma corelatii factoriale
rxc_df=pd.DataFrame(data=rxc,index=labels,columns=['C'+str(i+1) for i in range(rxc.shape[1])])
plt.figure(figsize=(8,8))
plt.title('Corelograma corelatii factoriale')
heatmap(rxc_df,vmin=-1,vmax=1,cmap='bwr',annot=True)
plt.show()

# cercul corelatiilor (ex: dintre c1 si c2)
plt.figure(figsize=(12,12))
plt.title('Cercul corelatiilor')
T = [t for t in np.arange(0,np.pi * 2, 0.01)]
X = [np.cos(t) for t in T]
Y = [np.sin(t) for t in T]
plt.plot(X,Y)
plt.axhline(0,c='g')
plt.axvline(0,c='g')
plt.scatter(rxc[:,0],rxc[:,1])
for i in range(rxc.shape[0]):
    plt.text(rxc[i,0],rxc[i,1],labels[i],fontsize=12,ha='right')
plt.show()

# calcul componente si scoruri (incert, n am inteles inca sigur care e faza cu ele)
componente=pca.components_
print(componente) # fiecare vector = o componenta
scores=C/np. np.sqrt(alpha) # scoruri ( sau C idk dar sa zicem ca asa)
print(scores)

# plot componente/scoruri (ex: cu primele 2 componente principale)
plt.figure(figsize=(10, 8))
plt.title('Plot scoruri principale (PC1 vs PC2)')
plt.scatter(scores[:,0],scores[:,1],color='b',alpha=0.6)
for i,country in enumerate(merged['Country']):
    plt.annotate(country,(scores[i,0],scores[i,1]))
plt.axhline(0,c='b')
plt.axvline(0,c='b')
plt.xlabel('Componenta principala 1')
plt.ylabel('Componenta principala 2')
plt.show()

#########################
C2=C**2
# cosinusuri
quality=np.transpose(C2.T/np.sum(C2,axis=1))

# contributii
contributions=C2/(x.shape[0]*alpha)

# comunalitati
communalities=np.cumsum(rxc*rxc,axis=1)

# corelograma comunalitati
communalities_df=pd.DataFrame(data=communalities,index=labels,columns=['C'+str(i+1) for i in range(communalities.shape[1])])
communalities_df.to_csv('./dateOUT/PCA_comunalitati')

plt.figure(figsize=(8,8))
plt.title('Corelograma comunalitati')
heatmap(communalities_df,vmin=-1,vmax=1,cmap='bwr',annot=True)
plt.show()