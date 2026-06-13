import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

rata_df = pd.read_csv("./dataIN/Rata.csv")
cod_df = pd.read_csv("./dataIN/CoduriTariExtins.csv")
cod_df = cod_df.rename(columns={"Country_Letter_code": "Three_Letter_Country_Code"})

# Cerinta 1
media_globala = rata_df["RS"].mean()
cerinta1 = rata_df[rata_df["RS"] < media_globala][["Three_Letter_Country_Code", "Country_Name", "RS"]]
cerinta1 = cerinta1.sort_values(by = "RS", ascending=False)
cerinta1 = cerinta1.to_csv("./dataOUT/Cerinta1.csv", index=False)

# Cerinta 2
indicatori_lista = list(rata_df.columns[2:])
t = rata_df.merge(cod_df[["Three_Letter_Country_Code", "Continent"]], on="Three_Letter_Country_Code")\
    .set_index("Three_Letter_Country_Code")\
    .groupby("Continent")[indicatori_lista]\
    .idxmax()\
    .reset_index()\
    .to_csv("./dataOUT/Cerinta2.csv", index=False)

# Cerinta 3

x = StandardScaler().fit_transform(rata_df[indicatori_lista])
pca = PCA()
pca.fit_transform(x)

alpha=pca.explained_variance_ #varianta componentelor
pve=pca.explained_variance_ratio_ #varianta explicata
alpha_cum=np.cumsum(alpha)#varianta cumulata
pve_cum=np.cumsum(pve)#procent din variant cumulata

print(alpha)
print(pve)
print(alpha_cum)
print(pve_cum)

pd.DataFrame(data={'Varianta componentelor': alpha,
                    'Varianta cumulata': alpha_cum,
                    'Procentul de varianta explicata': pve,
                    'Procentul cumulat': pve_cum}) \
.to_csv('./dataOUT/Varianta.csv')

