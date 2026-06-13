import numpy as np
import grafice as g
import pandas as pd


# sa creeze o matrice de valori aleatoare
vector = np.random.rand(180) # masiv de numere aleatoare in intervalul [0, 1]
nda_1 = np.ndarray(shape=(6, 4), buffer=vector, dtype=float,
                   order='C')
print(nda_1)

# calcul matricei de corelatie
corel = np.corrcoef(x=nda_1, rowvar=False) # avem variabilele pe coloane
print(corel)

# crearea corelogramei din numpy.ndarray
# g.corelograma(matrice=corel, dec=2, titlu='Corelograma din numpy.ndarray')
print('nr. elemente pe dimensiunea 1 a unui ndarray: ', corel.shape[0])
print('nr. elemente pe dimensiunea 2 a unui ndarray: ', corel.shape[1])
df_corel = pd.DataFrame(data=corel, index=('X'+str(i+1) for i in range(corel.shape[0])),
                        columns=('X'+str(j+1) for j in range(corel.shape[1])))
# creare corelograma din pandas.DataFrame
# g.corelograma(matrice=df_corel, dec=1, titlu='Corelograma din pandas.DataFrame')

# g.cerculCorelatiilor(matrice=corel, etichetaX='Variabila 1', etichetaY='Variabila 2')
g.cerculCorelatiilor(matrice=corel)
g.afisare()