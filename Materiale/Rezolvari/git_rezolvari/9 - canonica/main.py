import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cross_decomposition import CCA
from scipy.stats import chi2

emisii = pd.read_csv('./res/emmissions.csv', index_col=0)
print(emisii)
populatie = pd.read_csv('./res/PopulatieEuropa.csv', index_col=0)
print(populatie)

merged = emisii.merge(populatie[['Region', 'Population']], left_index=True, right_index=True)
print(merged)

lista_emisii = list(emisii)[1:]
print(lista_emisii)

# A

# 1 - emisii totale de particule, la nivel de tara, in tine
# codul, numele, emisii totale

emisii['Total'] = emisii[lista_emisii[:-2]].sum(axis=1)

cerinta1= emisii[['Country', 'Total']]

cerinta1.to_csv('./output/Cerinta1.csv', index = True)

# 2. emisii pe regiune / 100 000 locutori
# cod regiune si emisii

df_2 = merged[['Region', 'Population'] + lista_emisii]

suma_regiune = df_2.groupby('Region').sum()

cerinta2 = suma_regiune[lista_emisii].div(suma_regiune['Population'] / 100000, axis=0)

cerinta2.to_csv('./output/Cerinta2.csv', index = True)


# B - ANALIZA CANONICA

# preprocesare

date = pd.read_csv('emissions.csv')
x = date.iloc[:, 2:6].values
y = date.iloc[:, 6:].values
cca = CCA(n_components=2)
cca.fit(x, y)


# 1 scoruri canonice
x_scoruri, y_scoruri = cca.transform(x, y)

# 2 corelatii canonice
corelatii_canonice = np.corrcoef(x_scoruri.T, y_scoruri.T).diagonal(offset=x_s)
print("Corelatii canonice:\n", corelatii_canonice)

# 3 Bartlett
def test_bartlett(r2,n,p,q,m):
    x = 1-r2
    df=[(p-k+1)*(q-k+1) for k in range(1, m+1)]
    l = np.flip(np.cumprod(np.flip(x)))
    chi2_ = (-n+1+(p+q+1)/2)*np.log(1)
    return 1-chi2.cdf(chi2_, df)






























