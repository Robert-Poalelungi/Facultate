import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas este construita peste numpy pt a gestiona formate tabelare (randuri si coloane)
# expune 2 tipuri principale de date:
# - Series - seturi unidimensionale (coloane)
# - DataFrame - seturi bidimensionale

s = pd.Series([10,20,30], index = ['a', 'b', 'c'])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [25,32,41],
    'Salary': [5000, 6200, 8000]
})

df = pd.read_csv("res/employees.csv", index_col=1)

# proprietati pe dataframe
print("DF head\n", df.head()) # primele 5 randuri
print("DF tail\n",df.tail()) # ultimele 5 randuri
print("DF info\n", df.info()) # structura dataframe - tipuri de date, valori null
print("DF describe\n", df.describe()) # statistici despre coloanele numerice
print("DF shape\n", df.shape) # (rows,cols)
print("DF columns\n", df.columns) # lista cu denumirea coloanelor (variabile sau features)
print("DF index\n", df.index) # lista cu denumirea randurilor (instantelor)

# data access - folosim in continuare operatorul [] de indexare, cu mici variatii
# coloane
ages = df["Age"]
subset = df[["Gender", "Salary"]]

# acces folosind iloc
fr = df.iloc[0] # primul rand | iloc - index location
ftr = df.iloc[0:3] # primele 3 randuri

# acces folosind loc | loc - label based location, fie pe baza numelui coloanei sau a indexului asociat intern - read the docs
sr = df.loc["Bob"]
ors = df.loc["Eva":"Ivy", ["Gender", "Salary"]]

# filtrare pe baza de conditii boolean
fc = df[df["Age"] > 30]
sc = df[(df["Salary"] > 6000) & (df["Age"] < 40)]

# modificare de valori in dataframe
df["TaxedSalary"] = df["Salary"] * 0.9 # adaugare de coloana suplimentara in DF

df.rename(columns={"Salary": "GrossSalary"}, inplace=True)
# cand inplace=True, se modifica obiectul df din memorie. altfel, metoda intoarce o copie a datelor modificate
df.rename(columns={"GrossSalary": "Salary"}, inplace=True)

# eliminare coloane sau randuri
df.drop(columns=["TaxedSalary"], inplace=True) # drop la coloana numita TaxedSalary
df.drop(index=["Carol"], inplace=True) # drop la primul rand

# gestionarea valorilor lipsa sau data sanitization
# vrem sa tratam de fiecare data scenariile in care avem celule cu valori lipsa (nan)
# motivul este ca algoritmii de analiza de date arunca erori atunci cand intalnesc valori lipsa
# abordarile uzuale se rezuma la: fie fac drop coloanelor sau randurilor conflictuale, fie incerc
# sa substitui lipsurile
# avem 2 scenarii:
# 1. date numerice - in cazul lor vom substitui de obicei cu media (pe coloana cel mai adesea)
# 2. date categorice (stringuri) - in cazul lor vom substitui de obicei cu modulul (cea mai frecvent
# intalnita valoare) sau o valoare convenabil aleasa, care sa nu influenteze semnificativ operatiile

# detectia nan
count = df.isna().sum()

df.dropna() # elimina randurile care contin celule lipsa
df.dropna(axis = 1) # elimina coloanele care contin celule lipsa

df.fillna(0)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# data transformation
# vectorized
df["AgeInMonths"] = df["Age"] * 12

# lambda si apply
# def return_bracket(x):
#     if x > 6000:
#         return "High"
#     return "Low"
# df["IncomeBracket"] = df["Salary"].apply(return_bracket)
df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# transformari folosind metode de pe clasa string
df["Gender"] = df["Gender"].str.lower()


# statistica
# centrarea datelor - translatarea (data shift) in jurul valorii 0, astfel incat media sa fie 0
# se realizeaza scazand din fiecare element media: xi - x_
df["Salary_centered"] = df["Salary"] - df["Salary"].mean()

# scalarea datelor - aducerea valorilor de pe coloane la un ordin de marime comparabil (milimetri vs kilometri sau numar camere vs an constructie)

