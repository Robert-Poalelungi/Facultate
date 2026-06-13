# DSAD - Ghid Complet Analize

---

## Cuprins
1. [Preprocesare Generala](#0-preprocesare-generala)
2. [Partea A — Operatii Pandas](#partea-a--operatii-pandas)
3. [PCA - Analiza Componentelor Principale](#1-pca---analiza-componentelor-principale)
4. [EFA - Analiza Factoriala](#2-efa---analiza-factoriala)
5. [LDA - Analiza Discriminanta](#3-lda---analiza-discriminanta)
6. [HCA - Analiza de Clusteri](#4-hca---analiza-de-clusteri)
7. [CCA - Analiza Canonica](#5-cca---analiza-canonica)

---

## 0. Preprocesare Generala

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Citire fisiere
df = pd.read_csv('./input/Date.csv', index_col=0)
coduri = pd.read_csv('./input/Coduri.csv', index_col=0)

# Inlocuire NaN
df = df.fillna(0)
# SAU cu media/modul pe coloana:
for col in df.columns:
    if df[col].isna().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

# Merge
merged = df.merge(coduri[['Judet']], left_index=True, right_index=True)

# Lista indicatori numerici
lista = list(df.columns)[1:]  # sarim primul col daca e nenumeric
```

---

## 1. PCA - Analiza Componentelor Principale

### Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from seaborn import heatmap
```

### Pre-procesare + Aplicare PCA
```python
# Standardizare (obligatorie pentru PCA)
labels = list(date_numerice.columns)
scaler = StandardScaler()
x = scaler.fit_transform(date_numerice)

# Aplicare PCA
pca = PCA()
C = pca.fit_transform(x)       # componentele principale (scoruri brute)
a = pca.components_.T           # loadings
```

### Varianta componentelor
```python
alpha = pca.explained_variance_          # varianta componentelor
pve   = pca.explained_variance_ratio_    # procent varianta
pve_cum = np.cumsum(pve)                 # procent cumulat
alpha_cum = np.cumsum(alpha)             # varianta cumulata
```

### Plot varianta cu criterii de relevanta
```python
plt.figure(figsize=(8, 8))
plt.title('Plot varianta componente')
Xindex = ['C' + str(k+1) for k in range(len(alpha))]
plt.plot(Xindex, alpha, 'bo-')

# Criteriul Kaiser (eigenvalue > 1)
plt.axhline(1, c='r', label='Kaiser')

# Criteriul Cattell
eps = np.diff(alpha)
d = np.diff(eps)
if (d < 0).any():
    j_Cattell = np.where(d < 0)[0][0] + 2
    plt.axhline(alpha[j_Cattell - 1], c='m', label='Cattell')

# Criteriul Procent Minimal (80%)
procent_cumulat = np.cumsum(alpha) * 100 / np.sum(alpha)
j_procent = np.where(procent_cumulat > 80)[0][0] + 1
plt.axhline(alpha[j_procent - 1], c='c', label='Procent minimal > 80%')

plt.legend()
plt.xlabel('Componenta')
plt.ylabel('Varianta')
plt.show()
```

### Scoruri standardizate
```python
scores = C / np.sqrt(alpha)            # scoruri standardizate
# SAU:
# scores = pca.transform(x)           # scoruri brute (model deja antrenat)
# scores = pca.fit_transform(x)       # scoruri brute (model neantrenat)
```

### Corelatii factoriale (loadings)
```python
rxc = a * np.sqrt(alpha)   # corelatii variabile - componente

# Corelogram
rxc_df = pd.DataFrame(data=rxc, index=labels,
                      columns=['C' + str(i+1) for i in range(rxc.shape[1])])
plt.figure(figsize=(8, 8))
plt.title("Corelograma corelatii factoriale")
heatmap(rxc_df, vmin=-1, vmax=1, cmap='bwr', annot=True)
plt.show()
```

### Cercul corelatiilor (primele 2 componente)
```python
plt.figure(figsize=(12, 12))
plt.title('Cercul corelatiilor')
T = np.arange(0, np.pi * 2, 0.01)
plt.plot(np.cos(T), np.sin(T))
plt.axhline(0, c='g')
plt.axvline(0, c='g')
plt.scatter(rxc[:, 0], rxc[:, 1])
for i in range(rxc.shape[0]):
    plt.text(rxc[i, 0], rxc[i, 1], labels[i], fontsize=12, ha='right')
plt.xlim(-1.1, 1.1)
plt.ylim(-1.1, 1.1)
plt.show()
```

### Plot scoruri
```python
plt.figure(figsize=(8, 8))
plt.title('Plot scoruri')
plt.scatter(scores[:, 0], scores[:, 1])
for i, name in enumerate(merged.index):
    plt.annotate(name, (scores[i, 0], scores[i, 1]))
plt.xlabel('Score 1')
plt.ylabel('Score 2')
plt.show()
```

### Cosinusuri, Contributii, Comunalitati
```python
C2 = C * C
quality        = np.transpose(C2.T / np.sum(C2, axis=1))    # cosinusuri
contributions  = C2 / (x.shape[0] * alpha)                   # contributii
communalities  = np.cumsum(rxc * rxc, axis=1)                # comunalitati

# Corelogram comunalitati
communalities_df = pd.DataFrame(data=communalities, index=labels,
                                columns=['C' + str(i+1) for i in range(communalities.shape[1])])
plt.figure(figsize=(8, 8))
plt.title("Corelograma comunalitati")
heatmap(communalities_df, vmin=-1, vmax=1, cmap='bwr', annot=True)
plt.show()
```

---

## 2. EFA - Analiza Factoriala

### Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
from seaborn import heatmap
```

### Pre-procesare
```python
date = pd.read_csv("date.csv")
x = date.iloc[:, 1:]   # toate col numerice (sarim indexul daca exista)
labels = list(x.columns)
```

### Testul Bartlett (factorabilitate)
```python
bartlett_stat, bartlett_p = calculate_bartlett_sphericity(x)
print(f"Chi-square: {bartlett_stat}, P-value: {bartlett_p}")
# Vrem p_value < 0.05 (sau < 0.001)
if bartlett_p > 0.05:
    print("NU exista factori comuni semnificativi")
```

### Testul KMO (factorabilitate)
```python
kmo_all, kmo_model = calculate_kmo(x)
print(f"KMO: {kmo_model}")
# Vrem kmo_model > 0.6
if kmo_model < 0.6:
    print("Analiza factoriala nu este recomandata")
```

### Aplicare EFA cu/fara rotatie
```python
# Cu rotatie varimax
efa = FactorAnalyzer(n_factors=3, rotation='varimax')
# Fara rotatie
# efa = FactorAnalyzer(n_factors=3, rotation=None)
efa.fit(x)
```

### Varianta factorilor
```python
varianta_fact, proc_var_extrasa, proc_var_cum = efa.get_factor_variance()
# varianta_fact   = varianta factorilor comuni
# proc_var_extrasa = procentul de varianta extrasa
# proc_var_cum     = procentul cumulat

pd.DataFrame({
    'Varianta factorilor': varianta_fact,
    'Procent varianta extrasa': proc_var_extrasa * 100,
    'Procent varianta cumulata': proc_var_cum * 100
}).to_csv('./output/Varianta.csv', index=False)
```

### Corelatii factoriale (loadings)
```python
factorLoadings = efa.loadings_

factorLoadings_df = pd.DataFrame(data=factorLoadings, index=labels,
                                  columns=['F' + str(i+1) for i in range(factorLoadings.shape[1])])

# Corelogram
plt.figure(figsize=(8, 8))
plt.title('Corelograma corelatii factoriale')
heatmap(factorLoadings_df, vmin=-1, vmax=1, cmap='bwr', annot=True)
plt.show()
```

### Cercul corelatiilor (primii 2 factori)
```python
plt.figure(figsize=(8, 8))
plt.title("Cercul de corelatie pentru primii 2 factori comuni")
T = np.arange(0, np.pi * 2, 0.01)
plt.plot(np.cos(T), np.sin(T))
plt.axhline(0, c='g')
plt.axvline(0, c='g')
plt.scatter(factorLoadings[:, 0], factorLoadings[:, 1])
for i in range(factorLoadings.shape[0]):
    plt.text(factorLoadings[i, 0], factorLoadings[i, 1], labels[i], fontsize=12, ha='right')
plt.show()
```

### Comunalitati si varianta specifica
```python
communalities   = efa.get_communalities()   # cat din variabila e explicat de factori
specificFactors = efa.get_uniquenesses()    # varianta specifica (unicitate)

df_com = pd.DataFrame({
    'Comunalitati': communalities,
    'Varianta specifica': specificFactors
}, index=labels)

plt.figure(figsize=(10, 6))
plt.title('Comunalitati si varianta specifica')
heatmap(data=df_com, cmap='viridis', annot=True)
plt.show()
```

### Scoruri factoriale
```python
scores = efa.fit_transform(x)

plt.figure(figsize=(8, 8))
plt.title('Scatter plot scoruri factoriale (F1 vs F2)')
plt.scatter(scores[:, 0], scores[:, 1])
plt.xlabel('Factor 1')
plt.ylabel('Factor 2')
plt.show()
```

---

## 3. LDA - Analiza Discriminanta

### Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from seaborn import kdeplot
```

### Pre-procesare
```python
date = pd.read_csv("date.csv")
# NU se standardizeaza pentru LDA
tinta = 'VULNERAB'              # coloana target (specificata in cerinta)
variabile = list(date.columns[:-1])

x = date[variabile]
y = date[tinta]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)
# SAU cu setul de aplicare separat:
x_applied = pd.read_csv("date_aplicare.csv")
```

### Aplicare LDA
```python
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train)
```

### Scoruri discriminante
```python
scores = lda.transform(x_test)
print("Scoruri discriminante:\n", scores)
```

### Plot instante in axe discriminante
```python
plt.figure(figsize=(8, 6))
plt.scatter(scores[:, 0], scores[:, 1], c=y_test, cmap='viridis', edgecolors='k')
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.title('Instante in axe discriminante')
plt.colorbar(label='Clasa')
plt.show()

# Pentru o singura axa discriminanta:
plt.scatter(scores[:, 0], [0] * len(scores), c=y_test, cmap='viridis', edgecolors='k')
plt.yticks([])
```

### Plot distributii in axele discriminante (densitate)
```python
plt.figure(figsize=(8, 6))
for clasa in y_test.unique():
    kdeplot(scores[y_test == clasa, 0], label=f'Clasa {clasa}', fill=True)
plt.xlabel('LD1')
plt.ylabel('Densitate')
plt.title('Distributia scorurilor pe prima axa discriminanta')
plt.legend()
plt.show()
```

### Predictii - model Linear
```python
prediction_test    = lda.predict(x_test)
prediction_applied = lda.predict(x_applied)
```

### Evaluare model Linear (matrice confuzie + acuratete)
```python
cm = confusion_matrix(y_test, prediction_test)
print('Matricea de confuzie:\n', cm)

accuracy = accuracy_score(y_test, prediction_test)
print('Acuratete:', accuracy)

# Acuratete medie pe clase
class_accuracy = cm.diagonal() / cm.sum(axis=1)
print('Acuratete medie:', np.mean(class_accuracy))

print(classification_report(y_test, prediction_test))
```

### Model Bayesian (GaussianNB)
```python
gnb = GaussianNB()
gnb.fit(x_train, y_train)

prediction_test_bayesian    = gnb.predict(x_test)
prediction_applied_bayesian = gnb.predict(x_applied)

cm_bayesian = confusion_matrix(y_test, prediction_test_bayesian)
accuracy_bayesian = accuracy_score(y_test, prediction_test_bayesian)
print('Acuratete Bayesian:', accuracy_bayesian)
print(classification_report(y_test, prediction_test_bayesian))
```

---

## 4. HCA - Analiza de Clusteri

### Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from seaborn import histplot, countplot
```

### Pre-procesare
```python
date = pd.read_csv("date.csv")
labels_obs = list(date.index)   # numele observatiilor (pentru dendrograma)
labels_var = list(date.columns)

# Standardizare (obligatorie pentru HCA)
x = StandardScaler().fit_transform(date)
```

### Calcul ierarhie (matricea ierarhie)
```python
# Coloane matrice: [cluster1, cluster2, distanta, nr_elemente_noi]
HC = linkage(x, method='ward')
print("Matrice ierarhie:\n", HC)
```

### Partitie optimala prin metoda Elbow
```python
n = HC.shape[0]
dist_1 = HC[1:n, 2]
dist_2 = HC[0:n-1, 2]
diff = dist_1 - dist_2
j = np.argmax(diff)
t = (HC[j, 2] + HC[j+1, 2]) / 2   # pragul pentru dendrograma

# Etichetele clusterelor
cat = fcluster(HC, n - j, criterion='maxclust')
labels_clusters = ['C' + str(i) for i in cat]
print(f"Numar optim de clustere: {n - j}")
```

### Partitie fixa (k clustere prestabilite)
```python
k = 5
kmeans = KMeans(n_clusters=k, n_init=10)
k_labels = ['C' + str(i+1) for i in kmeans.fit_predict(x)]
merged['Clusters'] = k_labels
```

### Indice Silhouette
```python
# La nivel de partitie
silhouette_opt = silhouette_score(x, cat)
print(f"Silhouette partitie optima: {silhouette_opt}")

# La nivel de instante
silhouette_obs_opt   = silhouette_samples(x, cat)
silhouette_obs_fixed = silhouette_samples(x, kmeans.fit_predict(x))
```

### Dendrograma cu partitie evidentiata
```python
# Partitia optima
plt.figure(figsize=(12, 12))
plt.title("Dendograma - Partitie Optima")
dendrogram(HC, leaf_rotation=30, labels=merged.index.values)
plt.axhline(t, c='r')
plt.show()

# Partitie-k
plt.figure(figsize=(12, 12))
plt.title(f"Dendograma - Partitie {k} Clustere")
dendrogram(HC, leaf_rotation=30, labels=merged.index.values)
plt.axhline(HC[-(k-1), 2], c='r')
plt.show()
```

### Plot Silhouette
```python
plt.figure(figsize=(8, 8))
plt.title('Silhouette partitie optima')
plt.scatter(x[:, 0], x[:, 1], c=silhouette_obs_opt, cmap='viridis')
plt.xlabel('Componenta 1')
plt.ylabel('Componenta 2')
plt.show()
```

### Histograme clusteri pentru o variabila
```python
variabila = '2015'   # numele coloanei
plt.figure(figsize=(8, 8))
plt.title(f'Histograma pentru {variabila}')
histplot(data=merged, x=variabila, hue='Clusters', kde=True, bins=30)
plt.xlabel(variabila)
plt.ylabel('Frecventa')
plt.show()
```

### Countplot distributie instante in clustere
```python
plt.figure(figsize=(10, 5))
countplot(x=k_labels, palette='viridis')
plt.title(f"Distributia instantelor in {k} clustere")
plt.xlabel("Cluster")
plt.ylabel("Numar instante")
plt.show()
```

### Plot partitie in axe principale (PCA 2D)
```python
pca = PCA(n_components=2)
pca_scores = pca.fit_transform(x)

# Partitie optima
plt.figure(figsize=(10, 8))
scatter = plt.scatter(pca_scores[:, 0], pca_scores[:, 1],
                      c=cat, cmap='viridis', edgecolors='k')
plt.colorbar(scatter, label="Cluster")
plt.xlabel("Componenta Principala 1")
plt.ylabel("Componenta Principala 2")
plt.title("Clustere in axe PCA - Partitie Optima")
plt.show()

# K-partitii
kmeans2 = KMeans(n_clusters=k, n_init=10)
labels_kmeans = kmeans2.fit_predict(pca_scores)
plt.figure(figsize=(8, 8))
plt.scatter(pca_scores[:, 0], pca_scores[:, 1], c=labels_kmeans, cmap='viridis')
plt.colorbar()
plt.title(f"Partitie {k} clustere pe axe PCA")
plt.show()
```

---

## 5. CCA - Analiza Canonica

### Imports
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cross_decomposition import CCA
from scipy.stats import chi2
```

### Pre-procesare
```python
date = pd.read_csv('date_canonice.csv')

# Impartire in 2 grupuri de variabile
x = date.iloc[:, :3].values    # primul grup (primele 3 coloane)
y = date.iloc[:, 3:].values    # al doilea grup (restul coloanelor)

n = x.shape[0]   # nr observatii
p = x.shape[1]   # nr variabile in X
q = y.shape[1]   # nr variabile in Y
```

### Aplicare CCA
```python
cca = CCA(n_components=2)   # nr componente = min(p, q)
cca.fit(x, y)
```

### Scoruri canonice (variabile canonice)
```python
x_scoruri, y_scoruri = cca.transform(x, y)
print("Scoruri canonice X:\n", x_scoruri)
print("Scoruri canonice Y:\n", y_scoruri)
```

### Corelatii canonice
```python
m = cca.n_components
corelatii_canonice = np.corrcoef(x_scoruri.T, y_scoruri.T).diagonal(offset=m)
print("Corelatii canonice:\n", corelatii_canonice)
```

### Testul Bartlett (semnificatia corelatiilor canonice)
```python
def test_bartlett(r2, n, p, q, m):
    x_val = 1 - r2
    df = [(p - k + 1) * (q - k + 1) for k in range(1, m + 1)]
    l = np.flip(np.cumprod(np.flip(x_val)))
    chi2_ = (-n + 1 + (p + q + 1) / 2) * np.log(l)
    return 1 - chi2.cdf(chi2_, df)

r2 = corelatii_canonice ** 2
p_values = test_bartlett(r2, n, p, q, m)
print("P-values Bartlett:\n", p_values)
# Vrem p_value < 0.05 pentru corelatii semnificative
```

---

## Partea A — Operatii Pandas

Partea A apare in toate subiectele si are de obicei 2 cerinte:
- **Cerinta 1 (1p)** — calcul simplu la nivel de instanta (medie pe rand, suma, filtrare)
- **Cerinta 2 (2p)** — agregare pe grup (groupby judet/continent + max/count/per capita)

### Setup de baza (valabil pentru orice subiect)
```python
import pandas as pd
import numpy as np

# Citire date principale + coduri
df     = pd.read_csv('Date.csv', index_col=0)
coduri = pd.read_csv('Coduri.csv', index_col=0)

# Campul de legatura (ex: Siruta, CountryId) -> merge
merged = df.merge(coduri, left_index=True, right_index=True)
# SAU daca campul e coloana, nu index:
merged = df.merge(coduri, on='Siruta')

# Coloanele numerice (indicatori)
indicatori = [c for c in df.columns if c not in ('Siruta', 'Localitate', 'Judet', 'CountryId', 'Country')]
```

---

### Cerinta tip 1 — Medie pe rand + sortare

> "Sa se calculeze valoarea medie a indicelui (media pe ani) la nivel de localitate, salvata in ordine descrescatoare."

```python
# Media pe rand (pe toti indicatorii/anii)
df['Medie'] = df[indicatori].mean(axis=1)

# Sortare descrescatoare
rezultat = df[['Localitate', 'Medie']].sort_values('Medie', ascending=False)
# daca Localitate e coloana, nu index

rezultat.to_csv('Cerinta1.csv')
```

---

### Cerinta tip 2 — Filtrare (cel putin un 0 pe rand)

> "Sa se salveze localitatile in care cel putin pentru un an diversitatea a fost 0."

```python
# Mask: randuri unde cel putin o valoare din indicatori e 0
mask = (df[indicatori] == 0).any(axis=1)
rezultat = df[mask]

rezultat.to_csv('Cerinta1.csv')
```

---

### Cerinta tip 3 — Coeficient de variatie

> "Sa se calculeze coeficientii de variatie pentru fiecare indicator."

```python
# CV = std / mean (per coloana)
cv = df[indicatori].std() / df[indicatori].mean()

rezultat = pd.DataFrame({'Indicator': cv.index, 'CV': cv.values})
rezultat.to_csv('Cerinta1.csv', index=False)
```

---

### Cerinta tip 4 — Suma coloane (total venituri / cheltuieli)

> "Sa se calculeze total venituri si total cheltuieli pentru fiecare localitate."

```python
cols_venituri   = ['TVP', 'TVA_J', 'Subv', 'SumeUE']   # coloanele specificate in cerinta
cols_cheltuieli = ['CP', 'CBS', 'CD', 'CS']

df['Venituri']   = df[cols_venituri].sum(axis=1)
df['Cheltuieli'] = df[cols_cheltuieli].sum(axis=1)

rezultat = df[['Localitate', 'Venituri', 'Cheltuieli']]
rezultat.to_csv('Cerinta1.csv')
```

---

### Cerinta tip 5 — GroupBy + max per grup (localitatea cu max per judet)

> "Sa se determine pentru fiecare judet localitatea in care diversitatea medie este maxima."

```python
# Calculam mai intai media per localitate
merged['Medie'] = merged[indicatori].mean(axis=1)

# Gasim indexul maximului per judet
idx_max = merged.groupby('Judet')['Medie'].idxmax()

# Selectam randurile cu maximul
rezultat = merged.loc[idx_max, ['Judet', 'Localitate', 'Medie']]
rezultat.columns = ['Judet', 'Localitate', 'Diversitate Maxima']

rezultat.to_csv('Cerinta2.csv', index=False)
```

---

### Cerinta tip 6 — GroupBy + count zeros per an (pivot)

> "Sa se determine pentru fiecare judet si fiecare an, numarul de localitati care au diversitatea 0."

```python
# Pentru fiecare coloana-an, cream o coloana binara (0 = e zero, 1 = nu e zero)
zeros = (merged[indicatori] == 0).astype(int)
zeros['Judet'] = merged['Judet']

# Suma per judet (numarul de zerouri)
rezultat = zeros.groupby('Judet')[indicatori].sum()

rezultat.to_csv('Cerinta2.csv')
```

---

### Cerinta tip 7 — GroupBy + indicatorul cu CV maxim per grup

> "Sa se determine pentru fiecare continent indicatorul cu cel mai mare coeficient de variatie."

```python
def cv_per_grup(grup):
    cv = grup[indicatori].std() / grup[indicatori].mean()
    best = cv.idxmax()
    return pd.Series({'Indicator': best, 'CV': cv[best]})

rezultat = merged.groupby('Continent').apply(cv_per_grup).reset_index()
rezultat.to_csv('Cerinta2.csv', index=False)
```

---

### Cerinta tip 8 — Per capita (total judet / populatie judet)

> "Sa se calculeze veniturile si cheltuielile pe locuitor la nivel de judet."

```python
# 1. Adaugam populatia din al doilea fisier
pop = pd.read_csv('Populatie.csv')             # Siruta, Judet, Populatie
merged = df.merge(pop[['Siruta', 'Judet', 'Populatie']], on='Siruta')

# 2. Total per judet pentru fiecare capitol
total_judet = merged.groupby('Judet')[indicatori].sum()

# 3. Populatia totala per judet
pop_judet = merged.groupby('Judet')['Populatie'].sum()

# 4. Impartire (broadcasting automat pe coloane)
per_capita = total_judet.div(pop_judet, axis=0)

per_capita.to_csv('Cerinta2.csv')
```

---

### Cerinta tip 9 — Numar localitati per judet cu conditie + merge info

> "Sa se determine numarul de localitati per judet care indeplinesc o conditie."

```python
# Filtram
filtrat = merged[merged['Medie'] > prag]

# Numaram per judet
rezultat = filtrat.groupby('Judet').size().reset_index(name='NrLocalitati')

rezultat.to_csv('Cerinta2.csv', index=False)
```

---

### Tipare generale de rezolvare Partea A

| Cerinta | Pattern pandas |
|---------|---------------|
| Medie pe ani | `df[ani].mean(axis=1)` |
| Cel putin un 0 | `(df[ani] == 0).any(axis=1)` |
| Toti 0 | `(df[ani] == 0).all(axis=1)` |
| Suma coloane | `df[cols].sum(axis=1)` |
| Sortare desc | `df.sort_values(col, ascending=False)` |
| Max per grup | `df.groupby('Judet')[col].idxmax()` |
| Count per grup | `df.groupby('Judet').size()` |
| Sum per grup | `df.groupby('Judet')[cols].sum()` |
| CV global | `df[cols].std() / df[cols].mean()` |
| CV per grup | `.apply(lambda g: g.std()/g.mean())` |
| Per capita | `total.div(populatie, axis=0)` |
| Merge | `df.merge(cod, on='Siruta')` |
| Salvare | `df.to_csv('Cerinta.csv', index=False)` |

---

## Structura subiect tip examen

**Partea A** — operatii pandas de baza pe date (vezi sectiunea de mai jos pentru cod complet)

**Partea B** — una dintre analizele de mai sus (PCA / EFA / LDA / HCA / CCA)

### Template general subiect
```python
import pandas as pd
import numpy as np

# Citire date
df   = pd.read_csv('./input/Date.csv', index_col=0)
cod  = pd.read_csv('./input/Coduri.csv', index_col=0)

df = df.fillna(0)
cod = cod.fillna(0)

merged = df.merge(cod[['Judet']], left_index=True, right_index=True)
lista = list(df.columns)[1:]   # indicatori numerici

# --- CERINTA A1 ---
cerinta1 = merged[merged[lista[0]] < 0][['coloana1', 'coloana2']]
cerinta1.to_csv('./output/Cerinta1.csv', index=True)

# --- CERINTA A2 ---
cerinta2 = merged.groupby('Judet')[lista].mean()
cerinta2.to_csv('./output/Cerinta2.csv', index=True)

# --- CERINTA B - ANALIZA ---
# ... vezi sectiunile de mai sus
```
