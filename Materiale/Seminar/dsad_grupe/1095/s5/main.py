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

df = pd.read_csv("res/employees.csv", index_col=0)

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
subset = df[["Name", "Salary"]]

# acces folosind iloc
fr = df.iloc[0] # primul rand | iloc - index location
ftr = df.iloc[0:3] # primele 3 randuri

# acces folosind loc | loc - label based location, fie pe baza numelui coloanei sau a indexului asociat intern - read the docs
sr = df.loc[1]
ors = df.loc[1:3, ["Name", "Salary"]]

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
df.drop(index=[0], inplace=True) # drop la primul rand

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
df["Name"] = df["Name"].str.upper()


# statistica
# centrarea datelor - translatarea (data shift) in jurul valorii 0, astfel incat media sa fie 0
# se realizeaza scazand din fiecare element media: xi - x_

# scalarea datelor - aducerea valorilor de pe coloane la un ordin de marime comparabil (milimetri vs kilometri sau numar camere vs an constructie)

# standardizarea datelor = centrare + scalare

# media, mediana si modulul arata unde sunt distribuite datele
print(df["Salary"].mean())
print(df["Salary"].median())
print(df["Salary"].mode())

# cum sunt datele distribuite
print(df["Salary"].std())
print(df["Salary"].var())

# cum se influenteaza reciproc variabilele
print(df[["Age", "Salary"]].corr())



