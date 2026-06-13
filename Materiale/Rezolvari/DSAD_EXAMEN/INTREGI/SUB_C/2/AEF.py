import ACP as acp
import numpy as np

class AEF:
    def __init__(self,X):
        self.X = X
        acpModel = acp.ACP(self.X)
        # self.Xstd = acpModel.getXstd()
        self.Corr = acpModel.getCorr()
        # self.ValoriProprii = acpModel.getValoriProprii()
        self.Scoruri = acpModel.getScoruri()

    def getScoruri(self):
        return self.Scoruri

    def calculTestBartlett(self,loadings,epsilon):
        n = self.X.shape[0]
        m, q  = np.shape(loadings)
        V = self.Corr
