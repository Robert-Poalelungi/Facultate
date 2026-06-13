import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from seaborn import kdeplot
from sklearn.naive_bayes import GaussianNB

x=pd.read_csv('./dateIN/Pacienti.csv',index_col=0) # set de testare
x_apply=pd.read_csv('./dateIN/Pacienti_apply.csv',index_col=0) # set de aplicare

tinta='DECISION'
labels_lda=list(x.columns.values[:-1])

dict={'I':1,'S':2,'A':3}
x[tinta]=x[tinta].map(dict)

x_train,x_test,y_train,y_test=train_test_split(x[labels_lda],x[tinta],train_size=0.4)
lda=LinearDiscriminantAnalysis()

# antrenam modelul
lda.fit(x_train,y_train)

# scoruri discriminante
scores=lda.transform(x_train)
print(scores)
pd.DataFrame(data=scores).to_csv('./dateOUT/LDA_scoruri.csv')

# plot instante (scoruri) in axe discriminante (ex:primele 2) => scatter
plt.figure(figsize=(10,6))
plt.title('Instantele in primele 2 axe discriminante')
plt.scatter(scores[:,0],scores[:,1],c=y_train,cmap='viridis',alpha=0.7)
plt.xlabel('Prima axa discriminanta')
plt.ylabel('A doua axa discriminanta')
plt.colorbar(label='Clase')
plt.show()

# plot distributii in axe discriminante => kdeplot
plt.figure(figsize=(8,6))
plt.title('Distributiile in axe discriminante')
kdeplot(scores,fill=True)
# (cred) daca ar fi zis in primele 2 axe: kdeplot(scores[:,:2],fill=True)

# predictii si evaluare
################ MODEL LINIAR ###################

# predictii in setul de testare
predict_test=lda.predict(x_test)

# predictii in setul de aplicare
predict_apply=lda.predict(x_apply)

pd.DataFrame(data=predict_test).to_csv('./dateOUT/LDA_predict_test.csv')
pd.DataFrame(data=predict_apply).to_csv('./dateOUT/LDA_predict_apply.csv')

# evaluare
cm=confusion_matrix(y_test,predict_test) # matricea de acuratete (de confuzie)
accuracy=accuracy_score(y_test,predict_test) # acuratete globala
class_accuracy=cm.diagonal()/cm.sum(axis=1) # acuratete medie
medie_accuracy=np.mean(class_accuracy)

print('Matrice de acuratete: ',cm)
print('Acuratetea:' , accuracy)
print('Acuratetea medie: ',medie_accuracy)

################ MODEL BAYESIAN ###################
x_gaussian=GaussianNB()
x_gaussian.fit(x_train,y_train)

# predictii in setul de testare
gaussian_predict_test=x_gaussian.predict(x_test)
print(gaussian_predict_test)

# predictii in setul de aplicare
gaussian_predict_apply=x_gaussian.predict(x_apply)
print(gaussian_predict_apply)

# evaluare
cm_bayesian=confusion_matrix(y_test,gaussian_predict_test)
accuracy_bayesian=accuracy_score(y_test,gaussian_predict_test)
class_accuracy_bayesian=cm_bayesian.diagonal()/cm_bayesian.sum(axis=1)
medie_accuracy_bayesian=np.mean(class_accuracy_bayesian)

print('Matrice de acuratete: ',cm_bayesian)
print('Acuratetea:' , accuracy_bayesian)
print('Acuratetea medie: ',medie_accuracy_bayesian)