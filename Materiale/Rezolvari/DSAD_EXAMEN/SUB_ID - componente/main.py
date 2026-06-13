import pandas as pd
import numpy as np
import copy
import ACP as acp
import matplotlib.pyplot as plt
import seaborn as sb

populatie = pd.read_csv('dataIN/MiseNatPopTari.csv')
coduri = pd.read_csv('dataIN/CoduriTariExtins.csv')

t1 = copy.copy(populatie)
t2 = t1[['Country_Name', 'RS']]
cerinta1 = t2[t2['RS']<0]
cerinta1.reset_index(drop=True)
cerinta1.to_csv('dataOUT/Cerinta1.csv',index=False)

data_merge = pd.merge(populatie,coduri,on='Country_Number')
t3 = data_merge[['RS','FR', 'LM', 'MMR', 'LE', 'LEM', 'LEF', 'Continent']]
indicatatori = ['RS','FR', 'LM', 'MMR', 'LE', 'LEM', 'LEF']
cerinta2 = t3[indicatatori + ['Continent']].groupby(by='Continent').mean()
cerinta2.to_csv('dataOUT/Cerinta2.csv')

#ACP:
#Variantele componentelor principale->consola
tabel = pd.read_csv('dataIN/MiseNatPopTari.csv')
var = tabel.columns[3:].values
obs = tabel.index.values

X_brut = tabel[var].values

def inlocuireNAN(X):
    medie = np.nanmean(X,axis=0)
    pozitie = np.where(np.isnan(X))
    X[pozitie] = medie[pozitie[1]]
    return X

X = inlocuireNAN(X_brut)

def standardizare(X):
    medie = np.mean(a=X,axis=0)
    std = np.std(a=X,axis=0)
    Xstd = (X-medie)/std
    return Xstd

Xstd = standardizare(X)
obiect_acp = acp.ACP(Xstd)
componente = obiect_acp.getComponente()
print(componente)

#Scorurile asociate instantelor-> fisier
scoruri = obiect_acp.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri,columns=['C'+
                                                str(j+1) for j in  range(len(var))],index=obs)
scoruri_df.reset_index(drop=True)
scoruri_df.to_csv('dataOUT/scoruri.csv',index=False)

#Graficul scorurilor in primele doua axe principale
def corelograma(matrice,dec=1,titlu='Corelograma',valMin=-1,valMax=1):
     plt.figure(titlu,figsize=(11,8))
     plt.title(titlu,fontsize=10,color='b',
               verticalalignment='bottom')
     sb.heatmap(data=np.round(matrice,dec),c='bwr',vmin=valMin,vmax=valMax,annot=True)
     plt.show()

# corelograma(scoruri_df,'Graficul scorurilor in primele doua axe principale')




