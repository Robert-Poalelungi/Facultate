import pandas as pd
import numpy as np

industrieAlimentaraDF = pd.read_csv('IndustriaAlimentara.csv', index_col=0)
populatieLocalitatiDF = pd.read_csv('PopulatieLocalitati.csv', index_col=0)

coduriJudeteDF = pd.read_csv('Coduri_Judete.csv')
coduriRegiuniDF = pd.read_csv('Coduri_Regiuni.csv')

# cerinta 1
industrie_populatie = industrieAlimentaraDF.merge(right=populatieLocalitatiDF[['Populatie', 'Judet']], right_index=True, left_index=True)
cerinta_1 = industrie_populatie[industrie_populatie.iloc[:, 2:-2].values.sum(axis=1) > 0]

cerinta_1.to_csv('Cerinta_1.csv')


# cerinta 2
total_angajati_localitate = industrie_populatie.iloc[:, 2: -2].sum(axis=1)

coloane_industrii = industrie_populatie.columns[1: -2]

cerinta_2 = industrie_populatie.copy(deep=True)

for row in cerinta_2.index:
    cerinta_2.loc[row, coloane_industrii] = cerinta_2.loc[row, coloane_industrii] / total_angajati_localitate.loc[row] * 100

cerinta_2.to_csv("Cerinta_2.csv")

# cerinta 3
cerinta_3 = industrie_populatie.copy(deep=True)
agg_dict = list(coloane_industrii) + ["Populatie"]
cerinta_3_m = cerinta_3.groupby("Judet").agg({agg_dict[k]: "sum" for k in range(0, len(agg_dict))})

for row in cerinta_3_m.index:
    print(cerinta_3_m.loc[row])

print(cerinta_3_m)
