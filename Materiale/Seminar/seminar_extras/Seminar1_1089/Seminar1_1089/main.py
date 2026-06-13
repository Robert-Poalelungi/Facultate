import sys

import numpy as np
import pandas as pd

from functii import nan_replace, standardizare_centrare, tabelare_matrice, calcul_corelatii_covariante

pd.set_option("display.max_columns",None)
np.set_printoptions(5,threshold=sys.maxsize,suppress=True)

tabel_date = pd.read_csv("data_in/Teritorial_2022.csv",index_col=0)

# print(type(tabel_date))
# print(tabel_date)

variabile_numerice = list(tabel_date.columns[3:])
# print(variabile_numerice,type(variabile_numerice))

x = tabel_date[variabile_numerice].values
# print(type(x))
# print(x)
nan_replace(x)
# print(np.where(np.isnan(x)))

# Standardizare
x_std = standardizare_centrare(x)
# Centrare
x_c = standardizare_centrare(x,scal=False)
tabelare_matrice(x_std,tabel_date.index,variabile_numerice,"data_out/x_std.csv")

# Corelatii/Covariante
r = np.corrcoef(x,rowvar=False)
tabelare_matrice(r,variabile_numerice,variabile_numerice,"data_out/r.csv")
v = np.cov(x,rowvar=False)
tabelare_matrice(v,variabile_numerice,variabile_numerice,"data_out/v.csv")
r_v = calcul_corelatii_covariante(x,tabel_date["Regiunea"].values)
for v in r_v:
    # print("Regiunea ",v)
    # print("Corelatii:")
    print(r_v[v][0])
    tabelare_matrice(r_v[v][0],variabile_numerice,variabile_numerice,"data_out/R_"+v+".csv")
    # print("Covariante:")
    # print(r_v[v][1])
    tabelare_matrice(r_v[v][1],variabile_numerice,variabile_numerice,"data_out/V_"+v+".csv")
