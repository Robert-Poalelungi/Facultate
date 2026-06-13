import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

mortalitate = pd.read_csv('./input/Mortalitate.csv', index_col=0)
print(mortalitate)

coduri = pd.read_csv('./input/CoduriTariExtins.csv', index_col=0)
print(coduri)

merged = mortalitate.merge(coduri, left_index=True, right_index=True)
print(merged)

lista_indicatori = list(mortalitate)
print(lista_indicatori)


# A

# 1 - tarile in care rata sporului natural este negativa

rata_spor_natural = list(mortalitate)[:1]
print(rata_spor_natural)

cerinta1 = merged[merged[rata_spor_natural[0]] < 0]
cerinta1 = cerinta1['RS']
cerinta1.to_csv('./output/Cerinta1.csv', index=True)


# 2 - valori medii pentru toti indicatorii, la nivel de continent

cerinta2 = merged.groupby('Continent').mean()

cerinta2.to_csv('./output/Cerinta2.csv', index=True)


# B - componente principale

# preprocesare

date = pd.read_csv('./input/Mortalitate.csv')
print(date)

date_numerice = date.drop(columns={'Tara'})
print(date_numerice)

# standardizare date
scaler = StandardScaler()
date_standardizate = scaler.fit_transform(date_numerice)

# aplicare ACP
pca = PCA()
date_pca = pca.fit(date_standardizate)
componente_principale = pca.components_
print("Componente principale:\n", componente_principale)

# 1 - variantele componentelor principale
varianta = pca.explained_variance_
print("varianta:\n", varianta)

varianta_ratio = pca.explained_variance_ratio_
print("varianta_ratio:\n", varianta_ratio)

varianta_cumulata = np.cumsum(varianta_ratio)
print("varianta_cumulata:\n", varianta_cumulata)

# 2 - scorurile asociate
scoruri_componente = pca.transform(date_standardizate)

scoruri_df = pd.DataFrame(scoruri_componente)

scoruri_df.to_csv('./output/Scoruri.csv', index=True)

