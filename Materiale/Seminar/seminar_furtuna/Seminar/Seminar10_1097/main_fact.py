import sys

import numpy as np
import pandas as pd

from functii import nan_replace_df, salvare_ndarray, tabelare_varianta_fact
import factor_analyzer as fa
from geopandas import GeoDataFrame

from grafice import corelograma, show, plot_varianta, plot_scoruri_corelatii, plot_harta

pd.set_option("display.max_columns",None)
np.set_printoptions(3,threshold=sys.maxsize,suppress=True)

t = pd.read_csv("data_in/MortalitateRO2019/mortalitate_ro.csv",index_col=1)
nan_replace_df(t)

variabile_observate = list(t)[1:]

x = t[variabile_observate].values
n,m = x.shape

# Aplicare test Bartlett
test_bartlett = fa.calculate_bartlett_sphericity(x)
print("Test Bartlett\n","PValue:",test_bartlett[1])
if test_bartlett[1]>0.01:
    print("Lipsa factorabilitate!")
    exit(0)
# Calcul index KMO
kmo = fa.calculate_kmo(x)
# print(kmo)

t_kmo = pd.DataFrame(
    data={
        "KMO":np.append(kmo[0],kmo[1])
    },index=variabile_observate+["Global"]
)
t_kmo.to_csv("data_out_fa/kmo.csv")
corelograma(t_kmo,0,"Reds",titlu="Index KMO")

# Calcul matrice de corelatii
r = np.corrcoef(x,rowvar=False)
t_r = salvare_ndarray(
    r,variabile_observate,variabile_observate,"data_out_fa/R.csv"
)
corelograma(t_r,annot=m<15)

# Construire model
# metoda_rotatie = None
metoda_rotatie = "varimax"
model_fact = fa.FactorAnalyzer(n_factors=m,rotation=metoda_rotatie)
model_fact.fit(x)

# Analiza varianta
# Varianta factori comuni
varianta = model_fact.get_factor_variance()
alpha = varianta[0]
# print(varianta)
t_varianta = tabelare_varianta_fact(varianta)
t_varianta.to_csv("data_out_fa/Varianta.csv")
k = plot_varianta(alpha,"Plot varianta factori","Factor",70)
nr_factori = min( [v for v in k if v is not None] )
print("Numar factori comuni semnificativi:",nr_factori)
# Varianta factori specifici
psi = model_fact.get_uniquenesses()
t_psi = pd.Series(psi,variabile_observate,name="Varianta specifica")
t_psi.to_csv("data_out_fa/psi.csv")
corelograma(
    pd.DataFrame(t_psi),0,"Reds",titlu="Varianta specifica"
)
# Comunalitati
comm = model_fact.get_communalities()
t_comm = pd.Series(comm,variabile_observate,name="Comunalitati")
t_comm.to_csv("data_out_fa/comm.csv")
corelograma(
    pd.DataFrame(t_comm),0,"Blues",titlu="Comunalitati"
)


# Calcul corelatii factoriale
# Se utilizeaza primii nr_factori
r_xf = model_fact.loadings_[:,:nr_factori]
# print(r_xf)
etichete_factori = list(t_varianta.index)
t_r_xf = salvare_ndarray(
    r_xf,
    variabile_observate,
    etichete_factori[:nr_factori],
    "data_out_fa/r_xf.csv"
)
corelograma(
    t_r_xf,titlu="Corelatii factoriale"
)
# Trasare cerc corelatii
for i in range(2,nr_factori+1):
    plot_scoruri_corelatii(t_r_xf,
                           "Corelatii factoriale - AFact",
                           "F1",
                           "F"+str(i),
                           variabile_observate,
                           True)

# Analiza scoruri
f = model_fact.transform(x)
t_f = salvare_ndarray(
    f,
    t.index,
    etichete_factori,
    "data_out_fa/f.csv"
)
for i in range(2,nr_factori+1):
    plot_scoruri_corelatii(t_f,
                           "Plot scoruri - AFact",
                           "F1",
                           "F"+str(i),
                           t_f.index
                           )

# Trasare harti
gdf = GeoDataFrame.from_file("data_in/RO_NUTS2/Ro.shp")
# print(gdf)
camp_legatura = "snuts"
for factor in etichete_factori[:nr_factori]:
    plot_harta(gdf,camp_legatura,t_f,factor)

show()
