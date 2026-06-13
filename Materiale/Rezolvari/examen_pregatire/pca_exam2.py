import numpy as np
import pandas as pd
from scipy.stats import variation
from seaborn import heatmap
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer, calculate_bartlett_sphericity,calculate_kmo


rawGlobal=pd.read_csv('./dateIN/GlobalIndicatorsPerCapita_2021.csv',index_col=0)
rawContinents=pd.read_csv('./dateIN/CountryContinents.csv',index_col=0)
labels=list(rawGlobal.columns.values[1:])

merged=rawGlobal.merge(rawContinents,right_index=True,left_index=True)\
    .drop('Country_y',axis=1)\
    .rename(columns={'Country_x':'Country'})\
    [['Continent','Country']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(merged)

#A1
merged['Valoare adaugata']=merged[labels[7:]].sum(axis=1)
merged[['Country','Valoare adaugata']].to_csv('./dateOUT/Cerinta1_2.csv')

#A2
merged[['Continent']+labels].groupby('Continent').apply(lambda row: pd.Series({i:np.mean(row[i])/np.std(row[i])*100 for i in labels})).to_csv('./dateOUT/Cerinta2_2.csv')

#B1
x=StandardScaler().fit_transform(merged[labels])
pca=PCA()
C=pca.fit_transform(x)
alpha=pca.explained_variance_
pve=pca.explained_variance_ratio_
varianta_cumulata=np.cumsum(alpha)
varianta_explicata_cumulata=np.cumsum(pve)
print('Varianta componentelor: ',alpha)
print('Procent din varianta explicata: ',pve)
print('Varianta cumulata: ',varianta_cumulata)
print('Procent din varianta cumulata: ',varianta_explicata_cumulata)

#B2
scores=C/np.sqrt(alpha)
pd.DataFrame(data=scores).to_csv('./dateOUT/scoruri.csv')

#B3
plt.figure(figsize=(8,8))
plt.title('Grafic scoruri primele 2 axe principale')
continents=merged['Continent'].astype('category').cat.codes
plt.scatter(scores[:,0],scores[:,1],c=continents)
for i,country in enumerate(merged['Country']):
    plt.annotate(country,(scores[i,0],scores[i,1]),)
plt.xlabel('Componenta 1')
plt.ylabel('Componenta 2')
plt.show()

#varianta componenta cu evidentierea criteriilor(Kaiser,Cattell,procent minim)
plt.figure(figsize=(8,8))
plt.title('Plot pentru varianta componentelor cu evidentierea criteriilor')
xLabels=['C'+str(i+1) for i in range(len(alpha))]
plt.plot(xLabels,alpha,'bo-')
plt.axhline(1,c='r',label='Kaiser')
d=np.diff(np.diff(alpha))
if (d<0).any():
    j_cattell=np.where(d<0)[0][0]+2
    plt.axhline(alpha[j_cattell-1],c='m',label='Cattell')
print(d)

procent_cumulat=np.cumsum(alpha)*100/np.sum(alpha)
procent_minimal_k=np.where(procent_cumulat>80)[0][0]+1
plt.axhline(alpha[procent_minimal_k-1],c='g',label="Procent minimal>80%")
plt.legend()
plt.xlabel('Componenta')
plt.ylabel('Varinata')
plt.show()

#cerc corelatii factoriale
a=pca.components_.T
rxc=a*np.sqrt(alpha)

plt.figure(figsize=(8,8))
plt.title('Cerc corelatii factoriale')
T=np.arange(0,np.pi*2,0.01)
X=np.cos(T)
Y=np.sin(T)
plt.plot(X,Y)
plt.axvline(0,c='g')
plt.axhline(0,c='g')
plt.scatter(rxc[:,0],rxc[:,1])
for i in range(rxc.shape[0]):
    plt.annotate(labels[i],(rxc[i,0],rxc[i,1]))

plt.xlim(-1.1,1.1)
plt.ylim(-1.1,1.1)
plt.show()

#corelogarama comunalitati
communalities=np.cumsum(rxc*rxc,axis=1)
cummunalities_df=pd.DataFrame(data=communalities,index=labels,columns=['C'+str(i+1) for i in range(communalities.shape[0])])
plt.figure(figsize=(12,8))
plt.title('Corelograma comunalitati')
heatmap(cummunalities_df,vmin=-1,vmax=1,cmap='bwr',annot=True)
plt.show()



#EFA
bartlett_stat,bartlett_p=calculate_bartlett_sphericity(x)
if bartlett_p>0.001:
    print(bartlett_p)
    print('Nu exista factori comuni semnificativ')
    exit(0)