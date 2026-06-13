import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from functii import *

set_date = pd.read_csv('mortalitate_ro.csv', index_col=1)

#adaugare valori lipsa
valori_lipsa = set_date.isna().any().any()
if valori_lipsa:
    nan_replace(set_date)
variabile = set_date.copy()
variabile = variabile.drop(columns=['Judet'])

# Standardizare set de date
set_date_standardizat=((variabile.values-np.mean(variabile.values,axis=0))/np.std(variabile.values,axis=0))
print()

# Implementare PCA
pca = PCA()
pca.fit(set_date_standardizat)
componente = pca.components_

# Varianță componente
varianta_explicata = pca.explained_variance_
salvare(varianta_explicata,out="varianta_explicativa.csv")

# varianta explicativa %
varianta_explicativa_ratio = pca.explained_variance_ratio_
salvare(varianta_explicativa_ratio,out="varianta_explicativa_ratio.csv")

# Plot varianță componente
plt.bar(range(1, len(variabile.columns) + 1), varianta_explicata, alpha=0.5, align='center')
plt.step(range(1, len(variabile.columns) + 1), np.cumsum(varianta_explicata), where='mid')
plt.title('Varianță explicată de componente')
plt.xlabel('Număr componente')
plt.ylabel('Varianță explicată')
plt.show()

# Calcul corelații factoriale
corelații_factoriale = np.corrcoef(set_date_standardizat.T, componente.T, rowvar=False)
corelații_factoriale = corelații_factoriale[:variabile.shape[1], variabile.shape[1]:]
salvare(corelații_factoriale,out="corelatii_factoriale.csv")

# Trasare corelogramă corelații factoriale
plt.imshow(corelații_factoriale, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.title('Corelogramă corelații factoriale')
plt.show()

# Trasare cercul corelațiilor
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

plt.figure(figsize=(8, 8))
for i, (x, y) in enumerate(zip(loadings[:, 0], loadings[:, 1])):
    plt.arrow(0, 0, x, y, color='r', alpha=0.5)
    plt.text(x, y, f'Var{i+1}', color='g')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel('Componentă principală 1')
plt.ylabel('Componentă principală 2')
plt.title('Cercul corelațiilor')
plt.grid()
plt.show()

# Calcul componente și/sau scoruri
componenta_principala_1 = componente[:, 0]
componenta_principala_2 = componente[:, 1]

# Trasare plot componente/scoruri
plt.scatter(componenta_principala_1, componenta_principala_2)
plt.xlabel('Componentă principală 1')
plt.ylabel('Componentă principală 2')
plt.title('Plot componente/scoruri')
plt.show()

# Calcul cosinusuri
cosinusuri = loadings / np.sqrt(np.sum(loadings ** 2, axis=0))
salvare(cosinusuri,out="cosinusuri.csv")

# Calcul contribuții
contributii = varianta_explicata * 100
salvare(contributii,out="contributii.csv")

# Calcul comunalități
comunalitati = 1 - pca.explained_variance_ / np.var(set_date_standardizat, axis=0)
salvare(comunalitati,out="comunalitati.csv")

# Trasare corelogramă comunalități
plt.bar(range(1, len(variabile.columns) + 1), comunalitati)
plt.title('Corelogramă comunalități')
plt.xlabel('Variabilă')
plt.ylabel('Comunalitate')
plt.show()