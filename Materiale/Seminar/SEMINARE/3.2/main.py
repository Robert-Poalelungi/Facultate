import numpy as np
import pandas as pd
from functii import *

np.set_printoptions(precision=5, threshold=10000, suppress=True)

tabel = pd.read_csv("Teritorial_2022.csv", index_col=0)
#print(tabel,type(tabel))
variabile = list(tabel.columns)
variabile_numerice = variabile[3:]
print(variabile, variabile_numerice, sep="\n")

x = tabel[variabile_numerice].values
#print(x, type(x))

# Cerinta 1
nan_replace(x)
# print(x)

# Cerinta 2
macroregiuni = tabel["Macroregiunea"].values
corelatii, covariante = calcul_corelatii_covariante(x, macroregiuni)
print("----------------------------------------------------")
print (corelatii,covariante)
for v in corelatii:
    salvare(corelatii[v], variabile_numerice, variabile_numerice, "r_" + str(v) + ".csv")
for v in covariante:
    salvare(covariante[v], variabile_numerice, variabile_numerice, "v_" + str(v) + ".csv")

# Cerinta 3
t_pvalues, t_test = teste_c(x)
salvare(t_test, variabile_numerice, ["Shapiro", "KS", "Chi2"], "teste.csv")
