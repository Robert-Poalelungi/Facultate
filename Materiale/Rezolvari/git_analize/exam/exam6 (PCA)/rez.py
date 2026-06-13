import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

mrt_df = pd.read_csv("./dataIN/Mortalitate.csv")
cod_df = pd.read_csv("./dataIN/CoduriTariExtins.csv")
cod_df = cod_df.rename(columns={'Tari' : 'Tara'})

# Cerinta 1
rata_spor_natural = list(mrt_df.columns[1:2].values)
cerinta1 = mrt_df[mrt_df[rata_spor_natural].min(axis=1) < 0]
cerinta1 = cerinta1[["Tara"] + rata_spor_natural]
cerinta1.to_csv("./dataOUT/cerinta1.csv", index=False)

# Cerinta 2
ind_list = list(mrt_df.columns[1:].values)
t = mrt_df.merge(cod_df[["Tara", "Continent"]], on="Tara")\
    .groupby("Continent")[ind_list]\
    .mean()\
    .reset_index()\
    .to_csv('./dataOUT/cerinta2.csv', index=False)

# Cerinta 3
x = StandardScaler().fit_transform(mrt_df[ind_list])
pca = PCA()
pca.fit_transform(x)

alpha=pca.explained_variance_ #varianta componentelor
pve=pca.explained_variance_ratio_ #varianta explicata

print(alpha)
print(pve)