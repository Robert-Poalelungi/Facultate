# Pandas, Matplotlib & Machine Learning
## Bazat pe: `Python/04_Pandas_Library.pdf`, `03_Pandas_Recapitulare/`, `05_EDA/`, `06_Kmeans/`, `07_Clasificare/`, `08_Regresie/`, `09_Algoritmi_Predictie.py`

---

## 1. PANDAS — SERIES
*(din `04_Pandas_Library.pdf`)*

**Series** = structură de date unidimensională (array + index asociat).

```python
import pandas as pd

# Creare Series din listă — index implicit 0,1,2,...
s = pd.Series([10, 20, 30])
# 0    10
# 1    20
# 2    30

# Creare Series cu index personalizat
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s['a']   # → 10
s[0]     # → 10

# Creare Series din dicționar
d = {'Cluj': 324000, 'București': 1800000, 'Iași': 290000}
s = pd.Series(d)

# Accesare atribute
s.values   # → array cu valorile
s.index    # → indexul

# Valori lipsă: dacă cheia nu există în dict → NaN
s2 = pd.Series(d, index=['Cluj', 'București', 'California'])
# California → NaN

pd.isnull(s2)    # True unde e NaN
pd.notnull(s2)   # True unde nu e NaN
```

---

## 2. PANDAS — DATAFRAME
*(din `04_Pandas_Library.pdf`)*

**DataFrame** = structură tabelară (rânduri + coloane), fiecare coloană poate fi tip diferit.

```python
# Creare din dicționar de liste
df = pd.DataFrame({
    'Nume': ['Ana', 'Bob', 'Cara'],
    'Varsta': [25, 30, 35],
    'Scor': [90.5, 85.0, 92.3]
})

# Creare cu index și coloane explicite
df = pd.DataFrame(
    data=['A', 'B', 'C'],
    index=[0, 1, 2],
    columns=['Litera'],
    dtype=float
)

# Din CSV
df = pd.read_csv("fisier.csv")
df = pd.read_csv("fisier.csv", sep=";")

# set_index — setează o coloană ca index
df = df.set_index("Nume")             # inplace=False implicit → returnează copie
df.set_index("Nume", inplace=True)    # modifică df direct

# CAPCANA: set_index cu inplace=False → df NEMODIFICAT, dacă nu atribui rezultatul!
df2 = df.set_index("Nume", inplace=False)  # df neschimbat, df2 are index nou
```

### Selectare coloane
```python
df['Varsta']           # o coloană → Series
df[['Varsta', 'Scor']] # mai multe coloane → DataFrame
df.Varsta              # dot notation (nu merge dacă are spații)
df.iloc[:, 1]          # coloana cu index pozițional 1
```

---

## 3. PANDAS — EXPLORARE INIȚIALĂ (EDA)
*(din fișierele .py și `04_Pandas_Library.pdf`)*

```python
df.head()        # primele 5 rânduri
df.head(10)      # primele 10 rânduri
df.tail()        # ultimele 5 rânduri
df.shape         # (număr_rânduri, număr_coloane) — tuple, nu metodă!
df.dtypes        # tipul fiecărei coloane
df.info()        # info complet: tipuri, non-null counts, memorie
df.describe()    # statistici: count, mean, std, min, 25%, 50%, 75%, max
df.describe(include='all')  # include și coloane categoriale
df.columns       # lista cu numele coloanelor
df.index         # indexul rândurilor
len(df)          # numărul de rânduri
df.size          # total celule (rânduri × coloane)

# Valori lipsă
df.isnull()          # DataFrame boolean True=lipsă
df.isnull().sum()    # număr de valori lipsă per coloană
df.notnull()
df.dropna()          # șterge rândurile cu orice valoare lipsă
df.fillna(0)         # înlocuiește NaN cu 0
df.fillna(df.mean()) # înlocuiește cu media coloanei

# Valori unice
df['Coloana'].nunique()          # numărul de valori distincte
df['Coloana'].unique()           # array cu valorile distincte
df['Coloana'].value_counts()     # frecvența fiecărei valori
df['Coloana'].value_counts(normalize=True)  # procente

# Tipuri de coloane
df.select_dtypes(include='number').columns   # coloane numerice
df.select_dtypes(exclude='number').columns   # coloane non-numerice
```

---

## 4. SELECTARE — loc vs iloc
*(din `04_Pandas_Library.pdf`)*

**`loc`** = bazat pe **ETICHETE** (label-based)
**`iloc`** = bazat pe **POZIȚIE** (integer position-based)

```python
# Creare Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s[0]     # → 10 (index pozițional)

# Creare DataFrame din dicționar
df = pd.DataFrame({
    'Nume': ['Ana', 'Bob', 'Cara'],
    'Vârsta': [25, 30, 35],
    'Scor': [90.5, 85.0, 92.3]
})

# Din CSV
df = pd.read_csv("fisier.csv")
df = pd.read_csv("fisier.csv", sep=";")   # separator diferit
df = pd.read_csv("fisier.csv", encoding="utf-8")

# Din Excel
df = pd.read_excel("fisier.xlsx")
```

### 4.1 loc vs iloc — reguli

**`loc`** = bazat pe **ETICHETE** (label-based)
**`iloc`** = bazat pe **POZIȚIE** (integer position-based)

```python
# loc[rânduri, coloane] — folosește ETICHETE
df.loc[0]                    # rândul cu index-label 0
df.loc[0, 'Nume']            # o celulă
df.loc[0:2, 'Nume':'Scor']   # slice INCLUSIV ambele capete!
df.loc[:, 'Nume']            # coloana Nume, toate rândurile
df.loc[[0, 2], ['Nume', 'Scor']]  # rânduri și coloane specifice

# iloc[rânduri, coloane] — folosește POZIȚII (0-indexed)
df.iloc[0]                   # primul rând (poziție 0)
df.iloc[0, 1]                # rândul 0, coloana 1 (Vârsta)
df.iloc[0:3, 0:2]            # EXCLUSIV capătul drept (ca Python standard)!
df.iloc[:, -1]               # ultima coloană, toate rândurile
df.iloc[[0, 2], [0, 2]]      # rânduri și coloane specifice

# CAPCANA CRITICĂ:
# loc[0:3] → include rândul 3 (dacă indexul este 0,1,2,3)
# iloc[0:3] → exclude poziția 3 (rândurile 0, 1, 2)
```

