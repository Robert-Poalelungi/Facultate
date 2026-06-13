import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer,calculate_kmo,calculate_bartlett_sphericity
from seaborn import heatmap
from sklearn.preprocessing import StandardScaler

rawDiversitate=pd.read_csv('./dateIN/Diversitate.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/Coduri_Localitati.csv',index_col=0)
labels=list(rawDiversitate.columns.values[1:])

merged=rawDiversitate.merge(rawCoduri,right_index=True,left_index=True).drop('Localitate_y',axis=1).rename(columns={'Localitate_x':'Localitate'})[['Judet','Localitate']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(merged)

#1
merged[(merged[labels] == 0).any(axis=1)][['Localitate'] + labels].to_csv('./dateOUT/Central.csv')
#2
merged['Mean_Diversity'] = merged[labels].mean(axis=1)
max_diversity_localities = merged.loc[merged.groupby('Judet')['Mean_Diversity'].idxmax()]
print(max_diversity_localities)
max_diversity_localities[['Judet', 'Localitate', 'Mean_Diversity']].to_csv('./dateOUT/Cerinta2_2025.csv')

#B1
x=StandardScaler().fit_transform(merged[labels])
bartlett_stat,bartlett_p=calculate_bartlett_sphericity(x)
print(bartlett_p)
if bartlett_p>0.001:
    print('Nu exista factori comuni semnificativi')
    exit(0)
kmo_all,kmo=calculate_kmo(x)
if kmo<0.6:
    print('Analiza factorilor nu este recomandata')
    exit(0)

efa=FactorAnalyzer(n_factors=x.shape[1]-1,rotation='varimax')

scores=efa.fit_transform(x)
factorLoadings=efa.loadings_
#fara rotatie
eigenvalues=efa.get_eigenvalues()
explained_variance_percent=(eigenvalues[0]/np.sum(eigenvalues[0]))*100 #procent din variatia explicata
cum_variance=np.cumsum(explained_variance_percent) #variatia cumulata
efa_df=pd.DataFrame(data={
    'Varianta factorilor':eigenvalues[0],
    'Procent din varianta extrasa':explained_variance_percent,
    'Varinata cumulata':cum_variance
}).to_csv('./dateOUT/Varianta.csv',index=False)

#cu rotatie
varianta_fact,proc_var_extrasa,proc_var_cum=efa.get_factor_variance() # tuplu cu cele 3 valori cerute
print(varianta_fact,proc_var_extrasa,proc_var_cum)
df_varianta=pd.DataFrame(data={
    'Varianta factorilor': varianta_fact,
    'Procentul de varianta extrasa': proc_var_extrasa * 100,
    'Procentul de varianta cumulat': proc_var_cum *100
}).to_csv('./dateOUT/Varianta.csv',index=False)

#B2
print(factorLoadings)
loadings_df=pd.DataFrame(data=factorLoadings,index=labels).to_csv('./dateOUT/r.csv')

#B3
plt.figure(figsize=(8,8))
plt.title("Cercul de corelatie pentru primii 2 factori comuni")
T=np.arange(0,np.pi*2,0.01)
X=np.cos(T)
Y=np.sin(T)
plt.plot(X,Y)
plt.axhline(0,c='g')
plt.axvline(0,c='g')
plt.scatter(factorLoadings[:,0],factorLoadings[:,1])
for i in range(factorLoadings.shape[0]):
    plt.text(factorLoadings[i,0],factorLoadings[i,1],labels[i],fontsize=12,ha='right')


plt.show()

#corelograma corelatii factoriale
plt.figure(figsize=(15, 11))
plt.title('Correlogram')
heatmap(data=factorLoadings, vmin=-1, vmax=1, cmap='bwr', annot=True,xticklabels=labels,yticklabels=labels)
plt.xlabel('Factori')
plt.ylabel('Variabile')
plt.show()

#corelograma intre comunalitati si factori specifici
communalities = efa.get_communalities()
specificFactors = efa.get_uniquenesses()
df_comunalitati_varianta = pd.DataFrame({
    'Comunalități': communalities,
    'Varianță specifică': specificFactors
}, index=labels)  # Folosim labels pentru index

plt.figure(figsize=(10, 6))  # Ajustăm dimensiunea figurii
plt.title('Corelogramă - Comunalități și varianță specifică')

heatmap(data=df_comunalitati_varianta, cmap='viridis', annot=True)  # cmap='viridis' sau alt cmap potrivit

plt.show()
#trasare plot scoruri
plt.figure(figsize=(8, 8))
plt.title('Scatter plot al scorurilor factoriale (PC1 vs PC2)')
plt.xlabel('Componenta Principală 1')
plt.ylabel('Componenta Principală 2')
plt.scatter(scores[:, 0], scores[:, 1])  # Folosim primele două componente
plt.show()

#C
eigenvector=pd.read_csv('./dateIN/a.csv',header=None).values
# print(eigenvector)
eigenV=np.array([3.019, 1.2203, 0.6536, 0.102, 0.005])
explained_variance_pc1_pc2=(eigenV[0]+eigenV[1])/np.sum(eigenV)
communalities=np.sum(eigenvector[:,:2]**2,axis=1)
high_communalities_variables=np.where(communalities>0.9)[0]

variable_labels=['X' + str(i+1) for i in high_communalities_variables]
print(variable_labels)