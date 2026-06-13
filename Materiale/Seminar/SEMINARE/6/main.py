import numpy as np
import pandas as pd
from functii import *
from grafice import *

np.set_printoptions(5, 10000, suppress=True)

set_date = pd.read_csv("mortalitate_ro.csv", index_col=1)
variabile_observate = list(set_date)[1:]

nan_replace(set_date)

model_acp = acp(set_date, variabile_observate)
model_acp.fit()
# print("Varinta componentelor principale:")
# print(model_acp.alpha)

# Analiza variantei
varianta = model_acp.tabelare_varianta()
varianta.to_csv("Varianta.csv")
print(varianta)
print("Criterii de selectie:")
print(model_acp.criterii)
alpha = model_acp.alpha
plot_varianta(alpha, model_acp.criterii)

# Analiza corelatiilor factoriale
r = model_acp.r
etichete_componente = varianta.index
t_r = pd.DataFrame(r, variabile_observate, etichete_componente)
t_r.to_csv("R.csv")
corelograma(t_r)
scatter(t_r,titlu="Plot corelatii",corelatii=True)

# Analiza scorurilor
c = model_acp.c
s = c/np.sqrt(alpha)
t_s = pd.DataFrame(s,set_date.index,etichete_componente)
t_s.to_csv("Scoruri.csv")
scatter(t_s)
show()
