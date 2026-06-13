import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as hclust
from utils import nan_replace, histograma, show, partitie


def execute():
    tabel = pd.read_csv("./dataIN/ADN_Tari.csv", index_col=0)
    variabile = list(tabel)[1:]
    instante = list(tabel.index)

    n = len(instante)
    m = len(variabile)

    x = tabel[variabile].values
    nan_replace(x)

    # construire ierarhie
    metoda = "ward"
    h = hclust.linkage(x, method=metoda)
    print("h", h)

    p = n-1

    k_dif_max = np.argmax(h[1:, 2] - h[:(p-1), 2])
    print("k_dif_max", k_dif_max)
    nr_clusteri = p - k_dif_max
    print(nr_clusteri)

    partitie_opt_2 = partitie(h, nr_clusteri, p, instante, metoda)
    print("partitie_opt_2", partitie_opt_2)

    partitie_opt_2_t = pd.DataFrame(
        data={"Cluster": partitie_opt_2},
        index=instante
    )
    partitie_opt_2_t.to_csv("./dataOUT/partitie_opt_2.csv")

    partitie_opt_3 = partitie(h, 3, p, instante, metoda)
    print("partitie_opt_3", partitie_opt_3)

    partitie_opt_3_t = pd.DataFrame(
        data={"Cluster": partitie_opt_3},
        index=instante
    )
    partitie_opt_3_t.to_csv("./dataOUT/partitie_opt_3.csv")

    partitie_opt_4 = partitie(h, 4, p, instante, metoda)
    print("partitie_opt_4", partitie_opt_4)

    partitie_opt_4_t = pd.DataFrame(
        data={"Cluster": partitie_opt_4},
        index=instante
    )
    partitie_opt_4_t.to_csv("./dataOUT/partitie_opt_4.csv")

    for i in range(m):
        histograma(x[:, i], variabile[i], partitie_opt_2)

    show()


if __name__ == "__main__":
    execute()