### TABEL loc vs iloc
| Caracteristică | `loc` | `iloc` |
|---|---|---|
| Bază | Etichete (labels) | Poziții (integers 0-based) |
| Slice | **Inclusiv** ambele capete | **Exclusiv** capătul drept |
| Condiții | Suportă | Nu suportă direct |
| Utilizare | df.loc[0, 'Coloana'] | df.iloc[0, 1] |

### 4.2 Filtrare condiționată
```python
# Condiție simplă
df[df['Vârsta'] > 25]
df.loc[df['Vârsta'] > 25]

# Condiții multiple (& = și, | = sau, ~ = nu)
df[(df['Vârsta'] > 25) & (df['Scor'] > 90)]
df[(df['Vârsta'] < 25) | (df['Vârsta'] > 35)]
df[~(df['Vârsta'] == 30)]  # NOT

# isin — element în listă
df[df['Tip'].isin(['Hyper', 'Extra'])]

# str.contains — substring în string
df[df['Nume'].str.contains('An')]
df[df['Nume'].str.contains('an', case=False)]  # case-insensitive

# between
df[df['Vârsta'].between(25, 35)]  # inclusiv ambele capete

# query (sintaxă SQL-like)
df.query("Varsta > 25 and Scor > 90")
```

### 4.3 Modificare date
```python
# Modificare valori
df.loc[0, 'Scor'] = 95.0         # modifică o celulă
df.loc[df['Scor'] < 80, 'Scor'] = 80  # modifică condiționat

# Adăugare coloană
df['Nou'] = df['Scor'] * 1.1
df['Categorie'] = df['Vârsta'].apply(lambda x: 'tânăr' if x < 30 else 'adult')

# Ștergere
df.drop('Coloana', axis=1)           # șterge coloana (returnează copie!)
df.drop('Coloana', axis=1, inplace=True)  # modifică inplace
df.drop([0, 1], axis=0)             # șterge rândurile 0 și 1
df.drop(columns=['Col1', 'Col2'])   # sintaxă alternativă

# Redenumire
df.rename(columns={'Vechi': 'Nou'}, inplace=True)
df.rename(index={0: 'a'}, inplace=True)

# Resetare index
df.reset_index(drop=True, inplace=True)
```

---

## 5. GROUPBY ȘI AGG

### groupby — split-apply-combine
```python
# Grupare după o coloană
grouped = df.groupby('Tip')

# Agregare simplă
df.groupby('Tip')['Revenue'].sum()    # suma Revenue per Tip
df.groupby('Tip')['Revenue'].mean()   # media
df.groupby('Tip')['Revenue'].max()    # maximul
df.groupby('Tip')['Revenue'].count()  # numărul

# Grupare după mai multe coloane
df.groupby(['Tip', 'Property'])['Revenue'].sum()

# agg — multiple funcții simultan
df.groupby('Tip')['Revenue'].agg(['sum', 'mean', 'max', 'min', 'std'])

# agg cu dicționar — funcții diferite per coloană
df.groupby('Tip').agg({
    'Revenue': ['sum', 'mean', 'max'],
    'AreaStore': 'mean',
    'Checkout Number': 'max'
})

# agg cu funcții numite (pandas 0.25+)
df.groupby('Tip')['Revenue'].agg(
    Total='sum',
    Media='mean',
    Maxim='max'
)

# reset_index — transformă indexul grupalui în coloană
result = df.groupby('Tip')['Revenue'].sum().reset_index()
```

### idxmax / idxmin — indexul valorii maxime/minime
```python
# Găsire rândul cu Revenue maxim per Tip
idx_max = df.groupby('Tip')['Revenue'].idxmax()
df.loc[idx_max]  # rândurile complete cu Revenue maxim per Tip

# idx_max e o Series: {tip: index_rând_max}
```

### pd.cut — categorii din valori numerice
```python
# Împarte în intervale egale
df['Categorie_Varsta'] = pd.cut(df['Vârsta'], bins=3)
# → 3 intervale egale

df['Categorie_Varsta'] = pd.cut(df['Vârsta'], 
                                 bins=[0, 20, 40, 60], 
                                 labels=['tânăr', 'adult', 'senior'])
```

---

## 6. MERGE (JOIN)

```python
pd.merge(df1, df2, on='cheie_comună')
pd.merge(df1, df2, left_on='cheia_df1', right_on='cheia_df2')
```

### Tipuri de join
| Tip | Sintaxă | Comportament |
|---|---|---|
| Inner | `how='inner'` | Doar rândurile cu cheie în AMBELE tabele |
| Left | `how='left'` | TOATE din stânga + matching din dreapta |
| Right | `how='right'` | Matching din stânga + TOATE din dreapta |
| Outer (Full) | `how='outer'` | TOATE rândurile din ambele |

```python
# Inner join (implicit)
merged = pd.merge(df1, df2, on='id')
merged = pd.merge(df1, df2, on='id', how='inner')

# Left join
merged = pd.merge(df1, df2, on='id', how='left')

# Indicator — adaugă coloana _merge cu proveniența
merged = pd.merge(df1, df2, on='id', how='outer', indicator=True)
# _merge: 'left_only', 'right_only', 'both'

# Chei cu nume diferite
merged = pd.merge(df1, df2, left_on='student_id', right_on='id')
```

### concat — concatenare verticală
```python
result = pd.concat([df1, df2])                    # lipire verticală
result = pd.concat([df1, df2], ignore_index=True) # reindexare
result = pd.concat([df1, df2], axis=1)            # lipire orizontală
```

---

## 7. MATPLOTLIB — VIZUALIZARE

