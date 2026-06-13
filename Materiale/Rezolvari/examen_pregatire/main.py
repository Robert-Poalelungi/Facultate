import numpy as np
import pandas as pd


rawAir= pd.read_csv('./dateIN/AirQuality.csv', index_col=0)
rawCountryContinents=pd.read_csv('./dateIN/CountryContinents.csv',index_col=0)
labels=list(rawAir.columns.values[1:])


merge= rawAir.merge(rawCountryContinents,right_index=True,left_index=True).drop('Country_y',axis=1).rename(columns={'Country_x':'Country'})[['Continent','Country']+labels]
merge.fillna(np.mean(merge[labels],axis=0),inplace=True)
print(merge)

#1
merge[['Country']+labels].set_index('Country').idxmax(axis=0).reset_index().rename(columns={'index':'Indicator',0:'Country'}).to_csv('./dateOUT/Cerinta1.csv',index=False)

#2
merge.set_index('Country').groupby(['Continent']).apply(lambda df:pd.Series({ind: df[ind].idxmax() for ind in labels})).reset_index().to_csv('./dateOUT/Cerinta2.csv')

#B1


