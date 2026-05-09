# Materiale de Studiu — Test Grilă
> Pachete Software · Python + SAS · Bazat exclusiv pe `materiale-seminar/`

---

## Ordine recomandată de parcurgere

| # | Fișier | Conținut | Timp estimat |
|---|--------|----------|--------------|
| 1 | [Grile Rezolvate & Tipare](./04_GRILE_REZOLVATE_PATTERNS.md) | Citește primul — tipare de grile cu răspunsuri | ~30 min |
| 2 | [SAS — Sintaxă și Proceduri](./01_SAS_SINTAXA_SI_PROCEDURI.md) | Cel mai greu, cea mai mare pondere — toate seminarele SAS 1–4 | ~60 min |
| 3 | [Python — Structuri de Date](./02_PYTHON_STRUCTURI_DATE.md) | Liste, tuple, dict, seturi, funcții, lambda, output prediction | ~40 min |
| 4 | [Pandas, Matplotlib & ML](./03_PANDAS_ML.md) | Series, loc/iloc, groupby, merge, K-Means, clasificare, regresie, Decision Tree, Random Forest, Gradient Boosting, Streamlit | ~60 min |
| 5 | [Grile Rezolvate & Tipare](./04_GRILE_REZOLVATE_PATTERNS.md) | Recitește la final ca recapitulare rapidă înainte de test | ~15 min |

---

## Ce acoperă fiecare fișier

### [01 · SAS — Sintaxă și Proceduri](./01_SAS_SINTAXA_SI_PROCEDURI.md)
*Surse: `SAS/01_SAS_Seminar_1/`, `02/`, `03/`, `04/` — toate fișierele `.docx`*
23 secțiuni · ~1040 linii

| # | Secțiune |
|---|----------|
| 1 | Sintaxa SAS — reguli de bază |
| 2 | Seturi de date SAS — structură |
| 3 | Biblioteci (LIBNAME) — WORK temporar vs permanent |
| 4 | Citirea datelor — INPUT, INFILE, DATALINES, DSD/DLM/@@/MISSOVER |
| 5 | DROP și KEEP |
| 6 | DO loops și ARRAY — grup DO, buclă, DO WHILE/UNTIL, SUM operator, masive |
| 7 | WHERE vs IF — diferențe critice |
| 8 | PROC SORT |
| 9 | FORMAT vs INFORMAT |
| 10 | PROC PRINT |
| 11 | PROC MEANS |
| 12 | PROC UNIVARIATE |
| 13 | PROC CONTENTS |
| 14 | Combinarea seturilor — SET (concatenare/interclasare) și MERGE (join) |
| 15 | Funcții SAS pentru date |
| 16 | Titluri în SAS |
| 17 | Declarația SET vs setul de date intrare/ieșire |
| 18 | SAS Enterprise Guide — pointer vs copie, Query Builder, Data View |
| 19 | PROC FREQ — tabele uni/bidimensionale, opțiuni |
| 20 | PROC GCHART + PROC GPLOT — bare, pie, subgroup, sumvar, scatter |
| 21 | PROC CORR — Pearson, Spearman, Kendall |
| 22 | Grile tricky — capcane frecvente |
| 23 | Interpretarea outputurilor SAS — PROC PRINT/MEANS/UNIVARIATE/FREQ/CORR/GCHART/GPLOT |

### [02 · Python — Structuri de Date](./02_PYTHON_STRUCTURI_DATE.md)
*Surse: `Python/01_Introducere_Python.pdf`, `Python/02_Script_Introducere/s1.py`*
13 secțiuni · 647 linii

| # | Secțiune |
|---|----------|
| 1 | Tipuri de date fundamentale (int, float, str, bool, None) |
| 2 | Liste — mutable, metode, sort vs sorted |
| 3 | Tuple — imutabile, del t vs del t[0], (1,) vs (1) |
| 4 | Dicționare — chei hashable, get(), iterare |
| 5 | Seturi — reuniune, intersecție, diferență |
| 6 | Comprehensions — list, dict, set, generator |
| 7 | Funcții — *args, **kwargs, lambda, map(), filter() |
| 8 | Structuri de control — for, while, enumerate(), zip() |
| 9 | Funcții built-in esențiale |
| 10 | Module și import |
| 11 | Grile tipice — predicție output |
| 12 | Tabel comparativ structuri de date |
| 13 | Capcane frecvente la grile |