```python
import matplotlib.pyplot as plt

# Histogram
plt.hist(df['Revenue'], bins=20, color='blue', edgecolor='black')
plt.title('Distribuția Revenue')
plt.xlabel('Revenue')
plt.ylabel('Frecvență')
plt.show()

# Pie chart
counts = df['Property'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuția tipurilor de proprietate')
plt.show()

# Bar chart
avg_revenue = df.groupby('Tip')['Revenue'].mean()
avg_revenue.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Revenue mediu pe Tip')
plt.xlabel('Tip')
plt.ylabel('Revenue mediu')
plt.xticks(rotation=45)
plt.show()

# Line plot
plt.plot(x, y, color='red', linestyle='--', marker='o')

# Scatter plot
plt.scatter(df['x'], df['y'], c='blue', alpha=0.5)

# Subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(df['Revenue'], bins=20)
axes[1].boxplot(df['Revenue'])
plt.tight_layout()
plt.show()

# Seaborn (librărie bazată pe matplotlib)
import seaborn as sns
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
sns.boxplot(x='Tip', y='Revenue', data=df)
sns.histplot(df['Revenue'], kde=True)
sns.scatterplot(x='AreaStore', y='Revenue', hue='Tip', data=df)
```

---

## 8. MACHINE LEARNING — K-MEANS CLUSTERING

### 8.1 Concepte fundamentale
- **Tip algoritm:** **Nesupervizat** (nu are etichete, nu știm clusterele dinainte)
- **Scop:** Grupează datele în K clustere pe baza similitudinii
- **Distanța folosită:** Euclidiană (minimizează distanța intra-cluster)

### 8.2 Pași K-Means
1. Inițializare: alege K centroizi (aleatoriu sau k-means++)
2. Atribuire: fiecare punct → cel mai apropiat centroid
3. Actualizare: recalculează centroizii ca medie a punctelor din cluster
4. Repetă 2-3 până când centroizii nu se mai mișcă (convergență)

### 8.3 WCSS și Elbow Method
```python
# WCSS = Within-Cluster Sum of Squares = inerție
# Măsoară compactitatea clusterelor (mai mic = mai bun)
# WCSS scade pe măsură ce K crește

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Metoda Cotului (Elbow Method)')
plt.xlabel('Numărul de clustere K')
plt.ylabel('WCSS')
plt.show()
# Alegem K unde curba face "cotul" (se aplatizează)
```

### 8.4 Silhouette Score
```python
from sklearn.metrics import silhouette_score

# Măsoară calitatea clusterizării: [-1, 1]
# 1 = perfect (puncte în cluster corect, departe de celelalte)
# 0 = punctul e pe granița dintre clustere
# -1 = prost (punctul ar trebui în alt cluster)

scores = []
for k in range(2, 12):  # silhouette necesită minim 2 clustere!
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    scores.append(silhouette_score(X_scaled, labels))
```

### 8.5 Inițializare k-means++
- **k-means++**: alege centroizii inițiali distanțați (mai bun decât aleatoriu)
- Reduce probabilitatea de convergență la soluții locale proaste
- **init='k-means++'** în scikit-learn (default)

### 8.6 Cod complet K-Means
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Încărcare date
df = pd.read_csv("Mall_Customers.csv")

# EDA
print(df.isnull().sum())  # valori lipsă
print(df.describe())

# Encoding variabilă categorială
df['Genre'] = df['Genre'].map({'Male': 0, 'Female': 1})

# Selectare features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Standardizare
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow Method
wcss = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, init='k-means++', random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

# Aplicare K-Means cu K optim (ex: 5)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Vizualizare
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=df['Cluster'], cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            c='red', marker='X', s=200, label='Centroizi')
plt.show()

# Silhouette
score = silhouette_score(X_scaled, df['Cluster'])
print(f"Silhouette Score: {score:.4f}")
```

---

## 9. MACHINE LEARNING — CLASIFICARE (SUPERVIZAT)

### 9.1 Concepte
- **Supervizat:** antrenare cu etichete cunoscute (target/label)
- **Clasificare:** target categorial (0/1, spam/ham, etc.)
- **Regresie:** target numeric continuu

### 9.2 Flux standard
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix, 
                              classification_report, f1_score, roc_auc_score)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scalare (fit NUMAI pe train, transform pe ambele)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)   # NU fit_transform!

# Antrenare
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Predicție
y_pred = model.predict(X_test_scaled)
```

### 9.3 Metrici de evaluare
```python
# Accuracy
accuracy_score(y_test, y_pred)   # (TP+TN) / total

# Confusion Matrix
# [[TN, FP],
#  [FN, TP]]
cm = confusion_matrix(y_test, y_pred)

# Classification Report
print(classification_report(y_test, y_pred))
# Afișează: precision, recall, f1-score per clasă

# F1-Score
# F1 = 2 * (Precision * Recall) / (Precision + Recall)
# IDEAL pentru date DEZECHILIBRATE (imbalanced)
f1_score(y_test, y_pred)
f1_score(y_test, y_pred, average='macro')    # media f1 per clasă
f1_score(y_test, y_pred, average='weighted') # ponderat cu suportul

# ROC-AUC
# 0.5 = aleatoriu (clasificator prost)
# 1.0 = perfect
# AUC > 0.8 = bun
roc_auc_score(y_test, model.predict_proba(X_test_scaled)[:, 1])
```

### 9.4 Confusion Matrix — detaliu
```
                Prezis Negativ    Prezis Pozitiv
Real Negativ       TN                FP
Real Pozitiv       FN                TP

Precision = TP / (TP + FP)   — din cei prezis pozitiv, câți sunt corect?
Recall    = TP / (TP + FN)   — din toți pozitivii reali, câți am prins?
F1        = 2*P*R / (P+R)    — media armonică Precision + Recall
```

---

## 10. PREPROCESSING — SCALARE

### StandardScaler (Z-score normalization)
```python
from sklearn.preprocessing import StandardScaler
# Formulă: (x - mean) / std
# Rezultat: medie=0, std=1
# Bun pentru: algoritmi bazați pe distanță (K-Means, SVM, KNN)
# Nu e limitat la [0,1]!

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### MinMaxScaler
```python
from sklearn.preprocessing import MinMaxScaler
# Formulă: (x - min) / (max - min)
# Rezultat: toate valorile în [0, 1]
# Sensibil la outlieri!

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

### Diferența cheie
| | StandardScaler | MinMaxScaler |
|---|---|---|
| Range output | Fără limită (tipic -3 la +3) | [0, 1] |
| Outlieri | Mai robust | Sensibil |
| Formulă | (x-mean)/std | (x-min)/(max-min) |

