'''
Clasa care incapsuleaza implementarea modelului de ACP
'''
import numpy as np

class ACP:
#asumam ca pimim un constructor X ca numpy.ndarray
    def __init__(self, X):
        self.X = X

        #calcul matrice varianta-covarianta pentru X
        self.Cov = np.cov(m=X, rowvar=False) #avem variabile pe coloane
        print(self.Cov.shape)

        #calcul valori proprii si vectori proprii pentru matricea varianta-covarianta
        self.valProp, self.vectProp = np.linalg.eigh(a=self.Cov)
        print(self.valProp, self.valProp.shape)
        print(self.vectProp.shape)

    def getValoriProprii(self):
        return self.valProp




