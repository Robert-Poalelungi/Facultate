import numpy as np
import pandas as pd
from functii import *
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

set_date=pd.read_csv('mortalitate_ro.csv',index_col=1)
valori_lipsa=set_date.isna().any().any()
if valori_lipsa:
    nan_replace(set_date)
variabile=set_date.copy()
variabile=variabile.drop(columns=["Judet"])

#Standardizare
set_date_standardizat=((variabile.values-np.mean(variabile.values,axis=0))/np.std(variabile.values,axis=0))

#Model ACP
acp_model=PCA()
acp_model.fit(set_date_standardizat)
componente=acp_model.components_

#Varianta
varianta_explicata=acp_model.explained_variance_
varianta_explicata_ratio=acp_model.explained_variance_ratio_

#Corelatii
corelatii_fact=np.corrcoef(set_date_standardizat.T,componente.T,rowvar=False)
corelatii_fact=corelatii_fact[:variabile.shape[1],variabile.shape[1]:]

#Contributii
contributii=varianta_explicata*100

#Calcul componente si/sau scoruri
componenta_1=componente[:,0]
componenta_2=componente[:,1]
salvare(componenta_1)

# Calcul scoruri folosind metoda transform
scoruri = acp_model.transform(set_date_standardizat)
salvare(scoruri,out="scoruri.csv")

#Comunalitati
comunalitati=1-varianta_explicata/np.var(set_date_standardizat,axis=0)

#Cosinusuri
loadings=componente.T*np.sqrt(varianta_explicata)
cosinusuri=loadings/np.sqrt(np.sum(loadings**2),axis=0)
