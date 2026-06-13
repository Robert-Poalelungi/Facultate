import numpy as np
import pandas as pd
import matplotlib.pylab as plt

# pandas = a library built on top of numpy designed for tabular computations (rows and columns)
# it provides 2 main data structures:
# - Series - unidimensional data (a column in a file sheet)
# - DataFrame - bidimensional data (actually the entire sheet)

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

df = pd.DataFrame({
    'Name' : ['Alice', 'Bob', 'Carol'],
    'Age' : [32, 29, 25],
    'Salary' : [4000, 3500, 6000]
})

df = pd.read_csv('res/employees.csv', index_col=0)

# properties on the dataframe
print('DF head\n', df.head()) # first 5 rows
print('DF tail\n', df.tail()) # last 5 rows
print('DF info\n', df.info()) # structure of the dataframe: data types, null values
print('DF describe\n', df.describe()) # basic statistics per columns about your dataframe
print('DF shape', df.shape)
print('DF columns', df.columns)
print('DF index', df.index)

# data access - to access data you use the indexing operator [rows , columns]
# read columns
ages = df["Age"]

columns = ["Name", "Salary"]
subset = df[columns] # df[["Name", "Salary"]]

# read rows by index position | iloc - index location
fr = df.iloc[0] # first row. when using index values, they start from 0
ftr = df.iloc[0:3] # first three rows

# read rows by labels
# maybe the more intuitive way
# label1 = df.loc['Eva']
# label2 = df.loc['Carol':'Ivy', ["ID", "Salary"]]

label1 = df.loc[1]
label2 = df.loc[1:3, ["Name", "Salary"]]

# boolean filtering
f1 = df[df["Age"] > 30]
f2 = df[(df["Salary"] > 6000) & (df["Age"] < 40)]

# modify data
df["TaxedSalary"] = df["Salary"] * 0.9 # add a new column

df.rename(columns={'Salary':'GrossSalary'}, inplace=True)
df.rename(columns={'GrossSalary':'Salary'}, inplace=True)

df.drop(columns=['TaxedSalary'], inplace=True)
df.drop(index=[1], inplace=True)

# data sanitization = handling missing values
# when considering data you would be in one of the 2 cases:
# 1 - you deal with numerical data
# 2 - you deal with categorical data (strings)

# strategies for data sanitization:
# for numerical data: your either use the mean (average) of the column to replace missing values,
#                       or you just use a convenient value
# for categorical data: you either use the mode (the most frequently met value) of the column,
#                        or you just use a convenient value

missing = df.isna().sum()

# one strategy - replacing values
df.fillna(0)

replacement = df["Salary"].mean()
df["Salary"].fillna(replacement, inplace=True)

# alternative strategy
df.dropna() # drop any row that has NaN values. df.dropna(axis=0)
df.dropna(axis=1) # drop any column that has NaN values

# transforming data
# vectorized
df["AgeInMonths"] = df["Age"] * 12

# lambda and apply
# def return_bracket(x):
#     if x > 6000:
#         return "High"
#     return "Low"
# df["IncomeBracket"] = df["Salary"].apply(return_bracket)
df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# using string functions
df["Name"] = df["Name"].str.upper()

# statistics