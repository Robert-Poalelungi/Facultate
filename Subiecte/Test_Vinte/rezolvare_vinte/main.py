import numpy as np
import pandas as pd

# inlocuire nan
def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)


# citire fisiere
industrie = pd.read_csv('./dataIN/Industrie.csv', index_col= 0)
print(industrie)

populatie = pd.read_csv('./dataIN/PopulatieLocalitati.csv', index_col= 0)
print(populatie)

# inlocuire valori nan
nan_replace(industrie)
nan_replace(populatie)

# merge tabele
merge = industrie.merge(populatie[['Judet', 'Populatie']], left_index= True, right_index= True)
print(merge)

# creare lista de industrii
lista = list(industrie)[1:]
print(lista)

# 1. Să se salveze în fișierul Cerinta_1.csv cifra de afaceri pe locuitor pentru fiecare activitate, la nivel de localitate.
# Pentru fiecare localitate se va salva codul Siruta, numele localității și cifra de afaceri pe locuitor pentru fiecare
# activitate.



industrie_1 = industrie.groupby("Judet").agg({"Total": "sum", "Populatie": "sum"})

# Împărțim cifra de afaceri totală a județului la populația totală a județului
industrie_1["CifraAfaceriPeLocuitor"] = industrie_1["Total"] / industrie_1["Populatie"]

cerinta3 = industrie_1[["CifraAfaceriPeLocuitor"]].reset_index()

cerinta3.to_csv("Cerinta3.csv", index=False)












