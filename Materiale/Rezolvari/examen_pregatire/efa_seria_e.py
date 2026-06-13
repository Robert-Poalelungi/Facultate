import numpy as np
import pandas as pd
from factor_analyzer import FactorAnalyzer,calculate_bartlett_sphericity,calculate_kmo

rawDiversitate=pd.read_csv('./dateIN/Diversitate.csv',index_col=0)
rawCoduri=pd.read_csv('./dateIN/Coduri_localitati.csv',index_col=0)
labels=list(rawDiversitate.columns.values[1:])

merged=rawDiversitate.merge(rawCoduri,right_index=True,left_index=True)
print(merged)