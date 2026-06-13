import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

set_date=pd.read_csv("Industrie.csv",index_col=0)

def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if t[v].isna().any():
            t[v].fillna(t[v].mean(),inplace=True)
        else:
            t[v].fillna(t[v].mode()[0],inplace=True)

def salvare(x,linii=None,coloane=None,out="out.csv"):
    t=pd.DataFrame(x,linii,coloane)
    t.to_csv(out)

valori_lipsa=set_date.isna().any().any()
if valori_lipsa:
    nan_replace(set_date)

variabile=list(set_date)
variabile_numerice=variabile[1:]
date_numerice=set_date[variabile_numerice].values

#Cerinta1
set_populatie=pd.read_csv("PopulatieLocalitati.csv",index_col=0)
variabile_pop=list(set_populatie)
variabile_numerice_pop=variabile_pop[2:]
date_numerice=set_populatie[variabile_numerice_pop].values
tabel_=set_date.merge(set_populatie,left_index=True,right_index=True)
categorii=["Alimentara","Textila","Lemnului","ChimicaFarmaceutica","Metalurgica","ConstructiiMasini","CalculatoareElectronica","Mobila","Energetica"]
for categorie in categorii:
    tabel_[categorie] = tabel_[categorie] / tabel_["Populatie"]
salvare(tabel_[["Localitate_x","Alimentara","Textila","Lemnului","ChimicaFarmaceutica","Metalurgica","ConstructiiMasini","CalculatoareElectronica","Mobila","Energetica"]],out="cerinta1.csv")

#Cerinta2
set_date_fara_populatie = set_populatie.drop("Populatie", axis=1)
tabel2=set_date.merge(set_date_fara_populatie,on=["Siruta","Localitate"]).groupby(by="Judet").agg(sum)
categorie_max=tabel2.idxmax(axis=1)
cifra=tabel2[categorii].max(axis=1)
tabel2["Activitate"]=categorie_max
tabel2["Cifra"]=cifra
salvare(tabel2[["Activitate","Cifra"]],out="cerinta2.csv")

#Cerinta3
set_proiect=pd.read_csv("ProiectB.csv",index_col=0)
variabile=list(set_proiect)
predictori=variabile[:11]
clasa=variabile[11]

x_train,x_test,y_train,y_test=train_test_split(set_proiect[predictori],set_proiect[clasa],test_size=0.4)
lda=LinearDiscriminantAnalysis()
lda.fit(x_train,y_train)
lda_test_scores=lda.decision_function(x_test)
lda_train_scores=lda.decision_function(x_train)
salvare(lda_test_scores,out="z.csv")

#PREDICTIA IN SETUL DE TESTARE
lda_pred_test=lda.predict(x_test)
salvare(lda_pred_test,out="predict_test.csv")

lda_acc=accuracy_score(y_test,lda_pred_test)
lda_conf=confusion_matrix(y_test,lda_pred_test)

#PREDICTIA IN SETUL DE APLICARE
set_apply=pd.read_csv("ProiectB_apply.csv",index_col=0)
lda_predict_apply=lda.predict(set_apply[predictori])

qda=QuadraticDiscriminantAnalysis()
qda.fit(x_train,y_train)
qda_predictions_test=qda.predict(x_test)

qda_conf_matrix_test = confusion_matrix(y_test, qda_predictions_test)
qda_accuracy_test = accuracy_score(y_test, qda_predictions_test)

qda_predic_apply=qda.predict(set_apply[predictori])






