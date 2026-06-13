import pandas as pd
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo

# citire fisiere
diversitate = pd.read_csv('./input/Diversitate.csv', index_col=0)
coduri = pd.read_csv('./input/Coduri_Localitati.csv', index_col = 0)

# inlocuire valori NaN
diversitate = diversitate.fillna(0)
coduri = coduri.fillna(0)

# merge
merged = diversitate.merge(coduri['Judet'], left_index=True, right_index=True)

# lista
lista = list(diversitate)[1:]

# afisare date
print(diversitate)
print(coduri)
print(merged)
print(lista)

# A

# 1 - localitatile in care cel putin pentru un an diversitatea a fost 0
# codul siruta, denumirea, indicii de diversitate



cerinta1 = diversitate[diversitate[lista].min(axis=1) == 0]

cerinta1 = cerinta1[['Localitate'] + lista]

cerinta1.to_csv('./output/Cerinta1.csv', index=True)


# 2 - pentru fiecare judet - localitatea ce diversitatea medie maxima
# judet, localitatea, maximul

merged['Medie'] = merged[lista].mean(axis=1)

grupare = merged.groupby('Judet')

grupare = grupare['Medie'].idxmax()

grupare = merged.loc[grupare]

cerinta2 = grupare[['Judet', 'Localitate', 'Medie']]

cerinta2.to_csv('./output/Cerinta2.csv', index=False)


# B - ANALIZA FACTORIALA

# preprocesare

date = pd.read_csv('./input/Diversitate.csv')
date = date.fillna(0)
date = date.drop(columns={'Siruta', 'Localitate'})

# 1 - analiza factorilor comuni

analiza_factoriala = FactorAnalyzer(n_factors=3, rotation='varimax')
analiza_factoriala.fit(date)

analiza_finala = analiza_factoriala.get_factor_variance()

print("Varianta factori:\n", analiza_finala)


# 2 - corelatii factoriale

corelatii_factoriale = analiza_factoriala.loadings_

print("Corelatii factoriale:\n", corelatii_factoriale)


















