import numpy as an
import numpy as np
import pandas as pd
from functii2 import *

np.set_printoptions(threshold=np.inf)
tabel=pd.read_csv("prezenta_vot.csv",index_col=0)
variabile=list(tabel)
print("Valori lipsa?",tabel.isna().any().any())
indicatori=["Votanti_LP","Votanti_LS","LP","LS","LSC","UM","LT"]
categorii=["Barbati_18-24","Barbati_25-34","Barbati_35-44","Barbati_45-64","Barbati_65_","Femei_18-24","Femei_25-34","Femei_35-44","Femei_45-64","Femei_65_"]

#Cerinta1 - 1. Salvarea în fișierul Prezenta50.csv a localităților în care prezența la vot a fost mai mare decât
#50%. Va fi salvat codul, numele și procentul prezentei la vot.
#Relația de calcul pentru procentul participării la vot este: LT*100/(Votanti_LP+ Votanti_LS)
prezenta_vot=tabel["LT"]*100/(tabel["Votanti_LP"]+tabel["Votanti_LS"])
tabel1=tabel.copy()
tabel1["Prezenta_vot"]=prezenta_vot
prezenta_vot_50=tabel1[["Localitate","Judet","Prezenta_vot"]][prezenta_vot>50]
salvare(prezenta_vot_50,out="Prezenta501")

#Cerinta2
sortate=tabel1.sort_values(by="Prezenta_vot",ascending=False)
#salvare(sortate,out="PrezentaSort.csv")

#Cerinta3
judete=pd.read_csv("Coduri_Judete.csv",index_col=0)
prezenta_merged=tabel.merge(right=judete,left_on="Judet",right_index=True)
#print(prezenta_merged)
prezenta_reg=prezenta_merged[indicatori+categorii+["Regiune"]].groupby(by="Regiune").sum()

#Cerinta4
tabel1["Categorie_max"]=tabel[categorii].idxmax(axis=1)
print(tabel1[["Categorie_max"]])

#Cerinta5
categorie_varsta="Femei_45-64"
cerinta5=tabel1[tabel1["Categorie_max"]==categorie_varsta]
print(cerinta5)

#Cerinta6


