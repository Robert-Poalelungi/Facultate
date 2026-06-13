import pandas as pd
import functii as f

#citire csv ca pandas dataframe
etnii_df = pd.read_csv('./dataIN/Ethnicity.csv', index_col = 0);

#citire fisier EXCEL cu multiple spreadsheet-uri
judete_df = pd.read_excel('./dataIN/CoduriRomania.xlsx', sheet_name='Judete', index_col=0)


localitati_df = pd.read_excel('./dataIN/CoduriRomania.xlsx', sheet_name='Localitati', index_col=0)


regiuni_df = pd.read_excel('./dataIN/CoduriRomania.xlsx', sheet_name='Regiuni', index_col=0)


#construire lista de coloane utile
etnii = etnii_df.columns.values[1:]

ID = f.indiceDisimilaritate(etnii_df, etnii)

#construitre pandas.dataFrame din numpy.ndarray(fiindca momentan ID e un vector si nu il putem face CSV)
ID_df = pd.DataFrame(data=ID, columns=['IndiceDisimilaritate'], index=etnii_df['City'].values)
print(ID_df)

#salvarea in fisier CSV
ID_df.to_csv('./dataOUT/indiceDisimilaritateLocalitati.csv')

#AICI INCEPE SEMINARUL 6
#Cum am obtinut ora trecuta pe localitati, acum vrem sa facem pe judete, regiuni, s.a.m.d

#Realizam un merge de DataFrame pentru a pune in corespondenta localitatile cu judetele
etnii_judete_df = etnii_df.merge(right = localitati_df, left_index=True, right_index=True)

#creare lista de coloane utile pentru agregare la nivel de judet
col_judet = list(etnii) + ['County']

judet_agg_df = etnii_judete_df[col_judet].groupby(by='County').sum()
#print(judet_agg_df)

#salvare in fisier CSV
judet_agg_df.to_csv("./dataOUT/EtniiJudete.csv")

#agregare la nivel de regiune

