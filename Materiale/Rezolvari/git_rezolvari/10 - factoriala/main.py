import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity

# inlocuire valori nan
def nan_replace(df):
    for col in df.columns:
        if df[col].isna().any():
            if is_numeric_dtype(df[col]):
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)

# citire fisiere
diversitate = pd.read_csv('./res/Diversitate.csv')
print(diversitate)
coduri = pd.read_csv('./res/Coduri_Localitati.csv')
print(coduri)

# inlocuire valori nan
nan_replace(diversitate)
nan_replace(coduri)

#A

# 1. Să se calculeze și să se salveze în fișierul Cerinta1.csv, localitățile în care cel puțin pentru un an diversitatea a
# fost 0. Se va salva codul Siruta, denumirea localității și indicii de diversitate pentru toți anii.

lista_ani = list(diversitate.columns)[2:]
cerinta1 = diversitate[diversitate[lista_ani].min(axis=1) == 0]
cerinta1 = cerinta1[['Siruta', 'Localitate'] + lista_ani]
cerinta1.to_csv("./output/Cerinta1.csv", index=False)

# 2. Să se determine pentru fiecare județ localitatea în care diversitatea medie (media anilor) este maximă.
# Rezultatul va fi salvat în fișierul Cerinta2.csv. Se va salva indicativul de județ, localitatea cu diversitatea medie
# maximă și valoarea diversității medii.

merge = diversitate.merge(coduri[["Siruta", "Judet"]], on="Siruta")
print(merge)

merge['Media'] = merge[lista_ani].mean(axis=1)

maxim = (
    merge
    .groupby("Judet")['Media']
    .agg("max")
    .reset_index()
)

cerinta2 = merge.merge(maxim, on=['Judet', 'Media'])
cerinta2 = cerinta2[['Judet', 'Localitate', 'Media']]
cerinta2.to_csv("./output/Cerinta2.csv", index=False)


# B - ANALIZA FACTORIALA CU ROTATIE

# preprocesare

date = pd.read_csv('./res/Diversitate.csv')
print(date)
nan_replace(date)
x = date.iloc[:,2:]
print(x)
nan_replace(x)

# 1. Varianța factorilor comuni. Se va salva tabelul varianței în fișierul Varianta.csv. Se va salva varianța factorilor,
# procentul de varianță extrasă și procentul cumulat de varianță.

fa = FactorAnalyzer(n_factors=3, rotation='varimax')
fa.fit(x)

varianta_fact, proc_var_extrasa, proc_var_cum = fa.get_factor_variance()

pd.DataFrame({
    'Varianta factorilor': varianta_fact,
    'Procent varianta extrasa': proc_var_extrasa * 100,
    'Procent varianta cumulata': proc_var_cum * 100
}).to_csv('./output/Varianta.csv', index=False)

# 2. Corelațiile factoriale (corelațiile variabile - factori comuni). Acestea vor fi salvate în fișierul r.csv.

corelatii_factoriale = fa.loadings_
pd.DataFrame(corelatii_factoriale, index=x.columns).to_csv('./output/r.csv')









