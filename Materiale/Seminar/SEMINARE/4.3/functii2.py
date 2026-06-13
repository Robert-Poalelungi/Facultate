import numpy as np
import pandas as pd
from scipy.stats import entropy


def salvare(x,linii=None,coloane=None,out="out.csv"):
    t=pd.DataFrame(x,linii,coloane)
    t.to_csv(out)

def shannon(t):
    x = t.iloc[:, :-1].values
    # p = x / np.sum(x, axis=0)
    p = (x.T / np.sum(x,axis=1)).T
    h = entropy(p, base=2, axis=0)
    return pd.Series(h, t.columns[:-1])

