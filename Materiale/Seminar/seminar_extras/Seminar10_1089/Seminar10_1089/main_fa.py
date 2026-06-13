import sys

import numpy as np
import pandas as pd

from functii import nan_replace_df, salvare_ndarray, tabelare_varianta_factori
from grafice import plot_varianta, show, corelograma, scatterplot
from geopandas import GeoDataFrame

import factor_analyzer as fa

np.set_printoptions(3,sys.maxsize,suppress=True)
pd.set_option("display.max_columns",None)

set_date = pd.read_csv("data_in/Teritorial2022/Teritorial_2022.csv",index_col=0)
nan_replace_df(set_date)

variabile_observate = list(set_date)[3:]
x = set_date[variabile_observate].values
n,m = x.shape

# Analiza factorabilitatii
# Testul Bartlett
test_bartlett = fa.calculate_bartlett_sphericity(x)
# print(test_bartlett)
if test_bartlett[1]>0.001:
    print("Nu exista factori comuni!")
    exit(0)
# Index KMO
kmo = fa.calculate_kmo(x)
# print(kmo)
t_kmo = pd.DataFrame(
    data={
        "KMO":np.append(kmo[0],kmo[1])
    },index=variabile_observate+["Total"]
)
t_kmo.to_csv("data_out_fa/kmo.csv")
corelograma(t_kmo,"Index KMO",0,"Greens")
# show()

# Construire model factorial
model_fact = fa.FactorAnalyzer(m,rotation=None)
model_fact.fit(x)

# Analiza variantei
# Varianta factorilor comuni
varianta = model_fact.get_factor_variance()
# print(varianta)
t_varianta = tabelare_varianta_factori(varianta)
t_varianta.round(3).to_csv("data_out_fa/Varianta.csv")
# Varianta specifica (varianta factorilor specifici)
psi = model_fact.get_uniquenesses()
t_psi = pd.Series(
    np.append(psi,sum(psi)),
    variabile_observate+["Total"]
)
t_psi.name="Varianta"
t_psi.to_csv("data_out_fa/Varianta_specifica.csv")
# print(psi,sum(psi))
# Comunalitati
comm = model_fact.get_communalities()
t_comm = pd.Series(
    np.append(comm,sum(comm)),variabile_observate+["Total"]
)
t_comm.name="Comunalitate"
corelograma(pd.DataFrame(t_comm),"Comunalitati",0,"Blues")
corelograma(pd.DataFrame(t_psi),"Varianta specifica",0,"Reds")
k = plot_varianta(varianta[0],70,eticheta_x="Factor")
nr_min_factori = min( [v for v in k if v is not None] )

show()