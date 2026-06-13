import numpy as np
import pandas as pd
import pd
from functii import *

np.set_printoptions(threshold=np.inf)
tabel=pd.read_csv('Sanatate.csv',index_col=0)
variabile=list(tabel)
variabile_numerice=variabile[2:]
date_numerice=tabel[variabile_numerice].values
print("Valori lipsa? ", tabel.isna().any().any())
#print(tabel,type(tabel))

#Cerinta1
total_medici=tabel[variabile_numerice].sum(axis=1)
tabel1=tabel.copy()
tabel1["Total_medici_sanatate"]=total_medici
salvare(tabel1[["Judet","Localitate","Total_medici_sanatate"]],out="cerinta1.csv")

#Cerinta2
date=tabel.select_dtypes(include=[np.number])
medii=date.mean(axis=0)
abateri=date.std(axis=0)
coef=abateri/medii
cerinta2=pd.DataFrame({"Medii": medii, "Abateri": abateri,"Coeficienti":coef})
salvare(cerinta2,out="cerinta2.csv")

#Cerinta3
cerinta3=extragere(tabel,"AB")
#print(cerinta3)
salvare(cerinta3,out="cerinta3.csv")

#Cerinta4 - Sortarea descrescătoare a localităților după numărul de medici
selectie=["NrMedici_Privat","NrMedici_Public","MediciFamilie"]
total=tabel[selectie].sum(axis=1)
tabel4=tabel.copy()
tabel4["Total_medici_desc"]=total
#print(tabel4.sort_values(by="Total_medici_desc", ascending=False))
salvare(tabel4.sort_values(by="Total_medici_desc", ascending=False),out="cerinta4.csv")

#Cerinta5
selectie=["Judet","Localitate","PersonalMediu_privat","PersonalMediu_public"]
tabel5=tabel[selectie]
#print(tabel5)
salvare(tabel5,out="cerinta5.csv")