---

## 11. STATISTICI DESCRIPTIVE

### Măsuri de tendință centrală
```python
df['col'].mean()    # media aritmetică
df['col'].median()  # mediana (mijlocul valorilor sortate)
df['col'].mode()    # moda (cea mai frecventă valoare)

# CAPCANA: pentru distribuții SKEWED (asimetrice) → median e mai bun decât mean!
# Distribuție normală: mean ≈ median ≈ mode
# Distribuție right-skewed: mean > median > mode
```

### Măsuri de dispersie
```python
df['col'].std()     # deviație standard
df['col'].var()     # varianță
df['col'].min()
df['col'].max()
df['col'].range()   # NU există în pandas, folosiți max()-min()

# IQR = Interquartile Range = Q3 - Q1
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1

# Outlieri (Tukey's method)
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['col'] < lower_bound) | (df['col'] > upper_bound)]
```

### Corelație
```python
df.corr()                              # corelație Pearson între toate coloanele
df['col1'].corr(df['col2'])            # corelație între două coloane

# Valori corelație:
# +1.0: corelație pozitivă perfectă
# 0.0: fără corelație
# -1.0: corelație negativă perfectă

# Vizualizare corelație
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
```

---

## 12. STREAMLIT — COMPONENTE ESENȚIALE

```python
import streamlit as st
import pandas as pd

# Titlu și text
st.title("Titlu principal")
st.header("Header")
st.subheader("Subheader")
st.write("Text sau orice obiect Python")
st.markdown("**Bold** și *italic*")
st.text("Text simplu, monospace")

# Widget-uri (input de la utilizator)
# Fiecare returnează valoarea curentă

button = st.button("Click me")        # returnează True la click
text = st.text_input("Introduceți text", value="default")
number = st.number_input("Număr", min_value=0, max_value=100, value=50)
slider_val = st.slider("Alege", min_value=0, max_value=100, value=50)
selected = st.selectbox("Alege una", ["opțiunea 1", "opțiunea 2"])
multi = st.multiselect("Alege mai multe", ["A", "B", "C"])
radio_val = st.radio("Radio", ["X", "Y", "Z"])
checked = st.checkbox("Bifă-mă")
date = st.date_input("Data")
file = st.file_uploader("Fișier", type=["csv", "xlsx"])

# Afișare date
st.dataframe(df)          # tabel interactiv
st.table(df)              # tabel static
st.metric("Label", value=42, delta=5)

# Layout
with st.sidebar:
    st.write("Conținut în sidebar")

col1, col2 = st.columns(2)
with col1:
    st.write("Stânga")
with col2:
    st.write("Dreapta")

with st.expander("Click pentru mai mult"):
    st.write("Conținut expandat")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Conținut tab 1")

# Session State — persistă valorile între rerulări
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Incrementează"):
    st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")

# FĂRĂ session_state: la fiecare click totul se resetează la 0!
# CU session_state: valoarea persistă între rerulările scriptului

# Grafice
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.hist(df['col'], bins=20)
st.pyplot(fig)

st.bar_chart(df)
st.line_chart(df)
st.area_chart(df)
```

---

## 13. GRILE TIPICE — PANDAS & ML

### Grila 1: loc vs iloc slice
```python
df = pd.DataFrame({'A': [1,2,3,4,5]}, index=[0,1,2,3,4])

df.loc[1:3]    # rândurile cu label 1, 2, 3 (INCLUSIV 3)
df.iloc[1:3]   # rândurile la pozițiile 1, 2 (EXCLUSIV 3)
```

### Grila 2: groupby + agg
```python
# Care este revenue-ul total per tip?
df.groupby('Tip')['Revenue'].sum()  # CORECT
df.groupby('Tip').sum()['Revenue']  # CORECT (dar grupează toate coloanele)
```

### Grila 3: valori lipsă
```python
df.isnull().sum()   # numărul de NaN per coloană
df.isnull().any()   # există vreun NaN în fiecare coloană?
df.isnull().all()   # TOATE sunt NaN în fiecare coloană?
```

### Grila 4: merge inner vs outer
```python
df1 = pd.DataFrame({'id': [1,2,3], 'A': ['a','b','c']})
df2 = pd.DataFrame({'id': [2,3,4], 'B': ['x','y','z']})

inner = pd.merge(df1, df2, on='id')           # id 2,3
left  = pd.merge(df1, df2, on='id', how='left')   # id 1,2,3 (NaN pentru B la id=1)
outer = pd.merge(df1, df2, on='id', how='outer')  # id 1,2,3,4
```

### Grila 5: StandardScaler
```python
# StandardScaler: medie=0, std=1
# Dacă o valoare este exact media → scor z = 0
# Nu limitează la [0,1]

# MinMaxScaler: valori în [0,1]
# Valoarea minimă → 0, maximă → 1
```

### Grila 6: K-Means
```python
# WCSS = inertia — atribut kmeans.inertia_ după fit
# silhouette_score necesită MINIM 2 clustere
# k-means++ e mai bun la inițializare decât aleatoriu
# K-Means este algoritm NESUPERVIZAT
```

### Grila 7: Silhouette Score interpretare
```
-1 → punctul e în clusterul greșit
 0 → pe granița dintre clustere
+1 → perfect separat de celelalte clustere
Vrem valori cât mai apropiate de +1
```

### Grila 8: Distribuție skewed
```
Right-skewed (pozitiv): coada lungă la dreapta → mean > median
Left-skewed (negativ): coada lungă la stânga → mean < median
Outlieri mari trag media spre ei, mediana rezistă → pentru skewed: folosim MEDIAN
```

### Grila 9: fit vs transform
```python
scaler.fit(X_train)        # calculează parametrii (mean, std) DIN TRAIN
scaler.transform(X_train)  # aplică transformarea
scaler.fit_transform(X_train)  # ambii pași la fel

# ATENȚIE: pe test set, DOAR transform (nu fit!)
scaler.transform(X_test)   # CORECT
scaler.fit_transform(X_test)  # GREȘIT — data leakage!
```

### Grila 10: session_state Streamlit
```python
# FĂRĂ session_state:
counter = 0
if st.button("Incr"):
    counter += 1  # → mereu 1! se resetează la fiecare refresh

# CU session_state:
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if st.button("Incr"):
    st.session_state.counter += 1  # persiste!
```

