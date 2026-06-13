import numpy as np

# clasa ajutatoare in analiza PCA a unui set de date
class PCA:
    def __init__(self, X, regularizare=True):
        """
               Inițializează analiza componentelor principale (PCA).

               :param X: np.array - Setul de date inițial
               :param regularizare: bool - Dacă se normalizează vectorii proprii pentru interpretare (implicit: True)
        """
        # atribuirea setului de date
        self.X = X

        # stanardizarea setului de date cu formula (X - Medie(X)) / Stddev(X)
        self.Xstd = self.setModelStd()

        # calcularea matricei de corelatie
        self.Cov = np.cov(m=self.Xstd, rowvar=False)

        # calcularea valoriilor proprii si a vectorilor proprii pe baza matricei de corelatie
        eigenvalues, eigenvectors = np.linalg.eigh(a=self.Cov)

        # ordonarea descrescatoare a valorilor proprii si a vectorilor proprii (pentru a pastra componentele principale care explica cel mai mult varianta)
        reversedIndexes = [k for k in reversed(np.argsort(a=eigenvalues))]
        self.alpha = eigenvalues[reversedIndexes]
        self.a = eigenvectors[reversedIndexes]

        # regularizarea vectorilor proprii pentru interpretare mai usoara a corelogramei factor loadings
        if regularizare == True:
            for j in range(self.a.shape[1]):
                min = np.min(a=self.a[:, j])
                max = np.max(a=self.a[:, j])
                if np.abs(min) > np.abs(max):
                    self.a[:, j] = -self.a[:, j]

        # calcularea matricei cu componente principale (PC)
        self.PC = self.Xstd @ self.a

        # calcularea factor loadings
        self.factorloadings = self.a * np.sqrt(self.alpha)

        # calcularea scorurilor standardizate
        self.scores = self.PC / np.sqrt(self.alpha)

        # calcularea comunalitatilor
        self.communalities = np.sum(np.square(self.factorloadings), axis=1)

    # metoda ajutatoarea pentru standardizarea unei matrici
    def setModelStd(self):
        """
                Standardizează datele utilizând media și abaterea standard.

                :return: np.array - Datele standardizate
        """
        medii = np.mean(a=self.X, axis=0)
        abateri_std = np.std(a=self.X, axis=0)
        return (self.X - medii) / abateri_std

    # getteri pentru toate atributele clasei necesare in analiza PCA
    def getModelStd(self):
        return self.Xstd

    def getCov(self):
        return self.Cov

    def getEigenvalues(self):
        return self.alpha

    def getEigenvectors(self):
        return self.a

    def getPrincipalComponents(self):
        return self.PC

    def getFactorLoadings(self):
        return self.factorloadings

    def getScores(self):
        return self.scores

    def getCommunalities(self):
        return self.communalities