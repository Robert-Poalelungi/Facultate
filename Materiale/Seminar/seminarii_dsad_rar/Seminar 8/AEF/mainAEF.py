import numpy as np
import pandas as pd
import utile as utl
import aef.AEF as aef
import factor_analyzer as fa
import grafice as g
from sklearn.preprocessing import StandardScaler


tabel = pd.read_csv('dataIN/MortalityEU.csv', index_col=0, na_values=':')
print(tabel)

obsNume = tabel.index.values
varNume = tabel.columns.values
matrice_numerica = tabel.values

#inlocuire valori lipsa
X = utl.inlocuireNAN(matrice_numerica)
X_df = pd.DataFrame(data = X, index=obsNume, columns=varNume)
X_df.to_csv('./dataOUT/X.csv')

#calculam testul de sfericitate Bartlett
sfericitateBartlett = fa.calculate_bartlett_sphericity((X_df))
print(sfericitateBartlett)
if sfericitateBartlett[0] > sfericitateBartlett[1]:
    print('Exista cel putin un factor comun')
else:
    print('Nu exista factor comun')
    exit(-1)

#calcul indici de factorabilitatea a variabilelor intitale Kaise-Meyer-Olkin(KMO)
kmo = fa.calculate_kmo(X_df)
print(kmo)
if kmo[1] > 0.5:
  print('Variabilele observate pot fi exprimate prin cel putin un factor comun')
else:
    print('Variabilele observate nu pot fi exprimate prin cel putin un factor comun')
    exit(-2)

vector = kmo[0]
print(vector)
matrice = vector[:, np.newaxis]
print(matrice)
matrice_df = pd.DataFrame(data=matrice, index=varNume,
                          columns=['indici KMO'])
matrice_df.to_csv('./dataOUT/KMO.csv')

#creare corelograma indici KMO
g.corelograma(matrice=matrice_df, titlu="corelograma indicilor KMO")
#g.afisare()

#extragere numarul semnificativ de factori comuni
nrFacturoSemnificativi = 1
chi2TabMin = 1
for k in range(1, varNume.shape[0]):
    modelFA = fa.FactorAnalyzer(n_factors=k)
    modelFA.fit(X_df)
    factoriComuni = modelFA.loadings_ #extragere factori comuni
    factoriSpecifici = modelFA.get_uniquenesses() #extragere factori specifici
    print(factoriComuni)
    print(factoriSpecifici)

    #apel test Bartlett
    modelAEF = aef.AEF(X)
    chi2Calc, chi2Tab = modelAEF.calculTestBartlett(factoriComuni, factoriSpecifici)
    print(chi2Calc, chi2Tab)

    modelFA.get_eigenvalues()

    if np.isnan(chi2Calc) or np.isnan(chi2Tab):
        break
    if chi2Tab < chi2TabMin:
        chi2TabMin = chi2Tab
        nrFacturoSemnificativi = k

print('Numar factori seminficativi ', nrFacturoSemnificativi)
print()

