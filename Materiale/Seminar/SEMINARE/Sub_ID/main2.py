import numpy as np
import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype
from sklearn.decomposition import PCA

tabel=pd.read_csv('MiseNatPopTari.csv',index_col=0)

def nan_replace(t):
    for v in t.columns:
        if t[v].isna().any():
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

valori_lipsa=tabel.isna().any().any()
if valori_lipsa:
    nan_replace(tabel)
variabile=list(tabel)
variabile_numerice=variabile[2:]
date_numerice=tabel[variabile_numerice].values

#Cerinta1
RS=tabel["RS"].values
cerinta1=tabel[variabile_numerice][RS<0]
print(cerinta1)
#SAU
cerinta3=tabel[tabel["RS"]<0]
print(cerinta3)

#Cerinta2
tabel_cont=pd.read_csv('CoduriTariExtins.csv',index_col=0)
tabel_=tabel.merge(tabel_cont,right_index=True,left_index=True)
cerinta2=tabel_[variabile_numerice+["Continent"]].groupby(by="Continent").mean()
print(cerinta2)

#Cerinta3
variabile_analiza=tabel.copy()
variabile_analiza=variabile_analiza.drop(columns=["Country_Name","Three_Letter_Country_Code"])

set_date_standardizat=((variabile_analiza.values-np.mean(variabile_analiza.values,axis=0))/np.std(variabile_analiza.values,axis=0))
acp_model=PCA()
acp_model.fit(set_date_standardizat)
componente=acp_model.components_

varianta_explicata=acp_model.explained_variance_
varianta_explicata_ratio=acp_model.explained_variance_ratio_
print(varianta_explicata)
print(varianta_explicata_ratio)

#Cerinta4
def salvare(x,linii=None,coloane=None,out="out.csv"):
    t=pd.DataFrame(x,linii,coloane)
    t.to_csv(out)
scoruri = acp_model.transform(set_date_standardizat)
salvare(scoruri, out="scoruri2.csv")

#Cerinta5
#corelograma











































