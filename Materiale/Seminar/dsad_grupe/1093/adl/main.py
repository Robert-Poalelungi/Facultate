# Analiza discriminantă este o metodă de clasificare supervizată.
# Scopul său este de a separa clasele prin identificarea unor combinații liniare ale variabilelor explicative care
# maximizează separarea dintre clase.

# Analiza Discriminantă Liniară (LDA) presupune că variabilele predictive au distribuție normală, că matricile de
# covarianță sunt egale pentru toate clasele și determină axe care maximizează raportul dintre variația între clase
# și variația în interiorul claselor.

# Analiza Discriminantă Bayesiană (BDA) utilizează teorema lui Bayes împreună cu distribuții specifice fiecărei clase
# (în cazul GaussianNB se presupune distribuție normală).

# Concepte cheie:
#   Axa discriminantă: combinație liniară a variabilelor predictive care maximizează separarea dintre clase
#   Variația între clase vs. variația în interiorul claselor: obiectivul este maximizarea separării dintre clase și
#       minimizarea dispersiei în interiorul fiecărei clase
#   Numărul de axe discriminante: min(numarul de variabile predictive, numarul de clase−1)

# Ipoteze:
#   Distribuție normală multivariată a variabilelor predictive (pentru LDA)
#   Matrici de covarianță egale pentru toate clasele (pentru LDA)
#   Observațiile sunt independente (pentru BDA)

# Unde este utilizată analiza discriminantă în practică?
#   Diagnostic medical: clasificarea pacienților pe baza simptomelor sau a rezultatelor analizelor
#   Finanțe: estimarea riscului de neplată a creditelor (credit bun vs. credit rău)
#   Marketing: segmentarea clienților în funcție de comportamentul de cumpărare
#   Recunoașterea imaginilor: reducerea dimensionalității înainte de clasificare
#   Ecologie / Biologie: clasificarea speciilor pe baza măsurătorilor morfologice sau biologice

# Când alegem fiecare metodă?
#   Multe variabile, independente sau aproape independente → GaussianNB (rapid, simplu)
#   Variabile corelate, clase aproximativ normale cu matrici de covarianță similare → LDA (mai precis, oferă axe discriminante)
#   Dorim reducerea dimensionalității pentru vizualizare → LDA (furnizează axe discriminante liniare)

# Comparație între metode
# Caracteristică	                Analiza Discriminantă Bayesiană (GaussianNB)	                Analiza Discriminantă Liniară (LDA)
# Ipoteze privind variabilele	    Toate variabilele sunt independente                     	    Variabilele pot fi corelate; se presupune aceeași matrice de covarianță pentru toate clasele
# Complexitate algoritmică	        Simplu, foarte rapid	                                        Mai costisitor, dar tot rapid
# Output	                        Probabilități pentru fiecare clasă	                            Probabilități pentru fiecare clasă, plus axe discriminante liniare pentru reducerea dimensionalității

import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, cohen_kappa_score
import matplotlib.pyplot as plt
import seaborn as sb

# citire date
date_antrenament = pd.read_csv("park.csv")
date_test = pd.read_csv("park_test.csv")

variabila_tinta = date_antrenament.columns[-1]
variabile_predictor = date_antrenament.columns[:-1]

x_train = date_antrenament[variabile_predictor].values
y_train = date_antrenament[variabila_tinta].values

x_test = date_test[variabile_predictor].values
instante = date_antrenament.index

# matricea de confuzie = este un tabel care sumarizeaza cat de bine un model de clasificare a prezis fiecare clasa

# daca am avea un set de date care poate fi impartit in 3 clase, o posibila matrice de confuzie ar arata asa:

# True \ PRED     A       B       C
# A               50      2       3
# B               5       45      5
# C               2       4       54

# intr-o astfel de matrice valorile de pe diagonala principala ne arata cat de precis a fost modelul nostru in
# determinarea corecta a claselor

# elementele de pe diagonala principala: [50, 45, 54] - sunt predictii corecte
# celelalte elemente sunt predictii incorecte sau clasificari eronate


# functie de calculare a acuratetei
def calculeaza_acuratete(y_true, y_pred, clase):
    # calculam acuratetea globala, per clasa (la nivel de grup/categorie) si acuratetea medie
    matrice_confuzie = confusion_matrix(y_true, y_pred, labels=clase)

    # global
    acc_global = np.round(np.diagonal(matrice_confuzie).sum() * 100 / matrice_confuzie.sum(), 3)

    # grup
    acc_grup = np.round(np.diagonal(matrice_confuzie) * 100 / np.sum(matrice_confuzie, axis=1), 3)

    # medie
    acc_mediu = np.mean(acc_grup)

    return matrice_confuzie, acc_global, acc_grup, acc_mediu


# Analiza Discriminanta Bayesiana (GaussianNB)
bda_model = GaussianNB()
bda_model.fit(x_train, y_train)
clase_bda = bda_model.classes_

