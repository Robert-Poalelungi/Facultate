import pandas as pd
import numpy as np

import grafice

#creati o matrice de (30, 20) de valori aleatoare
#in virgula mobila in intervalul (1, 10)
matrice1 = np.random.uniform(1, 11, (30, 20))

print(matrice1)

#calcul matrice de corelatie
corr1 = np.corrcoef(matrice1,rowvar=False) #consideram ca avem variabile pe coloane
print("\n\n\n\n")

#apel corelograma
#grafice.corelograma(corr1, titlu="Corelograma din numpy.ndarray")

#creare pandas.DataFrame
coloane = ["V" + str(i+1) for i in range(corr1.shape[0])]
df1 = pd.DataFrame(data=corr1,
                   index=coloane, columns=coloane)

print(df1)

#grafice.corelograma(df1, titlu="Corelograma din pandas.dataframe")



#cercul corelatiilor
grafice.cerculCorelatiilor(corr1, titlu="Cercul corelatiilor din numpy.ndarray")

grafice.cerculCorelatiilor(df1, titlu="Cercul corelatiilor din pandas.dataframe")

grafice.afisare()