---

## 14. FUNCȚII APPLY ȘI MAP

```python
# apply — aplică funcție pe fiecare rând sau coloană
df['Nou'] = df['Revenue'].apply(lambda x: 'mare' if x > 1000 else 'mic')

df.apply(lambda col: col.max() - col.min())  # per coloană (axis=0 default)
df.apply(lambda row: row['A'] + row['B'], axis=1)  # per rând

# map — pe Series (înlocuire valori)
df['Gen'] = df['Gen'].map({'M': 'Masculin', 'F': 'Feminin'})
df['Gen'] = df['Gen'].map({'Male': 0, 'Female': 1})  # encoding

# applymap / map (DataFrame) — pe fiecare celulă
df.applymap(lambda x: x**2)   # pandas < 2.1
df.map(lambda x: x**2)        # pandas >= 2.1
```

---

## 15. TABEL REZUMATIV FUNCȚII PANDAS

| Funcție | Returnează | Modifică original? |
|---|---|---|
| `df.head(n)` | primele n rânduri | Nu |
| `df.info()` | None (printează) | Nu |
| `df.describe()` | DataFrame cu statistici | Nu |
| `df.isnull()` | DataFrame boolean | Nu |
| `df.dropna()` | DataFrame fără NaN | Nu (returnează copie) |
| `df.fillna(x)` | DataFrame cu NaN înlocuit | Nu (returnează copie) |
| `df.drop(col)` | DataFrame fără coloana/rândul | Nu (returnează copie) |
| `df.rename(...)` | DataFrame redenumit | Nu (returnează copie) |
| `df.sort_values(col)` | DataFrame sortat | Nu |
| `df.groupby(col)` | GroupBy object | Nu |
| `df.merge(df2)` | DataFrame nou | Nu |

---

## 16. MACHINE LEARNING — REGRESIE LINIARĂ
*(din `08_Regresie/housing_california.py`)*

**Regresie** = target numeric continuu (ex: prețul unei case). Supervised learning.

### 16.1 Flux complet regresie

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Încărcare și explorare
alldata = pd.read_csv('housesales.csv')
print(alldata.shape)             # (1460, 80) — rânduri, coloane
print(alldata['SalePrice'].describe())

# 2. Coloane numerice vs non-numerice
print(alldata.select_dtypes(include=np.number).columns.tolist())
print(alldata.select_dtypes(exclude=np.number).columns.tolist())

