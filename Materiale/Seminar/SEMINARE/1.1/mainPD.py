import numpy as np
import pandas as pd
from functii2 import *

np.set_printoptions(threshold=np.inf)
tabel=pd.read_csv("Educatie.csv",index_col=0)
variabile=list(tabel)
variabile_numerice=variabile[2:]
date_numerice=tabel[variabile_numerice].values
print("Valori lipsa?",tabel.isna().any().any())
print(variabile,variabile_numerice,date_numerice,sep="\n")

#Cerinta1
col_abs=["Abs_liceal","Abs_postlic","Abs_primar_gimn","Abs_profes","Abs_tehnic","Abs_univ"]
col_pop=["Pop_liceal","Pop_profess","Pop_primar_gimn","Pop_univ"]
tabel1=tabel.copy()
tabel1["Numar absolventi"]=tabel[col_abs].sum(axis=1)
tabel1["Populatie"]=tabel[col_pop].sum(axis=1)
rezultat=tabel1[["Localitate","Judet","Numar absolventi","Populatie"]]
#print(rezultat)
salvare(rezultat,out="cerinta1_pd.csv")

#Cerinta2
date = tabel.select_dtypes(include=[np.number])
medii = date.mean()
abateri_standard = date.std()
coeficienti_variatie = abateri_standard / medii
rezultate = pd.DataFrame({
    'Medii': medii,
    'Abateri_Standard': abateri_standard,
    'Coeficienti_Variatie': coeficienti_variatie
})
#print(rezultat)
salvare(rezultate,out="cerinta2_pd.csv")

#Cerinta3
localitati_cu_absolventi_universitari = tabel.loc[tabel["Abs_univ"]>0]
#print(localitati_cu_absolventi_universitari)
salvare(localitati_cu_absolventi_universitari,out="cerinta3_pd.csv")

#Cerinta4
pop_univ_desc=tabel.sort_values(by="Pop_univ",ascending=False)
#print(pop_univ_desc)
salvare(pop_univ_desc,out="cerinta4_pd.csv")

#Cerinta5
cerinta5=["Localitate","Pop_liceal","Pop_profess","Pop_primar_gimn","Pop_univ"]
#print(tabel[cerinta5])
salvare(tabel[cerinta5],out="cerinta5_pd.csv")








