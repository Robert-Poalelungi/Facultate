from PySide2 import QtWidgets
from PySide2.QtGui import QKeySequence
import PySide2.QtWidgets as qw
# from PySide2.QtWidgets import QMainWindow, QAction, QWidget, QHBoxLayout, QSizePolicy, QHeaderView, QPushButton, QVBoxLayout
from PySide2.QtWidgets import QApplication as qApp
from PySide2.QtCore import QAbstractTableModel, Qt

# Clasa pe post de container greu. Este extensie de QMainWindow care este container greu Qt
class Frame(qw.QMainWindow):
    # Constructor care primeste un panel de continut si titlul
    def __init__(self, panel,titlu):
        qw.QMainWindow.__init__(self)
        self.setWindowTitle(titlu)

        self.setCentralWidget(panel)
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = qw.QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)


        # Dimensionare fereastra
        self.adjustSize() #Punde dimensiunea in functie de continut

        # Pune dimensiunea in raport de rezolutia ecranului
        # geometry = qApp.desktop().availableGeometry(self)
        # self.setFixedSize(geometry.width() * 0.5, geometry.height() * 0.5)


# Clasa care defineste un model de tabel
# Necesita completare pentru a colora anumite celule dupa valoare, sau sortari etc.
# Vezi articolul dedicat din fisierul word de rezumat
class ModelTabel(QAbstractTableModel):
    # Primeste un pandas DataFrame
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
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

# Clasa de tip tabel
class Tabel(QtWidgets.QTableView):
    def __init__(self, data):
        QtWidgets.QTableView.__init__(self)
        self.horizontalHeader().setSectionResizeMode(
            qw.QHeaderView.ResizeToContents
        )
        self.verticalHeader().setSectionResizeMode(
            qw.QHeaderView.ResizeToContents
        )
        # self.horizontalHeader().setStretchLastSection(True) #Forteaza dimensiunea ultimei coloane
        size = qw.QSizePolicy(qw.QSizePolicy.Preferred, qw.QSizePolicy.Preferred)
        size.setHorizontalStretch(1)
        self.setSizePolicy(size)
        # Ii stabilesc modelul de data
        self.setModel(ModelTabel(data=data))
        self.setFixedSize(700,400)

# Panelul de continut. Primeste un gestionar de pozitionare. In acesta pun totul
class Panel(qw.QWidget):
    def __init__(self,gestionar_pozitionare):
        qw.QWidget.__init__(self)
        self.main_layout = gestionar_pozitionare
        self.setLayout(self.main_layout)

# Clasa generalizare buton
class Buton(qw.QPushButton):
    def __init__(self,text,w,h,stil=None,click = None):
        qw.QPushButton.__init__(self,text)
        self.setFixedHeight(h)
        self.setFixedWidth(w)
        if stil is not None:
            self.setStyleSheet(stil)
        if click is not None:
            self.clicked.connect(click)

# Clasa generalizare eticheta
class Eticheta(qw.QLabel):
    def __init__(self,text,w=None,h=None,stil=None):
        qw.QLabel.__init__(self,text)
        if w is not None:
            self.setFixedWidth(w)
        if h is not None:
            self.setFixedHeight(h)
        if stil is not None:
            self.setStyleSheet(stil)
