import numpy as np
import pandas as pd


# sa se creeze un dictionar cu 6 chei de forma 'var1', 'var2', ...
# avand ca valori asociate acestora liste a cate 7 numere aleatoare in intervalul [0, 1],
# utilizand dictionary comprehension
print(type(np.random.rand(6)), np.random.rand(6))
print(type(range(6)), range(6))

# dict_1 = {'var'+str(j+1): np.random.rand(6) for j in range(6)}
# dict_1 = {'var'+str(j+1): [x for x in np.random.rand(6)] for j in range(6)}
dict_1 = {'var'+str(j+1): list(np.random.rand(6)) for j in range(6)}
print(dict_1)

df_1 = pd.DataFrame(data=dict_1)
print(df_1)

print(type(df_1.columns), df_1.columns)
print(type(list(df_1.columns)), list(df_1.columns))

print(type(df_1.index), df_1.index)
print(type(list(df_1.index)), list(df_1.index))

print(type(df_1.values), df_1.values)

df_2 = pd.DataFrame(data=np.random.rand(6)) # un DataFrame cu o singura coloana
print(df_2)

# etichetati liniile in forma 'rand1', 'rand2', ...
etichete_linii = ('rand'+str(i+1) for i in range(6))
print(type(etichete_linii), etichete_linii)

# df_3 = pd.DataFrame(data=dict_1, index=['rand'+str(i+1) for i in range(6)])
# df_3 = pd.DataFrame(data=dict_1, index=etichete_linii)
df_3 = pd.DataFrame(data=dict_1, index=('rand'+str(i+1) for i in range(6)))
print(df_3)

# creare numpy.ndarray cu 2 dimensiuni dintr-unul cu 1 dimensiune
vector = np.random.rand(30)
print(type(vector), vector)
print('tip de data a unui element din masiv: ', type(vector[0]))
print('nr. de octeti pe care este reprezentat un element al masivului: ', vector.itemsize)

# matricea generata pe linii
nda_1 = np.ndarray(shape=(6, 4), buffer=vector, dtype=float,
                   offset=3*vector.itemsize,
                   order='C') # 'C' (Continuu), 'F' (Fortran), 'A' (Any)
print(nda_1)

# matricea generata pe coloane
# nda_2 = np.ndarray(shape=(6, 4), buffer=vector, dtype=float,
#                    order='F') # 'C' (Continuu), 'F' (Fortran), 'A' (Any)
# print(nda_2)


# sa se creeeze un pandas.DataFrame dintr-un numpy.ndarray cu 2 dimensiuni
df_4 = pd.DataFrame(data=nda_1, index=('obs'+str(i+1) for i in range(6)),
                    columns=('col'+str(j+1) for j in range(4)))
print(df_4)

df_5 = pd.read_csv('FisierIN.csv', sep=',', index_col=3)
print(df_5)
print(df_5.values)

df_5.to_csv('FisierOUT.csv')