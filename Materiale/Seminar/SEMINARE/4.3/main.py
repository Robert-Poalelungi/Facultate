import numpy as np
import pandas as pd
from functii import *

pd.set_option("display.max_columns", None)

prezenta_vot = pd.read_csv("prezenta_vot.csv", index_col=0)
# print(prezenta_vot)

valori_lipsa = prezenta_vot.isna().any().any()
if valori_lipsa:
    nan_replace(prezenta_vot)

indicatori_prezenta = ["Votanti_LP", "Votanti_LS", "LP", "LS", "LSC", "UM", "LT"]
categorii = ["Barbati_18-24", "Barbati_25-34", "Barbati_35-44", "Barbati_45-64",
             "Barbati_65_", "Femei_18-24", "Femei_25-34", "Femei_35-44", "Femei_45-64",
             "Femei_65_"]

# Cerinta 1
procent_participare = prezenta_vot["LT"] * 100 / (prezenta_vot["Votanti_LP"] + prezenta_vot["Votanti_LS"])
# print(procent_participare)
prezenta_vot["Procent_Participare"] = procent_participare
cerinta1 = prezenta_vot[["Localitate", "Judet", "Procent_Participare"]][procent_participare > 50]
cerinta1.to_csv("Prezenta50.csv")

# Cerinta 2
cerinta2 = (prezenta_vot[["Localitate", "Judet", "Procent_Participare"]].
            sort_values(by="Procent_Participare", ascending=False))
cerinta2.to_csv("PrezentaSort.csv")

k = np.flip(np.argsort(procent_participare.values))
cerinta2_ = prezenta_vot[["Localitate", "Judet", "Procent_Participare"]].iloc[k, :]
cerinta2_.to_csv("PrezentaSort_.csv")

# Cerinta 3
coduri_judete = pd.read_csv("Coduri_Judete.csv", index_col=0)
prezenta_vot_ = prezenta_vot.merge(right=coduri_judete, left_on="Judet", right_index=True)
# print(prezenta_vot_)
cerinta3 = prezenta_vot_[indicatori_prezenta + categorii + ["Regiune"]].groupby(by="Regiune").sum()
cerinta3.to_csv("Regiuni.csv")

# Cerinta 4
cerinta4 = prezenta_vot[["Localitate","Judet"]+categorii].apply(func=selectie,axis=1)
cerinta4.to_csv("Varsta.csv")

# Cerinta 5
categorie_varsta = "Femei_45-64"
cerinta5 = cerinta4[cerinta4["Categorie"] == categorie_varsta]
cerinta5.to_csv(categorie_varsta+".csv")

# Cerinta 6
cerinta6 = prezenta_vot[categorii+["Judet"]].groupby(by="Judet").apply(func=shannon)
# print(cerinta6)
cerinta6.to_csv("Shannon_disparitate.csv")
