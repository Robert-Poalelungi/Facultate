import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas = o biblioteca definita peste numpy, pentru operatii peste date tabelare (randuri si coloane)
# pune la dispozitie 2 tipuri:
# 1. Series - date unidimensionale (coloane in foaia de calcul)
# 2. DataFrame - date bidimensionale (foaia de calcul)

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [28, 32, 25],
    'Salary': [5000, 6000, 7000]
})

df = pd.read_csv('res/employees.csv', index_col=0)

# proprietati pe data frame
print("DF head\n", df.head()) # primele 5 randuri din df
print("DF tail\n", df.tail()) # ultimele 5 randuri din df
print("DF info\n", df.info()) # structura df: tipuri de date, valori null
print("DF describe\n", df.describe()) # statistici descriptive pe coloane
print("DF shape", df.shape) # (rows, columns)
print("DF columns", df.columns) # un obiect ce contine lista tuturor coloanelor
print("DF index", df.index) # un obiect ce contine lista tuturor referintelor randurilor

# accesul datelor - se foloseste operatorul de indexare [rows , columns]
# citirea datelor pe coloane
ages = df["Age"]

# coloane = ["Name", "Salary"]
# subset = df[df.columns - ["Name", "Salary"]]
subset = df[["Name", "Salary"]]

# citirea datelor pe randuri folosind indecsi | iloc - index location
fr = df.iloc[0] # primul rand din df
ftr = df.iloc[0:3] # primele 3 randuri

# citirea datelor pe randuri folosind etichete/labels | loc
# probabil mult mai intuitiv daca index_col = 1
# label1 = df.loc['Bob'] # cauta randul pentru care referinta (index value) = Bob
# label2 = df.loc['Eva':'Ivy', ["ID", "Salary"]]
# print(label1)
# print(label2)

label1 = df.loc[1] # cauta randul pentru care referinta (index value) = 1
label2 = df.loc[1:3, ["Name", "Salary"]]

# modificarea datelor
df["TaxedSalary"] = df["Salary"] * 0.9 # adaugarea unei coloane noi

# redenumire de coloane
df.rename(columns={'Salary':'GrossSalary'}, inplace=True)
df.rename(columns={'GrossSalary':'Salary'}, inplace=True)

# stergere de randuri sau coloane
df.drop(columns=["TaxedSalary"], inplace=True)
df.drop(index=[2], inplace=True)

# data sanitization = curatarea datelor - gestionarea celulor goale din data frame
# in general veti avea de a face cu unul din urmatoarele scenarii:
# 1 - operam cu date numerice
# 2 - operam cu date categorice (strings)
# in sanitizarea datelor fie alegem sa facem drop pe randuri sau coloane, fie substituim celulele
# lipsa cu valori convenabil alese
# - date numerice: de regula folosim media pe coloana sau o valoare potrivita in context
# - date categorice: de regula folosim modulul pe coloana (cea mai frecvent intalnita valoare)
#                    sau o valoare potrivita in context

missing = df.isna().sum()

# replace
value = df["Salary"].mean()
df["Salary"].fillna(value, inplace=True)

df.fillna(0)

# drop
df.dropna() # drop fiecarui rand care are NaN. echivalent: df.dropna(axis=0)
df.dropna(axis=1) # drop fiecarei coloane care are NaN

# transformari
# vectorizate
df["AgeInMonths"] = df["Age"] * 12

# lambda si apply
# def return_bracket(x):
#     if x > 6000:
#         return "High"
#     return "Low"
# df["IncomeBracket"] = df["Salary"].apply(return_bracket)

df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# metode din clasa string
df["Name"] = df["Name"].str.upper()

# statistici
# centrare

# scalare

# standardizare