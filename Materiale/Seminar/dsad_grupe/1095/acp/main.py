import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from utils import nan_replace, to_dataframe, corelograma, plot_corelatii, plot_componente

t = pd.read_csv("./Freelancer.csv", index_col=1)
nan_replace(t)

variabile_observate = list(t.columns)[2:]
x_orig = t[variabile_observate]

# la ACP mereu vom face standardizare!!!
# np.mean(x_orig) <=> x_orig.mean()
x = (x_orig - np.mean(x_orig, axis=0)) / np.std(x_orig, axis=0)

# dimensiunile setului de date
n, m = x.shape

# initializar model ACP
model_acp = PCA()  # apel de constructor
model_acp.fit(x)  # antrenam modelul ACP folosind datele noastre

# alpha reprezinta valorile proprii (eigen values)
alpha = model_acp.explained_variance_
print("alpha", alpha)

# a reprezinta vectorii proprii (eigen vectors) / loadings
a = model_acp.components_

# componentele principale rezultate in urma ACP, dupa formula: c = x @ a
c = model_acp.transform(x)

# afisarea componentelor principale
labels = ["C" + str(i+1) for i in range(len(alpha))]
componente_df = to_dataframe(c, t.index, labels, "componente.csv")
plot_componente(componente_df, "C1", "C2", aspect=1)

# determinarea numarului componentelor principale semnificative
# Kaiser
# intrucat in ACP variabilele noastre initiale sunt standardizate, inseamna ca std Vi = 1
# crit. Kaiser va considera ca fiind semnificative acele comp. principale care au std > 1
conditie = np.where(alpha > 1)  # np.where intoarce ca rezultat un tuplu, cu un singur element, de forma:  (array([0, 1, 2, 3, 4, 5, 6]),)
print("conditie Kasier: ", conditie)
array_din_where = conditie[0]
nr_comp_s_kaiser = len(array_din_where)
print("Comp principale semnificative cf crit Kaiser: ", nr_comp_s_kaiser)

# Cattel
eps = alpha[0 : (m-1)] - alpha[1 : m]  # diferenta dintre valori proprii consecutive
sigma = eps[0: (m-2)] - eps[1: len(eps)] # diferenta de ordin 2 - panta graficului
indici_negativi = (sigma < 0)
print("Indici Cattel:", indici_negativi)

if any(indici_negativi):
    conditie = np.where(indici_negativi) # rezultatul lui where o sa fie de forma  (array([True, False, True ...]),)
    array_din_where = conditie[0] # extragem primul si singurul element din tuplu

    nr_comp_s_cattel = array_din_where[0] + 1  # extrag indicele primei aparitii a lui True
else:
    nr_comp_s_cattel = None
print("Comp principale semnificative cf crit Cattel: ", nr_comp_s_cattel)

# procent de acoperire
ponderi = np.cumsum(alpha / sum(alpha))
conditie = np.where(ponderi > 0.8)

nr_comp_s_procent = conditie[0][0] + 1 # explicatiile sunt aceleasi ca mai sus
print("Comp principale semnificative cf crit procent de acoperire: ", nr_comp_s_procent)

# calcul corelatii intre variabilele initiale si componentele principale
# sau altfel spus: care variabile initiale imi compun componentele principale.

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# mare atentie cum alegeti indicii in slicing:
# daca ma intereseaza coef de corelatie dintre X si C: corr[:m, m:]
# daca ma intereseaza coef de corelatie dintre C si X: corr[m:, :m]

corr = np.corrcoef(x, c, rowvar=False)
print(f"Corrcoef: {corr.shape}, {n}, {m}, \n, {corr}")
r_x_c = corr[:m, m:]
r_x_c_df = to_dataframe(r_x_c, variabile_observate, labels, "corelatii_factoriale.csv")

corelograma(r_x_c_df)
plot_corelatii(r_x_c_df, "C1", "C2")
plot_corelatii(r_x_c_df, "C1", "C3")

# comunalitati - in ce masura varianta din variabilele initiale este pastrata/surprinsa de componentele principale
r_patrat = r_x_c * r_x_c
comunalitati = np.cumsum(r_patrat, axis=1)
comunalitati_df = to_dataframe(comunalitati, variabile_observate, labels, "comunalitati.csv")

corelograma(comunalitati_df, vmin=0, vmax=1, titlu="Comunalitati")

# cosinusuri -
c_patrat = c ** 2
sume = c_patrat.sum(axis=1, keepdims=True)
cosin = c_patrat / sume
cosin_df = to_dataframe(cosin, t.index, labels, "cosinusuri.csv")