### [03 · Pandas, Matplotlib & ML](./03_PANDAS_ML.md)
*Surse: `Python/04_Pandas_Library.pdf`, `03_Pandas_Recapitulare/`, `05_EDA/`, `06_Kmeans/`, `07_Clasificare/`, `08_Regresie/`, `09_Algoritmi_Predictie.py`*
20 secțiuni · ~1482 linii

| # | Secțiune |
|---|----------|
| 1 | Pandas Series — creare, index, isnull/notnull |
| 2 | Pandas DataFrame — creare, set_index, selectare coloane |
| 3 | EDA — head/info/describe/isnull/value_counts/select_dtypes |
| 4 | Selectare — loc vs iloc (label vs poziție, slice inclusiv/exclusiv) |
| 5 | GroupBy + agg — split-apply-combine, idxmax, pd.cut |
| 6 | Merge / Join — inner, left, right, outer, indicator |
| 7 | Matplotlib & Seaborn — hist, pie, bar, scatter, heatmap, boxplot |
| 8 | K-Means — WCSS, Elbow Method, silhouette, k-means++ |
| 9 | Clasificare — confusion matrix, F1, ROC-AUC, Logistic Regression |
| 10 | Preprocessing — StandardScaler vs MinMaxScaler |
| 11 | Statistici descriptive — mean/median/mode, IQR, outlieri, corelație |
| 12 | Streamlit — widgets, layout, session_state |
| 13 | Grile tipice — Pandas & ML |
| 14 | Funcții apply și map |
| 15 | Tabel rezumativ funcții Pandas |
| 16 | Regresie liniară — np.log(), pd.get_dummies(), MSE/RMSE/MAE/R² |
| 17 | Encoding — LabelEncoder, get_dummies, drop_first, corelație cu target |
| 18 | Algoritmi avansați — Decision Tree (Gini), Random Forest (bagging/OOB), Gradient Boosting |
| 19 | EDA avansat — pd.to_datetime, groupby+transform, outlieri IQR, target encoding |
| 20 | Interpretarea outputurilor Python/Pandas/ML — df.info/describe, confusion matrix, ROC, K-Means, scalere, metrici regresie |

### [04 · Grile Rezolvate & Tipare](./04_GRILE_REZOLVATE_PATTERNS.md)
*Surse: `grile-materiale/` — DOAR grilele propriu-zise*
- 40+ grile cu răspunsuri corecte și explicații
- Secțiuni: SAS, SAS Enterprise Guide, Python, Pandas, ML
- Rezumat ultra-rapid la final

---

## Notă despre surse

Toate fișierele de studiu conțin **exclusiv** teorie din `materiale-seminar/`. Fișierul `04_GRILE_REZOLVATE_PATTERNS.md` este singurul care folosește conținut din `grile-materiale/`.

---

## Notă despre acoperire

| Material seminar | Acoperit în |
|---|---|
| `SAS/01` – citire date, LIBNAME, formate | `01_SAS_SINTAXA_SI_PROCEDURI.md` |
| `SAS/02` – operatori, WHERE, IF, DO | `01_SAS_SINTAXA_SI_PROCEDURI.md` |
| `SAS/03` – SET, MERGE | `01_SAS_SINTAXA_SI_PROCEDURI.md` |
| `SAS/04` – PROC PRINT/UNIVARIATE/MEANS/FREQ/GCHART/GPLOT/CORR | `01_SAS_SINTAXA_SI_PROCEDURI.md` |
| `Python/01` – Introducere Python (PPT) | `02_PYTHON_STRUCTURI_DATE.md` |
| `Python/02` – Streamlit (s1.py) | `03_PANDAS_ML.md` |
| `Python/03` – Pandas + Merge (seminar_4_ex.py, s3_exercitii.py) | `03_PANDAS_ML.md` |
| `Python/05` – EDA + K-Means | `03_PANDAS_ML.md` |
| `Python/06` – K-Means detaliat | `03_PANDAS_ML.md` |
| `Python/07` – Clasificare | `03_PANDAS_ML.md` |
| `Python/08` – Regresie | `03_PANDAS_ML.md` |
| `Python/09` – Algoritmi predictie | `03_PANDAS_ML.md` |

> **Notă:** `Python/01_Introducere_Python.pdf` și `Python/06_Kmeans/kmeans.pdf` au fost convertite din .pptx și citite integral. Conținutul lor este inclus complet în fișierele de studiu.

> **Fișierul `04_TEORIA_LICENTE_CLOUD.md` a fost șters** — conținutul respectiv (licențe software, cloud computing) nu provine din `materiale-seminar/`.

---

> **Sfat:** Dacă ai timp limitat, parcurge **04 → 01 → 04**. SAS are cea mai mare pondere la test.
