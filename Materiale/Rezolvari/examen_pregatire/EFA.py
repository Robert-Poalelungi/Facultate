import numpy as np
from factor_analyzer import FactorAnalyzer,calculate_kmo,calculate_bartlett_sphericity
x = np.ndarray()  # Aici trebuie să pui datele corecte

bartlett_stat, bartlett_p = calculate_bartlett_sphericity(x)
if bartlett_p > 0.001:
    print("Testul Bartlett sugerează că NU există factori comuni semnificativi.")
    exit(0)

kmo_all,kmo_model = calculate_kmo(x)
print(f"Index KMO general: {kmo_model:.3f}")

if kmo_model < 0.6:
    print("Indicele KMO este prea mic. Analiza factorială NU este recomandată.")
    exit(0)

efa = FactorAnalyzer(n_factors= x.shape[1] - 1, rotation='varimax')
efa.fit(x)


factorLoadings = efa.loadings  # Corelațiile dintre variabile și factori comuni
eigenvalues = efa.get_eigenvalues()  # Valori proprii (eigenvalues)
communalities = efa.get_communalities()  # Comunalitățile (cât din variabilă este explicat de factori)
specificFactors = efa.get_uniquenesses()  # Unicitatea fiecărei variabile, variabile specifice


