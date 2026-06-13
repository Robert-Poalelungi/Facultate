'''
Clasa care incapsuleaza o implementare a modelului de analiza in componente principale (ACP)
'''
import numpy as np


class ACP:

    def __init__(self, matriceDate):
        self.X = matriceDate

        # calcul matrice de corelatie pentru X
        self.R = np.corrcoef(self.X, rowvar=False)  # avem variabilele pe coloane

        # standardizare a matrice de intrare X
        medii = np.mean(self.X, axis=0)  # sume pe coloane, prima axa
        abateri = np.std(self.X, axis=0)  # axele sunt numerotate de la dreapta la stanga intr-un ndarray
        self.Xstd = (self.X - medii) / abateri

        # calcul matrice de corelatie pentru X
        self.R = np.corrcoef(self.X, rowvar=False)  # avem variabilele pe coloane

        # calcul matrice varianta-covarianta
        self.Cov = np.cov(self.Xstd, rowvar=False)  # variabilele sunt pe coloane
        valProp, vectProp = np.linalg.eigh(self.Cov)  # pentru X standardizat poate fi utilizata si matrice de corelatie
        # sortarea descrescatoare a valorilor proprii
        k_des = [k for k in reversed(np.argsort(valProp))]
        # print(k_des)
        self.alpha = valProp[k_des]
        self.a = vectProp[:, k_des]

        # regularizarea vectorilor proprii
        for j in range(len(self.alpha)):
            minim = np.min(self.a[:, j])
            maxim = np.max(self.a[:, j])
            if np.abs(minim) > np.abs(maxim)
                self.a[:, j] *= -1  # inmultirea unui vector propriu cu un scalar nu modifica calitatea de vector propriu

        # calcul componente principale
        self.C = self.Xstd @ self.a  # operatorul @ este supraincarcat pentru inmultire matriceala

        # calculul matricei factorilor de corelatie (factor loadings)
        # reprezinta corelatia dintre variabilele initiale si componentele principale
        self.Rxc = self.a * np.sqrt(self.alpha)

        # calcul scorurilor (componentelor principale standardizate)
        self.Scoruri = self.C / np.sqrt(self.alpha)

        # calculul calitatii reprezentarii observatilor pe axele componentelor principale
        C2 = self.C * self.C
        C2Sum = np.sum(C2, axis=1)  # sume caculate pe linii (pentru fiecare observatie)
        self.CalObs = np.transpose(np.transpose(C2) / C2Sum)

        # contributia observatiilor la varianta axelor componentelor principale
        self.betha = C2 / (self.alpha * self.X.shape[0])

        # calcul comunitati - regasirea componentelor principale in variabilele initiale (observate)
        Rxc2 = self.Rxc * self.Rxc
        self.Comun = np.cumsum(Rxc2, axis=1)  # sume cumulative pe linii, pentru fiecare variabila observata


    def getXstd(self):
        return self.Xstd

    def getR(self):
        return self.R

    def getCov(self):
        return self.Cov

    def getValProp(self):
        return self.alpha

    def getCompPrin(self):
        return self.C

    def getFactoriCorelatie(self):
        return self.Rxc

    def getScoruri(self):
        return self.Scoruri

    def getCalObs(self):
        return self.CalObs

    def getBetha(self):
        return self.betha

    def getComun(self):
        return self.Comun
