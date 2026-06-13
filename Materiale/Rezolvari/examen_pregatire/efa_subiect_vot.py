import numpy as np
import pandas as pd
from factor_analyzer import calculate_kmo,calculate_bartlett_sphericity,FactorAnalyzer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

rawVot=pd.read_csv('./dateIN/Vot.csv',index_col=0)
rawCoduriLocalitate=pd.read_csv('./dateIN/Coduri_localitati.csv',index_col=0)
labels=list(rawVot.columns.values[1:])
print(rawVot)
merged=rawVot.merge(rawCoduriLocalitate,right_index=True,left_index=True).drop('Localitate_y',axis=1).rename(columns={'Localitate_x':'Localitate'})[['Judet','Localitate']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(str(merged))

#A1
merged['Categorie']=merged[labels].idxmin(axis=1)
merged[['Localitate','Categorie']].to_csv('./dateOUT/cerinta1_vot.csv')
print(merged)

#A2
merged[['Judet','Localitate']+labels].groupby('Judet').apply(lambda df:pd.Series({ind: np.mean(df[ind])for ind in labels})).to_csv('./dateOUT/cerinta2_vot.csv')

#B1
X=StandardScaler().fit_transform(merged[labels])

bartlett_stat,bartlett_p=calculate_bartlett_sphericity(X)
if bartlett_p>0.001:
    print('P-value ', bartlett_p)
    print('Nu exista factori comuni semnificativi')
else:
    print('P-value ', bartlett_p)
    print('Exista factori comuni semnificativi')

kmo_all,kmo_p=calculate_kmo(X)
if kmo_p<0.4:
    print('Setul de date nu este adecvat pentru Analiza factoriala')
    exit(0)

#B2
efa=FactorAnalyzer(n_factors=X.shape[1]-1,rotation=None)
scores=efa.fit_transform(X)
pd.DataFrame(data=scores).to_csv('./dateOUT/f.csv')

#B3
plt.figure(figsize=(8,8))
plt.title('Grafic scoruri pentru primii 2 factori')
plt.scatter(scores[:,0],scores[:,1])
plt.xlabel('Factor 1')
plt.ylabel('Factor 2')
plt.show()