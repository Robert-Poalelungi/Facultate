from unittest.mock import inplace

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# pandas = biblioteca de functiic construita peste numpy, specializata in manipularea datelor tabelare (randuri si coloane)
# pune la dispozitie 2 tipuri de date:
# 1. Series - date unidimensionale (coloane in foaia de calcul)
# 2. DataFrame - date bidimensionale (foaia de calcul)

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [30, 27, 32],
    'Salary': [4000, 6000, 5500]
})

df = pd.read_csv('res/employees.csv', index_col=0)

# proprietati pe data frame
print("DF head\n", df.head()) # primele 5 randuri din df
print("DF tail\n", df.tail()) # ultimele 5 randuri din df
print("DF info\n", df.info()) # structura datelor din df: tipuri de date, valori null
print("DF describe\n", df.describe()) # statistici simple pe coloane
print("DF shape", df.shape) # (rows, columns)
print("DF columns", df.columns) # un obiect care contine o lista cu numele coloanelor
print("DF index", df.index) # un obiect care contine o lista cu numele referintelor randurilor

# accesul datelor - se face folosind operatorul de indexare [rows , columns]
# citirea datelor pe coloane
ages = df["Age"]

# subset = df[df.columns - ["Name", "Salary"]]
subset = df[["Name", "Salary"]]

# citirea datelor pe randuri folosind indecsi | iloc - index location
fr = df.iloc[0]
ftr = df.iloc[0:3]

# citirea datelor pe randuri folosind etichete/labels | loc
# mult mai intuitiv in exemplul urmator:
# label1 = df.loc['Bob']
# label2 = df.loc['Carol':'Ivy', ["ID", "Salary"]]

label1 = df.loc[1]
label2 = df.loc[1:3, ["Name", "Salary"]]

# modificarea datelor
df["TaxedSalary"] = df["Salary"] * 0.9 # adaugare de coloane noi

# redenumire
df.rename(columns={'Salary':'GrossSalary'}, inplace=True)
df.rename(columns={'GrossSalary':'Salary'}, inplace=True)

# stergeri
df.drop(columns=["TaxedSalary"], inplace=True)
df.drop(index=[2], inplace=True)

# data sanitization = curatirea datelor
# in general va veti confrunta cu unul din urmatoarele cazuri:
# - date numerice
# - date categorice (strings)
# sanitizarea datelor presupune fie stergerea randurilor/coloanelor cu valori lipsa, fie completarea
# lor in mod convenabil
# - date numerice: completezi celulele lipsa cu media pe coloane sau cu o valoare potrivita in context
# - date categorice: completezi celulele lipsa cu modulul pe coloane (cea mai frecvent intalnita valoare)
#   sau cu o valoare potrivita in context

missing = df.isna().sum()
# replace
replace_value = df["Salary"].mean()
df["Salary"].fillna(replace_value, inplace=True)

df.fillna(0)

# drop
df.dropna() # drop tuturor randurilor care au celule goale. echivalent cu df.dropna(axis=0)
df.dropna(axis=1) # drop tuturor coloanelor care au celule goale

# transformari:
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