# predictii
y_train_pred_bda = bda_model.predict(x_train)
y_test_pred_bda = bda_model.predict(x_test)

# calcul acuratete
mat_conf_bda, global_acc_bda, group_acc_bda, avg_acc_bda = calculeaza_acuratete(y_train, y_train_pred_bda, clase_bda)

# afisare rezulate
print("---BDA---")
print("Global Acc: ", global_acc_bda)
print("Group Acc: ", group_acc_bda)
print("Avg Acc: ", avg_acc_bda)
print("Cohen's kappa: ", cohen_kappa_score(y_train, y_train_pred_bda))

# Cohen's kappa (K) = este o metrica prin care se masoara concordata dintre valorile prezise si cele reale,
# ajustate cu "ghicitul la intamplare" sau sansa

# aceasta metrica are valori in intervalul -1:1, unde 1 = concordata perfecta, 0 = ca si cum as ghici la intamplare, -1 = mai rau decat daca as ghici
# K = (P0 - Pe) / (1 - Pe), unde P0 = proportia observatiilor clasificate corect, iar Pe = probabilitatea de a ghici corect la intamplare

# salvare matrice de confuzie
tabel_mat_conf_bda = pd.DataFrame(mat_conf_bda, index=clase_bda, columns=clase_bda)
tabel_mat_conf_bda["Acuratete BDA"] = group_acc_bda
tabel_mat_conf_bda.to_csv("MatConfBDA.csv")

# salvare predictii
pd.DataFrame({variabila_tinta: y_train, "Predictie BDA": y_train_pred_bda}, index=instante).to_csv("ClasificareAntrenamentBDA.csv")
pd.DataFrame({"Predictie BDA": y_test_pred_bda}, index=date_test.index).to_csv("ClasificareTestBDA.csv")

# Analiza Discriminanta Liniara (LDA)
lda_model = LinearDiscriminantAnalysis()
lda_model.fit(x_train, y_train)
clase_lda = lda_model.classes_

# predictii
y_train_pred_lda = lda_model.predict(x_train)
y_test_pred_lda = lda_model.predict(x_test)

# calcul acuratete
mat_conf_lda, global_acc_lda, group_acc_lda, avg_acc_lda = calculeaza_acuratete(y_train, y_train_pred_lda, clase_lda)

# afisare rezulate
print("---LDA---")
print("Global Acc: ", global_acc_lda)
print("Group Acc: ", group_acc_lda)
print("Avg Acc: ", avg_acc_lda)
print("Cohen's kappa: ", cohen_kappa_score(y_train, y_train_pred_lda))

# salvare matrice de confuzie
tabel_mat_conf_lda = pd.DataFrame(mat_conf_lda, index=clase_lda, columns=clase_lda)
tabel_mat_conf_lda["Acuratete LDA"] = group_acc_lda
tabel_mat_conf_lda.to_csv("MatConfLDA.csv")

# salvare predictii
pd.DataFrame({variabila_tinta: y_train, "Predictie LDA": y_train_pred_lda}, index=instante).to_csv("ClasificareAntrenamentLDA.csv")
pd.DataFrame({"Predictie LDA": y_test_pred_lda}, index=date_test.index).to_csv("ClasificareTestLDA.csv")

# reducerea dimensionalitatii
# z_train = proiectiile datelor de antrenament in spatiul axelor discriminante
z_train = lda_model.transform(x_train)

# means_lda = valori care raspund intrebarii: Care este o observatie medie (tipica/reprezentativa) specifica fiecarei
# clase in variabilele initiale?
means_lda = lda_model.means_

# z_means = valorile centrale ale claselor in spatiul axelor discriminante
z_means = lda_model.transform(means_lda)

# numarul de dimensiuni LDA valide - formula de mai jos este o constrangere teoretica a algoritmului
n_axe = min(len(variabile_predictor), len(clase_lda) - 1)

if n_axe > 1:
    plt.figure(figsize = (9, 9))
    sb.scatterplot(x=z_train[:, 0], y=z_train[:, 1], hue=y_train, hue_order=clase_lda)
    sb.scatterplot(x=z_means[:, 0], y=z_means[:, 1], hue=clase_lda, marker='s', s=255, legend=False)
    plt.xlabel('LD1')
    plt.ylabel('LD2')
    plt.title("LDA: instante si mediile claselor")
    plt.show()
else:
    print("Numar insuficient de axe pentru a reprezenta grafic instantele (minim 2 sunt necesare)")

for i in range(n_axe):
    plt.figure(figsize=(9,9))
    for cls in clase_lda:
        # KDE = Kernel Density Eestimate - acest grafic creeaza o reprezentare continua care arata distributia de
        #       probabiliate a setului de date
        sb.kdeplot(z_train[y_train == cls, i], fill=True, label=cls)
    plt.title(f"Distributie de-a lungul LD{i+1}")
    plt.show()