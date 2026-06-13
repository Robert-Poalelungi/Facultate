import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

set_date_antrenare=pd.read_csv("park.csv",index_col=0)
val_lipsa=set_date_antrenare.isna().any().any()
def nan_replace(t):
    assert isinstance(t,pd.DataFrame)
    for v in t.columns:
        if t[v].isna().any():
            t[v].fillna(t[v].mean(),inplace=True)
        else:
            t[v].fillna(t[v].mode()[0],inplace=True)

if val_lipsa:
    nan_replace(set_date_antrenare)

variabile=list(set_date_antrenare) #toate coloanele mele
predictori=variabile[:-1] #toate coloanele mai putin cea cu status
clasa=variabile[-1] #statusul care e ultimul

x_train,x_test,y_train,y_test=train_test_split(set_date_antrenare[predictori],set_date_antrenare[clasa],test_size=0.4)
lda=LinearDiscriminantAnalysis()
lda.fit(x_train,y_train)

lda_test_scores=lda.decision_function(x_test)
lda_train_scores=lda.decision_function(x_train)

lda_test_prediction=lda.predict(x_test)

lda_confusion_matrix=confusion_matrix(y_test,lda_test_prediction)
lda_accuracy_test=accuracy_score(y_test,lda_test_prediction)

#Aplicare
set_aplicare=pd.read_csv("park_apply.csv",index_col=0)
valori_lipsa_aplicare = set_aplicare.isna().any().any()
if valori_lipsa_aplicare:
    nan_replace(set_aplicare)

lda_predict_aplicat=lda.predict(set_aplicare[predictori])

qda=QuadraticDiscriminantAnalysis()
qda.fit(x_train,y_train)
qda_predict_test=qda.predict(x_test)

qda_confusion_matrix=confusion_matrix(y_test,qda_predict_test)
qda_accuracy_test=accuracy_score(y_test,qda_predict_test)

qda_predict_apply=qda.predict(set_aplicare[predictori])























