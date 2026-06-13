import pandas as pd
import functii as f
import acp.ACP as acp
import grafice as g


tabel = pd.read_csv('./dataIN/Teritorial.csv', index_col=0)
#print(tabel)

#selectare coloane utile
numeVar = tabel.columns[1:]
#print(numeVar)

#creare lista etichete observatii
numeObs = tabel.index.values
#print(numeObs)

#initializare numar variabile
m = numeVar.shape[0];
#print(m)

#initializare numar observatii
n = len(numeObs)
#print(n)

#creare matrice model ca numpy.ndarray
X = tabel[numeVar].values
#print(X)

#standardizare valori variabile cauzale
Xstandardizat = f.standardizare(X)
print(Xstandardizat.shape)

#salvati in fisier CSV matricea X standardizata
Xstandardizat_df = pd.DataFrame(data=Xstandardizat,
                                index=numeObs,
                                columns=numeVar)
Xstandardizat_df.to_csv('./dataOUT/Xstandardizat.csv')

#instantiere clasa ACP
modelACP = acp.ACP(Xstandardizat)

valProp = modelACP.getValoriProprii()
g.componentePrincipale(valoriProprii=valProp)
g.afisare()
