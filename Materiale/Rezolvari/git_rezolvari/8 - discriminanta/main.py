import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import LinearNDInterpolator
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

industrie = pd.read_csv('./res/Industrie.csv', index_col= 0)
populatie = pd.read_csv('./res/PopulatieLocalitati.csv', index_col= 0)

print(industrie)
print(populatie)

merged = industrie.merge(populatie[['Judet', 'Populatie']], left_index=True, right_index=True)

print(merged)


lista_industrii = list(industrie)[1:]

print(lista_industrii)

# A

# 1. cifra de afaceri pe locuitor pentru fiecare activitate, la nivel de localitate

for i in lista_industrii:
    merged[i] = merged[i] / merged['Populatie']

cerinta1 = merged[['Localitate'] + lista_industrii]

cerinta1.to_csv('./output/Cerinta1.csv', index=True)

# 2. activitatea dominanta la nivel de judet
# judet, activitate, ca

altu =  merged.groupby('Judet')[lista_industrii].sum()
altu['CA'] = altu.max(axis=1)
altu['Dominanta'] = altu.idxmax(axis =1)

cerinta2 = altu[['Dominanta', 'CA']]

cerinta2.to_csv('./output/Cerinta2.csv', index=True)


# B - ANALIZA DISCRIMINANTA

# preprocesare
date = pd.read_csv('./res/ProiectB.csv')
x = date.drop(columns='VULNERAB')
y = date['VULNERAB']

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

# 1. aplicare analiza liniara discriminanta si calcul scoruri discriminante
analiza = LinearDiscriminantAnalysis()
analiza.fit(x_train, y_train)

scoruri = analiza.transform(x_test)

scoruri_df = pd.DataFrame(scoruri)

scoruri_df.to_csv('./output/z.csv')

# 3. predictii pe seturile de antrenare si testare

x_aplicare = pd.read_csv('./res/ProiectB_apply.csv')

predictie_test = analiza.predict(x_test)
predictie_aplicare = analiza.predict(x_aplicare)

predictie_test_df = pd.DataFrame(predictie_test)
predictie_aplicare_df = pd.DataFrame(predictie_aplicare)


predictie_test_df.to_csv('./output/predict_test.csv')
predictie_aplicare_df.to_csv('./output/predict_apply.csv')










