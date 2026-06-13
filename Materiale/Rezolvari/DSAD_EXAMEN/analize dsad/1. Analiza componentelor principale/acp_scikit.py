import pandas as pd
import numpy as np
from util import *
from sklearn.decomposition import PCA


def execute():
    tabel = pd.read_csv("Freelancer.csv", index_col=0)
    nan_replace(tabel)

    nume_variabile = list(tabel.columns)[2:]

    x = (tabel[nume_variabile] - np.mean(tabel[nume_variabile], axis=0)) / np.std(tabel[nume_variabile], axis=0)

    # construire model ACP + "rulare"
    model_acp = PCA()
    model_acp.fit(x)

    alpha = model_acp.explained_variance_
    print("Alpha: ", alpha)
    a = model_acp.components_
    print("A: ", a)
    c = model_acp.transform(x)
    print("C: ", c)

    tabel_componente = tabelare_matrice(c, tabel.index,
                        ["Comp" + str(i + 1) for i in range(len(alpha))], "Componente_Scikit.csv")
    plot_componente(tabel_componente, "Comp1", "Comp2")
    show()


if __name__ == "__main__":
    execute()
