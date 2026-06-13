import numpy as np
import pandas as pd

rawMortalitate=pd.read_csv('./dateIN/Mortalitate.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/CoduriTariExtins2.csv',index_col=0)
labels=list(rawMortalitate.columns.values[:])
print(labels)
merged=rawMortalitate.merge(rawCoduri,right_index=True,left_index=True)[['Continent']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)

#1
merged[merged['RS']<0].to_csv('./dateOUT/Cerinta1_6.csv')
print(merged)
#2
merged[['Continent']+labels].groupby('Continent').mean().to_csv('./dateOUT/Cerinta2_6.csv')