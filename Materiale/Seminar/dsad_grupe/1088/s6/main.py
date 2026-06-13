import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas = biblioteca construia peste numpy pentru gestiunea datelor tabelare (randuri si coloane)
# expune 2 tipuri mari de date:
# 1. Series = date unidimensionale (o coloana)
# 2. DataFrame = date bidimensionale (foaia de calcul)

# series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [25, 32, 41],
    'Salary': [5000, 6200, 8000]
})

df = pd.read_csv("res/employees.csv", index_col=1)

# proprietati pe df
print("DF head\n", df.head()) # primele 5 randuri din df
print("DF tail\n",df.tail()) # ultimele 5 randuri din df
print("DF info\n", df.info()) # structura df, cu tipuri de date si valori null
print("DF describe\n", df.describe()) # statistici simple cu privire la datele din df
print("DF shape\n", df.shape) # (rows,cols)
print("DF columns\n", df.columns) # lista cu coloanele din df
print("DF index\n", df.index) # lista cu randurile din df

# accesul datelor - operatorul utilizat este cel de indexare []
# coloane
ages = df["Age"] # extragerea datelor pe 1 singura coloana
subset = df[["Gender", "Salary"]] # extragere a datelor de pe 2 coloane

# randuri folosind indecsi | iloc - index location
df.iloc[0] # first row
df.iloc[0:3] # first 3 rows

# randuri folosind etichete/labels | loc - regasire folosind label sau indice asociat in mod default
df.loc["Bob"]
df.loc["Eva":"Ivy", ["Gender", "Salary"]]

# filtrare folosind conditii boolean
df[df["Age"] > 30]
df[(df["Salary"] > 6000) & (df["Age"] < 40)]

# modificarea datelor din df
df["TaxedSalary"] = df["Salary"] * 0.9 # adauga o coloana noua numita TaxedSalary

df.rename(columns={'Salary': 'GrossSalary'}, inplace=True)
df.rename(columns={'GrossSalary': 'Salary'}, inplace=True)

df.drop(columns=["TaxedSalary"], inplace=True) # drop pe coloana
df.drop(index=["Carol"], inplace=True) # drop pe rand

# sanitizarea datelor (gestionarea valorilor lipsa)
# identificare valori lipsa
count = df.isna().sum()

# cand vorbim despre sanitizarea datelor ne vom regasi intr-unul din cele 2 scenarii:
# - avem date numerice => celulele lipsa se completeaza de regula cu media pe coloana
#                           sau o valoare convenabil aleasa
# - avem date categorice (strings) => celulele lipsa se completeaza de regula cu modulul
#                                       (cea mai frecvent intalnita valoare pe coloana)
#                                       sau o valoare convenabil aleasa

# pt sanitizare fie vom sterge coloanele sau randurile cu valori lipsa, fie le completam
df.dropna() # drop any row with NaN
df.dropna(axis=1) # drop any column with NaN

df.fillna(0)
replace = df["Salary"].mean()
df["Salary"].fillna(replace, inplace=True)

# transformari de date
# vectorizata
df["AgeInMonths"] = df["Age"] * 12

# lambda si apply
# def return_bracket(x):
#     if x > 6000: return "High"
#     return "Low"
# df["IncomeBracket"] = df["Salary"].apply(return_bracket)
df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# metode din strings
df["Gender"] = df["Gender"].str.lower()

# statistica
# centrarea datelor => translatarea intregului set de date in raport cu o valoare, care se va gasi in centrul setului
#                       altfel spus: reaseazarea setului de date. implementarea presupune sa iei fiecare element si sa scazi din el media
df["Salary_Centered"] = df["Salary"] - df["Salary"].mean()

# scalarea datelor => presupune sa aduci variabilele la acelasi ordin de marime

