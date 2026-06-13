import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

air_df = pd.read_csv('./dataIN/AirQuality.csv')
country_df = pd.read_csv('./dataIN/CountryContinents.csv')

ind_list = list(air_df.columns[2:])

# Cerinta 1
air_df[["Country"] + ind_list]\
    .set_index('Country')\
    .idxmax(axis=0)\
    .to_csv('./dataOUT/cerinta1.csv')

# Cerinta 2
t = air_df.merge(country_df[["CountryId", "Continent"]], on='CountryId')\
    .set_index('Country')\
    .groupby("Continent")[ind_list]\
    .idxmax()\
    .to_csv('./dataOUT/cerinta2.csv')


# Cerinta 3
x=StandardScaler().fit_transform(air_df[ind_list])
HC=linkage(x,method='ward')
print(HC)