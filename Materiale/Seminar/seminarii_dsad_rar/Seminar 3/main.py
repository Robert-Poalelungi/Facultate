import numpy as np
import pandas as pd

# Nu exista tuple comprehension in Python
patrate = (x for x in range(1, 11))
print(patrate)

# un generator este un mecanisc prin care
# sunt generate calori in secta la runtime
# nu sunt stocate valorile in memorie, ci adresa de inceput a generatorului
for patrat in patrate:
    print(patrat)

# expresii lambda
media = lambda a, b: (a + b) / 2
print(media(2, 3))

# media valorilor unui vector
mediaVector = lambda vector: np.mean(vector)
print(mediaVector([1, 2, 3, 4]))

print(
    "\n\n---------------------------------------------------PANDAS--------------------------------------------------\n\n")

# sa se creeze un dictionar cu chei de forma S1, S2, ..., S6
# si valori de forma unor liste de 5 elemente intregi aleatoare in [1, 10]
dictionarStudenti = {'S' + str(k):
                         [v for v in np.random.randint(1, 11, 5)]
                     for k in range(6)}
print(dictionarStudenti)

# Cu pandas
print("Conversia dictionarului intr-un dataFrame pandas")
dataFrame = pd.DataFrame(data=dictionarStudenti)
print(dataFrame)

# extragere etichete linii
print(dataFrame.index)

# Extragere etichete coloane
print(dataFrame.columns)

# creati o matrice (6, 4) cu intregi in [1, 10]
matrice1 = np.random.randint(1, 11, (6, 4))
print(matrice1)

vector1 = np.random.randint(1, 11, 30)
print(vector1)

# creare ndarray de dimensiuni multiple dintru-un ndarray unidimensional
nda = np.ndarray(shape=(6, 4), buffer=vector1, dtype=int, offset=2 * vector1.itemsize, order='C')
print(nda)

# creare pandas.DataFrame din numpy.ndarray
dataFrame2 = pd.DataFrame(data=matrice1)
print(dataFrame2)

dataFrame3 = pd.DataFrame(data=nda,
                          index=['L' + str(i) for i in range(6)],
                          columns=('C' + str(j + 1) for j in range(4)))
print(dataFrame3)

# acces la valori pentru etichete de linii si coloane ca ndarray
print(dataFrame3.index.values)

# accesare valori in pandas.DataFrame(linia 3, coloana 2)
print(dataFrame3['C2'].iloc[2])
print(dataFrame3['C2'].loc['L2'])
print(dataFrame3['C2']['L2'])

# extragere submatrice utilizand list slicing
print(dataFrame3.iloc[1: 4].iloc[1: 3])
print(dataFrame3.iloc[1: 4, 1: 3])