# standardizarea datelor = centrare + scalare
df["Salary_std"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()
# datele standardizate au valori in intervalul -inf:+inf
# procesul de standardizare nu altereaza reprezentarea datelor
# relevanta pentru situatii in care plecam de la premisa ca datele noastre respecta o distributie normala: ACP, regresii s.a.

# normalizarea datelor = presupunere aducerea valorilor intr-un interval anume, adesea [0:1]
# normalizarea datelor presupune transformarea lor pe baza formulei:
# (xi - xmin) / (xmax - xmin)
# utilitate: cand operam cu retele neuronale, cu inputuri care au domeniu de definitie finit (procesare de imagini)

# unde sunt datele noastre reprezentate
df["Salary"].mean()
df["Salary"].median() # valoare ce imparte setul de date in 2 jumatati egale
df["Salary"].mode() # in romana: modul - valoarea cea mai frecvent intalnita

# dispersia datelor
df["Salary"].std()
df["Salary"].var()

# cum se influenteaza reciproc
df[["Age", "Salary"]].corr()

# daca valorile coef de corelatie sunt pozitive: intre var x si y exista o relatie directa - cand 1 creste si cealalta creste si invers
# daca valorile coef de corelatie sunt negative: intre var x si y exista o relatie inversa - cand 1 creste, cealalta scade si invers
# daca valorile sunt in jurul lui 0: variabilele sunt necorelate

df["Salary"].hist(bins=5, edgecolor='red')
# plt.show()

# merge pe tabele - operatiile merge, concat
df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob", "Carol"]
})

df2 = pd.DataFrame({
    "ID": [4,5,6],
    "Name": ["Eva", "Ivy", "Mark"]
})

df3 = pd.DataFrame({
    "ID": [1,2,3],
    "Department": ["IT", "HR", "Finance"]
})

# merge pe baza de cheie
# cazul de mai jos pleaca de la premisa ca atat in df1, cat si in df3 exista o coloana (df.columns, nu df.index!!!) care se numeste ID
merge = df1.merge(df3, on="ID")
print(merge)

# concatenare
concat = pd.concat([df1, df2])
print(concat)

# merge-urile de data frames sunt echivalentul unor joins din SQL. plecam de la premisa ca mai jos operatiile sunt de forma: df1.merge(df2)
# inner - ce este comun lui DF1 si DF2
# left - tot ce este in DF1
# right - tot ce este in DF2
# outer - DF1 + DF2

employees = pd.read_csv("res/employees.csv")
departments = pd.read_csv("res/departments.csv")

# exemplele de mai jos merg atata timp cat exista aceasta coloana DepartmentID in employees si departments
# inner
inner = employees.merge(departments, on="DepartmentID", how="inner")
print("inner\n", inner)

# left
left = employees.merge(departments, on="DepartmentID", how="left")
print("left\n", left)

# right
right = employees.merge(departments, on="DepartmentID", how="right")
print("right\n", right)

# outer
outer = employees.merge(departments, on="DepartmentID", how="outer")
print("outer\n", outer)

# exemple de merge intre surse de date diferite, folosind index-ul si nu coloanele
tabel_etnii = pd.read_csv('res/Ethnicity.csv', index_col=0)
# nan_replace()

variabile_etnii = list(tabel_etnii.columns)[1:]

# calcul populatie pe etnii la nivel de judet
localitati = pd.read_excel("res/CoduriRomania.xlsx", index_col=0)
t1 = tabel_etnii.merge(right=localitati, right_index=True, left_index=True)
print(t1)

g1 = t1[variabile_etnii + ["County"]].groupby(by="County").agg(sum)
print(g1)

# calcul populatie pe etnii la nivel de regiune
judete = pd.read_excel("res/CoduriRomania.xlsx", index_col=0, sheet_name="Judete")
t2 = g1.merge(right=judete, right_index=True, left_index=True)
print(t2)

g2 = t2[variabile_etnii + ["Regiune"]].groupby(by="Regiune").agg(sum)
print(g2)

# calcul populatie pe etnii la nivel de macroregiune
regiuni = pd.read_excel("res/CoduriRomania.xlsx", index_col=0, sheet_name="Regiuni")
t3 = g2.merge(right=regiuni, right_index=True, left_index=True)
print(t3)

g3 = t3[variabile_etnii + ['MacroRegiune']].groupby(by="MacroRegiune").agg(sum)
print(g3)

# indici de diversitate