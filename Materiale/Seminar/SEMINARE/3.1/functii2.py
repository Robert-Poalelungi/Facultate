import numpy as np
import pandas as pd
from scipy.stats import shapiro, kstest, norm, chi2


def nan_replace(date_numerice):
    val_zero=np.isnan(date_numerice)
    poz=np.where(val_zero)
    date_numerice[poz]=np.nanmean(date_numerice[:,poz[1]],axis=0)

def salvare(x,linii=None,coloane=None,out="out.csv"):
    t=pd.DataFrame(x,linii,coloane)
    t.to_csv(out)


def standardizare(x,std=True):
    x_=x-np.mean(x,axis=0)
    if std:
        x_=x_/np.std(x,axis=0)
    return x_







