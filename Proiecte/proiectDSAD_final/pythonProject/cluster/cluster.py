import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_samples
from scipy.cluster.hierarchy import fcluster


# Clasa pentru analiza de clusterizare HAC
class hclust:
    def __init__(self, t, variabile, metoda="ward"):
        """
        Initializeaza modelul de clusterizare ierarhica.

        :param t: DataFrame - Datele de intrare
        :param variabile: List - Variabile utilizate pentru clusterizare
        :param metoda: str - Metoda de legatura (implicit: "ward")
        """
        self.metoda = metoda
        self.x = t[variabile].values
        self.h = linkage(self.x, method=metoda)

        # Salveaza structura ierarhica intr-un fisier CSV
        t_h = pd.DataFrame(self.h, columns=["Cluster 1", "Cluster 2", "Distanta", "Frecventa"])
        t_h.index.name = "Jonctiune"
        t_h.to_csv("./dateOUT/Ierarhie.csv")

        self.etichete = t.index
        self.threshold = None  # Inițializare `threshold`
        self.p = None  # Inițializare pentru clustere
        self.calcul_partitie()  # Calculați partitia implicit

    def calcul_partitie(self, k=None):
        """
        Calculeaza partitia clusterelor, scorurile silhouette si culorile asociate.

        :param k: int - Numarul de clustere (optional)
        """
        # Distanțe din matricea de linkage
        distante = self.h[:, 2]

        # Determina numarul optim de clustere daca nu este specificat
        if k is None:
            k = 3  # Valoare implicită, poate fi înlocuită cu o metodă automată

        self.threshold = (distante[-k] + distante[-k + 1]) / 2

        # Genereaza etichete pentru clustere
        self.p = fcluster(self.h, self.threshold, criterion='distance')

    def plot_ierarhie(self, titlu="Dendograma HAC"):
        """
        Deseneaza dendrograma pentru clusterizarea ierarhica.
        :param titlu: str - Titlul graficului
        """
        if self.threshold is None:
            raise ValueError("Threshold nu a fost calculat. Apelati `calcul_partitie` mai intai.")

        # Creeaza figura si axele pentru grafic
        fig, ax = plt.subplots(figsize=(12, 7))
        ax.set_title(f"{titlu} - Metoda: {self.metoda}")

        # Utilizare corectă a etichetelor
        dendrogram(self.h, labels=list(self.etichete), leaf_rotation=90, ax=ax)

        plt.xlabel("Țări")
        plt.ylabel("Distanță")
        plt.grid()
        plt.show()