import numpy as np
import pandas as pd
from functii import *

np.set_printoptions(threshold=np.inf)
tabel=pd.read_csv('RataFM.csv',index_col=0)
variabile=list(tabel)
variabile_numerice=variabile[:]
date_numerice=tabel[variabile_numerice].values
#print(tabel,type(tabel))
#print(variabile,variabile_numerice,date_numerice,sep="\n")

#Cerinta1]
an_rata_max= tabel.iloc[:, 1:].idxmax(axis=1)
tabel1=tabel.copy()
tabel1['An_Max_Rata'] = an_rata_max
#print(tabel1['An_Max_Rata'])
salvare(tabel1["An_Max_Rata"],out="cerinta1.csv")

#Cerinta2
date=tabel.select_dtypes(include=[np.number])
medii=date.mean(axis=0)
abateri=date.std(axis=0)
coef=abateri/medii
cerinta2=pd.DataFrame({"Medii":medii, "Abateri":abateri,"Coef":coef})
salvare(cerinta2,out="cerinta2.csv")

#Cerinta3
cerinta3=tabel.loc[tabel["2020"]>80]
#print(cerinta3)
salvare(cerinta3,out="cerinta3.csv")

#Cerinta4
media=date.mean(axis=1)
tabel4=tabel.copy()
tabel4["Rata_medie"]=media
salvare(tabel4.sort_values(by="Rata_medie",ascending=False),out="cerinta4.csv")

#Cerinta5
selectie=["2015","2018"]
#print(tabel[selectie])
salvare(tabel[selectie],out="cerinta5.csv")