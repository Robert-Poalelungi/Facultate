import pandas as pd
import numpy as np
import copy
import sklearn.cross_decomposition as skl
import matplotlib.pyplot as plt

vot = pd.read_csv('dataIN/Vot.csv')
localitati = pd.read_csv('dataIN/Coduri_localitati.csv')

# print(vot.columns)
categorii = ['Barbati_25-34', 'Barbati_35-44', 'Barbati_45-64', 'Barbati_65_', 'Femei_18-24', 'Femei_35-44',
       'Femei_45-64', 'Femei_65_']

t1 = copy.copy(vot)
for categorie in categorii:
    t1[categorie] = t1[categorie]*100/t1['Votanti_LP']

del t1['Votanti_LP']
cerinta1 = t1.reset_index(drop=True)
cerinta1.to_csv('dataOUT/Cerinta1_Verif.csv',index=False)

data_merge = pd.merge(vot,localitati,on='Siruta')
t2 = data_merge[['Judet','Votanti_LP','Barbati_25-34','Barbati_35-44', 'Barbati_45-64',
                 'Barbati_65_', 'Femei_18-24','Femei_35-44', 'Femei_45-64', 'Femei_65_']]
t3 = t2.groupby(by='Judet').agg(sum)

for categorie in categorii:
    t3[categorie] = t3[categorie] * 100 / t3['Votanti_LP']

del t3['Votanti_LP']
cerinta2 = t3
cerinta2.to_csv('dataOUT/Cerinta2_Verif.csv')

#ACC
#1. calc scorurilor canonice z si u
tabel = pd.read_csv('dataIN/Vot.csv')
obs = tabel.index.values
var = tabel.columns.values
x_col = var[3:7]
y_col = var[7:]

X = tabel[x_col].values
Y = tabel[y_col].values

def standardizare(X):
    medii = np.mean(X,axis=0)
    std = np.std(X,axis=0)
    Xstd = (X-medii)/std
    return Xstd

Xstd = standardizare(X)
Ystd = standardizare(Y)

n,p = np.shape(X)
q = np.shape(Y)[1]
m = min(p,q)

modelACC = skl.CCA(n_components=m)
modelACC.fit(X=Xstd,Y=Ystd)
z,u = modelACC.transform(X=Xstd,Y=Ystd)
z_df = pd.DataFrame(data=z,index=obs,columns=['z'+ str(j+1) for j in
                                              range(p)])
u_df = pd.DataFrame(data=u,index=obs,columns=['u'+ str(j+1) for j in
                                              range(p)])

z_df.to_csv('dataOUT/z.csv')
u_df.to_csv('dataOUT/u.csv')

#2. Calc corelatiilor canonice r
Rxz = modelACC.x_loadings_
Rxz_df = pd.DataFrame(data=Rxz,index=x_col,columns=['z'+ str(j+1)
                                                    for j in range(p)])
Ryu = modelACC.y_loadings_
Ryu_df = pd.DataFrame(data=Ryu,index=x_col,columns=['u'+ str(j+1)
                                                    for j in range(p)])

Rxz_df.to_csv('dataOUT/Rxz_df.csv')
Ryu_df.to_csv('dataOUT/Ryu_df.csv')

#3.trasarea graficului pt primele 2 rad canonice (x:z1,y:z2) si (x:u1,y:u2)
def biplot(x,y,xlabel,ylabel,titlu,e1,e2):
    f = plt.figure(figsize=(11,8))
    ax = f.add_subplot(1,1,1)
    assert isinstance(ax,plt.Axes)
    ax.set_title(titlu,fontsize=14)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.scatter(x=x[:,0],y=x[:,1],c='r',label='Set X')
    ax.scatter(x=y[:,0],y=y[:,1],c='b',label='Set Y')
    if e1 is not None:
        for i in range (len(e1)):
            ax.text(x=x[i,0],y=x[i,1],s=e1[i])
    if e2 is not None:
        for i in range (len(e2)):
            ax.text(x=y[i,0],y=y[i,1],s=e2[i])
    ax.legend()
    plt.show()

biplot(z[:,:2],u[:,:2],xlabel='(z1,z2)',ylabel='(u1,u2)',
       titlu='Biplot var in spatiul rad canonice (z1,z2) si (u1,u2)',
       e1=list(obs),e2=list(obs))


