import pandas as pd
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from seaborn import kdeplot

ind_df = pd.read_csv('./dataIN/Industrie.csv')
pop_df = pd.read_csv('./dataIN/PopulatieLocalitati.csv')
ind_list = list(ind_df.columns[2:].values)

# Cerinta1
t = ind_df.merge(pop_df[["Siruta", "Populatie"]], on="Siruta")
for i in ind_list:
    t[i] = t[i] / t["Populatie"]

cerinta1 = t[["Siruta", "Localitate"] + ind_list]
cerinta1.to_csv('./dataOUT/Cerinta1.csv', index=False)

# Cerinta2
t2 = ind_df.merge(pop_df[["Siruta", "Judet"]], on="Siruta")

rez = (
    t2.groupby("Judet")[ind_list]
    .agg("max")
    .reset_index()
)

rez["Activiate"] = rez[ind_list].idxmax(axis=1)
rez["Cifra de Afaceri"] = rez[ind_list].max(axis=1)

cerinta2 = rez[["Judet", "Activiate", "Cifra de Afaceri"]]
cerinta2.to_csv("./dataOUT/Cerinta2.csv", index=False)

# Cerinta 3
x = pd.read_csv('./dataIN/ProiectB.csv')
x_applied = pd.DataFrame()

tinta = 'VULNERAB' # column specified in the requirements
variabile = list(x.columns.values[1:]) # the other columns

dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
x[tinta] = x[tinta].map(dict)

x_train, x_test, y_train, y_test = train_test_split(x[variabile], x[tinta], train_size=0.4)
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train) # trains the model

scores = lda.transform(x_train)

pd.DataFrame(data=scores) \
.to_csv('./dataOUT/z.csv')

