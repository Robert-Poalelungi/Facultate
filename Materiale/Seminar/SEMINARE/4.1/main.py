import pandas as pd
from functii import *

pd.set_option("display.max_columns", None)

etnicitate = pd.read_csv("Ethnicity.csv", index_col=0)
# print(etnicitate)
print("Valori lipsa:", etnicitate.isna().any().any())
etnii = list(etnicitate)[1:]

# Cerinta 1
coduri_localitati = pd.read_csv("Coduri_Localitati.csv", index_col=0)
etnicitate_ = etnicitate.merge(right=coduri_localitati, left_index=True, right_index=True)
# print(etnicitate_)
etnicitate_judet = etnicitate_[etnii + ["County"]].groupby(by="County").sum()
# print(etnicitate_judet)
etnicitate_judet.to_csv("Etnicitate_judete.csv")

coduri_judete = pd.read_csv("Coduri_Judete.csv", index_col=0)
etnicitate_judet_ = etnicitate_judet.merge(coduri_judete, left_index=True, right_index=True)
etnicitate_regiune = etnicitate_judet_[etnii + ["Regiune"]].groupby(by="Regiune").sum()
etnicitate_regiune.to_csv("Etnicitate_regiuni.csv")

coduri_regiuni = pd.read_csv("Coduri_Regiuni.csv", index_col=0)
etnicitate_regiune_ = etnicitate_regiune.merge(coduri_regiuni, left_index=True, right_index=True)
etnicitate_macroregiune = etnicitate_regiune_.groupby(by="MacroRegiune").sum()
etnicitate_macroregiune.to_csv("Etnicitate_macroregiuni.csv")

# Cerinta 2
etnicitate_p = etnicitate[etnii].apply(func=procente, axis=1)
etnicitate_p.to_csv("Etnicitate_p.csv")
etnicitate_judet_p = etnicitate_judet[etnii].apply(func=procente, axis=1)
etnicitate_judet_p.to_csv("Etnicitate_judete_p.csv")
etnicitate_regiune_p = etnicitate_regiune[etnii].apply(func=procente, axis=1)
etnicitate_regiune_p.to_csv("Etnicitate_regiuni_p.csv")
etnicitate_macroregiune_p = etnicitate_macroregiune[etnii].apply(func=procente, axis=1)
etnicitate_macroregiune_p.to_csv("Etnicitate_macroregiuni_p.csv")

# Cerinta 3
disim = etnicitate_[etnii + ["County"]].groupby(by="County").apply(func=disimilaritate, coloane=etnii)
print(disim)
