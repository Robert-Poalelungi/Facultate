import numpy as np
import pandas as pd
from functii import *

np.set_printoptions(threshold=np.inf)
etnicitate=pd.read_csv('Ethnicity.csv',index_col=0)
variabile=list(etnicitate)
variabile_numerice=variabile[1:]
print("Valori lipsa?",etnicitate.isna().any().any())

#Cerinta1
localitati=pd.read_csv('Coduri_Localitati.csv',index_col=0)
etnicitate_=etnicitate.merge(localitati,right_index=True,left_index=True)
etnicitate_judet=etnicitate_[variabile_numerice+["County"]].groupby(by="County").sum()
#print(etnicitate_judet)

judete=pd.read_csv('Coduri_Judete.csv',index_col=0)
etnicitate_judet_=etnicitate_judet.merge(judete,right_index=True,left_index=True)
etnicitate_regiuni=etnicitate_judet_[variabile_numerice+["Regiune"]].groupby(by="Regiune").sum()
#print(etnicitate_regiuni)

regiuni=pd.read_csv('Coduri_Regiuni.csv',index_col=0)
etnicitate_regiuni_=etnicitate_regiuni.merge(regiuni,right_index=True,left_index=True)
etnicitate_macro=etnicitate_regiuni_[variabile_numerice+["MacroRegiune"]].groupby(by="MacroRegiune").sum()
#print(etnicitate_macro)

#Cerinta2
etnicitate_loc_p=etnicitate[variabile_numerice].apply(func=procente,axis=1)
#print(etnicitate_loc_p)

etnicitate_jud_p=etnicitate_judet[variabile_numerice].apply(func=procente,axis=1)
#print(etnicitate_jud_p)

etnicitate_regiuni_p=etnicitate_regiuni[variabile_numerice].apply(func=procente,axis=1)
#print(etnicitate_regiuni_p)

etnicitate_macro_p=etnicitate_macro[variabile_numerice].apply(func=procente,axis=1)
#print(etnicitate_macro_p)

#Cerinta3
dis=etnicitate_[variabile_numerice+["County"]].groupby(by="County").apply(func=disimilaritate,coloane=variabile_numerice)
print(dis)
