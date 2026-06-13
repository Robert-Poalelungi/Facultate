import numpy as np
import pandas as pd
#import scipy.cluster.hierarchy as hiclu
import matplotlib.pyplot as plt
import factor_analyzer as fact

# #SUB 1 (cred SUB_C)
#
# alcohol = pd.read_csv("./dataIN/alchol.csv", index_col=1)
# tariExt = pd.read_csv("./dataIN/CoduriTariExtins.csv", index_col=0)
# variabile = list(alcohol.columns[1:])
#
# #cerinta1
# medie = np.mean(alcohol[variabile].values, axis=1)
# #print(medie)
# alcohol["Medie"] = medie
# alcohol["Medie"].to_csv("./dataOUT/Cerinta1_intreg.csv")
#
# #cerinta2
# tabel = alcohol.merge(right=tariExt, right_index=True, left_index=True).groupby(by="Continent").agg(sum)
# #print(tabel)
# def consum_max(t):
#     linie = t.values
#     max_pe_linie = np.argmax(linie)
#     return pd.Series(
#         data={"Anul": t[max_pe_linie]},
#         index=["Anul"])
#
# cerinta2 = tabel.apply(func=consum_max, axis=1)
# cerinta2.to_csv("./dataOUT/Cerinta2_intreg.csv")
#
# #cerinta3
# data = pd.read_csv("./dataIN/alchol.csv", index_col=1)
# cap_linii = list(data.index)
# #print(cap_linii)
# cap_coloane = list(data.columns[1:])
# #print(cap_coloane)
# n = len(cap_linii)
# m = len(cap_coloane)
# x = data[cap_coloane].values
# #print(x)
# h = hiclu.linkage(x, method="ward")
# coloane = ["Primul cluster","Al doilea cluster","Distanta","Nr instante noul cluster"]
# cerinta3 = pd.DataFrame(h, columns=coloane)
# #print(cerinta3)
#
#
# def plot_dendograma(h, cap_linii, titlu, prag = None):
#     fig = plt.figure(figsize=(10,9))
#     ax = fig.add_subplot(1, 1, 1)
#     ax.set_title(titlu)
#     hiclu.dendrogram(h,labels=cap_linii,color_threshold=prag,ax=ax)
#
# p = n-1
# k_dif_max = np.argmax(h[1:, 2]-h[:(p-1), 2])
# #print(k_dif_max)
# prag = (h[k_dif_max, 2] + h[k_dif_max+1, 2])/2
# nr_clust = p - k_dif_max
#
# # print(h)
# plot_dendograma(h,cap_linii,"Partitie cu "+str(nr_clust)+" clusteri",prag)
#
# def partitie(h, nr_clust):
#     c = np.arange(n)
#     for i in range(n-nr_clust):
#         k1 = h[i,0]
#         k2 = h[i,1]
#         c[c==k1] = n+i
#         c[c==k2] = n+i
#     coduri = pd.Categorical(c).codes
#     return np.array(["c"+str(i+1) for i in coduri])
#
# partitie_opt = partitie(h, nr_clust)
# print(partitie_opt)
#
# #plot_dendograma(partitie_opt,cap_linii,"dend",prag)
# plt.show()

#SUB 2 (cred)SUB-C
#cerinta1
vot = pd.read_csv("Vot.csv", index_col=0)
codLoc = pd.read_csv("Coduri_localitati.csv", index_col=0)
variabile=list(vot.columns[2:])


categorie_minima = np.argmin(vot[variabile].values, axis=1)
vot["Categorie"] = vot[variabile].columns[categorie_minima]
#print(vot)

#cerinta2
tabel = vot.merge(right=codLoc, right_index=True, left_index=True).groupby(by="Judet").\
    agg({'Barbati_25-34':'mean','Barbati_35-44':'mean','Barbati_45-64':'mean','Barbati_65_':'mean',
         'Femei_18-24':'mean','Femei_35-44':'mean','Femei_45-64':'mean','Femei_65_':'mean'})
# cerinta2 = tabel[variabile]
# print(cerinta2)

vot_merged = vot.merge(right=codLoc["Judet"], right_index=True, left_index=True)
#print(vot_merged.columns)
vot_merged.drop(["Categorie", "Localitate", "Votanti_LP"], axis=1, inplace=True)
#print(vot_merged)

#cerinta3
date = pd.read_csv("Vot.csv", index_col=0)
variabile = list(date.columns[2:])
print(variabile)
x = variabile.values
n,m = x.shape()

model_fact = fact.FactorAnalyze(n_components = m, rotation = None)
test_bartlett = fact.calculate_barlett_sphericity(x)
kmo = fact.test_kmo(x)
scor = model_fact.transform(x)
tabel_scor = pd.DataFrame(scor,date.index, ["F" +str(i+1) for i in range(m)])
corelatii = model_fact.loadings
comunalitati = model_fact.communalaties

def plot_componente(x, var_x, var_y, titlu, aspect="auto"):
    fig = plt.figure(figsize=(10,9))
    ax = fig.add_subplt(1, 1, 1)
    ax.set_xlabel(var_x, fontdict={'fontsize': 12, 'color': 'b'})
    ax.set_ylabel(var_y, fontdict={'fontsize': 12, 'color': 'b'})
    ax.set_title(titlu, fontdict={'fontsize': 12, 'color': 'b'})
    ax.scatter(x[var_x], x[var_y], color="r")
    for i in range(x):
        ax.text(x[var_x].iloc[i], x[var_y].iloc[i], x.index[i])

#grafic scoruri factoriale
plot_componente(tabel_scor,"f1","f2","Plot scoruri")
#pentru primele 2 se va schimba tabel_fact sa mearga pana la 2


#SUB 2 (CRED)SUB-E


