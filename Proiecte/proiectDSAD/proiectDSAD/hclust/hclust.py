import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_samples
from graphics import elbow
from scipy.cluster.hierarchy import fcluster


# clasa ajutatoare pentru implementarea analizei de clusterizare HAC
class hclust:
    def __init__(self, t, variabile, metoda="ward"):
        """
        Initializeaza modelul de clusterizare ierarhica.

        :param t: DataFrame - Datele de intrare
        :param variabile: List - Variabile utilizate pentru clusterizare
        :param metoda: str - Metoda de legatura (implicit: "ward")
        """
        self.metoda = metoda
        # extrage valorile pentru variabilele selectate
        self.x = t[variabile].values
        # calculeaza matricea de legaturi intre clustere folosind metoda specificata
        self.h = linkage(self.x, method=metoda)

        # salveaza structura ierarhica intr-un fisier CSV
        t_h = pd.DataFrame(self.h, columns=["Cluster 1", "Cluster 2", "Distanta", "Frecventa"])
        t_h.index.name = "Jonctiune"
        t_h.to_csv("./dataOUT/Ierarhie.csv")

        # etichetele observatiilor
        self.etichete = t.index
        # calculeaza partitia finala a clusterelor
        self.calcul_partitie()

    def calcul_partitie(self, k=None):
        """
        Calculeaza partitia clusterelor, scorurile silhouette si culorile asociate.

        :param k: int - Numarul de clustere (optional)
        """
        # numarul de fuziuni din matricea de legaturi
        nr_jonctiuni = self.h.shape[0]

        # determina numarul optim de clustere daca nu este specificat
        if k is None:
            k_max, k = elbow(self.h[:, 2])
        self.k = k

        # calculeaza pragul de taiere pentru dendrograma
        self.threshold = (self.h[k_max, 2] + self.h[k_max + 1, 2]) / 2

        # genereaza etichete pentru clustere
        self.p = fcluster(self.h, self.threshold, criterion='distance')

        # calculeaza scorurile silhouette pentru validarea calitatii clusterizarii
        self.s_index = silhouette_samples(self.x, self.p)

        # atribuie culori pentru fiecare cluster
        n_clusters = len(np.unique(self.p))
        cmap = plt.get_cmap('viridis')
        self.culori = [cmap(i / n_clusters) for i in range(n_clusters)]

    def plot_ierarhie(self, titlu="Dendograma HAC"):
        """
        Deseneaza dendrograma pentru clusterizarea ierarhica.
        :param titlu: str - Titlul graficului
        """
        # creeaza figura si axele pentru grafic
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_title(f"{titlu} - Metoda: {self.metoda}")
        # deseneaza dendrograma utilizand distantele calculate
        dendrogram(self.h, labels=self.etichete, color_threshold=self.threshold, ax=ax)
        plt.show()
