import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from seaborn import kdeplot
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.naive_bayes import GaussianNB

rawIndustrie=pd.read_csv('./dateIN/Industrie.csv',index_col=0)
rawPopulatie=pd.read_csv('./dateIN/PopulatieLocalitati.csv',index_col=0)
labels=list(rawIndustrie.columns.values[1:])

merged=rawIndustrie.merge(rawPopulatie,right_index=True,left_index=True)\
    .drop('Localitate_y',axis=1).rename(columns={'Localitate_x':'Localitate'})\
    [['Judet','Localitate','Populatie']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
print(merged)

#A1

merged[['Localitate','Populatie']+labels].apply(lambda df: df[labels]/df['Populatie'],axis=1).to_csv('./dateOUT/Cerinta1_8.csv')
#A2
r2=merged[['Judet']+labels].groupby('Judet').sum()
r2['Cifra de afaceri']=r2.max(axis=1)
r2['Activitate']=r2.idxmax(axis=1)
r2[['Activitate','Cifra de afaceri']].to_csv('./dateOUT/Cerinta2_8.csv')

#B1
x=pd.read_csv('./dateIN/ProiectB.csv',index_col=0)
tinta='VULNERAB'
labels_lda=list(x.columns.values[:-1])

dict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7}
x[tinta]=x[tinta].map(dict)

x_train,x_test,y_train,y_test=train_test_split(x[labels_lda],x[tinta],train_size=0.4)
lda=LinearDiscriminantAnalysis()
lda.fit(x_train,y_train)
scores=lda.transform(x_train)
pd.DataFrame(data=scores).to_csv('./dateOUT/z.csv')

#B2
plt.figure(figsize=(8,8))
plt.title('Plot intre primele 2 axe discriminante')
kdeplot(scores[:,:2],fill=True)
#plt.scatter(scores[:,0],scores[:,1],c='r')
plt.show()
print(scores)
#B3
x_apply=pd.read_csv('./dateIN/ProiectB_apply.csv',index_col=0)

predict_test=lda.predict(x_test)
predict_apply=lda.predict(x_apply)

pd.DataFrame(data=predict_apply).to_csv('./dateOUT/predict_apply.csv')
pd.DataFrame(data=predict_test).to_csv('./dateOUT/predict_test.csv')

cm=confusion_matrix(y_test,predict_test)
accuracy=accuracy_score(y_test,predict_test)
#print(cm,accuracy)

x_gaussian=GaussianNB()
x_gaussian.fit(x_train,y_train)

gaussian_predict=x_gaussian.predict(x_test)#test
gaussian_predict_apply=x_gaussian.predict(x_apply)#apply
#print(gaussian_predict_apply)

