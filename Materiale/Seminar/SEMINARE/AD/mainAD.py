import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.dtypes.common import is_numeric_dtype
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, accuracy_score

set_antrenare_testare=pd.read_csv('park.csv',index_col=0)

#adaugare valori lipsa
def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if t[v].isna().any():
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

valori_lipsa = set_antrenare_testare.isna().any().any()
if valori_lipsa:
    nan_replace(set_antrenare_testare) #functie custom in functii.py

variabile = list(set_antrenare_testare)
predictori = variabile[:-1]
clasa = variabile[-1]

# Split datelor in set de antrenament și set de testare
x_train, x_test, y_train, y_test = train_test_split(
    set_antrenare_testare[predictori],
    set_antrenare_testare[clasa],
    test_size=0.4
)

# Antrenare model liniar
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train)

# Calcul scoruri discriminante model liniar
lda_scores_train = lda.decision_function(x_train)
lda_scores_test = lda.decision_function(x_test)

# Predicție în setul de testare model liniar
lda_predictions_test = lda.predict(x_test)

# Evaluare model liniar pe setul de testare
lda_conf_matrix_test = confusion_matrix(y_test, lda_predictions_test)
lda_accuracy_test = accuracy_score(y_test, lda_predictions_test)

print("Matrice de confuzie pentru modelul liniar (setul de testare):")
print(lda_conf_matrix_test)
print("Acuratețe pentru modelul liniar (setul de testare):", lda_accuracy_test)

# Aplicare
set_aplicare = pd.read_csv('park_apply.csv', index_col=0)
#adaugare valori lipsa
valori_lipsa_aplicare = set_aplicare.isna().any().any()
if valori_lipsa_aplicare:
    nan_replace(set_aplicare) #functie custom in functii.py

# Predicție în setul de aplicare model liniar
lda_predictions_apply = lda.predict(set_aplicare[predictori])
print(lda_predictions_apply)

# Predicția în setul de testare model bayesian
qda = QuadraticDiscriminantAnalysis()
qda.fit(x_train, y_train)
qda_predictions_test = qda.predict(x_test)

# Evaluare model bayesian pe setul de testare
qda_conf_matrix_test = confusion_matrix(y_test, qda_predictions_test)
qda_accuracy_test = accuracy_score(y_test, qda_predictions_test)

print("\nMatrice de confuzie pentru modelul bayesian (setul de testare):")
print(qda_conf_matrix_test)
print("Acuratețe pentru modelul bayesian (setul de testare):", qda_accuracy_test)

# Predicția în setul de aplicare model bayesian
qda_predictions_apply = qda.predict(set_aplicare[predictori])
print(qda_predictions_apply)