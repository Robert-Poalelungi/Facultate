import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# citire fisiere
alcool = pd.read_csv('./input/alcohol.csv', index_col=0)
continente = pd.read_csv('./input/CoduriTariExtins.csv', index_col=0)

# inlocuire NaN
alcool = alcool.fillna(0)
continente = continente.fillna(0)

# merge date
merged = alcool.merge(continente, left_index=True, right_index=True)

# creare lista ani
lista_ani = list(alcool)[1:]

# afisare date
print(alcool)
print(continente)
print(merged)
print(lista_ani)


# A

# 1 - media consumului in 5 ani per tara
# tara, codul si media

alcool['Medie'] = alcool[lista_ani].mean(axis=1)

cerinta1 = alcool[['Code', 'Medie']]

cerinta1.to_csv('./output/Cerinta1.csv', index=False)


# 2 - anul cu cea mai mare valoare medie pe continent
# nume continent, anul
# medie pe continent pentru toti anii, si afisez anul maxim

grupare_continente = merged.groupby('Continent')

grupare_continente = grupare_continente[lista_ani].mean()

cerinta2 = grupare_continente.idxmax(axis=1)
cerinta2.name = 'Anul'

cerinta2.to_csv('./output/Cerinta2.csv')


# B - CLUSTERI

# preprocesare

date = pd.read_csv('./input/alcohol.csv')

date = date.fillna(0)

date_procesate = date[lista_ani]


# 1 - matricea ierarhie

z = linkage(date_procesate, method='ward')
print('matrice ierarhie:\n', z)

# dendograma random

plt.figure(figsize=(10,7))
dendrogram(z)
plt.title("Dendrograma - Calcul Ierarhie")
plt.show()

# 2 - dendograma partitie optimala

# calcul partitie optima
distanta = z[:, 2]
diferente = np.diff(distanta, 2)
punct_elb = np.argmax(diferente) + 1
print("Numarul optim de clustere este: ", punct_elb)

# dendograma partitie optimala
plt.figure(figsize=(10,7))
dendrogram(z, color_threshold=distanta[punct_elb-1])
plt.title("Dendrograma Partitie Optimala")
plt.show()



















