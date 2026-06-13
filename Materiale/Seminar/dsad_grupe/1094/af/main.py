# V1, V2 ... Vn
#
# ...... Analiza Componentelor Principale
#
# C1 = a11 * V1 + a12 * V2 + ... + a1n * Vn
# C2 = a21 * V1 + a22 * V2 + ... + a2n * Vn
# ...
# Cn = an1 * V1 + an2 * V2 + ... + ann * Vn
#
# ...... Analiza Factoriala
# V1 = a11 * F1 + a12 * F2 + ... + a1n * Fn + E1
# V2 = a21 * F1 + a22 * F2 + ... + a2n * Fn + E2
# ...
# Vn = an1 * F1 + an2 * F2 + ... + ann * Fn + En

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
from pandas.core.dtypes.common import is_numeric_dtype


def nan_replace(df):
    for col in df.columns:
        if df[col].isna().any():
            if is_numeric_dtype(df[col]):
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)


def to_dataframe(x, row_names, col_names, filename):
    df = pd.DataFrame(x, index=row_names, columns=col_names)
    df.to_csv(filename)
    return df


def scree_plot(valori_proprii):
    """
    Reprezentam grafic valorile proprii in ordine descrescatoare si alegem numarul de factori latenti semnificativi folosind
    criteriul Kaiser: conform acestui criteriu sunt considerati factori semnificativi acei factori care au val. prop. > 1
    """
    plt.figure(figsize=(8,6))
    plt.plot(range(1, len(valori_proprii)+1), valori_proprii, marker='o')
    plt.title('Scree plot')
    plt.xlabel('Componenta/Factor')
    plt.ylabel('Valoare proprie')
    plt.axhline(1, color='red', linestyle='--')  # 1 deoarece cf crit. Kaiser factori latenti semnificativi sunt cei cu valoarea proprie > 1
    plt.show()


def heatmap(df, vmin=0, vmax=1, title="Heatmap"):
    """
    Grafic de uz general folosit pentru a vizuliza legaturile dintre:
    - corelatii
    - comunalitati
    - factori de incarcare (loadings)
    """
    plt.figure(figsize=(8, 6))
    sb.heatmap(df, vmin=vmin, vmax=vmax, annot=True, cmap="RdYlGn")
    plt.title(title)
    plt.show()


def main():
    # citim setul de date
    df = pd.read_csv("Freelancer.csv", index_col=1)
    nan_replace(df)

    # C,C_Test,Html,Html_test,Java,Java_test,PHP,PHP_test,InternetPenetration,InternetUsers,UploadSpeed,Download,FixedBroadbandSubscriptions,ChargesIntellProperty,GovernmentExpenditureOnEducation,GrossEnrolmentRatio,HighTechnologyExports,GINIindex,IncomeShareLow20,SurveyMeanIncome,Unemployment,UnemploymentTertiaryEducation,GDP_BM
    variable_names = list(df.columns)[2:]
    x = df[variable_names].values

    # teste care raspund intrebarii: se preteaza datele noastre initiale la Analiza Factoriala?
    # testele: Bartlett si KMO
    # testul Bartlett verifica daca matricea coeficientilor de corelatie difera semnificativ de matricea identitate I
    # testul Bartlett este un test de tip Student cu H0: nu exista corelatii intre variabilele initiale si H1: exista corelatii

    # testul KMO verifica daca exista corelatii partiale si cat de compacte sunt acestea

    chi2, p_value = calculate_bartlett_sphericity(x)
    print(f"Bartlett: chi2 = {chi2}, p_value = {p_value}")

    if p_value > 0.05:
        print("Bartlett p_value este prea mare, iar prin urmare se accepta ipoteza nula H0 - nu putem aplica Analiza Factoriala")
        return

    kmo_all, kmo_overall = calculate_kmo(x)
    print(f"KMO overall: {kmo_overall}")

    if kmo_overall < 0.6:
        print("KMO value este prea mic, prin urmare datele noastre nu se preteaza la Analiza Factoriala")
        return

    # determinarea numarului de factori latenti semnificativi
    fa_n = FactorAnalyzer(rotation=None)
    fa_n.fit(x)

    valori_proprii, _ = fa_n.get_eigenvalues()
    print(f"Valori proprii: ", valori_proprii)

    # conform crit. Kaiser: vom considera ca fiind semnificativi acei factori care au valorile_proprii > 1
    n_factori = sum(valori_proprii > 1)
    print("Numar factori latenti semnificativi:", n_factori)

    scree_plot(valori_proprii)

    # initializam un nou model de AF folosind n_factors = 7 si rotation='varimax'
    fa = FactorAnalyzer(n_factors=n_factori, rotation='varimax')
    fa.fit(x)

    factor_labels = [f"F{i+1}" for i in range(n_factori)]

    # loadings - factori de incarcare = reprezinta cat de importanti sunt factorii pentru variabilele initiale
    # principalul output al Analizei Factoriale
    loadings = fa.loadings_
    loadings_df = to_dataframe(loadings, variable_names, factor_labels, "Loadings.csv")
    print("Loadings:", loadings_df)

    heatmap(loadings_df, vmin=-1, vmax=1, title='Factor loadings')

    # comunalitati
    # proportia dispersiei(variantei) explicate de toti factorii latenti impreuna
    comunalitati = fa.get_communalities()
    comunalitati_df = to_dataframe(comunalitati, variable_names, ["Comunalitati"], "Comunalities.csv")
    heatmap(comunalitati_df, vmin=0, vmax=1, title='Comunalities')

    # dispersie explicata
    # - dispersie la nivelul fiecarui factor
    # - proportia dispersiei
    # - dispersia cumulata
    dispersie, dispersie_prop, dispersie_cum = fa.get_factor_variance()
    dispersie_df = pd.DataFrame(data={
        "Dispersie": dispersie,
        "Proportie": dispersie_prop,
        "Cumulat": dispersie_cum
    }, index=factor_labels)
    dispersie_df.to_csv("Dispersie.csv")
    print("Dispersie:", dispersie_df)

    # scoruri factoriale
    # coordonatele observatiilor initiale (randurilor) in spatiul factorilor


    scoruri = fa.transform(x)
    scoruri_df = to_dataframe(scoruri, df.index, factor_labels, "Scoruri.csv")

    plt.figure(figsize=(8,6))
    plt.scatter(scoruri_df["F1"], scoruri_df["F2"])

    for i in range(len(scoruri_df)):
        plt.text(scoruri_df["F1"].iloc[i], scoruri_df["F2"].iloc[i], scoruri_df.index[i])

    plt.title("Scoruri factoriale F1 vs F2")
    plt.xlabel("F1")
    plt.ylabel("F2")
    plt.show()


main()




