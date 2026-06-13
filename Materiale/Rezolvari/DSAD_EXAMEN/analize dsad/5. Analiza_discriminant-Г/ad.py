import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, cohen_kappa_score
from utils import *


class AnalizaDiscriminanta:

    def __init__(self):
        self.t = pd.read_csv("./dataIN/park.csv", index_col=0)
        self.t_ = pd.read_csv("./dataIN/park_test.csv", index_col=0)

        self.variabila_tinta = self.t.columns[-1:][0]
        self.variabile_predictor = self.t.columns[:-1]
        self.instante = list(self.t.index)

    # Bayes     x si y => f(x) = y
    def creare_model(self):
        x = self.t[self.variabile_predictor].values
        self.y = self.t[self.variabila_tinta].values

        model_bayes = GaussianNB()
        model_bayes.fit(x, self.y)

        self.clase = model_bayes.classes_
        self.y_predict = model_bayes.predict(x)
        self.mat_conf = confusion_matrix(self.y, self.y_predict)
        self.index_cohen_kappa = cohen_kappa_score(self.y, self.y_predict)

        x_ = self.t_[self.variabile_predictor].values
        self.y_predict_test = model_bayes.predict(x_)

        self.model_creat = True

    #LDA
    def creare_model_lda(self):
        x = self.t[self.variabile_predictor].values
        self.y = self.t[self.variabila_tinta].values

        model_lda = LinearDiscriminantAnalysis()
        model_lda.fit(x, self.y)

        self.z = model_lda.transform(x)
        self.clase = model_lda.classes_
        g = model_lda.means_
        self.zg = model_lda.transform(g)

        self.y_predict_ = model_lda.predict(x)
        self.mat_conf_ = confusion_matrix(self.y, self.y_predict_)
        self.index_cohen_kappa_ = cohen_kappa_score(self.y, self.y_predict_)

        self.nr_axe = min(len(self.variabile_predictor), len(self.clase) - 1)

        x_ = self.t_[self.variabile_predictor].values
        self.y_predict_test_ = model_lda.predict(x_)

        self.model_creat_lda = True

    # Bayes
    def afisare_acuratete(self):
        if not self.model_creat:
            self.creare_model()

        n = len(self.t)
        acuratete_globala = np.round(sum(np.diagonal(self.mat_conf)) * 100 / n, 3)
        acuratete_grupe = np.round(np.diagonal(self.mat_conf) * 100 / np.sum(self.mat_conf, axis=1))
        acuratete_medie = np.mean(acuratete_grupe)

        t_matconf = pd.DataFrame(self.mat_conf, self.clase, self.clase)
        t_matconf["Acuratete"] = acuratete_grupe

        print("Acuratete globala: " + str(acuratete_globala))
        print("Acuratete medie: " + str(acuratete_medie))
        print("Index Cohen-Kappa: " + str(self.index_cohen_kappa))

        t_matconf.to_csv("./dataOUT/MatriceConfuzie.csv")

    # LDA
    def afisare_acuratete_lda(self):
        if not self.model_creat_lda:
            self.creare_model_lda()

        n = len(self.t)
        acuratete_globala = np.round(sum(np.diagonal(self.mat_conf_)) * 100 / n, 3)
        acuratete_grupe = np.round(np.diagonal(self.mat_conf_) * 100 / np.sum(self.mat_conf_, axis=1))
        acuratete_medie = np.mean(acuratete_grupe)

        t_matconf = pd.DataFrame(self.mat_conf_, self.clase, self.clase)
        t_matconf["Acuratete"] = acuratete_grupe

        print("Acuratete globala (LDA): " + str(acuratete_globala))
        print("Acuratete medie (LDA): " + str(acuratete_medie))
        print("Index Cohen-Kappa (LDA): " + str(self.index_cohen_kappa_))

        t_matconf.to_csv("./dataOUT/MatriceConfuzieLDA.csv")

    # Bayes
    def clasificare_antrenament(self):
        if not self.model_creat:
            self.creare_model()

        t_clasif = pd.DataFrame(
            data={
                self.variabila_tinta: self.y,
                "Predictie Bayes": self.y_predict
            },
            index=self.instante
        )

        t_clasif.to_csv("./dataOUT/ClasificareInSetulDeAntrenareBayes.csv")

    # LDA
    def clasificare_antrenament_lda(self):
        if not self.model_creat_lda:
            self.creare_model_lda()

        t_clasif = pd.DataFrame(
            data={
                self.variabila_tinta: self.y,
                "Predictie LDA": self.y_predict_
            },
            index=self.t.index
        )

        t_clasif.to_csv("./dataOUT/ClasificareInSetulDeAntrenareLDA.csv")

    # Bayes
    def clasificare_aplicare(self):
        if not self.model_creat:
            self.creare_model()

        t_clasif = pd.DataFrame(
            data={
                "Predictie Bayes": self.y_predict_test
            },
            index=self.t_.index
        )

        t_clasif.to_csv("./dataOUT/ClasificareInSetulDeAplicareBayes.csv")

    # LDA
    def clasificare_aplicare_lda(self):
        if not self.model_creat_lda:
            self.creare_model_lda()

        t_clasif = pd.DataFrame(
            data={
                "Predictie LDA": self.y_predict_test_
            },
            index=self.t_.index
        )

        t_clasif.to_csv("./dataOUT/ClasificareInSetulDeAplicareLDA.csv")

    def plot_instante(self):
        if not self.model_creat_lda:
            self.creare_model_lda()

        if self.nr_axe > 1:
            for i in range(1, self.nr_axe):
                plot_instante(self.z, 0, i, self.zg, self.y, self.clase)
        else:
            print("Numar insuficient de axe (" + str(self.nr_axe) + ")")

    def plot_distributie(self):
        if not self.model_creat_lda:
            self.creare_model_lda()

        for i in range(self.nr_axe):
            distributie(self.z, i, self.y, self.clase)
