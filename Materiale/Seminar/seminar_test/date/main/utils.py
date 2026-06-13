import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype


def nan_replace(df):
    for col in df.columns:
        if df[col].isna().any():
            if is_numeric_dtype(df[col]):
                df[col].fillna(df[col].mean() , inplace=True)
            else:
                # outputul functiei mode() e de regula de forma:
                # 0 abc
                # 1 def
                df[col].fillna(df[col].mode()[0], inplace=True)


def to_dataframe(x, nume_randuri=None, nume_coloane=None,
                 nume_fisier=None):
    df = pd.DataFrame(data=x, index=nume_randuri,
                      columns=nume_coloane)
    if nume_fisier is not None:
        df.to_csv(nume_fisier)

    return df