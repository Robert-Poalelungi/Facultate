import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
from functii import *

set_date = pd.read_csv('mortalitate_ro.csv', index_col=1)

#adaugare valori lipsa
valori_lipsa = set_date.isna().any().any()
if valori_lipsa:
    nan_replace(set_date)

variabile = set_date.copy()
variabile = variabile.drop(columns=['Judet'])

#Standardizare
set_date_standardizat=((variabile.values-np.mean(variabile.values,axis=0))/np.std(variabile.values,axis=0))

#Bartlett
chi_square,p_value=calculate_bartlett_sphericity(set_date_standardizat)
print(f'chi_square:{chi_square}\np_value:{p_value}')

#KMO
kmo_all,kmo_model=calculate_kmo(set_date_standardizat)
print(f'KMO Overall: {kmo_all}\nKMO Model: {kmo_model}')

#Varianta
fa=FactorAnalyzer(n_factors=3,rotation=None)
fa.fit(set_date_standardizat)
varianta=fa.get_factor_variance()
print(varianta)

#Corelatii
set_date_standardizat_df=pd.DataFrame(set_date_standardizat,columns=variabile.columns)
corelatii=set_date_standardizat_df.corr()
print(corelatii)

#Comunalitati
comunalitati=fa.get_communalities()
varianta=fa.get_uniquenesses()
comunalitati_df=pd.DataFrame([comunalitati], columns=variabile.columns)
varianta_df=pd.DataFrame([varianta], columns=variabile.columns)
print(comunalitati_df)
print(varianta_df)

#Scoruri
scoruri=fa.transform(set_date_standardizat)
print(scoruri)






