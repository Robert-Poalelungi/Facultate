from functii import *

fisier = open("Educatie.csv")
# print(type(fisier))
linii = fisier.readlines()
# print(linii)
fisier.close()
# Citire antet
linia0 = linii[0][:-1].split(",")
# print(linia0)
nume_index = linia0[0]
variabile = linia0[1:]
variabile_numerice = variabile[2:]
print(nume_index, variabile, variabile_numerice, sep="\n")

# Citire date
tabel = dict()
for i in range(1, len(linii)):
    linie_str = linii[i][:-1].split(",")
    linie = linie_str[1:3]
    for j in range(3, len(linie_str)):
        linie.append(float(linie_str[j]))
    tabel[int(linie_str[0])] = tuple(linie)
for v in tabel:
    print(v, tabel[v])

# Cerinta 1
cerinta1 = {} #forma scurta de la dictionar
for v in tabel:
    cerinta1[v] = (tabel[v][0], tabel[v][1], sum(tabel[v][2:8]), sum(tabel[v][8:])) #tavel[v][0] afiseaza primul element din fiecare tuplu din dictionar
print("--> Cerinta 1")
for v in cerinta1:
    print(v, cerinta1[v])
salvare(cerinta1,
        ["Denumire localitate", "Indicativ judet", "Numar absolventi", "Populatia scolara"],
        nume_index, "cerinta1.csv"
        )

# Cerinta 2
print("--> Cerinta 2")
cerinta2 = calcul_indicatori(tabel, variabile_numerice)
for v in cerinta2:
    print(v, cerinta2[v])
salvare(cerinta2, ["Media", "Abaterea standard", "Coeficientul de variatie"],
        "Variabile", "cerinta2.csv")

# Cerinta 3
print("--> Cerinta 3")
for v in filter(functie_filtru, tabel.values()): #functia filter iti itereaza doar prin valorile din tabel pentru care functie_filtru iti returneaza TRUE
    print(v)
nume_variabila = "Abs_postlic"
for v in filter(lambda x: filtru_lambda(x, variabile.index(nume_variabila), 0), tabel.values()):
    print(v)
cerinta3 = dict(
    filter(lambda x: filtru_lambda1(x, variabile.index(nume_variabila), 0), tabel.items())) #items iti returneaza toata linia din tabel, inclusiv cheia
salvare(cerinta3, variabile, nume_index, "cerinta3.csv")

# Cerinta 4
nume_variabila_sortare = "Pop_univ"
cerinta4 = dict(sorted(
    tabel.items(),
    key=lambda x: criteriu_sortare(x, variabile.index(nume_variabila_sortare)),
    reverse=True
))
print("--> Cerinta 4")
for v in cerinta4:
    print(v, cerinta4[v])
salvare(cerinta4, variabile, nume_index, "cerinta4.csv")

# Cerinta 5
print("--> Cerinta 5")
cerinta5 = dict(map(selector, tabel.items()))
for v in cerinta5:
    print(v, cerinta5[v])
salvare(cerinta5, variabile[8:], nume_index, "cerinta5.csv")