# standardizarea datelor = centrare + scalare
df["Salary_standardized"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()

# normalizarea datelor = aducerea valorilor intr-un interval [0:1] sau mai rar [-1: 1]
# se realizeaza adesea dupa formula: x' = (xi - xmin) / (xmax - xmin)

# la nivel de impact asupra datelor:
# - standardizarea se aseamana cu o redimensionare si translatare a distributiei
# - normalizarea - modifica distributia datelor, ceea ce inseamna ca reprezentarea grafica se modifica

# media, mediana si modulul arata unde sunt distribuite datele
print(df["Salary"].mean())
print(df["Salary"].median()) # valoarea care imparte setul de date in 2 jumatati egale
print(df["Salary"].mode()) # valoarea cea mai frecvent intalnita

# cum sunt datele distribuite
print(df["Salary"].std())
print(df["Salary"].var())

# cum se influenteaza reciproc variabilele
print(df[["Age", "Salary"]].corr())

# valorile sunt intre -inf si +inf;
# cand valoarea este pozitiva, exista o relatie directa intre cele 2 variabile - daca una creste, cealalta creste si ea si invers
# cand valoarea este cat mai apropiata de 0 - variabilele sunt independente - variatia unei nu influenteaza dinamica celeilalte
# cand valoarea este negativa, exista o relatie inversa intre cele 2 variabile - daca una creste, cealalta scade si invers

df["Salary"].hist(bins=15)
#plt.show()

# combinarea datelor din surse distincte
df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob", "Carol"]
})

df2 = pd.DataFrame({
    "ID": [4,5,6],
    "Name": ["David", "Eva", "Ivy"]
})

df3 = pd.DataFrame({
    "ID": [1,2,3],
    "Department": ["IT", "HR", "Finance"]
})

# merge in functie de o cheie
merged = df1.merge(df3, on="ID")
print("merged\n", merged)

# concatenare
concat = pd.concat([df1, df2])
print("concat\n", concat)

# tipuri de merge la nivel de dateframe - similar cu SQL joins
# inner - doar randuri care exista in ambele DF - intersectia dintre df1 si df2
# left - tot ce se afla in stanga - df1
# right - tot ce se afla in dreapta - df2
# outer - df1 + df2

employees =  pd.read_csv("res/employees.csv")
departments =  pd.read_csv("res/departments.csv")

# cele 4 metode de mai jos functioneaza in scenariile in care avem o coloana comuna (df.columns, nu df.index)
# inner join
inner = employees.merge(departments, on="DepartmentID", how="inner")
print("Inner join\n", inner)

# left join
left = employees.merge(departments, on="DepartmentID", how="left")
print("Left join\n", left)

# right join
right = employees.merge(departments, on="DepartmentID", how="right")
print("Right join\n", right)

# outer join - toate DepartmentID unice
outer = employees.merge(departments, on="DepartmentID", how="outer")
print("Outer join\n", outer)

# exercitiu siruta
tabel_etnii = pd.read_csv("res/Ethnicity.csv", index_col=0)
# nan_replace()

variabile_etnii = list(tabel_etnii.columns)[1:]

# calcul populatie pe etnii la nivel de judet
localitati = pd.read_excel("res/CoduriRomania.xlsx", index_col=0)

print(tabel_etnii)
print(localitati)

# in conditiile in care criteriul de merge este indexul si nu o coloana anume, vom folosi:
t1 = tabel_etnii.merge(right=localitati, right_index=True, left_index=True)
print(t1)

g1 = t1[variabile_etnii + ["County"]].groupby(by="County").agg(sum)
print(g1)
g1.to_csv("res/output_etnii_judete.csv")

# calcul populatie pe etnii la nivel de regiune
judete = pd.read_excel("res/CoduriRomania.xlsx", index_col=0, sheet_name="Judete")
t2 = g1.merge(right=judete, right_index=True, left_index=True)

g2 = t2[variabile_etnii + ["Regiune"]].groupby(by="Regiune").agg(sum)
print(g2)
g2.to_csv("res/output_etnii_regiuni.csv")

# calcul populatie pe etnii la nivel de macroregiune
regiuni = pd.read_excel("res/CoduriRomania.xlsx", index_col=0, sheet_name="Regiuni")
t3 = g2.merge(right=regiuni, right_index=True, left_index=True)

g3 = t3[variabile_etnii + ["MacroRegiune"]].groupby(by="MacroRegiune").agg(sum)
print(g3)
g3.to_csv("res/output_etnii_macroregiuni.csv")

# indici de diversitate
