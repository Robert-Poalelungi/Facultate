import pandas as pd
import numpy as np
import copy
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,cohen_kappa_score
import matplotlib.pyplot as plt
from seaborn import kdeplot

buget = pd.read_csv('dataIN/Buget.csv')
popultatie = pd.read_csv('dataIN/PopulatieLocalitati.csv')

t1 = copy.copy(buget)
t1.insert(15,'Venituri',True)
t1.insert(16,'Cheltuieli',True)

venituri = ['V1', 'V2', 'V3', 'V4', 'V5']
cheltuieli = ['C1', 'C2', 'C3','C4', 'C5', 'C6', 'C7', 'C8']

t1['Venituri'] = 0
for venit in venituri:
    t1['Venituri'] = t1['Venituri'] + t1[venit]

t1['Cheltuieli'] = 0
for cheltuiala in cheltuieli:
    t1['Cheltuieli'] = t1['Cheltuieli'] + t1[cheltuiala]

t2 = t1[['Siruta', 'Localitate','Venituri','Cheltuieli']]
cerinta1 = t2.reset_index(drop=True)
cerinta1.to_csv('dataOUT/Cerinta1_Verif.csv',index=False)

data_merge = pd.merge(buget,popultatie,on='Siruta')
date_jud = data_merge[['Judet']+venituri+['Populatie']]\
    .groupby(by='Judet').agg(sum)
t3 = copy.copy(date_jud)
for venit in venituri:
    t3[venit] = t3[venit]/t3['Populatie']

cerinta2 = copy.copy(t3)
del cerinta2['Populatie']
cerinta2 = cerinta2.sort_values(by='V1',ascending=False)
cerinta2.to_csv('dataOUT/Cerinta2_Verif.csv')

#ADL:
tabel_invatare_testare = pd.read_csv('dataIN/Pacienti.csv')
t2 = pd.read_csv('dataIN/Pacienti_apply.csv')

variabile = list(tabel_invatare_testare)
predictori = variabile[1:7]
tinta = variabile[-1]

x_train, x_test, y_train, y_test = train_test_split(
    tabel_invatare_testare[predictori],
    tabel_invatare_testare[tinta],test_size=0.4)

modelADL = LinearDiscriminantAnalysis()
modelADL.fit(x_train,y_train)

#Predictie in setul de date:
predictie_ADL_test = modelADL.predict(x_test)
predictie_ADL_test_df = pd.DataFrame(data={"Predictii:":predictie_ADL_test},
                                     index=x_test.index)
predictie_ADL_test_df.to_csv('dataOUT/predict.csv')

#Evaluare model liniar(matricea de confuzie + indicatori de acuratețe)
def calcul_matrici(y,y_,clase):
    c = confusion_matrix(y,y_)
    print(c)
    tabel_c = pd.DataFrame(c,clase,clase)
    print(tabel_c)
    tabel_c['Acuratete'] = np.round(np.diag(c)*100/np.sum(c,axis=1),3)
    print(tabel_c)

clase = modelADL.classes_
matrice_ADL = calcul_matrici(y_test,predictie_ADL_test,clase)
print(matrice_ADL)

#Graficul distributiei in axele discriminante
def plot_distributii(scoruri,y,i=0):
    fig = plt.figure(figsize=(11,8))
    ax = fig.add_subplot(1,1,1)
    assert isinstance(ax,plt.Axes)
    ax.set_title("Distributie in axa discriminanta "+str(i+1),
                 fontsize=11,color='b')
    kdeplot(x=scoruri[:,i],hue=y,fill=True,ax=ax)
    plt.show()

scoruri_test = modelADL.transform(x_test)
q = len(clase)
m = q - 1
for i in range(m):
    plot_distributii(scoruri_test,y_test,i)





