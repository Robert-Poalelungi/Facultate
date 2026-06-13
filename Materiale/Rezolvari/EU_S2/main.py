# importuri
import pandas as pd
from pandas.api.types import is_numeric_dtype

# inlocuire NaN
def nan_replace_t(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

# citire din fisier
alcool = pd.read_csv("alcohol.csv", index_col=1)
coduri = pd.read_csv("CoduriTariExtins.csv", index_col=2)

#inlocuire valori NaN
nan_replace_t(alcool)
nan_replace_t(coduri)

#alcatuire lista cu ani
ani = list(alcool)[1:]

# CERINTA 1
# - consumul mediu la nivel de tara, descresacator dupa consum
# - cod, nume, consum mediu

cerinta1 = alcool.apply(
    lambda x:pd.Series(
        [x["Country"],x.iloc[1:].mean()],
        ["Country","Consum Mediu"]
    ),
    axis=1)

cerinta1.sort_values(by="Consum Mediu",ascending=False,inplace=True)

cerinta1.to_csv("Cerinta1.csv")


































