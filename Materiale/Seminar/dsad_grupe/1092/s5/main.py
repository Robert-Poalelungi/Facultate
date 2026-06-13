import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# pandas = bilblioteca definita peste numpy, destinata procesarii datelor tabelare (randuri si coloane)
# pune la dispozitie 2 obiecte:
# 1. Series - date unidimensionale (coloana in foaia de calcul)
# 2. DataFrame - date bidimensionale (foaia de calcul)

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [27, 29, 31],
    'Salary': [4000, 5000, 6000]
})

df = pd.read_csv('res/employees.csv', index_col=0)

# proprietati pe data frame
print("DF head\n", df.head()) # primele 5 randuri din DF
print("DF tail\n", df.tail()) # ultimele 5 randuri din DF
print("DF info\n", df.info()) # detalii despre structura DF: tipuri de data, valori null
print("DF describe\n", df.describe()) # statistici descriptive despre coloanele din DF
print("DF shape", df.shape) # (rows, columns)
print("DF columns", df.columns) # un obiect ce contine o lista a numelor coloanelor
print("DF index", df.index) # un obiect ce contine o lista a numelor referintelor randurilor

# accesul datelor - folosind operatorul de indexare [rows , columns]
# citirea datelor pe coloane
ages = df["Age"]

# coloane = ["Name", "Salary"]
# subset = df[df.columns - ["Name", "Salary"]]
subset = df[["Name", "Salary"]]

# cititul datelor pe randuri folosind indecsi numerici | iloc - index location
fr = df.iloc[0] # primul rand
ftr = df.iloc[0:3] # primele 3 randuri

# cititul datelor pe randuri folosind etichete/labels | loc
# diferenta dintre iloc si loc e mult mai evidenta cand index_col = 1 pe setul nostru de date
# label1 = df.loc["Bob"]
# label2 = df.loc["Eva":"Ivy", ["ID", "Salary"]]
# print(label1)
# print(label2)

label1 = df.loc[1]
label2 = df.loc[1:3, ["Name", "Salary"]]
print(label1)
print(label2)

# modificari ale datelor
df["TaxedSalary"] = df["Salary"] * 0.9 # adaugare de coloana noua

# redenumire coloane
df.rename(columns={'Salary':'GrossSalary'}, inplace=True)
df.rename(columns={'GrossSalary':'Salary'}, inplace=True)

# stergere de randuri sau coloane
df.drop(columns=["TaxedSalary"], inplace=True)
df.drop(index=[2], inplace=True)

# data sanitization = curatare a datelor
# uzual veti avea de a face cu date care pot fi:
# - date numerice
# - date categorice (strings)
# iar sanitizarea datelor va presupune fie stergerea randurilor/coloanelor, fie completarea
# celulelor lipsa cu valori convenabil alese
# - date numerice: adesea se va folosi media pe coloana sau o alta valoare potrivita in context
# - date categorice: adesea se va folosi modulul pe coloana (cea mai frecvent intalnita valoare)
#                       sau o alta valoare potrivita in context

missing = df.isna().sum()

# provizionare de valori (interpolate)
df.fillna(0)
value = df["Salary"].mean()
df["Salary"].fillna(value, inplace=True)

# drop
df.dropna() # drop tuturor randurilor care contin NaN. echivalent: df.dropna(axis=0)
df.dropna(axis=1) # drop tuturor coloanelor care contin NaN

# transformari
# vectorizate
df["AgeInMonths"] = df["Age"] * 12

# lambda si apply
# def return_bracket(x):
#     if x > 6000:
#         return "High"
#     return "Low"
# df["IncomeBracket"] = df["Salary"].apply(return_bracket)
# print(df)
df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# metode din clasa string
df["Name"] = df["Name"].str.upper()

# statistici
# centrare

# scalare

# standardizare