# 3. Valori lipsă — analiză
total = alldata.isnull().sum().sort_values(ascending=False)
percent = (alldata.isnull().sum() / alldata.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
print(missing_data.head(20))

# 4. Tratare valori lipsă
alldata = alldata.fillna({"PoolQC": "NA"})       # înlocuire cu string NA (categorial)
alldata = alldata.fillna({"MiscFeature": "NA"})
meanlot = alldata['LotFrontage'].mean()
alldata = alldata.fillna({"LotFrontage": meanlot}) # înlocuire cu media (numeric)
alldata = alldata.dropna()                          # elimină restul rândurilor cu NaN
```

### 16.2 Distribuție skewed — transformare log

```python
# Verificare distribuție target
sns.distplot(tuple(alldata['SalePrice']), fit=norm)
plt.show()
# Dacă e skewed (asimetrică) → regresia liniară are probleme

# Transformare logaritmică — face distribuția normală
y = np.log(alldata['SalePrice'])
sns.distplot(y, fit=norm)
plt.show()
# Acum y urmează distribuția normală → algoritm mai precis

# La final, pentru predicție reală:
predicted_log = model.predict(X_test)
predicted_real = np.exp(predicted_log)   # inversul log = exp
```

### 16.3 Encoding categorial cu get_dummies

```python
# pd.get_dummies — One-Hot Encoding pentru variabile nominale (fără ordine)
# Convertește fiecare valoare unică → coloană separată cu 0/1

X = pd.get_dummies(X)
# Ex: SaleType cu valori [WD, New, ConLw] →
#   SaleType_WD | SaleType_New | SaleType_ConLw
#        1      |      0      |       0

# drop_first=True — elimină prima coloană (evită multicolinearitatea dummy trap)
df_onehot = pd.get_dummies(df, columns=['room_type'], drop_first=True)
# Ex: room_type cu [Entire, Private, Shared] → 2 coloane (nu 3)
# CAPCANA: get_dummies creează coloane bool/int, nu float!
# Dacă modelul necesită float: X = pd.get_dummies(X).astype(float)
```

### 16.4 Antrenare și evaluare model

```python
# Separare X și y
X = alldata.drop(['SalePrice'], axis=1)
X = pd.get_dummies(X)
y = np.log(alldata['SalePrice'])    # y în logaritm

# Train/Test split (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=63, test_size=0.20)

# Antrenare Linear Regression
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
y_predicted = model.predict(X_test)

# Metrici de evaluare REGRESIE
mse  = mean_squared_error(y_test, y_predicted)
rmse = np.sqrt(mse)
mae  = mean_absolute_error(y_test, y_predicted)
r2   = r2_score(y_test, y_predicted)

print(f"MSE:  {mse:.4f}")    # media pătratelor erorilor — penalizează outlieri
print(f"RMSE: {rmse:.4f}")   # în aceleași unități cu y — ușor de interpretat
print(f"MAE:  {mae:.4f}")    # media erorilor absolute — mai robust la outlieri
print(f"R²:   {r2:.4f}")     # 0-1; 1 = perfect; 0.8+ = bun; sub 0.5 = slab

# Vizualizare predicție vs real
plt.scatter(y_predicted, y_test)
plt.xlabel('Predicted Sale Price')
plt.ylabel('Actual Sale Price')
plt.plot(range(11, 15), range(11, 15), color='red')  # linia perfectă
plt.show()

# Predicție pentru un singur exemplu
single = model.predict(X_test[2:3])
print(np.exp(single))   # exp inversează log → prețul real
```

### 16.5 METRICI REGRESIE — rezumat
| Metrică | Formulă | Interpretare |
|---|---|---|
| **MSE** | mean((y-ŷ)²) | penalizează outlieri (pătrat); nu e în unități y |
| **RMSE** | √MSE | în unități y; RMSE=80€ → eroare medie 80€ |
| **MAE** | mean(\|y-ŷ\|) | robust la outlieri; eroare medie absolută |
| **R²** | 1 - SS_res/SS_tot | 1=perfect; 0=la fel ca media; <0=mai rău ca media |

---

## 17. ENCODING DATE CATEGORIALE
*(din `07_Clasificare/clasificare_seminar6.ipynb`)*

### LabelEncoder — înlocuiește fiecare valoare cu un număr

```python
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

# fit_transform — calculează maparea și aplică simultan
df['EDUCATION'] = le.fit_transform(df['EDUCATION'])
# ['Liceu', 'Facultate', 'Master'] → [1, 0, 2] (ordine alfabetică)

# Atenție: LabelEncoder presupune ordine implicită (0 < 1 < 2)
# Potrivit pentru variabile ORDINALE sau pentru target y (nu pentru features nominale)
```

### Comparație LabelEncoder vs get_dummies

| | LabelEncoder | pd.get_dummies |
|---|---|---|
| Rezultat | 1 coloană cu numere | N coloane binare (0/1) |
| Implică ordine | Da (periculos pentru nominale) | Nu |
| Utilizare corectă | variabile ordinale, target y | variabile nominale (fără ordine) |
| Exemplu | Vârstă: tânăr<adult<senior | Oraș: București/Cluj/Iași |

### Analiză corelație cu target

```python
# Corelație Pearson cu variabila target
corr = df.corr(method='pearson')
corr.sort_values(["Y_BOX_GAMES"], ascending=False, inplace=True)
print(corr.Y_BOX_GAMES)   # afișează corelațiile ordonate descrescător

# Heatmap corelație
import seaborn as sns
corrmat = df.corr()
f, ax = plt.subplots(figsize=(20, 20))
sns.heatmap(corrmat, vmax=1, annot=True, fmt=".2f", square=True)
plt.show()
```

---

## 18. ALGORITMI DE CLASIFICARE AVANSAȚI
*(din `09_Algoritmi_Predictie.py`)*

### 18.1 Decision Tree (Arbore de Decizie)

```python
from sklearn.tree import DecisionTreeClassifier

# Creează și antrenează
dt = DecisionTreeClassifier(max_depth=4, random_state=0)
dt.fit(X_train, y_train)

# Predicție și evaluare
y_pred = dt.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(roc_auc_score(y_test, dt.predict_proba(X_test)[:, 1]))
```

**Concepte cheie Decision Tree:**
- **Gini impurity** = 1 - Σ(pᵢ²) — cât de impur e un nod (0 = pur, 0.5 = maxim haos)
- **max_depth** — limitează adâncimea pentru a preveni overfitting
- **Overfitting**: fără max_depth → 100% pe train, 68% pe test
- **Cu max_depth=4**: 84% pe train și test — generalizează bine

### 18.2 Random Forest

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

rf = RandomForestClassifier(n_estimators=200, oob_score=True, random_state=0)
rf.fit(X_train, y_train)

# OOB Score — estimare calitate fără set de validare separat
print(rf.oob_score_)    # ~0.91 = model bun

# Feature Importance
print(rf.feature_importances_)

# Cross-Validation (5-fold)
cv_scores = cross_val_score(rf, X_train, y_train, cv=5, scoring='roc_auc')
print(f"CV AUC medie: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
```

**Concepte cheie Random Forest:**
- **Bagging** = Bootstrap Aggregating — N arbori independenți, fiecare pe un subset diferit
- **Bootstrap sampling** = extragere cu repetiție → ~63% unice, ~37% duplicate per arbore
- **Feature randomness** = la fiecare nod, alege doar √p features (nu toate)
- **OOB (Out-of-Bag)** = exemplele nefolosite la antrenamentul unui arbore → validare gratuită
- **Predicție finală** = **votul majorității** arborilor (clasificare) sau **media** (regresie)
- Reduce varianta fără a crește bias-ul

### 18.3 Gradient Boosting

```python
from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(n_estimators=100, max_depth=3,
                                 learning_rate=0.1, random_state=42)
gb.fit(X_train, y_train)
y_pred = gb.predict(X_test)
```

**Concepte cheie Gradient Boosting:**
- **Boosting** = arbori secvențiali — fiecare arbore se antrenează pe **erorile** celui anterior
- **Rezidualuri** = y_real - y_prezis → arborele următor le minimizează
- **learning_rate (eta)** = cât contribuie fiecare arbore (0.01-0.3); mai mic = mai robustm mai lent
- **Boosting vs Bagging**: Bagging = paralel+independent (reduce varianta), Boosting = secvențial (reduce și bias)
- **Early Stopping** = oprire automată dacă eroarea de validare nu se îmbunătățește

### 18.4 Comparație algoritmi ML

| Algoritm | Tip | Avantaje | Dezavantaje |
|---|---|---|---|
| Logistic Regression | Clasificare | Rapid, interpretabil, probabil calibrat | Nu capturează neliniarități |
| Decision Tree | Clasificare/Regresie | Vizualizabil, explicabil | Overfitting sever |
| Random Forest | Clasificare/Regresie | Robust, OOB, feature importance | Lent, greu de interpretat |
| Gradient Boosting | Clasificare/Regresie | Cel mai precis (adesea) | Lent, mulți hiperparametri |
| K-Means | Clustering (nesupervizat) | Simplu, rapid | Trebuie să specifici K |
| Linear Regression | Regresie | Complet interpretabil, rapid | Doar relații liniare |

---

## 19. DATE TEMPORALE ȘI TEHNICI EDA SUPLIMENTARE
*(din `05_EDA/EDA EXAMPLE.ipynb`)*

### 19.1 Lucrul cu date datetime

```python
# Conversie la datetime
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
# errors='coerce' → valorile invalide devin NaT (Not a Time), nu aruncă eroare

# Extragere componente din datetime
df['review_year']      = df['last_review'].dt.year
df['review_month']     = df['last_review'].dt.month
df['review_dayofweek'] = df['last_review'].dt.dayofweek   # 0=luni, 6=duminică

# Creare coloană binară: are/nu are recenzie
df['has_review'] = df['last_review'].apply(lambda x: 0 if pd.isnull(x) else 1)
```

### 19.2 Imputare cu groupby + transform

```python
# Înlocuire NaN cu mediana grupului (nu media globală)
df['reviews_per_month'] = df.groupby('neighbourhood_group')['reviews_per_month'] \
                            .transform(lambda x: x.fillna(x.median()))
# transform returnează o Series cu același index ca originalul — compatibil cu assignare directă

# Alternativă: înlocuire cu 0 dacă lipsa are sens (ex: 0 recenzii)
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
```

### 19.3 Eliminare outlieri — metode

```python
# Metoda IQR
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
df_clean = df[~df.index.isin(outliers.index)]   # elimină outlierii

# Metoda percentile (top 1%)
price_limit = df['price'].quantile(0.99)
df = df[df['price'] <= price_limit]

# Transformare logaritmică (alternativă la eliminare)
df['price_log'] = np.log1p(df['price'])   # log1p = log(1 + x), bun și pentru x=0
```

### 19.4 Target Encoding (encoding avansat)

```python
# Target encoding: înlocuiește categoria cu media target-ului per categorie
target_mean = df.groupby('room_type')['price'].mean()
df['room_type_encoded'] = df['room_type'].map(target_mean)

# Frequency encoding: înlocuiește cu frecvența categoriei
freq = df['room_type'].value_counts() / len(df)
df['room_type_freq'] = df['room_type'].map(freq)
```

---

## 20. INTERPRETAREA OUTPUTURILOR PYTHON / PANDAS / ML

### 20.1 df.info()

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149      ← numărul de rânduri
Data columns (total 5 columns):        ← numărul de coloane
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   sepal_length  150 non-null    float64   ← 0 valori lipsă
 1   sepal_width   150 non-null    float64
 2   petal_length  148 non-null    float64   ← 2 valori lipsă (150-148)
 3   petal_width   150 non-null    float64
 4   species        150 non-null    object    ← tip string/categoric
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
```

**Ce urmărești la grilă:**
- `Non-Null Count` < număr total rânduri → valori lipsă
- `object` = string/categoric (necesită encoding înainte de ML)
- `RangeIndex` = indexul implicit (0, 1, 2...) — nu a fost setat un index custom

### 20.2 df.describe()

```
       age        salary
count  100.0      98.0     ← count = non-null (salary are 2 NaN!)
mean    35.2    5200.0
std      8.4    1200.0
min     22.0    3000.0
25%     29.0    4400.0     ← Q1 — 25% din valori sunt sub această valoare
50%     34.0    5100.0     ← mediana (Q2)
75%     41.0    5900.0     ← Q3 — 75% din valori sunt sub această valoare
max     60.0    9800.0
```

**Reguli critice:**
- `count` = numărul de valori **non-null** — dacă e mai mic decât nr. rânduri → există NaN
- `describe()` implicit afișează doar coloanele **numerice**
- `describe(include='all')` sau `describe(include='object')` pentru coloane categorice
- IQR = Q3 - Q1 = 75% - 25%
- Outlieri: sub Q1 - 1.5×IQR sau peste Q3 + 1.5×IQR

### 20.3 df.value_counts() și df.groupby().agg()

```python
df['species'].value_counts()
# Output:
# setosa        50
# versicolor    50
# virginica     50
# Name: species, dtype: int64
# ← sortare descrescătoare după frecvență (implicit)
```

```python
df.groupby('species')['sepal_length'].agg(['mean', 'max', 'count'])
# Output:
#             mean   max  count
# species
# setosa      5.00  5.8     50
# versicolor  5.94  7.0     50
# virginica   6.59  7.9     50
# ← indexul = valorile coloanei din groupby
```

### 20.4 merge() cu indicator=True

```python
result = pd.merge(df1, df2, on='id', how='outer', indicator=True)
result['_merge'].value_counts()
# Output:
# both          45   ← id există în AMBELE df-uri (matched)
# left_only     12   ← id există NUMAI în df1 (stânga)
# right_only     8   ← id există NUMAI în df2 (dreapta)
```

**Valorile coloanei `_merge`:**
| Valoare | Semnificație |
|---------|-------------|
| `both` | rândul există în ambele tabele |
| `left_only` | rândul există numai în tabelul stâng |
| `right_only` | rândul există numai în tabelul drept |

### 20.5 loc vs iloc — output

```python
df.loc[2:4, 'name']      # rânduri cu INDEX LABEL 2,3,4 — INCLUSIV capătul
df.iloc[2:4, 0]          # rânduri cu POZIȚIE 2,3 — EXCLUSIV capătul
```

**Capcana clasică:**
- `loc[2:4]` → 3 rânduri (2, 3, 4 — slice inclusiv)
- `iloc[2:4]` → 2 rânduri (2, 3 — slice exclusiv ca în Python normal)

### 20.6 confusion_matrix

```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
# Output (clasificare binară 0/1):
# [[TN  FP]
#  [FN  TP]]
#
# Exemplu:
# [[85  15]
#  [10  90]]
```

**Poziții în matrice (clasificare binară):**
```
                 Predicție 0    Predicție 1
Actual 0    →   TN (col [0,0])  FP (col [0,1])
Actual 1    →   FN (col [1,0])  TP (col [1,1])
```

**Formule derivate:**
- Accuracy = (TP + TN) / Total
- Precision = TP / (TP + FP)  ← din toate prezise pozitive, câte sunt corect?
- Recall = TP / (TP + FN)     ← din toate pozitivele reale, câte au fost găsite?
- F1 = 2 × (Precision × Recall) / (Precision + Recall)

**Exemplu cu cm = [[85,15],[10,90]]:**
- TN=85, FP=15, FN=10, TP=90
- Accuracy = (90+85)/200 = 87.5%
- Precision = 90/(90+15) = 85.7%
- Recall = 90/(90+10) = 90%

### 20.7 classification_report

```
              precision    recall  f1-score   support

           0       0.85      0.90      0.87       100   ← clasa 0: 100 exemple reale
           1       0.90      0.85      0.87       100   ← clasa 1: 100 exemple reale

    accuracy                           0.87       200   ← accuracy globală
   macro avg       0.87      0.87      0.87       200   ← media SIMPLĂ per clasă
weighted avg       0.87      0.87      0.87       200   ← media PONDERATĂ cu support
```

**Coloane:**
- `precision` = TP / (TP + FP) — din ce am prezis că e clasa X, câte sunt corect?
- `recall` = TP / (TP + FN) — din ce e efectiv clasa X, câte am prins?
- `f1-score` = media armonică precision + recall
- `support` = numărul de exemple REALE din acea clasă în y_test
- `macro avg` = media simplă a tuturor claselor (ignoră dezechilibrul)
- `weighted avg` = media ponderată cu support (relevantă când clasele sunt dezechilibrate)

### 20.8 ROC Curve și AUC

```
TPR (Sensitivity/Recall)
1.0 |     *****
    |   **
    |  *           ← curba ROC: cu cât mai sus-stânga, cu atât mai bun
    | *
    |*
0.0 +-----------> FPR (1-Specificity)
   0.0            1.0
```

**Interpretare AUC (Area Under Curve):**
| AUC | Interpretare |
|-----|-------------|
| 1.0 | Model perfect |
| 0.9–1.0 | Excelent |
| 0.8–0.9 | Bun |
| 0.7–0.8 | Acceptabil |
| 0.5 | Aleatoriu (diagonala) — model inutil |
| < 0.5 | Mai rău decât aleatoriu |

- Diagonala (linie dreaptă de la (0,0) la (1,1)) = clasificator aleatoriu, AUC=0.5
- TPR = True Positive Rate = Recall = TP/(TP+FN)
- FPR = False Positive Rate = FP/(FP+TN)

### 20.9 K-Means — output

```python
kmeans = KMeans(n_clusters=3, random_state=0)
labels = kmeans.fit_predict(X)
# labels = array([0, 2, 1, 0, 2, 2, 1, ...])
# ← fiecare valoare = clusterul atribuit observației respective (0-indexed)

print(kmeans.cluster_centers_)
# [[3.14, 2.56],    ← centrul clusterului 0 (coordonate în spațiul feature-urilor)
#  [6.81, 3.07],    ← centrul clusterului 1
#  [5.01, 3.42]]    ← centrul clusterului 2

print(kmeans.inertia_)   # WCSS — suma pătratelor distanțelor față de centru
# 78.85               ← mai mic = clustere mai compacte
```

**Silhouette score:**
| Valoare | Interpretare |
|---------|-------------|
| ~1.0 | Clustere separate și compacte — perfect |
| ~0.0 | Observații la granița dintre clustere |
| < 0 | Observații probabil în clusterul greșit |

### 20.10 StandardScaler vs MinMaxScaler — output

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# Rezultat: valori centrate la 0 cu std=1
# Ex: [-1.23,  0.45, -0.87,  2.01, ...]
# Valori negative = sub medie; pozitive = peste medie

scaler2 = MinMaxScaler()
X_scaled2 = scaler2.fit_transform(X)
# Rezultat: valori în intervalul [0, 1]
# Ex: [0.0, 0.3, 0.7, 1.0, ...]
# 0.0 = minimul original; 1.0 = maximul original
```

**Diferența critică:**
- `StandardScaler`: z-score = (x - mean) / std — nu garantează interval fix; sensibil la outlieri
- `MinMaxScaler`: (x - min) / (max - min) — interval garantat [0,1]; **foarte** sensibil la outlieri

### 20.11 Metrici de regresie — interpretare valori

```python
mse  = mean_squared_error(y_test, y_pred)    # Media pătratelor erorilor
rmse = np.sqrt(mse)                           # Rădăcina — în aceleași unități cu y
mae  = mean_absolute_error(y_test, y_pred)    # Media valorilor absolute ale erorilor
r2   = r2_score(y_test, y_pred)               # Coeficient determinare
```

**Interpretare:**
| Metrică | Interval | Mai bun când |
|---------|----------|-------------|
| MSE | [0, ∞) | → 0 |
| RMSE | [0, ∞) | → 0 (interpretabil: unități ca y) |
| MAE | [0, ∞) | → 0 (robust la outlieri vs RMSE) |
| R² | (-∞, 1] | → 1 (R²=1: model perfect; R²=0: model = media y; R²<0: model mai rău decât media) |

**RMSE vs MAE:**
- RMSE penalizează mai mult erorile mari (pătrat)
- MAE tratează toate erorile egal
- Dacă RMSE >> MAE → există outlieri în erori

### 20.12 Feature Importance (Random Forest / Decision Tree)

```python
importances = rf.feature_importances_
# array([0.42, 0.28, 0.18, 0.12])
# ← suma = 1.0; mai mare = mai important pentru predicție

feat_df = pd.Series(importances, index=X.columns).sort_values(ascending=False)
# petal_length    0.42
# petal_width     0.28
# sepal_length    0.18
# sepal_width     0.12
```

**Interpretare:**
- Suma tuturor feature importance = 1.0
- O variabilă cu importance 0.42 explică ~42% din puterea de separare a arborelui
- Feature importance ≠ corelație — poate captura relații neliniare

### 20.13 cross_val_score — output

```python
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='roc_auc')
# array([0.88, 0.91, 0.87, 0.93, 0.89])
# ← 5 scoruri (câte un fold) — variabilitate = cât de stabil e modelul

print(cv_scores.mean())   # 0.896  ← performanța medie estimată
print(cv_scores.std())    # 0.021  ← mic = stabil; mare = instabil/overfitting
```

**Capcana grilă:** `cv=5` → se rulează 5 antrenări, nu 1. Output-ul are 5 valori, nu 1.

### 20.14 Pandas Series vs DataFrame — output vizual

```python
# Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# a    10
# b    20
# c    30
# dtype: int64
# ← index stânga, valori dreapta, un singur dtype

# DataFrame
df = pd.DataFrame({'x': [1,2], 'y': [3,4]})
#    x  y
# 0  1  3
# 1  2  4
# ← header cu nume coloane, index pe rândul din stânga
```

**Diferența cheie:**
- `s['a']` → returnează un scalar (10)
- `df['x']` → returnează o Series (coloana x)
- `df[['x']]` → returnează un DataFrame (o coloană, dar tot DataFrame)
