import pandas as pd

print("-------------------------CERINTA 1-------------------------")
natalitate = pd.read_csv("natalitate.csv",index_col=0)
variabile_natalitate=list(natalitate)
variabile_numerice=variabile_natalitate[1:]
date_numerice=natalitate[variabile_numerice].values

nuts = pd.read_csv("RO_NUTS.csv",index_col=0)
print(natalitate)
print(nuts)

print("-------------------------CERINTA 2-------------------------")
# Calculăm matricea de corelație
corelation_matrix = natalitate.corr()
print(corelation_matrix)
corelation_matrix.to_csv("Output1.csv")

print("-------------------------CERINTA 3-------------------------")
cerinta3=natalitate.copy()
total_f=natalitate["NascutiFemininUrban"]+natalitate["NascutiFemininRural"]
total_m=natalitate["NascutiMasculinUrban"]+natalitate["NascutiMasculinRural"]
cerinta3["Total_feminim"]=total_f
cerinta3["Total_masculin"]=total_m
print(cerinta3)
cerinta3.to_csv("Output2.csv")

print("-------------------------CERINTA 4-------------------------")
cerinta4=natalitate.copy()
total_u=natalitate["NascutiFemininUrban"]+natalitate["NascutiMasculinUrban"]
total_r=natalitate["NascutiFemininRural"]+natalitate["NascutiMasculinRural"]
cerinta4["Total_urban"]=total_u
cerinta4["Total_rural"]=total_r
natalitate_merge=cerinta4.merge(nuts,right_index=True,left_index=True)
per_reg=natalitate_merge[["Total_urban","Total_rural","Regiune"]].groupby(by="Regiune").sum()
print(per_reg)
per_reg.to_csv("Output3.csv")

