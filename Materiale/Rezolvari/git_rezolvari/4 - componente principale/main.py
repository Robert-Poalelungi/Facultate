import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.ma.extras import average
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

rata = pd.read_csv('./input/Rata.csv', index_col=0)
cod = pd.read_csv('./input/CoduriTariExtins.csv', index_col=0)

rata = rata.fillna(0)
cod = cod.fillna(0)

merged = rata.merge(cod['Continent'], left_index=True, right_index=True)

lista = list(rata)[1:]

print(rata)
print(cod)
print(merged)
print(lista)

# A

# 1 - tarile in care rata sporului natural < rata medie a sporului natural global, descrescator

media = rata['RS'].mean()

cerinta1 = rata[rata['RS'] < media]

cerinta1 = cerinta1[['Country_Name', 'RS']]

cerinta1 = cerinta1.sort_values(by='RS', ascending=False)

cerinta1.to_csv('./output/Cerinta1.csv', index=True)



# 2 - pentru fiecare continent tarile cu cele mai mai valori pentru fuecare dintre indicatorii miscarii naturale a populatiei

grupare = merged.groupby('Continent')

cerinta2 = grupare[lista].idxmax()

cerinta2.to_csv('./output/Cerinta2.csv', index=True)


# B - ANALIZA COMPONENTELOR PRINCIPALE

# preprocesare

date = pd.read_csv('./input/Rata.csv')

date_numerice = date.drop(columns={'Three_Letter_Country_Code', 'Country_Name'})

# standardizare date
scaler = StandardScaler()
date_standard = scaler.fit_transform(date_numerice)

# aplicare ACP
pca = PCA()

date_pca = pca.fit(date_standard)

componente_principale = pca.components_

# 1 - tabelul variatiei componentelor pricipale

varianta = pca.explained_variance_

var_ratio = pca.explained_variance_ratio_

var_cumulata = np.cumsum(var_ratio)
























