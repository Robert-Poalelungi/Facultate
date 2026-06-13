from gui_ import *
import spatial
import controller
import functii
import factor_analyzer as fa
import pandas as pd
import numpy as np
import grafice


class Frame(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.director = "D:/Titus/Profesional"
        self.setWindowTitle("Analiza Factoriala")
        self.model_creat = False
        self.procent_minim = 0.7
        self.setupUi(self)
        self.metode = ['minres', 'ml']
        self.buton_citire.clicked.connect(self.citire)
        self.buton_selectie.clicked.connect(lambda x: controller.selectie_generala(self.list_variabile))
        self.buton_factorabilitate.clicked.connect(self.factorabilitate)
        self.buton_varianta.clicked.connect(self.varianta_factori)
        self.buton_plot_varianta.clicked.connect(self.plot_varianta)
        self.buton_corelatii.clicked.connect(self.corelatii)
        self.pushButton.clicked.connect(self.corelograma_cortelatii)
        self.buton_plot_corelatii.clicked.connect(self.plot_corelatii)
        self.buton_scoruri.clicked.connect(self.scoruri)
        self.buton_plot_scoruri.clicked.connect(self.plot_scoruri)
        self.buton_harta.clicked.connect(self.plot_harta)
        self.combo_rotatie.currentTextChanged.connect(self.reset)
        self.combo_metode.currentTextChanged.connect(self.reset)

    def plot_harta(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        t_f = functii.tabelare_matrice(self.f[:, :self.numar_factori_seminificativi], self.t.index,
                                       self.etichete_factori[:self.numar_factori_seminificativi])
        dialog_harta = spatial.Dialog(t_f, self)
        dialog_harta.show()

    def plot_scoruri(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        grafice.plot_instante(self.f[:, self.combo_axa1.currentIndex()],
                              self.f[:, self.combo_axa2.currentIndex()],
                              self.combo_axa1.currentText(), self.combo_axa2.currentText(),
                              self.t[self.coloana_etichete].values, "Factor Scores", aspect=1)
        # grafice.scatter_3d(self.f[:, 0],
        #                    self.f[:, 1],
        #                    self.f[:, 2], "F1", "F2", "F3",
        #                    self.t[self.coloana_etichete].values, "Factor Scores", aspect="auto")
        grafice.show()

    def scoruri(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        nume_fisier_out = "out/" + self.nume_fisier + "_fscores.csv"
        t_f = functii.tabelare_matrice(np.round(self.f[:, :self.numar_factori_seminificativi], 5),
                                       self.t.index, self.etichete_factori[:self.numar_factori_seminificativi],
                                       nume_fisier_out)
        dialog = controller.DialogNonModal(self, t_f, titlu="Scoruri factoriale")
        dialog.show()

    def plot_corelatii(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        t_l = functii.tabelare_matrice(np.round(self.l[:, :self.numar_factori_seminificativi], 3), self.variabile,
                                       self.etichete_factori[:self.numar_factori_seminificativi], "l.csv")
        grafice.plot_corelatii(t_l, self.combo_axa1.currentText(), self.combo_axa2.currentText(), aspect=1)
        grafice.show()

    def corelatii(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        t_l = functii.tabelare_matrice(np.round(self.l[:, :self.numar_factori_seminificativi], 3), self.variabile,
                                       self.etichete_factori[:self.numar_factori_seminificativi], "l.csv")
        dialog = controller.DialogNonModal(self, t_l, titlu="Corelatii factoriale")
        dialog.show()

    def corelograma_cortelatii(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        t_l = functii.tabelare_matrice(np.round(self.l[:, :self.numar_factori_seminificativi], 3), self.variabile,
                                       self.etichete_factori[:self.numar_factori_seminificativi], "l.csv")
        grafice.corelograma(t_l, titlu="Factor Loadings. Extraction:" +
                                       self.combo_metode.currentText() + ". Rotation:" + self.combo_rotatie.currentText())
        grafice.show()

    def plot_varianta(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        grafice.plot_varianta(self.varianta[0], self.nrfact, self.procent_minim * 100, "Factors",
                              "Scree Plot. Extraction:" +
                              self.combo_metode.currentText() + ". Rotation:" + self.combo_rotatie.currentText())
        grafice.show()

    def factorabilitate(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        t_kmo = pd.DataFrame(data={"KMO": np.append(self.kmo[0], self.kmo[1])}, index=self.variabile + ["Total"])
        t_kmo.to_csv("kmo.csv")
        grafice.corelograma(t_kmo, vmin=0, titlu="Index KMO")
        grafice.show()

    def varianta_factori(self):
        if self.model_creat is False:
            if not self.creare_model():
                return
        t_varianta = pd.DataFrame(
            data=np.round(np.array(self.varianta).T, 3),
            index=self.etichete_factori,
            columns=["Variance", "Proportional Variance", "Cumulative Variance"]
        )
        nume_fisier = "out/" + self.nume_fisier + "_Variance_" + self.combo_metode.currentText() + "_" + self.combo_rotatie.currentText() + ".csv"
        t_varianta.to_csv(nume_fisier)
        dialog = controller.DialogNonModal(self, t_varianta, titlu="Varianta factori")
        dialog.show()

    def citire(self):
        rezultat = controller.citire_fisier_variabile(self.combo_index, self.list_variabile, self.director)
        if rezultat is not None:
            self.t = rezultat[0]
            functii.nan_replace(self.t)
            self.text_fisier.setText(rezultat[1])
            controller.init_combo(self.combo_etichete, list(self.t))
            controller.init_combo(self.combo_metode, self.metode)
            controller.init_combo(self.combo_rotatie,
                                  ["None", "varimax", "promax", "oblimin", "oblimax", "quartimin", "quartimax"
                                      , "equamax", "geomin_obl", "geomin_ort"])
            self.schimbare_selectie()
            self.director = rezultat[1][:rezultat[1].rfind("/")]
            nume_fisier_extins = rezultat[1]
            self.nume_fisier = nume_fisier_extins[nume_fisier_extins.rfind("/") + 1:nume_fisier_extins.rfind(".csv")]
            # print(self.nume_fisier)

    def schimbare_selectie(self):
        # self.combo_rotatie.stateChanged.connect(self.reset)
        self.check_bartlett.stateChanged.connect(self.reset)
        for i in range(self.list_variabile.count()):
            item = self.list_variabile.item(i)
            check = self.list_variabile.itemWidget(item)
            check.stateChanged.connect(self.reset)

    def reset(self):
        self.model_creat = False

    def creare_model(self):
        if not self.text_fisier.text():
            return False
        self.variabile = controller.selectii_lista(self.list_variabile)
        coloana_index = self.combo_index.currentText()
        self.coloana_etichete = self.combo_etichete.currentText()
        self.t.index = self.t[coloana_index]
        self.t.index.name = coloana_index
        nume_instante = self.t[coloana_index]
        m = len(self.variabile)
        functii.nan_replace(self.t)
        x = self.t[self.variabile].values
        self.kmo = fa.calculate_kmo(x)
        # Determinarea numarului de factori semnificativi
        if self.check_bartlett.isChecked():
            p_value_minim = 1
            numar_factori_bartlett = 2
            for i in range(2, m + 1):
                fa_model = fa.FactorAnalyzer(n_factors=i, rotation=None)
                fa_model.fit(x)
                chi2, p_value = functii.bartlett_test(len(nume_instante), fa_model.loadings_,
                                                      x, fa_model.get_uniquenesses())
                if np.isnan(p_value):
                    break
                else:
                    if p_value < p_value_minim:
                        p_value_minim = p_value
                        numar_factori_bartlett = i
        self.etichete_factori = ["F" + str(i) for i in range(1, m + 1)]
        tip_rotatie = self.combo_rotatie.currentText()
        if tip_rotatie != "None":
            rotatie = tip_rotatie
        else:
            rotatie = None
        model_afact = fa.FactorAnalyzer(n_factors=m, rotation=rotatie)
        model_afact.fit(x)
        rotation_matrix = model_afact.rotation_matrix_
        print(rotation_matrix)
        self.varianta = model_afact.get_factor_variance()
        self.nrfact = functii.ncomp_estim(self.varianta[0], self.varianta[2], limita=self.procent_minim)
        if self.check_bartlett.isChecked():
            self.nrfact.append(numar_factori_bartlett)
        self.numar_factori_seminificativi = int(np.nanmax(self.nrfact))

        self.l = model_afact.loadings_
        self.f = model_afact.transform(x)
        self.h = model_afact.get_communalities()
        controller.init_combo(self.combo_axa1, self.etichete_factori[:self.numar_factori_seminificativi])
        controller.init_combo(self.combo_axa2, self.etichete_factori[:self.numar_factori_seminificativi])
        self.combo_axa1.setCurrentIndex(0)
        self.combo_axa2.setCurrentIndex(1)

        self.model_creat = True
        return True
