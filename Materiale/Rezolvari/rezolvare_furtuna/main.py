# importuri
import numpy as np
import pandas as pd

# citire din fisier
diversitate = pd.read_csv('./res/Diversitate.csv', index_col= 0)
print(diversitate)

localitati = pd.read_csv('./res/Coduri_Localitati.csv', index_col= 0)
print(localitati)

# merge fisiere
merge = diversitate.merge(localitati['Judet'], left_index= True, right_index= True)
print(merge)

# 1. Să se calculeze și să se salveze în fișierul Cerinta1.csv, localitățile în care cel puțin pentru un an diversitatea a fost 0. Se va salva codul Siruta, denumirea localității și indicii de diversitate pentru toți anii.



# 2. Să se determine pentru fiecare județ localitatea în care diversitatea medie (media anilor) este maximă. Rezultatul va fi salvat în fișierul Cerinta2.csv. Se va salva indicativul de județ, localitatea cu diversitatea medie maximă și valoarea diversității medii.



























