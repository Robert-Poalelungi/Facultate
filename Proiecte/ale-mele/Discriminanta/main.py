import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, cohen_kappa_score

# Citirea datelor dintr-un fișier CSV
df = pd.read_csv("park.csv", index_col=0)

# Extrage variabilele predictor și variabila țintă
variabile_predictor = df.columns[:-1].to_numpy()
variabila_tinta = df.columns[-1:].to_numpy()
instante = df.index.to_numpy()

# Extrage matricea de caracteristici (X) și vectorul țintă (Y)
X = df[variabile_predictor].to_numpy()
Y = df[variabila_tinta].to_numpy()

# Inițializare și antrenare model LDA
model_lda = LinearDiscriminantAnalysis()
model_lda.fit(X, Y)

# Informații extrase din model LDA
clase = model_lda.classes_  # Etichetele claselor sau grupurilor formate de model
centrii_grupa = model_lda.means_  # Mediile fiecărei grupe

# Transformarea centrilor de grup în spațiul discriminant folosind modelul LDA
zg = model_lda.transform(centrii_grupa)

# Predictii pe baza datelor de antrenare
predict_Y = model_lda.predict(X)

# Calcul matrice de confuzie și index Cohen-Kappa
# Kappa = 1: Indică acord perfect între evaluatori.
# Kappa = 0: Arată că acordul este doar atât cât s-ar aștepta să fie întâmplător.
# Kappa < 0: Indică acord mai slab decât acordul întâmplător.

# Matrice:        Positive true       Negative false
# Predict true
# Predict false
#                 Positive false      Negative true
mat_conf = confusion_matrix(Y, predict_Y)
index_cohen_kappa = cohen_kappa_score(Y, predict_Y)

# Calculare număr de axe - minim dintre numărul de caracteristici și numărul de clase minus 1
nr_axe = min(len(variabile_predictor), len(clase)) - 1

# Predictii pe baza datelor complete (inclusiv datele de testare)
X_ = df[variabile_predictor].to_numpy()
predict_Y_test = model_lda.predict(X_)

# Calculare acuratețe globală și acuratețe pentru fiecare clasă/grupă
n = len(df)
acuratete_globala = np.round(sum(np.diagonal(mat_conf)) * 100 / n, 3)
acuratete_grupe = np.round(np.diagonal(mat_conf) * 100 / np.sum(mat_conf, axis=1))
acuratete_medie = np.mean(acuratete_grupe)

# Afișare rezultate
print("Acuratete globala: " + str(acuratete_globala))
print("Acuratete medie: " + str(acuratete_medie))
print("Index Cohen-Kappa: " + str(index_cohen_kappa))
