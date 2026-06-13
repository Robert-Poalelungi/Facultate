import numpy as np
import pandas as pd
from sklearn.cross_decomposition import CCA
from sklearn.preprocessing import normalize
from util import *

# Analiza Corelatiilor Canonice (CCA)
def execute():
    t1 = pd.read_csv("./dataIN/mortalitate.csv", index_col=1)
    variabile1 = list(t1)[1:]

    t2 = pd.read_csv("./dataIN/teritorial.csv", index_col=1)
    variabile2 = list(t2)[3:]

    nan_replace(t1)
    nan_replace(t2)

    t = t1[variabile1].join(t2[variabile2], how="inner")
    nume_instante = t.index

    x = t[variabile1].values
    y = t[variabile2].values

    n, p = x.shape  # n = numarul de instante (nr randuri)
    _, q = y.shape

    m = min(p, q)  # m = numar radacini posibile (nr coloane)

    et_z = ["z"+str(i+1) for i in range(m)]
    et_u = ["u" + str(i + 1) for i in range(m)]
    et_rad = ["rad" + str(i + 1) for i in range(m)]

    # construire model CCA
    model_cca = CCA(m)
    model_cca.fit(x, y)

    # calcul variabile canonice (scoruri canonice) z, u
    z, u = model_cca.transform(x, y)

    z_std = np.std(z, axis=0, ddof=1)
    u_std = np.std(u, axis=0, ddof=1)

    # normalizare variabile canonice
    normalize(z, axis=0, copy=False)
    normalize(u, axis=0, copy=False)

    # identificare radacini semnificative (zk, uk)
    lista_r = list()
    for i in range(m):
        lista_r.append(np.corrcoef(z[:, i], u[:,i])[0, 1])

    array = np.array(lista_r)
    r2 = array * array

    p_values = test_bartlett(r2, n, p, q, m)
    print("p_values test_bartlett", p_values)

    tabel_radacini = pd.DataFrame(
        data={
            'R': np.round(array, 3),
            'R2': np.round(r2, 3),
            "p_values": np.round(p_values, 5)
        },
        index=et_rad
    )

    tabel_radacini.to_csv("./dataOUT/radacini.csv")

    criteriu_radacini = np.where(p_values > 0.05)
    print("Criteriu alegere: ", criteriu_radacini)

    nr_rad_semnificative = criteriu_radacini[0][0]
    print("Nr rad semnificative: ", nr_rad_semnificative)

    # calcul corelatii dintr var observate si var canonice
    r_xz = model_cca.x_loadings_ * z_std
    tabel_r_xz = tabelare_matrice(r_xz, variabile1, et_z, "./dataOUT/r_xz.csv")

    r_yu = model_cca.y_loadings_ * u_std
    tabel_r_yu = tabelare_matrice(r_yu, variabile2, et_u, "./dataOUT/r_yu.csv")

    # afisare grafice
    for i in range(1, nr_rad_semnificative):
        plot_corelatii(tabel_r_xz, "z1", et_z[i], tabel_r_yu, "u1", et_u[i])

    tabel_z = tabelare_matrice(z, nume_instante, et_z, "./dataOUT/z.csv")
    tabel_u = tabelare_matrice(u, nume_instante, et_u, "./dataOUT/u.csv")

    for i in range(1, nr_rad_semnificative):
        scatter(tabel_z, "z1", et_z[i], tabel_u, "u1", et_u[i])


if __name__ == "_main_":
    execute()
