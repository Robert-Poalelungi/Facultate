import numpy as np
import pandas as pd
from factor_analyzer import *

set_date=pd.read_csv("prezenta_vot.csv",index_col=0)
variabile=list(set_date)
variabile_numerice=variabile[10:]
print(variabile_numerice)
date_numerice=set_date[variabile_numerice].values

def nan_replace(t):
    for v in t.columns:
        if t[v].isna().any():
            t[v].fillna(t[v].mean,inplace=True)
        else:
            t[v].fillna(t[v].mode()[0], inplace=True)

def salvare(x,linii=None,coloane=None,out="out.csv"):
    t=pd.DataFrame(x,linii,coloane)
    t.to_csv(out)

valori_lipsa=set_date.isna().any().any()
if valori_lipsa:
    nan_replace(set_date)

#Cerinta1
categorie_minima=set_date[variabile_numerice].idxmax(axis=1)
set_date_1=set_date.copy()
set_date_1["Categorie_minima"]=categorie_minima
print(set_date_1[["Localitate","Categorie_minima"]])

#Cerinta2
cerinta2=set_date[variabile_numerice+["Judet"]].groupby(by="Judet").mean()
print(cerinta2)

#Cerinta3
set_AF=set_date.copy()
set_AF=set_AF.drop(columns=["Localitate","Judet","Mediu","Votanti_LP","Votanti_LS","LP","LS","LSC","UM","LT"])
print(set_AF)
set_date_standardizat=((set_AF.values-np.mean(set_AF.values,axis=0))/ np.std(set_AF.values,axis=0))
fa=FactorAnalyzer(n_factors=10,rotation=None)
fa.fit(set_date_standardizat)

#Bartlett
chi_square,p_value=calculate_bartlett_sphericity(set_date_standardizat)
print(f"chi_square:{chi_square}\np_value:{p_value}")

#KMO
kmo_all,kmo_model=calculate_kmo(set_date_standardizat)
print(f"kmo_all:{kmo_all}\nkmo_model:{kmo_model}")

#Scoruri
scoruri=fa.transform(set_date_standardizat)
salvare(scoruri,out="f.csv")











