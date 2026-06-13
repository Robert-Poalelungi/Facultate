import pandas as pd
import numpy as np
from sklearn.cross_decomposition import CCA
from sklearn.preprocessing import StandardScaler

emm_df = pd.read_csv("./dataIN/emmissions.csv")
pop_df = pd.read_csv("./dataIN/PopulatieEuropa.csv")

emm_list = list(emm_df.columns[2:])
# Cerinta 1
emm_df["Emisii_Total_Tone"] = emm_df[emm_list].sum(axis=1)
emm_df[["ThreeLetterCountryCode", "Country", "Emisii_Total_Tone"]]\
    .to_csv("./dataOUT/cerinta1.csv", index=False)

# Cerinta 2

t = emm_df.merge(pop_df[["Country", "Region"]], on="Country")\
    .groupby("Region")[emm_list]\
    .mean()\
    .reset_index()

for i in emm_list:
    t[i] = t[i] / 10000

t.to_csv("./dataOUT/cerinta2.csv", index=False)

# Cerinta 3
labels1 = emm_list[:4]
labels2 = emm_list[4:]
x = StandardScaler().fit_transform(emm_df[labels1])
y = StandardScaler().fit_transform(emm_df[labels2])

p = x.shape[1]
q = y.shape[1]
m = min(p, q)
cca = CCA(n_components=m)
z, u = cca.fit_transform(x, y)
# rxz = np.corrcoef(x, z[:, :m], rowvar=False)[:p, p:]
# ryu = np.corrcoef(y, u[:, :m], rowvar=False)[:q, q:]

pd.DataFrame(data=z).to_csv('./dataOUT/z.csv', index=False)
pd.DataFrame(data=u).to_csv('./dataOUT/u.csv', index=False)

# Cerinta 4
r = []
for i in range(m):
    r.append(np.corrcoef(z[:, i], u[:, i], rowvar=False)[0, 1])
pd.DataFrame(r).to_csv('./dataOUT/r.csv')
