import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pandas is built on top of numpy to handle tabular formats (rows and columns)
# exposes 2 main types of data:
# - Series - one-dimensional sets (columns)
# - DataFrame - two-dimensional sets

s = pd.Series([10,20,30], index = ['a', 'b', 'c'])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [25,32,41],
    'Salary': [5000, 6200, 8000]
})

df = pd.read_csv("res/employees.csv", index_col=1)

# DataFrame properties
print("DF head\n", df.head()) # first 5 rows
print("DF tail\n",df.tail()) # last 5 rows
print("DF info\n", df.info()) # DataFrame structure - data types, null values
print("DF describe\n", df.describe()) # statistics for numeric columns
print("DF shape\n", df.shape) # (rows,cols)
print("DF columns\n", df.columns) # list of column names (variables or features)
print("DF index\n", df.index) # list of row names (instances)

# data access - we continue using the [] indexing operator with small variations
# columns
ages = df["Age"]
subset = df[["Gender", "Salary"]]

# access using iloc
fr = df.iloc[0] # first row | iloc - index location
ftr = df.iloc[0:3] # first 3 rows

# access using loc | loc - label-based location, either by column name or internal index - read the docs
sr = df.loc["Bob"]
ors = df.loc["Eva":"Ivy", ["Gender", "Salary"]]

# filtering based on boolean conditions
fc = df[df["Age"] > 30]
sc = df[(df["Salary"] > 6000) & (df["Age"] < 40)]

# modifying values in the DataFrame
df["TaxedSalary"] = df["Salary"] * 0.9 # add an extra column to the DF

df.rename(columns={"Salary": "GrossSalary"}, inplace=True)
# when inplace=True, the df object is modified in memory. Otherwise, the method returns a modified copy
df.rename(columns={"GrossSalary": "Salary"}, inplace=True)

# dropping columns or rows
df.drop(columns=["TaxedSalary"], inplace=True) # drop the column named TaxedSalary
df.drop(index=["Carol"], inplace=True) # drop the first row

# handling missing values or data sanitization
# we always want to handle scenarios with missing values (nan)
# the reason is that data analysis algorithms throw errors when encountering missing values
# common approaches: either drop conflicting columns/rows or try to substitute missing values
# we have 2 scenarios:
# 1. numeric data - usually replace with the column mean
# 2. categorical data (strings) - usually replace with the mode (most frequent value) or a convenient value that doesn't significantly affect operations

# detect nan
count = df.isna().sum()

df.dropna() # remove rows containing missing cells
df.dropna(axis = 1) # remove columns containing missing cells

df.fillna(0)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)

# data transformation
# vectorized
df["AgeInMonths"] = df["Age"] * 12

# lambda and apply
# def return_bracket(x):
#     if x > 6000:
#         return "High"
#     return "Low"
# df["IncomeBracket"] = df["Salary"].apply(return_bracket)
df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# transformations using string methods
df["Gender"] = df["Gender"].str.lower()

# statistics
# centering data - shift data around 0 so the mean is 0
# done by subtracting the mean from each element: xi - x_
df["Salary_centered"] = df["Salary"] - df["Salary"].mean()

# scaling data - bring column values to comparable magnitudes (millimeters vs kilometers or number of rooms vs year built)

# standardization = centering + scaling
df["Salary_standardized"] = (df["Salary"] - df["Salary"].mean()) / df["Salary"].std()

# normalization = bring values to a range [0:1] or sometimes [-1:1]
# often done with: x' = (xi - xmin) / (xmax - xmin)

# impact on data:
# - standardization is like resizing and shifting the distribution
# - normalization modifies the distribution, changing graphical representation

# mean, median, and mode show data distribution
print(df["Salary"].mean())
print(df["Salary"].median()) # value dividing dataset into 2 equal halves
print(df["Salary"].mode()) # most frequent value

# how data is distributed
print(df["Salary"].std())
print(df["Salary"].var())

# correlation between variables
print(df[["Age", "Salary"]].corr())

# values are between -inf and +inf
# positive value: direct relationship between variables - if one increases, the other increases
# value close to 0: variables are independent - variation in one doesn't affect the other
# negative value: inverse relationship - if one increases, the other decreases

df["Salary"].hist(bins=15)
#plt.show()

# combining data from different sources
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

# merge based on a key
merged = df1.merge(df3, on="ID")
print("merged\n", merged)

# concatenation
concat = pd.concat([df1, df2])
print("concat\n", concat)

# types of DataFrame merge - similar to SQL joins
# inner - only rows present in both DF - intersection of df1 and df2
# left - all rows in left DF - df1
# right - all rows in right DF - df2
# outer - df1 + df2

employees =  pd.read_csv("res/employees.csv")
departments =  pd.read_csv("res/departments.csv")

# the 4 methods below work when there is a common column (df.columns, not df.index)
# inner join
inner = employees.merge(departments, on="DepartmentID", how="inner")
print("Inner join\n", inner)

# left join
left = employees.merge(departments, on="DepartmentID", how="left")
print("Left join\n", left)

# right join
right = employees.merge(departments, on="DepartmentID", how="right")
print("Right join\n", right)

# outer join - all unique DepartmentID
outer = employees.merge(departments, on="DepartmentID", how="outer")
print("Outer join\n", outer)

# exercise - ethnicity
tabel_etnii = pd.read_csv("res/Ethnicity.csv", index_col=0)
# nan_replace()

variabile_etnii = list(tabel_etnii.columns)[1:]

# population by ethnicity at county level
localitati = pd.read_excel("res/CoduriRomania.xlsx", index_col=0)

print(tabel_etnii)
print(localitati)

# when the merge criterion is the index, not a specific column:
t1 = tabel_etnii.merge(right=localitati, right_index=True, left_index=True)
print(t1)

g1 = t1[variabile_etnii + ["County"]].groupby(by="County").agg(sum)
print(g1)
g1.to_csv("res/output_etnii_judete.csv")

# population by ethnicity at region level
judete = pd.read_excel("res/CoduriRomania.xlsx", index_col=0, sheet_name="Judete")
t2 = g1.merge(right=judete, right_index=True, left_index=True)

g2 = t2[variabile_etnii + ["Regiune"]].groupby(by="Regiune").agg(sum)
print(g2)
g2.to_csv("res/output_etnii_regiuni.csv")

# population by ethnicity at macro-region level
regiuni = pd.read_excel("res/CoduriRomania.xlsx", index_col=0, sheet_name="Regiuni")
t3 = g2.merge(right=regiuni, right_index=True, left_index=True)

g3 = t3[variabile_etnii + ["MacroRegiune"]].groupby(by="MacroRegiune").agg(sum)
print(g3)
g3.to_csv("res/output_etnii_macroregiuni.csv")

# diversity indices
