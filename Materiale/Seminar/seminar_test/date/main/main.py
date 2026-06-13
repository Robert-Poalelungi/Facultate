import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils import nan_replace, to_dataframe
from sklearn.decomposition import PCA # pip install scikit-learn

t = pd.read_csv("Freelancer.csv", index_col=1)
nan_replace(t)

variabile_observate = list(t.columns)[2:]  # elimin din coloane valorile: Country,Continent

x_orig = t[variabile_observate]
# atunci cand avem de a face cu ACP - de fiecare data vom face standardizare!!!
# np.mean(x_orig, axis=0) <=> x_orig.mean(axis=0)
x = (x_orig - np.mean(x_orig, axis=0)) / np.std(x_orig, axis=0)

# dimensiunile setului de date
n, m = x.shape # n - nr de randuri | m - nr de coloane

# instantierea modelului de ACP
model = PCA()
# antrenam modelul pe baza datelor noastre
model.fit(x)

# alpha = valorile proprii (eigen values)
alpha = model.explained_variance_
print("alpha", alpha)
# 7.32992191e+00 => 7.32992191 * 10^0 => 7.32992191 * 1 => 7.32992191
# 7.32992191e+02 => 7.32992191 * 10^2 => 7.32992191 * 100 => 732.992191
# 5.47312534e-01 => 5.47312534 / 10^1 => 5.47312534 / 10 => 0.547312534
# 3.84267861e-03 => 3.84267861 / 10^3 => 3.84267861 / 1000 => 0.00384267861

# a = vectorii proprii (eigen vectors) / loadings
a = model.components_

# c = componentele principale determinate de ACP folosind formula: C = X @ A
c = model.transform(x)

# afisati datele in functie de unele componente principale
labels = ["C" + str(i+1) for i in range(len(alpha))]
componente_df = to_dataframe(c, t.index, labels, "componente.csv")

# plot_componente()

# criterii de selectie al numarului de comp. princip. semnificative
# Kaiser
# intrucat in ACP fiecare variabila initiala a fost standardizata, std(Vi) = 1
# crit Kaiser considera ca fiind comp. principale acele componente care au alpha > 1
conditie = np.where(alpha > 1)
print("Conditie Kaiser:", conditie)
# (array([0, 1, 2, 3, 4, 5, 6]),)
first_elem = conditie[0] # obtin o ref la array([0, 1, 2, 3, 4, 5, 6])
no_comp_s_kaiser = len(first_elem)
print("Nr comp semnificative cf crit Kaiser", no_comp_s_kaiser)

# Cattell
eps = alpha[0 : (m-1)] - alpha[1 : m] # diferente de ordin 1 intre valorile alpha
sigma = eps[0 : (m-2)] - eps[1 : len(eps)] # diferente de ordin 2
indici_negativi = (sigma < 0)

if any(indici_negativi):
    conditie = np.where(indici_negativi)
    print("Conditie Cattell: ", conditie)
    no_comp_s_cattell = conditie[0][0] + 1
    print("Nr comp semnificative cf crit Cattell", no_comp_s_cattell)

# procent de acoperire
ponderi = np.cumsum(alpha / sum(alpha))
conditie = np.where(ponderi > 0.8)
no_comp_s_procent = conditie[0][0] + 1
print("Nr comp semnificative cf crit procent", no_comp_s_procent)

# corelatii

# comunalitati

# cosinusuri