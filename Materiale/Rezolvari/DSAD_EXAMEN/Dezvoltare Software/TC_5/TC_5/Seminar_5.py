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
print(df_corel)
# creare corelograma din pandas.DataFrame
# g.corelograma(matrice=df_corel, dec=1, titlu='Corelograma din pandas.DataFrame')

print(len(corel))
print(corel.shape[0])
# crearea cercului corelatiilor din numpy.ndarray
# g.cerculCorelatiilor(matrice=corel, etichetaX='Variabila 1', etichetaY='Variabila 2')
# g.cerculCorelatiilor(matrice=corel)

# crearea cercului corelatiilor din pandas.DataFrame
print(df_corel.iloc[0, 1]) # accesare celulelor din pandas.DataFrame pe baza indicilor de linie si coloana
print(df_corel.loc['X1', 'X2']) # # accesare celulelor din pandas.DataFrame pe baza etichetelor de rand si coloana
print('nr. randuri pandas.DataFrame = ', df_corel.values.shape[0])
print('nr. randuri pandas.DataFrame = ', df_corel.index.shape[0])
print('nr. randuri pandas.DataFrame = ', len(df_corel.index))
# g.cerculCorelatiilor(matrice=df_corel)

# g.componentePrincipale([5.4, 4.3, 2.6, 1.3, 0.93, 0.78, 0.45, 0.23])
# sa se creeze o lista de 25 valori aleatoare in intervalul [0.2, 4.8]

# [0, 1] -> [0.2, 4.8]
def random(a, b, n):
    return (a + np.random.rand(n) * (b - a))

valoriProprii = random(0.2, 4.8, 25)
print(type(valoriProprii), valoriProprii)
valoriProprii.sort()

# g.componentePrincipale(valoriProprii=valoriProprii[-1::-1])

# sa se creeze o matrice (30, 8) cu valori aleatore in intervalul [1.2, 6.9]
g.norPuncte(matrice=corel)
g.afisare()