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

df = pd.read_csv("res/employees.csv", index_col=0)

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
subset = df[["Name", "Salary"]] # extragere a datelor de pe 2 coloane

# randuri folosind indecsi | iloc - index location
df.iloc[0] # first row
df.iloc[0:3] # first 3 rows

# randuri folosind etichete/labels | loc - regasire folosind label sau indice asociat in mod default
df.loc[1]
df.loc[1:3, ["Name", "Salary"]]

# filtrare folosind conditii boolean
df[df["Age"] > 30]
df[(df["Salary"] > 6000) & (df["Age"] < 40)]

# modificarea datelor din df
df["TaxedSalary"] = df["Salary"] * 0.9 # adauga o coloana noua numita TaxedSalary

df.rename(columns={'Salary': 'GrossSalary'}, inplace=True)
df.rename(columns={'GrossSalary': 'Salary'}, inplace=True)

df.drop(columns=["TaxedSalary"], inplace=True) # drop pe coloana
df.drop(index=[1], inplace=True) # drop pe rand

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
df["Name"] = df["Name"].str.upper()

# statistica
# centrarea datelor => translatarea intregului set de date in raport cu o valoare, care se va gasi in centrul setului
#                       altfel spus: reaseazarea setului de date. implementarea presupune sa iei fiecare element si sa scazi din el media
df["Salary_Centered"] = df["Salary"] - df["Salary"].mean()

# scalarea datelor => presupune sa aduci variabilele la acelasi ordin de marime

# standardizarea datelor = centrare + scalare
df["Salary_std"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()

# unde sunt datele noastre reprezentate
df["Salary"].mean()
df["Salary"].median()
df["Salary"].mode()

# dispersia datelor
df["Salary"].std()
df["Salary"].var()

# cum se influenteaza reciproc
df[["Age", "Salary"]].corr()