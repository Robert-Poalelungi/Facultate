import numpy as np

class ACP:
    def __init__(self,X):
        self.X = X
        self.R = np.corrcoef(self.X,rowvar=False)

        medii = np.mean(self.X, axis=0)
        abateri = np.std(self.X, axis=0)
        self.Xstd = (self.X - medii) / abateri

        self.Cov = np.cov(self.X,rowvar=False)
        self.val_prop,self.vect_prop = np.linalg.eigh(self.Cov)
        k_des = [k for k in reversed(np.argsort(self.val_prop))]
        self.alpha = self.val_prop[k_des]
        self.a = self.vect_prop[:,k_des]
        self.C = self.X @ self.a
        self.Rxc = self.a * np.sqrt(self.alpha)
        self.scoruri = self.C/np.sqrt(self.alpha)

    def getScoruri(self):
        return self.scoruri

    # def getXstd(self):
    #     return self.Xstd
    #
    def getCorr(self):
        return self.R
    #
    # def getValoriProprii(self):
    #     return self.val_prop