import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas = o biblioteca de functii construita peste numpy, pentru calcul tabelar (randuri si coloane)
# pandas expune 2 tipuri de obiecte:
# 1. Series = date unidimensionale (coloana intr-un tabel)
# 2. DataFrame = date bidimensionale (tabele propriu-zise)

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [30, 32, 35],
    'Salary': [4000, 4500, 4700]
})

df = pd.read_csv('employees.csv', index_col=0)

# proprietati pe dataframe
print("df head\n", df.head()) # primele 5 randuri din df
print("df tail\n", df.tail()) # ultimele 5 randuri din df
print("df info\n", df.info()) # structura informatiilor din df: tipuri de date, valori null
print("df describe\n", df.describe()) # statistici simple cu privire la datele din coloane
print("df shape", df.shape) # (rows, columns)
print("df columns", df.columns) # lista cu denumirile coloanelor
print("df index", df.index) # lista cu denumirile referintelor randurilor

# accesarea datelor
# citirea - accesul se face folosind operatorul de indexare [idx_randuri , idx_coloane]
# citirea datelor pe coloane
ages = df['Age']
subset = df[["Name", "Salary"]]

# citirea datelor pe randuri in fc de pozitie | iloc = index location
fr = df.iloc[0] # primul rand
ftr = df.iloc[0:3] # primele 3 randuri

# citirea datelor pe randuri in fc de etichete (stringuri) | loc
l1 = df.loc[1]
l2 = df.loc[1:3, ["Name", "Salary"]]

# transformari
# adaugarea unei coloane noi
df["TaxedSalary"] = df["Salary"] * 0.9

df.rename(columns={"Salary": "GrossSalary"}, inplace=True)
df.rename(columns={"GrossSalary": "Salary"}, inplace=True)

# drop pe randuri si coloane
df.drop(columns=["TaxedSalary"], inplace=True) # drop pe coloana
df.drop(index=[9], inplace=True) # drop pe rand

# data sanitization
# in general, cand vorbim de data sanitization, ne vom gasi intr-unul din urmatoarele scenarii:
# - operam cu date numerice
# - operam cu date categorice (stringuri)
# cand avem celule lipsa, de regula urmarim fie sa inlocuim valorile lipsa, fie sa stergem ori coloanele, ori randurile probelematice
# - daca datele sunt numerice: inlocuim fie cu media pe coloana, fie cu o valoare convenabil aleasa
# - daca datele sunt categorice: inlocuim fie cu modulul (valoarea cea mai frecvent intalnita) pe coloana,
#   fie cu o valoare convenabil aleasa
missing = df.isna().sum()

# drop al coloanelor care contin NaN
df.dropna() # facem drop pe toate randurile care au NaN. echivalent cu df.dropna(axis=0)
df.dropna(axis=1) # cand axis = 1, facem drop pe toate coloanele care au NaN

# replace
df.fillna(0)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# alte transformari pe coloane
# vectorizare
df["AgeInMonths"] = df["Age"] * 12

# lambda si apply
# def return_bracket(x):
#     if x > 6000:
#         return "High"
#     return "Low"
# df["IncomeBracket"] = df["Salary"].apply(return_bracket)
df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# functii pe clasa string
df["Name"] = df["Name"].str.upper()

# statistici
# centrarea datelor = translatara intregului set relativ la o valoare de referinta care va sta in centrul setului de date
df["Salary_Centered"] = df["Salary"] - df["Salary"].mean()

# scalarea datelor = aducerea valorilor pe coloane la ordine de marime comparabile

# standardizarea = centrare + scalare
df["Salary_Std"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()

df["Salary"].mean()
df["Salary"].median()
df["Salary"].mode()