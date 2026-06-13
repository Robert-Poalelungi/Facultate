import sys

import numpy as np
import pandas as pd

from functii import nan_replace_df, acp, tabelare_varianta, salvare_ndarray
from grafice import plot_varianta, show, corelograma, scatterplot

np.set_printoptions(3,sys.maxsize,suppress=True)
pd.set_option("display.max_columns",None)

set_date = pd.read_csv("data_in/Teritorial2022/Teritorial_2022.csv",index_col=0)
nan_replace_df(set_date)

variabile_observate = list(set_date)[3:]
x = set_date[variabile_observate].values

# print(x)
x_,r_v,alpha,a = acp(x)
t_r = salvare_ndarray(r_v,
                      variabile_observate,
                      variabile_observate,
                      "Indicatori",
                      "data_out/R.csv"
                      )
corelograma(t_r,annot=len(variabile_observate)<10)

# Analiza variantei componentelor
t_varianta = tabelare_varianta(alpha)
t_varianta.round(3).to_csv("data_out/Varianta.csv")
k1,k2,k3 = plot_varianta(alpha)

# Analiza corelatiilor dintre variabilele observare si componente
c = x_@a
s = c/np.sqrt(alpha)
etichete_componente = list(t_varianta.index)
t_c = salvare_ndarray(c,
                      set_date.index,
                      etichete_componente,
                      set_date.index.name,
                      "data_out/C.csv"
                      )

t_s = salvare_ndarray(s,
                      set_date.index,
                      etichete_componente,
                      set_date.index.name,
                      "data_out/S.csv"
                      )
n,m = x.shape
r_XC = np.corrcoef(x_,c,rowvar=False)[:m,m:]
t_r_XC = salvare_ndarray(
    r_XC,variabile_observate,etichete_componente,
    "Indicatori","data_out/R_XC.csv"
)
corelograma(t_r_XC,"Corelatii variabile-componente",annot=m<10)

# Analiza scorurilor
scatterplot(t_c,titlu="Plot componente")
scatterplot(t_s)
show()
