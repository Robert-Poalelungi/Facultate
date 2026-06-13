import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.preprocessing import StandardScaler

alch_df = pd.read_csv("./dataIN/alcohol.csv")
cod_df = pd.read_csv("./dataIN/CoduriTariExtins.csv")

ani_list = list(alch_df.columns[2:])

# Cerinta 1
alch_df["Media"] = alch_df[ani_list].mean(axis=1)
alch_df[["Code", "Media"]]\
    .to_csv("./dataOUT/cerinta1.csv", index=False)

# Cerinta 2
t = alch_df.merge(cod_df[["Tari", "Continent"]], on="Tari") \
    .groupby("Continent")[ani_list]\
    .mean()\
    .idxmax(axis=1)\
    .reset_index() \
    .rename(columns={0: "Anul"}) \
    .to_csv("./dataOUT/cerinta2.csv",index=False)


# Cerinta 3
x=StandardScaler().fit_transform(alch_df[ani_list])
HC=linkage(x,method='ward')
print(HC)

