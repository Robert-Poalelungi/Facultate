import pandas as pd
import numpy as np
import factor_analyzer as fa
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sb
import AEF as aef

vot = pd.read_csv('dataIN/Vot.csv')
localitati = pd.read_csv('dataIN/Coduri_localitati.csv')

def categoriaMin(t):
    x = t.values
    min = np.argmin(x)
    return pd.Series(data=[t.index[min]], index=['Categoria'])

categorii = ['Barbati_25-34', 'Barbati_35-44',
       'Barbati_45-64', 'Barbati_65_', 'Femei_18-24', 'Femei_35-44',
       'Femei_45-64', 'Femei_65_']
t1 = vot[categorii].apply(func=categoriaMin,axis=1)
t2 = vot[['Siruta', 'Localitate']]
cerinta1 = pd.concat([t2, t1], axis=1, join='inner')
cerinta1.reset_index(drop=True)
cerinta1.to_csv('dataOUT/Cerinta1_Verif.csv',index=False)

data_merge = pd.merge(vot,localitati,on='Siruta')
t3 = data_merge[['Judet','Barbati_25-34', 'Barbati_35-44',
       'Barbati_45-64', 'Barbati_65_', 'Femei_18-24', 'Femei_35-44',
       'Femei_45-64', 'Femei_65_']]

cerinta2 = t3.groupby('Judet').mean()
cerinta2.to_csv('dataOUT/Cerinta2_Verif.csv')

#AEF:
tabel = pd.read_csv('dataIN/Vot.csv')
obs = tabel.index.values
var = tabel.columns.values
X_brut = tabel[var].values

def inlocuireNAN(X):
    medie = np.nanmean(a=X,axis=0)
    pozitie = np.where(np.isnan(X))
    X[pozitie] = medie[pozitie[1]]
    return X

X = inlocuireNAN(X_brut)

scalare = StandardScaler()
Xstd = scalare.fit_transform(X)
Xstd_df = pd.DataFrame(data=Xstd,index=obs,columns=var)

aefModel = aef.AEF(X)
# testul Bartlett
nrFactoriSemnificativi = 1

for k in range(1, var.shape[0]):
    faModel = fa.FactorAnalyzer(n_factors=k)
    faModel.fit(X=Xstd_df)
    factoriComuni = faModel.loadings_
    print(factoriComuni)
    factoriSpecifici = faModel.get_uniquenesses()
    print(factoriSpecifici)
    aefModel.calculTestBartlett(factoriComuni, factoriSpecifici)

#scorurile factoriale
scoruri = aefModel.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri)
scoruri_df.to_csv('f.csv')

#graficul scorurilor factoriale pentru primii 2 fact
def corelograma(matrice=None,dec=1,titlu='',valMin=-1,valMax=1):
    plt.figure(titlu,figsize=(11,8))
    plt.title(titlu,fontsize=14,color='b',verticalalignment='bottom')
    sb.heatmap(data=np.round(matrice,dec),cmap='bwr',vmin=valMin,vamx=valMax,annot=True)
    plt.show()

corelograma(matrice=scoruri_df,titlu='Corelograma scorurilor')





