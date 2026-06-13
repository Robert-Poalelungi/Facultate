import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas = biblioteca de functii construita peste numpy, destinata pentru operatii cu date
#           tabelare (randuri si coloane, foi de calcul)
# pune la dispozitie 2 tipuri de date:
# 1. Series - date unidimensionale (coloane in tabel)
# 2. DataFrame - date bidimensionale (tabelul propriu-zis)

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [27, 28, 24],
    'Salary': [4800, 5000, 3200]
})

df = pd.read_csv('res/employees.csv', index_col=1)

# proprietati pe data frame
print('DF head\n', df.head()) # primele 5 randuri din df
print('DF tail\n', df.tail()) # ultimele 5 randuri din df
print('DF info\n', df.info()) # structura datelor din df: tipuri de date, valori null
print('DF describe\n', df.describe()) # statistici descriptive pe coloane
print('DF shape', df.shape) # (rows, cols)
print('DF columns', df.columns) # un obiect ce contine o lista cu denumirile coloanelor
print('DF index', df.index) # un obiect ce contine o lista cu denumirile referintelor randurilor

# accesul datelor - se face folosind operatorul de indexare [rows , cols]
# citirea datelor pe coloane
ages = df["Age"] # coloana age
# ids = df[0] # citim prima coloana

# coloane = ["Salary", "Gender"]
# subset = df[df.columns - ["Salary", "Gender"]]
subset = df[["Salary", "Gender"]]

# citirea datelor pe randuri folosind indecsi | iloc - index location
fr = df.iloc[0]
ftr = df.iloc[0:3]

# citirea datelor pe randuri folosind etichete | loc
# loc se uita in valorile din index (in cazul nostru in valorile coloanei Name)
# si iterand prin acestea le compara 1 cate 1 cu valoarea dintre []. Daca gaseste valoarea
# se intoarce randul in cauza. Daca nu, se intoarce KeyError, echivalent cu not found
l1 = df.loc["Bob"]
l2 = df.loc["Eva": "Ivy", ["Salary","Gender"]]

print(l1)
print(l2)

# modificarea datelor
df["TaxedSalary"] = df["Salary"] * 0.9 # adaugare de coloana noua

df.rename(columns={'Salary':'GrossSalary'}, inplace=True)
df.rename(columns={'GrossSalary':'Salary'}, index={'Bob': 'Tim'}, inplace=True)

df.drop(columns=["TaxedSalary"], inplace=True)
df.drop(index=["Tim"], inplace=True)

# data sanitization = curatarea datelor - cum gestionam valorile lipsa
# in general veti opera cu date din urmatoarele cateogrii:
# 1. date numerice
# 2. date categorice (strings)
# iar sanitizarea datelor va presupune fie renuntarea la randuri/coloane, fie completarea
# celulelor lipsa cu valori convenabil alese
# 1. date numerice: inlocuim adesea cu media pe coloana sau cu alta valoare potrivita in context
# 2. date categorice: inlocuim adesea cu modulul (cea mai frecvent intalnita valoare)
# pe coloana sau cu alta valoare potrivita in context

missing = df.isna().sum()

df.dropna() # drop fiecarui rand care are NaN. echivalent cu df.dropna(axis=0)
df.dropna(axis=1) # drop fiecarei coloane care are NaN

df.fillna(0) #  df.fillna(0, inplace=True)
value = df["Salary"].mean() # date categorice: df["Gender"].mode()
df["Salary"].fillna(value, inplace=True)

# tranformari
# vectorizate
df["AgeInMonths"] = df["Age"] * 12

# lambda si apply
def return_bracket(x):
    if x > 6000:
        return "High"
    return "Low"
df["IncomeBracket"] = df["Salary"].apply(return_bracket)
df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# metode din clasa string
df["Gender"] = df["Gender"].str.lower()

print(df)

# statistici