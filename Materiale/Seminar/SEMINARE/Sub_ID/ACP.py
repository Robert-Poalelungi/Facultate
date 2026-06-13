import numpy as np

class ACP:
    def __init__(self,X):
        self.X = X
        self.Cov = np.cov(self.X,rowvar=False)
        self.val_prop,self.vect_prop = np.linalg.eigh(self.Cov)
        k_des = [k for k in reversed(np.argsort(self.val_prop))]
        self.alpha = self.val_prop[k_des]
        self.a = self.vect_prop[:,k_des]
        self.C = self.X @ self.a
        self.Rxc = self.a * np.sqrt(self.alpha)
        self.scoruri = self.C / np.sqrt(self.alpha)

    def getComponente(self):
        return self.C

    def getScoruri(self):
        return self.scoruri



