import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer, calculate_kmo,calculate_bartlett_sphericity
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from seaborn import heatmap



rawDiversitate=pd.read_csv('./dateIN/Diversitate.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/Coduri_Localitati.csv',index_col=0)
labels=list(rawDiversitate.columns.values[1:])

merged=rawDiversitate.merge(rawCoduri,right_index=True,left_index=True).drop('Localitate_y',axis=1).rename(columns={'Localitate_x':'Localitate'})[['Judet','Localitate']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(merged)

# EFA
# standardizare
x=StandardScaler().fit_transform(merged[labels])
bartlett_stat,bartlett_p=calculate_bartlett_sphericity(x)

# test bartlett de relevanta - analiza factorabilitatii
if bartlett_p>0.001:
    print('Nu exista factori comuni semnificativi')
    exit(0)

# KMO pt a verifica daca datele sunt potrivite pt EFA - analiza factorabilitatii
kmo_all,kmo=calculate_kmo(x)
if kmo< 0.6:
    print("Indicele KMO este prea mic. Analiza factoriala NU este recomandata")
    exit(0)

# daca vrem fara rotatie => rotation=None
efa=FactorAnalyzer(n_factors=x.shape[1]-1,rotation='varimax') # x.shape[1] =  nr de coloane
print(x.shape)

# calcul scoruri factoriale
scores=efa.fit_transform(x) # antreneaza modelul EFA pe datele x dar si returneaza „scorurile factorilor”
# daca nu ne cere scorurile la vreo cerinta => putem folosi efa.fit() pt a antrena modelul
df_scores=pd.DataFrame(scores,columns=["Factor_"+str(i) for i in range (scores.shape[1])], index=merged['Localitate'])
df_scores.to_csv('./dateOUT/EFA_scoruri.csv')

# plot scoruri factoriale - graficul scorurilor fact pt 2 factori (ex f0 si f1)
# scatter plot !!
plt.figure(figsize=(12,12))
plt.scatter(scores[:,0],scores[:,1],color='blue')
plt.title('Graficul scorurilor pentru primii 2 factori')
plt.xlabel('Factor 1')
plt.ylabel("Factor 2")
plt.axhline(0,c='black')
plt.axvline(0,c='black')
for i,ind in enumerate(merged['Localitate']):
    plt.annotate(ind,(scores[i,0],scores[i,1]))
plt.show()

# varianta factori comuni (varianta, procentul de varianta extrasa, procentul cumulat de varianta)
varianta_fact,proc_var_extrasa,proc_var_cum=efa.get_factor_variance() # tuplu cu cele 3 valori cerute
print(varianta_fact,proc_var_extrasa,proc_var_cum)
df_varianta=pd.DataFrame(data={
    'Varianta factorilor': varianta_fact,
    'Procentul de varianta extrasa': proc_var_extrasa * 100,
    'Procentul de varianta cumulat': proc_var_cum *100
}).to_csv('./dateOUT/EFA_Varianta.csv',index=False)

# corelatiile factoriale
factor_loadings=efa.loadings_
df_factor_loadings=pd.DataFrame(factor_loadings,index=labels).to_csv('./dateOUT/EFA_cor_fact.csv')

# corelograma corelatii factoriale
plt.figure(figsize=(15, 11))
plt.title('Corelograma corelatiilor factoriale')
heatmap(data=factor_loadings, vmin=-1, vmax=1, cmap='bwr', annot=True,xticklabels=labels,yticklabels=labels)
plt.xlabel('Factori')
plt.ylabel('Variabile')
plt.show()

print(df_scores.var())

# cercul corelatiilor pt 2 factori
plt.figure(figsize=(8,8))
plt.title("Cercul de corelatie pentru primii 2 factori comuni")
T=np.arange(0,np.pi*2,0.01)
X=np.cos(T)
Y=np.sin(T)
plt.plot(X,Y)
plt.axhline(0,c='g')
plt.axvline(0,c='g')
plt.scatter(factor_loadings[:,0],factor_loadings[:,1])
for i in range(factor_loadings.shape[0]):
    plt.text(factor_loadings[i,0],factor_loadings[i,1],labels[i],fontsize=12,ha='right')

plt.show()

# calcul comunalitati si varianta specifica
communalities=efa.get_communalities() # cat din variabila este explicat de factori
print(communalities)

specificFactors = efa.get_uniquenesses()  # cat din varianta variabilei nu e explicat de factori
print(specificFactors)

df_comunalitati_varianta = pd.DataFrame({
    'Comunalități': communalities,
    'Varianță specifică': specificFactors
}, index=labels)  # Folosim labels pentru index
df_comunalitati_varianta.to_csv('./dateOUT/EFA_comunalitati_varianta_specifica.csv')

# corelograma comunalitati si varianta specifica
plt.figure(figsize=(10, 6))
plt.title('Corelogramă - Comunalități și varianță specifică')
heatmap(data=df_comunalitati_varianta, cmap='viridis', annot=True)
plt.show()



