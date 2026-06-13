# from PySide2.QtWidgets import *
# from PySide2.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import pandas as pd


# Selectie generala intr-o lista de obiecte QCheckBox
# lista - lista QListWidget de obiecte QCheckBox
def selectie_generala(lista):
    for i in range(lista.count()):
        item = lista.item(i)
        check = lista.itemWidget(item)
        assert isinstance(check, QCheckBox)
        check.setChecked(not check.isChecked())


# Initializare combo
# combo - QComboBox
# items - lista de siruri
def init_combo(combo, items):
    combo.clear()
    combo.addItems(items)
    combo.setCurrentIndex(0)


# Initializare lista 'list_check' cu elemente din lista items
def init_list_check(list_check, items):
    list_check.clear()
    for v in items:
        item = QListWidgetItem(list_check)
        cb = QCheckBox(v)
        list_check.setItemWidget(item, cb)


# Citire fisier cu rezultat in tabel
# Este intors tabelul si numele fisierului
def citire_fisier(director="."):
    dialog = QFileDialog(directory=director)
    dialog.setNameFilter("Fisiere csv (*.csv)")
    dialog.exec_()
    fisiere = dialog.selectedFiles()
    if len(fisiere) > 0:
        return pd.read_csv(fisiere[0]), fisiere[0]


# Citire fisier, variabile si variabila index cu QFileDialog
# lista - obiect QListWidget
# combo - obiect QComboBox
# Este intors tabelul si numele fisierului
def citire_fisier_variabile(combo=None, lista=None, director="."):
    dialog = QFileDialog(directory=director)
    dialog.setNameFilter("Fisiere csv (*.csv)")
    dialog.exec_()
    fisiere = dialog.selectedFiles()
    if len(fisiere) > 0:
        t = pd.read_csv(fisiere[0])
        variabile = list(t)
        if combo is not None:
            combo.clear()
            combo.addItems(variabile)
            combo.setCurrentIndex(0)
        if lista is not None:
            lista.clear()
            for v in variabile:
                item = QListWidgetItem(lista)
                cb = QCheckBox(v)
                lista.setItemWidget(item, cb)
        return t, fisiere[0]


class ModelTabel(QAbstractTableModel):
    def __init__(self, data):
        super(ModelTabel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            coloana = index.column()
            linia = index.row()
            valoare = self._data.iloc[linia, coloana]
            return str(valoare)

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data.columns)

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])


# t - Tabelul vizualizat (DataFrame)
def afisare_tabel(t, w=700, h=500, titlu="Tabel"):
    tabel = QTableView()
    model = ModelTabel(data=t)
    tabel.setModel(model)
    tabel.setFixedSize(w, h)
    layout1 = QHBoxLayout()
    layout1.addWidget(tabel)
    dialog = QDialog()

    dialog.setWindowTitle(titlu)
    dialog.setLayout(layout1)
    dialog.setWindowModality(Qt.NonModal)
    # dialog.setModal(True)
    dialog.show()



class DialogNonModal(QDialog):
    def __init__(self, parent, t, w=700, h=500, titlu="Tabel"):
        QDialog.__init__(self, parent)
        self.setModal(0)

        tabel = QTableView()
        model = ModelTabel(data=t)
        tabel.setModel(model)
        tabel.setFixedSize(w, h)
        layout1 = QHBoxLayout()
        layout1.addWidget(tabel)
        self.setLayout(layout1)

        # b1 = QPushButton("ok", self)
        # layout1 = QHBoxLayout()
        # layout1.addWidget(b1)
        # self.setLayout(layout1)
        # b1.clicked.connect(self.exit)
        self.setWindowTitle(titlu)

# Preluare selectii dintr-o lista QListWidget de obiecte QCheckBox
def selectii_lista(lista):
    variabile_selectate = []
    for i in range(lista.count()):
        item = lista.item(i)
        check = lista.itemWidget(item)
        assert isinstance(check, QCheckBox)
        if check.isChecked():
            variabile_selectate.append(check.text())
    return variabile_selectate


#
def adugare_tabel_QTextEdit(text_edit, tabel):
    assert isinstance(text_edit, QTextEdit)
    assert isinstance(tabel, pd.DataFrame)
    text_edit.append(",".join(tabel.columns))
    n = len(tabel)
    for i in range(n):
        text_edit.append(tabel.index[i] + "," + ",".join([str(v) for v in tabel.iloc[i, :]]))
