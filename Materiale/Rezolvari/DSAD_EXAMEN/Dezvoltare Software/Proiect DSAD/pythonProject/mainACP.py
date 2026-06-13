import pandas as pd
import acp.ACP as acp
import grafice as g


tabel = pd.read_csv('dataIN/Date.csv', index_col=0)
print(tabel)

obsNume = tabel.index[:]
print(obsNume)
varNume = tabel.columns[1:]
print(varNume)
# X = tabel.values[:, 1:]

X = tabel[varNume].values
# print(X)  # avem un 2D numpy.ndarray

# instantiere obiect ACP
acpModel = acp.ACP(X)
Xstd = acpModel.getXstd()
# salvare in fisier CSV a matricei initiale standardizate
Xstd_df = pd.DataFrame(data=Xstd, index=obsNume, columns=varNume)
Xstd_df.to_csv('dataOUT/Xstd.csv')

# creare grafic valori proprii
valProp = acpModel.getValProp()
print(valProp)
g.componentePrincipale(valoriProprii=valProp)
# g.afisare()
componente = ['C'+str(j+1) for j in range(varNume.shape[0])]

# corelograma matricei de corelatie a variabilelor initiale
R = acpModel.getR()
R_df = pd.DataFrame(data=R, index=varNume, columns=varNume)
g.corelograma(matrice=R_df, dec=2, titlu='Corelograma matricei de corelatie a variabilelor observate')
#g.afisare()

# salvare componente principale in fisier CSV
C = acpModel.getCompPrin()
C_df = pd.DataFrame(data=C, index=obsNume, columns=componente)
C_df.to_csv('dataOUT/ComponentePricipale.csv')

# crearea corelogramei factorilor de corelatie
Rxc = acpModel.getFactoriCorelatie()
Rxc_df = pd.DataFrame(data=Rxc, index=varNume, columns=('C'+str(j+1) for j in range(varNume.shape[0])))
# salvare matrice factor loadings in fisier CSV
Rxc_df.to_csv('dataOUT/FactoriCorelatie.csv')
g.corelograma(matrice=Rxc_df, dec=2, titlu='Corelograma factorilor de corelatie')
# g.afisare()

# creare cerc al corelatiilor pentru componentele 1 si 2
g.cerculCorelatiilor(matrice=Rxc_df, titlu='Distributia variabilelor observate in spatiul componentelor C1 si C2')
# g.afisare()

scoruri = acpModel.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri, index=obsNume, columns=componente)
# salvare scoruri in fisier CSV
# TO DO
# creare corelograma scoruri
g.corelograma(matrice=scoruri_df, dec=2, titlu='Corelograma scorurilor (componentele principale standardizate)')
# g.afisare()

# creare corelograma a calitatii reprezentarii observatiilor pe axele componentelor principale
calObs = acpModel.getCalObs()
# salvare calitatea reprezentarii observatiilor in fisier CSV
# TO DO
calObs_df = pd.DataFrame(data=calObs, index=obsNume, columns=componente)
g.corelograma(matrice=calObs_df, dec=2, titlu='Corelograma calitatii reprezentarii observatiilor pe axele componentelor principale')
# g.afisare()

# creare corelograma betha
betha = acpModel.getBetha()
# salvare betha in fisier CSV
# TO DO
betha_df = pd.DataFrame(data=betha, index=obsNume, columns=componente)
g.corelograma(matrice=betha_df, dec=2, titlu='Corelograma contributiei observatiilor la varianta axelor componentelor principale')
# g.afisare()

# creare corelograma comunitati
comunitati = acpModel.getComun()
comunitati_df = pd.DataFrame(data=comunitati, index=varNume, columns=componente)
g.corelograma(matrice=comunitati_df, dec=2, titlu='Corelograma comunitatilor')
g.afisare()
