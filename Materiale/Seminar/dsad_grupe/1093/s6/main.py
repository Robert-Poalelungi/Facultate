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
# df["Salary"].fillna(value, inplace=True) - warning fix
df.fillna({"Salary": value}, inplace=True)

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
# standardizarea datelor = e un procedeu compus din 2 pasi: centrarea datelor si scalarea datelor
# procesul de standardizare doar redimensioneaza si deplaseaza pe axe reprezentarea grafica a datelor, fara a o distorsiona
# veti face intotdeauna standardizarea datelor atunci cand veti utiliza algoritmi care pleaca de la premisa ca datele
# respecta o distributie normala (Gaussiana): ACP, regresiile

# centrarea datelor = deplasarea valorilor datelor in jurul unei valori centrale, fara a le schimba ordinul de marime
# centrarea se realizeaza conform formulei:
df["Salary_centered"] = df["Salary"] - df["Salary"].mean()

# standardizarea are ca si consecinta existenta a 2 relatii: Xmediu (X_) = 0 si Sx = 1
df["Salary_standardized"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()

# normalizarea datelor = aducerea valorilor unei variabile intr-un interval, de regula [0:1]
# formula de normalizare este: Xn = (Xi - Xmin) / (Xmax - Xmin)
# normalizarea de regula se foloseste in algoritmi de ML cu retele neuronale (functii de activare)
# sau atunci cand operam cu variabile care au domenii de definitie finite (procesare de imagini)

# statistici descriptive
df["Salary"].mean() # media aritmetica: suma din elemente / nr elemente
df["Salary"].median() # valoarea care imparte setul in 2 jumatati egale
df["Salary"].mode() # in romana: modul - valoarea cea mai des intalnita (pe coloane)

df["Salary"].std() # abatere standard
df["Salary"].var()

# relatia intre 2 variabile
df[["Age", "Salary"]].corr()
# daca valoarea coef este pozitiva, intre cele 2 var exista o relatie directa: daca 1 creste si cealalta creste si invers
# daca valoarea coef este negativa, intre cele 2 var exista o relatie de inversa proportionalitate:
#                           daca 1 creste si cealalta scade si invers
# daca valorile sunt aprox 0: cele 2 variabile sunt independente

# desenare direct din pandas
# df["Salary"].hist(bins=15, edgecolor='red')
df["Age"].plot()
# plt.show()

# merge si concatenate
df1 = pd.DataFrame({
    "ID": [1,2,3],
    "Name": ["Alice", "Bob", "Carol"]
})

df2 = pd.DataFrame({
    "ID": [4,5,6],
    "Name": ["Mark", "Eva", "Ivy"]
})

df3 = pd.DataFrame({
    "ID": [1,2,3],
    "Department": ["IT", "HR", "Finance"]
})

merged = df1.merge(df3, on="ID")
print(merged)

concat = pd.concat([df1, df2])
print(concat)

# merge in functie de coloane - merge-ul pe coloane pleaca de la premisa ca exista o coloana cu aceeasi denumire in ambele surse de date
# iar prin coloana intelegem o valoare din df.columns (nu df.index!!!)
employees = pd.read_csv('res/employees.csv')
departments = pd.read_csv('res/departments.csv')

# tipuri de merge, plecand de la premisa ca avem 2 data frames: df1 si df2,
# iar operatia de merge respecta o structura de forma: df1.merge(df2)
# inner - intersectia dintre df1 si df2
# left - toate datele care se gasesc in df1 (randurile din df2 care nu au corespondent in df1 se pierd)
# right - toate datele care se gasesc in df2 (randurile din df1 care nu au corespondent in df2 se pierd)
# outer - reuniunea dintre df1 si df2 (toate datele reunite)

# inner
inner = employees.merge(departments, on="DepartmentID", how="inner")
print(inner)

# left
left = employees.merge(departments, on="DepartmentID", how="left")
print(left)

# right
right = employees.merge(departments, on="DepartmentID", how="right")
print(right)

# outer
outer = employees.merge(departments, on="DepartmentID", how="outer")
print(outer)

# merge in functie de index
tabel_etnii = pd.read_csv('res/Ethnicity.csv', index_col=0)
# nan_replace()

variabile_etnii = list(tabel_etnii.columns)[1:]

# calcul populatie pe etnii la nivel de judet
localitati = pd.read_excel('res/CoduriRomania.xlsx', index_col=0, sheet_name='Localitati')

t1 = tabel_etnii.merge(right=localitati, right_index=True, left_index=True)
print(t1)

g1 = t1[variabile_etnii + ["County"]].groupby(by="County").agg("sum")
print(g1)

#print(g1.loc["ph"]["Hungarians"])

# calcul populatie pe etnii la nivel de regiune
judete = pd.read_excel('res/CoduriRomania.xlsx', index_col=0, sheet_name='Judete')

t2 = g1.merge(right=judete, right_index=True, left_index=True)
print(t2)

g2 = t2[variabile_etnii + ["Regiune"]].groupby(by="Regiune").agg("sum")
print(g2)

# calcul populatie pe etnii la nivel de macroregiune
regiuni = pd.read_excel('res/CoduriRomania.xlsx', index_col=0, sheet_name='Regiuni')

t3 = g2.merge(right=regiuni, right_index=True, left_index=True)
print(t3)

g3 = t3[variabile_etnii + ["MacroRegiune"]].groupby(by="MacroRegiune").agg("sum")
print(g3)

g1.to_csv('res/output_etnii_judete.csv')
g2.to_csv('res/output_etnii_regiuni.csv')
g3.to_csv('res/output_etnii_macroregiuni.csv')

# indici de diversitate