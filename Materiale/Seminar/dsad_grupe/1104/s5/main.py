import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# pandas is a library built on top of numpy, designed for tabular data (rows and columns,
# excel file sheet)
# pandas exposes 2 main data types:
# 1. Series - for unidimensional data (a column in a table)
# 2. DataFrame - for bidimensional data (the actual table)

s = pd.Series([10,20,30], index=['a', 'b', 'c'])

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Carol'],
    'Age': [27, 33, 29],
    'Salary': [5000, 4900, 5100]
})

df = pd.read_csv('employees.csv', index_col=1)

# properties on data frame
print('DF head\n', df.head()) # first 5 rows
print('DF tail\n', df.tail()) # last 5 rows
print('DF info\n', df.info()) # details about the DF structure: data types, null values
print('DF describe\n', df.describe()) # descriptive statistics about columns
print('DF shape', df.shape) # (rows, columns)
print('DF columns', df.columns) # an object containing a list of column names
print('DF index', df.index) # an object containing a list of row references

# data access - is done using the indexing operator [rows , cols]
# read data by columns
ages = df["Age"] # read an entire column

# remove_columns = ["Name", "Salary"]
# subset = df[df.columns - remove_columns]
subset = df[["Age", "Salary"]]

# read data by rows using index values | iloc - index location
fr = df.iloc[0] # first row
ftr = df.iloc[0:3] # first 3 rows

# read data by rows using labels | loc
label1 = df.loc['Bob']
label2 = df.loc['Eva':'Ivy', ["Age", "Salary"]]

print(label1)
print(label2)

# data changes
df["TaxedSalary"] = df["Salary"] * 0.9

df.rename(columns={'Salary':'GrossSalary'}, inplace=True)
df.rename(columns={'GrossSalary':'Salary'}, index={'Bob':'Tim'}, inplace=True)
print(df)

df.drop(columns=["TaxedSalary"], inplace=True) # drop columns
df.drop(index=["Tim"], inplace=True) # drop rows

# data sanitization = cleaning the data
# usually, you deal with either
# 1 - numerical data or
# 2 - categorical data (strings)
# and data sanitization involves either deleting rows or columns, or providing a convenient
# substitution:
# 1 - for numerical data, you either use the mean (average) of the column,
#       or other specific value relevant in that context
# 2 - for categorical data, you either use the mode (the most frequently met value) of the column,
#       or other specific value relevant in that context

missing = df.isna().sum()

df.fillna(0)

value = df["Salary"].mean() # for categorical data df["Gender"].mode()
df["Salary"].fillna(value, inplace=True)

# transformations
# vectorized
df["AgeInMonths"] = df["Age"] * 12

# lambda and apply
def return_bracket(x):
    if x > 6000:
        return "High"
    return "Low"
df["IncomeBracket"] = df["Salary"].apply(return_bracket)
df["IncomeBracket"] = df["Salary"].apply(lambda x: "High" if x > 6000 else "Low")

# methods from string class
df["Gender"] = df["Gender"].str.lower()

print(df)

# statistics