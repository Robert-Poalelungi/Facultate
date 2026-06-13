from gui_harta import *
import controller
from geopandas import GeoDataFrame
from grafice import harta, show, plot_bokeh


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, t, parent):
        QDialog.__init__(self, parent)
        self.setModal(0)
        self.setupUi(self)
        self.t = t
        controller.init_list_check(self.list_harta, list(t))
        controller.init_combo(self.combo_tip_bokeh, ["Numeric", "Categorial"])
        controller.init_combo(self.combo_tip_index, ["Numeric", "Categorial"])
        self.buton_fisier.clicked.connect(self.citire_fisier_spatial)
        self.buton_harta.clicked.connect(self.desenare_harti)
        self.buton_bokeh.clicked.connect(self.desenare_harta_Bokeh)

    def desenare_harti(self):
        variabile_harta = controller.selectii_lista(self.list_harta)
        harta(self.t_spatial, self.combo_index.currentText(), self.t[variabile_harta],titlu="Map of factor scores",min_max_comun=False)
        show()

    def desenare_harta_Bokeh(self):
        variabile_informatii = controller.selectii_lista(self.list_spatial)
        camp_harta = controller.selectii_lista(self.list_harta)[0]
        plot_bokeh(self.t_spatial, self.combo_index.currentText(),self.combo_tip_index.currentText(), variabile_informatii,
                   self.t, camp_harta, self.combo_tip_bokeh.currentText())

    def citire_fisier_spatial(self):
        dialog = QFileDialog(directory=".")
        dialog.setNameFilter("Fisiere shp (*.shp)")
        dialog.exec_()
        fisiere = dialog.selectedFiles()
        if len(fisiere) > 0:
            self.t_spatial = GeoDataFrame.from_file(fisiere[0])
            self.text_fisier.setText(fisiere[0])
            self.variabile_spatiale = list(self.t_spatial)
            controller.init_combo(self.combo_index, self.variabile_spatiale)
            controller.init_list_check(self.list_spatial, self.variabile_spatiale)
