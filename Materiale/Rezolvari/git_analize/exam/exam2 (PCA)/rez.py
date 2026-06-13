import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

country_df = pd.read_csv("./dataIN/CountryContinents.csv")
ind_df = pd.read_csv("./dataIN/GlobalIndicatorsPerCapita_2021.csv")

ind_list = list(ind_df.columns[9:].values)

# Cerinta 1
ind_df = ind_df.rename(columns={"index": "CountryId"})

cerinta1 = ind_df[["CountryId", "Country"] + ind_list].copy()
cerinta1["Valoare Adaugata"] = cerinta1[ind_list].sum(axis=1)
cerinta1 = cerinta1[["CountryId", "Country", "Valoare Adaugata"]]

cerinta1.to_csv("./dataOUT/cerinta1.csv", index=False)

# Cerinta 2
ind_list_2 = list(ind_df.columns[2:].values)
t = ind_df.merge(country_df[["CountryId", "Continent"]], on="CountryId")\
    .groupby("Continent")[ind_list_2]\
    .mean()\
    .reset_index()\
    .to_csv("./dataOUT/cerinta2.csv", index=False)

# Cerinta 3

x = StandardScaler().fit_transform(ind_df[ind_list])
pca = PCA()
pca.fit_transform(x)
alpha=pca.explained_variance_ #varianta componentelor
pve=pca.explained_variance_ratio_ #varianta explicata


print("Alpha:", alpha)
print("Pve:", pve)
