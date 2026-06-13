"""
Analiza corelatiilor canonice = tehnica de reducere a dimensionalitatii

Recapitulativ:
- analiza in comp. principale: daca putem grupa var initiale in combinatii liniare, a.i. sa maximizam dispersia
- analiza factoriala: daca putem identifica o serie de factori latenti care sa explice dispersia din variabilele initiale

Analiza corelatiilor canonice cauta sa identifice perechi de combinatii liniare in seturile initiale de date,
combinatii liniare ce sunt maxim corelate intre ele.
Prin urmare, nu mai vorbim de un singur set de date, ci de mai multe (2, notate X si Y).

Zk = akT * X
Uk = bkT * Y
corr(Zk, Uk) sa fie maxim

(zk, uk) sunt practic perechi de forma [(z1, u1), (z2, u2), ... (zm, um)]

Analiza corelatiilor canonice se utilizeaza in viata reala in:
- economie si demografie:
    indicatori de sanatate - indicatori socio-economici
    mortalitate - infrastructura, mediu, urbanizare

- psihologie:
    teste cognitive - trasaturi de personalitate
    neurosemnale - comportamente masurate

- marketing:
    comportamentul consumatorului - date demografice
    cheltuieli cu publicitatea - metrici din vanzari

Concepte relevante pentru ACC:
 - corelatii canonice = intensitatea legaturilor intre 2 seturi de date
 - componente canonice z si u (canonical variates) = variabile noi, sintetice, caree sumarizeaza informational seturile initiale
 - scoruri canonice = coordonatele observatiilor initiale in spatiul componentelor canonice
 - factori de incarcare canonici (canonical loadings) = corelatiile dintre variabilele initiale si comp. canonice
 - indici de redundanta = sunt legaturile/componentele canonice utile/relevante in practica in analiza
 - Bartlett test = cate dintre perechile de componente canonice sunt relevante

ACC este o tehnica de reducere a dimensionalitatii deoarece obtinem rezultate derivate de forma:
    z1 este o combinatie liniara a variabilelor initiale X, insa din toate, doar cateva vor fi relevante
    u1 este o combinatie liniara a variabilelor initiale Y, insa din toate, doar cateva vor fi relevante
    si intr-un scenariu optimist z1 si u1 sunt corelate si explica un procent semnificativ din varianta totala

prin urmare, in loc sa incercam sa interpretam relatiile dintre nr de variabile din X si nr de variabile din Y, vom
restrange domeniul de analiza la nr de variabile semnificative pt z (2-3-4) vs nr de variabile semnificative pt u
"""

import numpy as np
import pandas as pd
from sklearn.cross_decomposition import CCA
from sklearn.preprocessing import StandardScaler
from utils import *


def main():
    # citire seturi de date si inlocuire celule lipsa
    # X: date despre mortalitate
    # Y: indicatori socio-economici
    # arhiva res se gaseste pe gitlab in "shared resources\acc"
    df1 = pd.read_csv('res/mortalitate.csv', index_col=1)
    nan_replace(df1)

    df2 = pd.read_csv('res/Teritorial.csv', index_col=1)
    nan_replace(df2)

    # extragerea variabilelor si a observatiilor
    variabile_x = list(df1.columns)[1:]  # eliminam coloana Judet
    variabile_y = list(df2.columns)[3:]  # eliminam coloanele Judet, Regiune, Macroregiune

    # restrangerea setului de date astfel incat sa pastram doar randurile comune
    df_merged = df1[variabile_x].join(df2[variabile_y], how='inner')

    nume_instante = df_merged.index
    x = df_merged[variabile_x].values
    y = df_merged[variabile_y].values

    # determinarea numarului maxim de perechi de componente canonice
    n, p = x.shape  # n - nr randuri (judete) si q - nr coloane
    _, q = y.shape  # _ - ignoram numarul randuri (este acelasi cu n de mai sus), q - nr coloane

    m = min(p, q)  # numarul maxim de dimensiuni canonice (de perechi)

    # standardizarea datelor - un pas f important in ACC
    sc_x = StandardScaler()
    sc_y = StandardScaler()

    x = sc_x.fit_transform(x)
    y = sc_y.fit_transform(y)

    # etichete / labels
    etichete_z = ['z' + str(i+1) for i in range(m)]
    etichete_u = ['u' + str(i+1) for i in range(m)]
    etichete_radacini = ['rad' + str(i+1) for i in range(m)]

    # constructia si antrenareea modelului ACC
    model_cca = CCA(n_components=m)
    model_cca.fit(x, y)

    # determinarea componentelor canonice z si u (canonical variates)
    # z: combinatie liniara de X
    # u: combinatie liniara de Y
    z, u = model_cca.transform(x, y)

    # z si u in pct de fata reprezinta liste de combinatii liniare forma:
    # z: [z1, z2, z3, ... zm]
    # u: [u1, u2, u3, ... um]

    # corelatii canonice - vom calcula coef de corlatie pentru fiecare pereche:
    # r = [corrcoef(z1, u1), corrcoef(z2, u2), ... corrcoef(zm, um)]
    r = np.array([np.corrcoef(z[:, i], u[:, i])[0, 1] for i in range(m)])
    r_squared = r ** 2

    # testul Bartlett - testarea perechilor de componente canonice semnificative
    p_values = test_bartlett(r_squared, n, p, q, m)
    df_radacini = pd.DataFrame({
        "R": np.round(r, 3),
        "R2": np.round(r_squared, 3),
        "p_value": np.round(p_values, 4)
    }, index=etichete_radacini)
    df_radacini.to_csv("radacini_canonice.csv")

    # numarul de perechi de componente canonice (zi, ui) semnificative
    nr_rad_semnificative = np.sum(p_values < 0.05)
    print(df_radacini)
    print("Numar dimensiuni canonice:", nr_rad_semnificative)

    # factori de incarcare canonici (canonical loadings)
    # - corelatiile dintre variabilele initiale si componentele canonice
    z_std = np.std(z, axis=0, ddof=1)
    u_std = np.std(u, axis=0, ddof=1)

    r_xz = model_cca.x_loadings_ * z_std
    r_yu = model_cca.y_loadings_ * u_std

    df_r_xz = to_dataframe(r_xz, variabile_x, etichete_z, "r_xz.csv")
    df_r_yu = to_dataframe(r_yu, variabile_y, etichete_u, "r_yu.csv")

    # indici de redundanta (de regula nu sunt ceruti la examen, insa in practica sunt f importanti)
    # acesti indici de redundanta raspund intrebarii: cat de multa dispersie intr-un set de date este explicata de catre celalalt set?
    redund_x = np.mean(r_xz[:, :nr_rad_semnificative] ** 2, axis=0) * r_squared[:nr_rad_semnificative]
    redund_y = np.mean(r_yu[:, :nr_rad_semnificative] ** 2, axis=0) * r_squared[:nr_rad_semnificative]

    print("Redundanta X -> Y:", redund_x)
    print("Redundanta Y -> X:", redund_y)

    # scoruri canonice
    df_scoruri_z = to_dataframe(z, nume_instante, etichete_z, "scoruri_z.csv")
    df_scoruri_u = to_dataframe(u, nume_instante, etichete_u, "scoruri_u.csv")

    # grafice
    for i in range(nr_rad_semnificative):
        plot_corelatii(df_r_xz, "z1", etichete_z[i],
                       df_r_yu, "u1", etichete_u[i])

        scatter_2d(df_scoruri_z, 'z1', etichete_z[i],
                   df_scoruri_u, "u1", etichete_u[i])

        show()


if __name__ == '__main__':
    main()
