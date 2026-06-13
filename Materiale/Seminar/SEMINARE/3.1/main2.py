import numpy as np
import pandas as pd
from functii2 import *

np.set_printoptions(threshold=np.inf)
tabel=pd.read_csv('Teritorial_2022.csv',index_col=0)
variabile=list(tabel)
variabile_numerice=variabile[3:]
date_numerice=tabel[variabile_numerice].values
print(date_numerice)
print("Valori lipsa:", tabel.isna().any().any())

#Cerinta1
nan_replace(date_numerice)
salvare(date_numerice,tabel.index,variabile_numerice,out="cerinta1.csv")

#Cerinta2
x_centrat=standardizare(date_numerice,std=False)
salvare(x_centrat,tabel.index,variabile_numerice,out="x_centrat.csv")
x_standardizat=standardizare(date_numerice,std=True)
salvare(x_standardizat,tabel.index,variabile_numerice,out="x_standardizat.csv")

#Cerinta3
r=np.corrcoef(date_numerice,rowvar=False)
salvare(r,variabile_numerice,variabile_numerice,out="corelatie.csv")
v=np.cov(date_numerice,rowvar=False)
salvare(v,variabile_numerice,variabile_numerice,out="covarianta.csv")



