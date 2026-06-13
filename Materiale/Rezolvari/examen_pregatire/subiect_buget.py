import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
from seaborn import kdeplot

x= pd.read_csv('./dateIN/Pacienti.csv',index_col=0)
labels=list(x.columns.values[:-1])
tinta='DECISION'

dict={'I':1,'S':2,'A':3}
x[tinta]=x[tinta].map(dict)

x_test,x_train,y_test,y_train=train_test_split(x[labels],x[tinta],train_size=0.4)
lda=LinearDiscriminantAnalysis()
lda.fit(x_train,y_train)

#B1
predict_test=lda.predict(x_test)
pd.DataFrame(data=predict_test).to_csv('./dateOUT/predict.csv')

#B2
cm=confusion_matrix(y_test,predict_test)
accurancy=accuracy_score(y_test,predict_test)
class_accurancy=cm.diagonal()/cm.sum(axis=1)
medie=np.mean(class_accurancy)
print(y_test)
print('Matrice de acuratete: ',cm)
print('Acuratetea:' , accurancy)
print('Acuratetea medie: ',medie)

#B3
scores=lda.transform(x_train)
print(scores)
plt.figure(figsize=(8,8))
plt.title('Grafic distributiile in axele discriminante')
kdeplot(scores, fill=True)
plt.show()
