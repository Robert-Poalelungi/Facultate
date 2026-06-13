import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from seaborn import kdeplot

x = pd.DataFrame() # DOES NOT need to be standardized
x_applied = pd.DataFrame() # DOES NOT need to be standardized

tinta = 'VULNERAB' # column specified in the requirements
variabile = list(x.columns.values[:-1]) # the other columns

x_train, x_test, y_train, y_test = train_test_split(x[variabile], x[tinta], train_size=0.4)
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train) # trains the model

scores = lda.transform(x_test)
prediction_test = lda.predict(x_test)
prediction_applied = lda.predict(x_applied)

# Calcul scoruri discriminante model liniar
scores = lda.transform(x_test)

#Trasare plot instanțe în axe discriminante

plt.figure(figsize=(8, 6))
plt.scatter(scores[:, 0], scores[:, 1], c=y_test)  # Culoarea punctelor este dată de etichetele y_test
plt.xlabel('LD1')  # Eticheta axei x (prima componentă discriminantă)
plt.ylabel('LD2')  # Eticheta axei y (a doua componentă discriminantă)
plt.title('Plot instanțe în axe discriminante')
plt.show()

#Trasare plot distribuții în axele discriminante
plt.figure(figsize=(8, 6))
kdeplot(scores[y_test == 0, 0], label='Clasa 0')  # Distribuția scorurilor pentru clasa 0 pe LD1
kdeplot(scores[y_test == 1, 0], label='Clasa 1')  # Distribuția scorurilor pentru clasa 1 pe LD1
plt.xlabel('LD1')
plt.ylabel('Densitate')
plt.title('Distribuția scorurilor pe prima axă discriminantă (LD1)')
plt.legend()
plt.show()

#Predicția în setul de testare model liniar
prediction_test = lda.predict(x_test)

#Evaluare model liniar pe setul de testare (matricea de confuzie + indicatori de acuratețe)


cm = confusion_matrix(y_test, prediction_test)
print('Matricea de confuzie:\n', cm)

accuracy = accuracy_score(y_test, prediction_test)
print('Acuratețe:', accuracy)

# Predicția în setul de aplicare model liniar
prediction_applied = lda.predict(x_applied)

#Predicția în setul de testare model bayesian


gnb = GaussianNB()
gnb.fit(x_train, y_train)

prediction_test_bayesian = gnb.predict(x_test)

# Evaluare model bayesian (matricea de confuzie + indicatori de acuratețe)
cm_bayesian = confusion_matrix(y_test, prediction_test_bayesian)
print('Matricea de confuzie (Bayesian):\n', cm_bayesian)

accuracy_bayesian = accuracy_score(y_test, prediction_test_bayesian)
print('Acuratețe (Bayesian):', accuracy_bayesian)

print(classification_report(y_test, prediction_test_bayesian))

#Predicția în setul de aplicare model bayesian
prediction_applied_bayesian = gnb.predict(x_applied)