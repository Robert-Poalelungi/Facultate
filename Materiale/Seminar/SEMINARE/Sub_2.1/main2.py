import numpy as np
import pandas as pd
from functii import *

np.set_printoptions(threshold=np.inf)
tabel=pd.read_csv('Vot.csv',index_col=0)
variabile=list(tabel)
variabile_numerice=variabile[2:]
date_numerice=tabel[variabile_numerice].values
categorii=["Barbati_25-34","Barbati_35-44","Barbati_45-64","Barbati_65_","Femei_18-24","Femei_35-44","Femei_45-64","Femei_65_"]
print(tabel,type(tabel))

#Cerinta1
# Calculul procentelor participării la vot pentru fiecare categorie de alegători
procente_participare = (tabel[categorii].div(tabel["Votanti_LP"], axis=0)) * 100

# Adăugarea rezultatelor la dataframe
tabel = pd.concat([tabel, procente_participare.add_prefix("Procent_")], axis=1)

# Salvarea rezultatelor în fișierul cerinta1.csv
tabel.to_csv("cerinta1.csv", columns=["Localitate"] + categorii + procente_participare.columns.tolist())

