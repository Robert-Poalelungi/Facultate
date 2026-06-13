import numpy as np


def inlocuireNAN(X): #asumam ca primim un numpy.ndarray
    medieCols = np.nanmean(a=X, axis = 0) #avem variabile pe coloane
    locs = np.where(np.isnan(X));

    print(locs);
    X[locs] = medieCols[locs[1]] #pe baza indicilor de coloane

    return X
