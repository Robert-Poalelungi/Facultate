import PySide2.QtWidgets as qw
import main_window as mw
import pandas as pd
import numpy as np
from PySide2.QtCore import Qt
import functii
import grafice
import spatial

# Clasa implementeaza ACP.
# Este creat un layout orizontal cu toate elementele (layout central). Este radacina sistemului de gestionare.
# Toate componentele sunt puse in gestionarele de pozitionare continute de layoutul central.
# Se instantiaza un panel de continut cu layoutul central si apoi un container greu.
# Containerul greu este membru al clasei si este lansat in modulul apelator.
class acp():
    def __init__(self):
        h_buton = 40
        stil1 = "color: rgb(0, 0, 255); font: 14pt \"Times New Roman\";"
        stil2 = "color: rgb(0, 0, 255); font: 12pt \"Times New Roman\";"

        self.model_creat = False
        self.variabile_selectate = []
        self.tabel_date = None
        # Numar de componente semnificative. Se calculeaza la graficul de varianta
        self.k_s = 2

        self.b_citire = mw.Buton("Citire date", 300, h_buton, stil1, self.citire_fisier)
        self.c_variabila_index = qw.QComboBox()
        self.c_variabila_index.setStyleSheet(stil2)
        self.l_variabile_selectate = qw.QListWidget()
        self.l_variabile_selectate.setFixedSize(300, 300)
        self.l_variabile_selectate.setStyleSheet(stil2)
        self.l_variabile_selectate.setSelectionMode(qw.QAbstractItemView.ExtendedSelection)
        self.ch_selectie_variabile = qw.QCheckBox("Selectie toate")
        self.ch_selectie_variabile.setStyleSheet(stil2)
        self.ch_selectie_variabile.stateChanged.connect(self.selectie_toate_variabilele)
        self.c_axa1 = qw.QComboBox()
        self.c_axa1.setStyleSheet(stil2)
        self.c_axa2 = qw.QComboBox()
        self.c_axa2.setStyleSheet(stil2)

        self.b_afisare_varianta = mw.Buton("Afisare varianta", 200, h_buton, stil1, self.afisare_varianta)
        self.b_plot_varianta = mw.Buton("Plot varianta", 200, h_buton, stil1, self.plot_varianta)
        self.b_afisare_corelatii = mw.Buton("Afisare corelatii",200, h_buton,stil1,self.afisare_corelatii)
        self.b_corelograma =  mw.Buton("Corelograma",200, h_buton,stil1,self.corelograma)
        self.b_plot_corelatii = mw.Buton("Plot corelatii",200, h_buton,stil1,self.plot_corelatii)
        self.b_afisare_scoruri = mw.Buton("Afisare scoruri",200, h_buton,stil1,self.afisare_scoruri)
        self.b_plot_scoruri = mw.Buton("Plot scoruri",200, h_buton,stil1,self.plot_scoruri)

        self.b_harta_geopandas = mw.Buton("Harta GeoPandas",200, h_buton,stil1,self.harta)
        self.b_harta_bokeh = mw.Buton("Harta Bokeh",200, h_buton,stil1,self.harta_bokeh)
        self.b_cosin = mw.Buton("Cosinusuri",200, h_buton,stil1,self.cosin)

        self.b_contrib = mw.Buton("Contributii",200, h_buton,stil1,self.contrib)
        self.b_comunalitati = mw.Buton("Comunalitati",200, h_buton,stil1,self.comunalitati)
        self.b_corelograma_com = mw.Buton("Corelograma comm",200, h_buton,stil1,self.corelograma_com)
        # Layoutul central
        layout_acp = qw.QHBoxLayout()
        layout_parametrii = qw.QVBoxLayout()
        layout_parametrii.addWidget(self.b_citire)
        formLayout = qw.QFormLayout()
        formLayout.addRow(mw.Eticheta("Variabila index:", stil=stil2), self.c_variabila_index)
        formLayout.addRow(mw.Eticheta("Selectie variabile:", stil=stil2), self.ch_selectie_variabile)
        layout_parametrii.addLayout(formLayout)
        layout_parametrii.addWidget(self.l_variabile_selectate)

        layout_axe = qw.QHBoxLayout()
        layout_axe.addWidget(mw.Eticheta("Axe", stil=stil2))
        layout_axe.addWidget(self.c_axa1)
        layout_axe.addWidget(self.c_axa2)
        layout_parametrii.addLayout(layout_axe)

        layout_acp.addLayout(layout_parametrii)

        grup_rezultate = qw.QGroupBox("REZULTATE")

        layout_rezultate = qw.QHBoxLayout()
        layout_varianta = qw.QVBoxLayout()
        # layout_varianta.tr("cvb xcv")
        layout_varianta.addWidget(self.b_afisare_varianta)
        layout_varianta.addWidget(self.b_plot_varianta)
        layout_varianta.setAlignment(Qt.AlignTop)

        layout_corelatii_factoriale = qw.QVBoxLayout()
        layout_corelatii_factoriale.addWidget(self.b_afisare_corelatii)
        layout_corelatii_factoriale.addWidget(self.b_corelograma)
        layout_corelatii_factoriale.addWidget(self.b_plot_corelatii)
        layout_corelatii_factoriale.setAlignment(Qt.AlignTop)

        layout_scoruri = qw.QVBoxLayout()
        layout_scoruri.addWidget(self.b_afisare_scoruri)
        layout_scoruri.addWidget(self.b_plot_scoruri)
        layout_scoruri.addWidget(self.b_harta_geopandas)
        layout_scoruri.addWidget(self.b_harta_bokeh)
        layout_scoruri.setAlignment(Qt.AlignTop)

        layout_metrici = qw.QVBoxLayout()
        layout_metrici.addWidget(self.b_cosin)
        layout_metrici.addWidget(self.b_contrib)
        layout_metrici.addWidget(self.b_comunalitati)
        layout_metrici.addWidget(self.b_corelograma_com)
        layout_metrici.setAlignment(Qt.AlignTop)

        layout_rezultate.addLayout(layout_varianta)
        layout_rezultate.addLayout(layout_corelatii_factoriale)
        layout_rezultate.addLayout(layout_scoruri)
        layout_rezultate.addLayout(layout_metrici)
        grup_rezultate.setLayout(layout_rezultate)

        layout_acp.addWidget(grup_rezultate)
        panel_continut = mw.Panel(layout_acp)

        self.form = mw.Frame(panel=panel_continut, titlu="ANALIZA IN COMPONENTE PRINCIPALE")

    def citire_fisier(self):
        dialog = qw.QFileDialog(directory=".")
        dialog.setFileMode(qw.QFileDialog.AnyFile)
        dialog.setNameFilter("Images (*.csv)")
        dialog.setViewMode(qw.QFileDialog.Detail)
        fileNames = []
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        if len(fileNames) == 0:
            return
        self.fisier = fileNames[0]
        self.tabel_date = pd.read_csv(self.fisier)
        variabile = list(self.tabel_date)
        self.l_variabile_selectate.clear()
        self.c_variabila_index.clear()
        for v in variabile:
            # self.l_variabile_selectate.addItem(qw.QListWidgetItem(v))
            # Se instantiaza un item si se indica prin parametru lista la care va fi adaugat
            item = qw.QListWidgetItem(self.l_variabile_selectate)
            ch = qw.QCheckBox(v)
            # Inregistrare semnal de schimbare stare
            ch.stateChanged.connect(self.selectie_variabila)
            self.l_variabile_selectate.setItemWidget(item, ch)
            self.c_variabila_index.addItem(v)

    def selectie_variabila(self):
        self.model_creat = False

    def selectie_toate_variabilele(self):
        flag = self.ch_selectie_variabile.isChecked()
        for i in range(self.l_variabile_selectate.count()):
            item = self.l_variabile_selectate.item(i)
            self.l_variabile_selectate.itemWidget(item).setChecked(flag)
        self.model_creat = False

    def creare_model(self):
        if self.tabel_date is None:
            msgBox = qw.QMessageBox()
            msgBox.setText("Nu au fost citite datele!")
            msgBox.exec()
            return
        self.variabile_selectate.clear()
        for i in range(self.l_variabile_selectate.count()):
            item = self.l_variabile_selectate.item(i)
            checkItem = self.l_variabile_selectate.itemWidget(item)
            if checkItem.isChecked():
                self.variabile_selectate.append(checkItem.text())
        self.coloana_index = self.c_variabila_index.currentText()
        self.tabel_date.index = [str(v) for v in self.tabel_date[self.coloana_index]]
        self.nume_instante = self.tabel_date[self.coloana_index]
        self.m = len(self.variabile_selectate)
        if self.m < 2:
            msgBox = qw.QMessageBox()
            msgBox.setText("Prea putine variabile selectate!")
            msgBox.exec()
            return
        for i in range(1, self.m + 1):
            self.c_axa1.addItem(str(i))
            self.c_axa2.addItem(str(i))
        self.c_axa1.setCurrentIndex(0)
        self.c_axa2.setCurrentIndex(1)
        t = self.tabel_date[self.variabile_selectate]
        X = t.values
        functii.inlocuire_na(X)
        print("Model creat!")
        self.R, self.alpha, self.a, self.Rxc, self.C = functii.acp(X)
        pd.DataFrame(data=np.round(self.a,2),columns=["a"+str(i+1) for i in range(self.m)]).to_csv("pca_output/a.csv")
        self.model_creat = True

    def afisare_varianta(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            tabel_varianta = functii.tabelare_varianta(self.alpha)
            tabel_varianta.to_csv("pca_output/varianta.csv")
            tabel = mw.Tabel(tabel_varianta)
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Varianta componentelor")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec_()

    def plot_varianta(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            j_criterii = grafice.plot_varianta(self.alpha)
            self.k_s = min([v for v in j_criterii if v is not None])
            grafice.show()

    def corelograma(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            rxc_tab = functii.tabelare(self.Rxc, nume_coloane=["C" + str(i) for i in range(1, self.m + 1)],
                                       nume_instante=self.variabile_selectate)
            rxc_tab.to_csv()
            grafice.corelograma(rxc_tab, "Corelatii variabile-componente")
            grafice.show()

    def corelograma_com(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            comm = np.cumsum(self.Rxc * self.Rxc, axis=1)
            t_comm = functii.tabelare(comm, nume_coloane=["C" + str(i) for i in range(1, self.m + 1)],
                                       nume_instante=self.variabile_selectate)
            grafice.corelograma(t_comm, "Comunalitati",valmin=0)
            grafice.show()

    def comunalitati(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            comm = np.cumsum(self.Rxc * self.Rxc, axis=1)
            t_comm = functii.tabelare(np.round(comm,2), nume_coloane=["C" + str(i) for i in range(1, self.m + 1)],
                                       nume_instante=self.variabile_selectate,tabel="pca_output/comm.csv")
            tabel = mw.Tabel(t_comm)
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Comunalitati")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec_()

    def afisare_corelatii(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            rxc_tab = functii.tabelare(self.Rxc, nume_coloane=["C" + str(i) for i in range(1, self.m + 1)],
                                       nume_instante=self.variabile_selectate, tabel="PCA_Output\\Rxc.csv")
            tabel = mw.Tabel(rxc_tab)
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Corelatii variabile-componente")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec_()

    def afisare_scoruri(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            c_tab = functii.tabelare(self.C, nume_coloane=["C" + str(i) for i in range(1, self.m + 1)],
                                     nume_instante=self.nume_instante, tabel="PCA_Output\\C.csv")
            s = self.C/np.sqrt(self.alpha)
            pd.DataFrame(s,self.nume_instante,["C" + str(i) for i in range(1, self.m + 1)]).to_csv("PCA_Output\\S.csv")
            tabel = mw.Tabel(c_tab)
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Scoruri")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec_()

    def cosin(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            c2 = self.C * self.C
            cos = np.transpose(np.transpose(c2) / np.sum(c2, axis=1))
            cos_tab = functii.tabelare(cos, nume_coloane=["a" + str(i) for i in range(1, self.m + 1)],
                                       nume_instante=self.nume_instante, tabel="PCA_Output\\cos2.csv")
            tabel = mw.Tabel(cos_tab)
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Cosinusuri")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec_()

    def contrib(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            n = len(self.nume_instante)
            c2 = self.C * self.C
            beta = c2 / (n * self.alpha)
            beta_tab = functii.tabelare(beta, nume_coloane=["a" + str(i) for i in range(1, self.m + 1)],
                             nume_instante=self.nume_instante, tabel="PCA_Output\\contributii.csv")
            tabel = mw.Tabel(beta_tab)
            layout1 = qw.QHBoxLayout()
            layout1.addWidget(tabel)
            dialog = qw.QDialog()
            dialog.setWindowTitle("Contributii")
            dialog.setLayout(layout1)
            dialog.setModal(True)
            dialog.exec_()

    def plot_corelatii(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            grafice.plot_corelatii(self.Rxc, k1=self.c_axa1.currentIndex(), k2=self.c_axa2.currentIndex(),
                                   nume_variabile=self.variabile_selectate)
            grafice.show()

    def plot_scoruri(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            grafice.plot_instante(self.C, k1=self.c_axa1.currentIndex(), k2=self.c_axa2.currentIndex(),
                                  nume_instante=self.nume_instante)
            grafice.show()

    def harta(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            dialog = qw.QFileDialog(directory=".")
            dialog.setFileMode(qw.QFileDialog.AnyFile)
            dialog.setNameFilter("Shape (*.shp)")
            dialog.setViewMode(qw.QFileDialog.Detail)
            fileNames = []
            if dialog.exec_():
                fileNames = dialog.selectedFiles()
            if len(fileNames) == 0:
                return
            fisier_shp = fileNames[0]
            spatial.plot_map(fisier_shp, self.C[:, 0:self.k_s], self.nume_instante)
            grafice.show()

    def harta_bokeh(self):
        if self.model_creat is False:
            self.creare_model()
        if self.model_creat:
            dialog = qw.QFileDialog(directory=".")
            dialog.setFileMode(qw.QFileDialog.AnyFile)
            dialog.setNameFilter("Shape (*.shp)")
            dialog.setViewMode(qw.QFileDialog.Detail)
            fileNames = []
            if dialog.exec_():
                fileNames = dialog.selectedFiles()
            if len(fileNames) == 0:
                return
            fisier_shp = fileNames[0]
            tabel_scoruri = pd.DataFrame(data=self.C[:, 0:self.k_s], index=self.nume_instante,
                                         columns=["C" + str(i) for i in range(1, self.k_s + 1)])
            spatial.plot_bokeh(fisier_shp, tabel_scoruri, "Plot scoruri")
            grafice.show()
