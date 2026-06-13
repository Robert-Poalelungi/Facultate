# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_harta.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(552, 393)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 20, 511, 101))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.buton_fisier = QPushButton(self.formLayoutWidget)
        self.buton_fisier.setObjectName(u"buton_fisier")
        self.buton_fisier.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.buton_fisier)

        self.text_fisier = QLineEdit(self.formLayoutWidget)
        self.text_fisier.setObjectName(u"text_fisier")
        self.text_fisier.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.text_fisier)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.combo_index = QComboBox(self.formLayoutWidget)
        self.combo_index.setObjectName(u"combo_index")
        self.combo_index.setMinimumSize(QSize(200, 0))
        self.combo_index.setMaximumSize(QSize(200, 16777215))
        self.combo_index.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.combo_index)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.combo_tip_index = QComboBox(self.formLayoutWidget)
        self.combo_tip_index.setObjectName(u"combo_tip_index")
        self.combo_tip_index.setMinimumSize(QSize(200, 0))
        self.combo_tip_index.setMaximumSize(QSize(200, 16777215))
        self.combo_tip_index.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.combo_tip_index)

        self.formLayoutWidget_2 = QWidget(Dialog)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 140, 511, 191))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.list_spatial = QListWidget(self.formLayoutWidget_2)
        self.list_spatial.setObjectName(u"list_spatial")
        self.list_spatial.setMinimumSize(QSize(250, 0))
        self.list_spatial.setMaximumSize(QSize(250, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.list_spatial)

        self.list_harta = QListWidget(self.formLayoutWidget_2)
        self.list_harta.setObjectName(u"list_harta")
        self.list_harta.setMinimumSize(QSize(250, 0))
        self.list_harta.setMaximumSize(QSize(250, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.list_harta)

        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.combo_tip_bokeh = QComboBox(self.formLayoutWidget_2)
        self.combo_tip_bokeh.setObjectName(u"combo_tip_bokeh")
        self.combo_tip_bokeh.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.combo_tip_bokeh)

        self.buton_harta = QPushButton(Dialog)
        self.buton_harta.setObjectName(u"buton_harta")
        self.buton_harta.setGeometry(QRect(20, 340, 251, 31))
        self.buton_harta.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")
        self.buton_bokeh = QPushButton(Dialog)
        self.buton_bokeh.setObjectName(u"buton_bokeh")
        self.buton_bokeh.setGeometry(QRect(280, 340, 251, 31))
        self.buton_bokeh.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 85, 0);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.buton_fisier.setText(QCoreApplication.translate("Dialog", u"Fisier spatial", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Index:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Tip index:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Informatii fisier spatial:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Campuri harta:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Tip camp harta pentru Bokeh:", None))
        self.buton_harta.setText(QCoreApplication.translate("Dialog", u"PLot harti GeoPandas", None))
        self.buton_bokeh.setText(QCoreApplication.translate("Dialog", u"Plot harta Bokeh", None))
    # retranslateUi

