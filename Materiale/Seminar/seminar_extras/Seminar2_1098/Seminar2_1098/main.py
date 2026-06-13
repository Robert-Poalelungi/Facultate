import pandas as pd

pd.set_option("display.max_columns",None)

from functii import nan_replace_df, f_categorie, f_disparitate

prezenta_vot = pd.read_csv("data_in/prezenta_vot.csv",index_col=0)

nan_replace_df(prezenta_vot)
variabile = list(prezenta_vot)

variabile_vot = variabile[3:]
categorii_varsta = variabile_vot[variabile_vot.index("Barbati_18-24"):]

# Cerinta 1
# LT*100/(Votanti_LP+ Votanti_LS)
procent_participare = prezenta_vot["LT"]*100/(prezenta_vot["Votanti_LP"]+prezenta_vot["Votanti_LS"])
procent_participare.name = "Procent_Participare"
# print(procent_participare)
cerinta1 = pd.DataFrame(procent_participare)
cerinta1.insert(0,"Localitate",prezenta_vot["Localitate"])
cerinta1[procent_participare>50].to_csv("data_out/Prezenta50.csv")

prezenta_sort = cerinta1.sort_values(by="Procent_Participare",ascending=False)
prezenta_sort.to_csv("data_out/Prezenta_sort.csv")

# Cerinta 3

coduri_judete = pd.read_csv("data_in/Coduri_Judete.csv",index_col=0)
prezenta_vot_ = prezenta_vot.merge(coduri_judete,left_on="Judet",right_index=True)
# print(prezenta_vot_)

prezenta_vot_regiuni = prezenta_vot_[variabile_vot+["Regiune"]].groupby(by="Regiune").sum()
prezenta_vot_regiuni.to_csv("data_out/Regiuni.csv")

# Cerinta 4
categorie_dominanta = prezenta_vot[categorii_varsta].apply(func=f_categorie,axis=1)
# print(categorie_dominanta)
assert isinstance(categorie_dominanta,pd.DataFrame)
categorie_dominanta.insert(0,"Localitate",prezenta_vot["Localitate"])
categorie_dominanta.to_csv("data_out/Varsta.csv")

# Cerinta 5
# categorie_ = "Barbati_45-64"
categorie_ = "Barbati_35-44"
cerinta5 = categorie_dominanta[categorie_dominanta["Categorie_Max"]==categorie_]
cerinta5.to_csv("data_out/"+categorie_+".csv")

# Cerinta 6
cerinta6 = prezenta_vot[categorii_varsta+["Judet"]].\
    groupby(by="Judet").apply(func=f_disparitate,include_groups=False)
cerinta6.to_csv("data_out/disparitate_vot.csv")
