import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hiclu

alchol = pd.read_csv('dataIN/alchol.csv')
tari = pd.read_csv('dataIN/CoduriTariExtins.csv')

ani = ['2000', '2005', '2010', '2015', '2018']
t1 = alchol
t1.insert(7,'Suma',True)
t1.insert(8,'Media',True)

t1['Suma'] = 0
for an in ani:
    t1['Suma'] += t1[an]

t1['Media'] = 0
for row in t1.index:
    t1['Media'] = t1['Suma']/5

cerinta1 = t1[['Code','Media']]
cerinta1.reset_index(drop=True)
cerinta1.to_csv('dataOUT/Cerinta1_Verif.csv',index=False)

data_merge = pd.merge(alchol,tari,on='Code')
del data_merge['Țara']
del data_merge['Suma']
del data_merge['Media']

def anValMaxMedieContinent(t):
    x = t.values
    max_linie = np.argmax(x)
    return pd.Series(data=[t.index[max_linie]],index=['Anul'])

date_cont = data_merge.groupby(by='Continent').mean()
t2 = date_cont.apply(func=anValMaxMedieContinent,axis=1)
t2.to_csv('dataOUT/Cerinta2_verif.csv')

#AC
#MATRICEA IERARCHICA
tabel = pd.read_csv('dataIN/alchol.csv')
obs = tabel.index.values
var = tabel.columns[2:].values

X_brut = tabel[var].values

def inlocuireNAN(X):
    medie = np.nanmean(X,axis=0)
    pozitie = np.where(np.isnan(X))
    X[pozitie] = medie[pozitie[1]]
    return X

X = inlocuireNAN(X_brut)

def standardizare(X):
    if isinstance(X,np.ndarray):
        medii = np.mean(a=X,axis=0)
        std = np.std(a=X,axis=0)
        Xstd = (X-medii)/std
        return Xstd

Xstd = standardizare(X)
Xstd_df = pd.DataFrame(data=Xstd,index=obs,columns=var)

def calculThreshold(h):
    nrJonctiuni = h.shape[0]
    dist_1 = h[1:,2]
    dist_2 = h[:nrJonctiuni-1,2]
    dif = dist_1 - dist_2
    print(dif);
    jonctDifMax = np.argmax(dif)
    print(jonctDifMax)
    threshold = (h[jonctDifMax,2]+h[jonctDifMax+1,2])/2
    return threshold,nrJonctiuni,jonctDifMax

h_1 = hiclu.linkage(y=Xstd,method='single',metric='euclidean')
# print("H_1:")
# print(h_1)

threshold,nrJonctiuni,jonctDifMax = calculThreshold(h_1)
print(threshold,nrJonctiuni,jonctDifMax)

def dendograma(h,etichete,titlu,threshold):
    plt.figure(figsize=(11,8))
    plt.title(titlu,fontsize=14,color='k')
    hiclu.dendrogram(Z=h,labels=etichete,color_threshold=threshold,leaf_rotation=45)
    plt.axhline(y=threshold,c='r')
    #plt.show()

dendograma1 = dendograma(h=h_1,etichete=obs,titlu='Clusterizarea obs single-eucledian',threshold=threshold)

h_2 = hiclu.linkage(y=np.transpose(Xstd),method='single',metric='correlation')
threshold,nrJonctiuni,jonctDifMax = calculThreshold(h_2)
dendograma(h=h_2,etichete=var,titlu='Clustericare var single-correlation',threshold=threshold)

#ChatGTP:
def determinareClustere(h, jonctiuneDifMax):
    n = len(h)  # numărul de noduri
    clustere = []  # lista de clustere rezultate

    for i in range(n):
        if np.all(h[i] <= jonctiuneDifMax):
            # crează un nou cluster pentru nodul i
            cluster = [i]
            clustere.append(cluster)
        else:
            # găsește clusterul existent cel mai apropiat de nodul i
            min_dif = float('inf')
            min_cluster_idx = None

            for idx, cluster in enumerate(clustere):
                dif = abs(h[i] - h[cluster[0]])
                if np.all(dif < min_dif):
                    min_dif = dif
                    min_cluster_idx = idx

            # adaugă nodul i la clusterul cel mai apropiat (dacă s-a găsit un cluster)
            if min_cluster_idx is not None:
                clustere[min_cluster_idx].append(i)
            else:
                # crează un nou cluster pentru nodul i (în cazul în care nu s-a găsit un cluster existent)
                cluster = [i]
                clustere.append(cluster)

    return clustere


clustere = determinareClustere(h=h_1,jonctiuneDifMax=jonctDifMax)
clustere_df = pd.DataFrame(data=clustere, index={'Cluster': [node for cluster in clustere for node in cluster]})
clustere_df.to_csv('dataOUT/popt.csv')