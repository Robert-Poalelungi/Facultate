import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
from pandas.core.dtypes.common import is_numeric_dtype

# pip install factor_analyzer

# analiza in comp. principale
# C1 = a11 * V1 = a12 * V2 + ... + a1n * Vn
# C2 = a21 * V1 = a22 * V2 + ... + a2n * Vn
# ...
# Cn = an1 * V1 = an2 * V2 + ... + ann * Vn

# analiza factoriala
# V1 = a11 * F1 = a12 * F2 + ... + a1n * Fn + E1
# V2 = a21 * F1 = a22 * F2 + ... + a2n * Fn + E2
# ...
# Vn = an1 * F1 = an2 * F2 + ... + ann * Fn + En

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
    Reprezentam grafic valorile proprii in ordine descrescatoare.
    Acest grafic ne ajuta sa alegem numarul factorilor latenti semnificativi.
    In selectia acestui numar se foloseste critriul Kaiser, conform caruia sunt considerati
    factori semnificativi, aceia care au valoarea proprie asociata > 1
    """
    plt.figure(figsize=(8,6))
    plt.plot(range(1, len(valori_proprii) + 1), valori_proprii, marker='o')
    plt.title("Scree plot")
    plt.xlabel("Factor")
    plt.ylabel("Valoare proprie")
    # alegem valoarea 1 deoarece crit. Kaiser foloseste 1 ca prag de selectie
    plt.axhline(1, color='red', linestyle='--')
    plt.show()


def heatmap(df, vmin=0, vmax=1, title='Heatmap'):
    """
    Grafic de uz general folosit pentru a evidentia legatura dintre:
    - corelatii
    - comunalitati
    - factori de incarcare (loadings)
    """
    plt.figure(figsize=(8,6))
    sb.heatmap(df, vmin=vmin, vmax=vmax, annot=True, cmap='RdYlGn')
    plt.title(title)
    plt.show()


def main():
    # citim date
    df = pd.read_csv("Freelancer.csv", index_col=1)
    nan_replace(df)

    variable_names = list(df.columns)[2:]
    x = df[variable_names].values

    # teste care raspund intrebarii: pot aplica Analiza Factoriala pe datele mele?
    # exista 2 teste: Bartlett si KMO
    # testul Bartlett este un test tip Student - are 2 ipoteze H0: nu exista corelatii intre variabilele initiale si H1: exista corelatie
    # testul Bartlett compara matricea coef de corelatie a variabilelor initiale cu matricea identitate I

    # testul KMO masoara daca exista corelatii partiale la nivelul datelor si cat de compacte sunt acestea

    chi2, p_value = calculate_bartlett_sphericity(x)
    print(f"Bartlett: chi2 = {chi2}, p_value = {p_value}")

    if p_value > 0.05:
        print("Valoarea p_value este prea mare, prin urmare nu putem respinge H0 si nu putem aplica AF")
        return

    kmo_all, kmo_overall = calculate_kmo(x)
    print(f"KMO: kmo_overall = {kmo_overall}")

    if kmo_overall < 0.6:
        print("Valoarea kmo_overall este prea mica si nu putem aplica AF")
        return

    # determinarea numarului de factori latenti semnificativi
    fa_n = FactorAnalyzer(rotation=None)
    fa_n.fit(x)

    valori_proprii, _  = fa_n.get_eigenvalues()
    print("Valori proprii: ", valori_proprii)

    # selectia se face folosind criteriul Kaiser
    n_factori = sum(valori_proprii > 1)
    print("Numar factori latenti semnificativi:", n_factori)

    scree_plot(valori_proprii)

    # re-initializarea modelului de AF folosind n_factori si rotation='varimax'
    fa = FactorAnalyzer(n_factors=n_factori, rotation='varimax')
    fa.fit(x)

    factor_labels = [f"F{i+1}" for i in range(n_factori)]

    # loadings = reprezinta importanta sau cat de relevant e fiecare factor pentru fiecare variabila initiala
    loadings = fa.loadings_
    loadings_df = to_dataframe(loadings, variable_names, factor_labels, "Loadings.csv")
    heatmap(loadings_df, vmin=-1, vmax=1, title="Factor loadings")

    # comunalitati = proportia dispersiei (variantei) explicate de catre toti factorii semnificativi (in cazul nostru 7)
    #               pentru fiecare variabila in parte
    comunalitati = fa.get_communalities()
    comunalitati_df = to_dataframe(comunalitati, variable_names, ["Comunalitati"], "Comunalitati.csv")
    heatmap(comunalitati_df, vmin=0, vmax=1, title="Comunalitati")

    # dispersia (varianta) explicata - aceste valori explica de ce selectam anumiti factori:
    # - la nivel de fiecare factor
    # - proportional
    # - cumulat
    dispersie, dispersie_prop, dispersie_cum = fa.get_factor_variance()
    dispersie_df = pd.DataFrame(
        data = {
            "Dispersie": dispersie,
            "Proportie": dispersie_prop,
            "Cumulat": dispersie_cum
        },
        index = factor_labels
    )
    dispersie_df.to_csv("Dispersie.csv")

    # scoruri factoriale = coordonatele fiecarei observatii (rand) in noul spatiu al factorilor
    scoruri = fa.transform(x)
    scoruri_df = to_dataframe(scoruri, df.index, factor_labels, "Scoruri.csv")

    # reprezentare grafica a observatiilor in spatiul factorilor F1 si F2
    plt.figure(figsize=(8,6))

    plt.scatter(scoruri_df['F1'], scoruri_df['F2'])
    for i in range(len(scoruri_df)):
        plt.text(scoruri_df['F1'].iloc[i], scoruri_df['F2'].iloc[i], scoruri_df.index[i])

    plt.title("Scoruri factoriale F1 vs F2")
    plt.xlabel("F1")
    plt.ylabel("F2")
    plt.show()

main()
