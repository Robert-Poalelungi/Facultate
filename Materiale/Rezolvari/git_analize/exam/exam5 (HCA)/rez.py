import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.preprocessing import StandardScaler

alch_df = pd.read_csv('./dataIN/alcohol.csv')
cod_df = pd.read_csv('./dataIN/CoduriTariExtins.csv')

#Cerinta 1

ani_list = list(alch_df.columns[2:].values)

alch_df["Consum Mediu"] = alch_df[ani_list].mean(axis=1)

cerinta1 = alch_df[["Code", "Country", "Consum Mediu"]]
cerinta1.to_csv('./dataOUT/Cerinta1.csv', index=False)

# Cerinta 2
t = alch_df.merge(cod_df[["Country", "Continent"]], on="Country")\
    .groupby("Continent")[ani_list]\
    .mean()\
    .idxmax(axis=1)\
    .reset_index()\
    .rename(columns={'Continent' : 'Continent_Name'})\
    .rename(columns={0 : 'Anul'})\
    .to_csv('./dataOUT/Cerinta2.csv', index=False)

# Cerinta 3
x=StandardScaler().fit_transform(alch_df[ani_list])
HC=linkage(x,method='ward')
print(HC)