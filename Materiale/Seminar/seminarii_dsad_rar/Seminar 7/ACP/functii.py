import numpy as np


def standardizare(X):   #asumam ca primim un numpy.ndarray
    medii = np.mean(a=X, axis=0) #facem mediile pe coloane
    abateriStandard = np.std(a=X, axis=0) #avem variabilele pe coloane

    return (X - medii) /abateriStandard
