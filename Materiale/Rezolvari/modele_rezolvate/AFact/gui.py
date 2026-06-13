# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1027, 570)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 401, 361))
        self.buton_citire = QPushButton(self.groupBox)
        self.buton_citire.setObjectName(u"buton_citire")
        self.buton_citire.setGeometry(QRect(20, 20, 151, 31))
        self.buton_citire.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")
        self.text_fisier = QLineEdit(self.groupBox)
        self.text_fisier.setObjectName(u"text_fisier")
        self.text_fisier.setGeometry(QRect(20, 55, 361, 20))
        self.formLayoutWidget = QWidget(self.groupBox)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 80, 361, 71))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.combo_index = QComboBox(self.formLayoutWidget)
        self.combo_index.setObjectName(u"combo_index")
        self.combo_index.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.combo_index)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.combo_etichete = QComboBox(self.formLayoutWidget)
        self.combo_etichete.setObjectName(u"combo_etichete")
        self.combo_etichete.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.combo_etichete)

        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 160, 361, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.label_3)

        self.list_variabile = QListWidget(self.verticalLayoutWidget)
        self.list_variabile.setObjectName(u"list_variabile")
        self.list_variabile.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.list_variabile)

        self.buton_selectie = QPushButton(self.verticalLayoutWidget)
        self.buton_selectie.setObjectName(u"buton_selectie")
        self.buton_selectie.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.buton_selectie)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 390, 401, 131))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.combo_metode = QComboBox(self.groupBox_2)
        self.combo_metode.setObjectName(u"combo_metode")
        self.combo_metode.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.combo_metode, 1, 1, 1, 1)

        self.combo_axa2 = QComboBox(self.groupBox_2)
        self.combo_axa2.setObjectName(u"combo_axa2")
        self.combo_axa2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.combo_axa2, 2, 2, 1, 1)

        self.combo_axa1 = QComboBox(self.groupBox_2)
        self.combo_axa1.setObjectName(u"combo_axa1")
        self.combo_axa1.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.combo_axa1, 2, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.checkBox, 1, 2, 1, 1)

        self.check_bartlett = QCheckBox(self.groupBox_2)
        self.check_bartlett.setObjectName(u"check_bartlett")
        self.check_bartlett.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")

        self.gridLayout.addWidget(self.check_bartlett, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(440, 30, 571, 181))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buton_corelatii = QPushButton(self.groupBox_3)
        self.buton_corelatii.setObjectName(u"buton_corelatii")
        self.buton_corelatii.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.buton_corelatii, 2, 0, 1, 1)

        self.buton_plot_scoruri = QPushButton(self.groupBox_3)
        self.buton_plot_scoruri.setObjectName(u"buton_plot_scoruri")
        self.buton_plot_scoruri.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.buton_plot_scoruri, 3, 1, 1, 1)

        self.buton_scoruri = QPushButton(self.groupBox_3)
        self.buton_scoruri.setObjectName(u"buton_scoruri")
        self.buton_scoruri.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.buton_scoruri, 3, 0, 1, 1)

        self.buton_harta = QPushButton(self.groupBox_3)
        self.buton_harta.setObjectName(u"buton_harta")
        self.buton_harta.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.buton_harta, 3, 2, 1, 1)

        self.buton_plot_corelatii = QPushButton(self.groupBox_3)
        self.buton_plot_corelatii.setObjectName(u"buton_plot_corelatii")
        self.buton_plot_corelatii.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.buton_plot_corelatii, 2, 2, 1, 1)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.pushButton, 2, 1, 1, 1)

        self.buton_plot_varianta = QPushButton(self.groupBox_3)
        self.buton_plot_varianta.setObjectName(u"buton_plot_varianta")
        self.buton_plot_varianta.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.buton_plot_varianta, 1, 2, 1, 1)

        self.buton_varianta = QPushButton(self.groupBox_3)
        self.buton_varianta.setObjectName(u"buton_varianta")
        self.buton_varianta.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.buton_varianta, 1, 1, 1, 1)

        self.buton_factorabilitate = QPushButton(self.groupBox_3)
        self.buton_factorabilitate.setObjectName(u"buton_factorabilitate")
        self.buton_factorabilitate.setStyleSheet(u"color: rgb(0, 85, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout_3.addWidget(self.buton_factorabilitate, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 1, 1, 1)

        self.text_out = QTextEdit(self.centralwidget)
        self.text_out.setObjectName(u"text_out")
        self.text_out.setGeometry(QRect(450, 220, 561, 291))
        self.text_out.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1027, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Date", None))
        self.buton_citire.setText(QCoreApplication.translate("MainWindow", u"Set de date", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Index:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Etichete:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Variabile:", None))
        self.buton_selectie.setText(QCoreApplication.translate("MainWindow", u"Selectie", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parametrii", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Axe:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Metoda:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Varimax", None))
        self.check_bartlett.setText(QCoreApplication.translate("MainWindow", u"Utilizare Bartlett", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Rezultate", None))
        self.buton_corelatii.setText(QCoreApplication.translate("MainWindow", u"Corelatii", None))
        self.buton_plot_scoruri.setText(QCoreApplication.translate("MainWindow", u"Plot scoruri", None))
        self.buton_scoruri.setText(QCoreApplication.translate("MainWindow", u"Scoruri", None))
        self.buton_harta.setText(QCoreApplication.translate("MainWindow", u"Harta scoruri", None))
        self.buton_plot_corelatii.setText(QCoreApplication.translate("MainWindow", u"Plot corelatii", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Corelograma", None))
        self.buton_plot_varianta.setText(QCoreApplication.translate("MainWindow", u"Plot varianta", None))
        self.buton_varianta.setText(QCoreApplication.translate("MainWindow", u"Varianta factori", None))
        self.buton_factorabilitate.setText(QCoreApplication.translate("MainWindow", u"Factorabilitate", None))
    # retranslateUi

