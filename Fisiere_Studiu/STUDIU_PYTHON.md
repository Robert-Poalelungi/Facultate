# FIȘIER DE STUDIU PYTHON — TEST GRILĂ
> Acoperă toate seminarele Python (1–9)

---

## SEMINAR 2 — STREAMLIT + PANDAS BASICS

### Ce este Streamlit?
Bibliotecă Python open-source pentru aplicații web interactive **fără HTML/CSS/JS**.
```
streamlit run app.py
```

### Elementele principale Streamlit

| Funcție | Descriere |
|---|---|
| `st.title("text")` | Titlul aplicației |
| `st.header("text")` | Header secțiune |
| `st.write("text")` | Afișare generică (text, date, grafice) |
| `st.markdown("text")` | Text formatat Markdown |
| `st.code("cod", language="python")` | Bloc de cod |

### Widget-uri interactive
```python
st.button("Apasă-mă!")           # buton
st.text_input("Introdu text:")    # casetă text
st.text_area("Text lung:")        # casetă text mare
st.number_input("Număr:", value=0)
st.slider("Valoare", 0, 100, 50)  # (label, min, max, default)
st.selectbox("Alege:", ["A","B","C"])
st.multiselect("Mai multe:", ["A","B","C"])
st.radio("Opțiune:", ["X","Y","Z"])
st.checkbox("Bifează")
st.date_input("Dată:")
st.file_uploader("Fișier:", type=["csv","txt"])
```

### Layout
```python
st.sidebar.radio("Navighează:", ["Sec1","Sec2"])   # bară laterală
col1, col2 = st.columns(2)                          # coloane
with col1: st.write("Col 1")
with st.expander("Click pentru mai mult"): st.write("...")
tab1, tab2 = st.tabs(["Tab1","Tab2"])
with tab1: st.write("...")
```

### Session State (păstrare date între reîncărcări!)
```python
if 'numar_clickuri' not in st.session_state:
    st.session_state.numar_clickuri = 0

def creste():
    st.session_state.numar_clickuri += 1

st.button("Click!", on_click=creste)
```
**Atenție!** Fiecare interacțiune reexecută ÎNTREG scriptul. `st.session_state` salvează datele între reîncărcări.

---

### Pandas — Structuri de date

#### Series (unidimensional)
```python
import pandas as pd

# Din listă
s = pd.Series([10, 20, 30])             # index implicit: 0, 1, 2
s = pd.Series([10,20,30], index=['a','b','c'])  # index custom

# Din dicționar
s = pd.Series({'California': 10, 'Texas': 20})
```

#### DataFrame (bidimensional — tabel)
```python
# Din dicționar
df = pd.DataFrame({'Nume': ['Alice','Bob'], 'Vârstă': [25,30]})

# Din listă
df = pd.DataFrame(['A','B','C'], columns=['Literă'])

# Din Series
df = pd.DataFrame({'col1': series1, 'col2': series2})
```

---

### Selecție și filtrare

#### `.loc[]` — după ETICHETĂ (label-based)
```python
df.loc[3]                          # rândul cu eticheta 3
df.loc[1:2]                        # rânduri cu etichete 1 și 2 (INCLUSIV 2!)
df.loc[df['Preț'] < 1.0, ['Produs','Cantitate']]  # condiție + coloane
df.loc[conditie, 'coloana'] = valoare  # actualizare
```

#### `.iloc[]` — după POZIȚIE (position-based, 0-indexed)
```python
df.iloc[3]                         # al 4-lea rând (poziție 3)
df.iloc[1:3, 0:2]                  # rânduri 1-2, coloane 0-1 (EXCLUSIV capătul!)
df.iloc[[0, 3], [0, 2]]            # rânduri și coloane non-consecutive
```

> **Diferența cheie:**
> - `loc` folosește **etichete** → `df.loc[3]` = rândul cu indexul 3
> - `iloc` folosește **poziții** → `df.iloc[3]` = al 4-lea rând
> - `iloc['banana']` → **EROARE**, iloc acceptă doar întregi!
> - Dacă indexul are duplicate, `loc[2]` returnează **TOATE** rândurile cu eticheta 2

#### Filtrare condițională
```python
df[df['Cantitate'] >= 100]                          # simplu
df[(df['Preț'] >= 1.0) & (df['Preț'] <= 2.0)]      # AND → &
df[(df['Tip'] == 'A') | (df['Tip'] == 'B')]         # OR → |
```

#### Operații pe coloane
```python
df.rename(columns={'vechi': 'nou'})    # redenumire
df.drop(columns=['col1'])              # ștergere coloană
df['col'].isna().sum()                 # număr valori lipsă
```

---

## SEMINAR 3 — PANDAS AVANSAT (GroupBy, Merge, Vizualizare)

### Date — phone_data.csv
Coloane: `index, date, duration, item, month, network, network_type`
- `item`: calls, sms, data
- `network`: Vodafone, Meteor, Three, Tesco, voicemail, landline, data, world

### Conversie date
```python
import dateutil
df['date'] = df['date'].apply(dateutil.parser.parse, dayfirst=True)
```

### Statistici simple
```python
df['item'].count()                    # număr înregistrări
df['duration'].max()                  # valoarea maximă
df['duration'].sum()                  # suma
df['month'].value_counts()            # frecvența pe luni
df['network'].nunique()               # număr valori unice
df.describe()                         # statistici descriptive (count, mean, std, min, max, quartile)
```

### GroupBy
```python
# Vizualizare grupuri
df.groupby(['item']).groups.keys()
len(df.groupby(['month']).groups['2014-11'])

# Agregare simplă
df.groupby('item').first()            # prima înregistrare din fiecare grup
df.groupby('month')['duration'].sum() # suma duratelor per lună

# Grupare pe mai multe coloane
df.groupby(['month', 'item'])['date'].count()

# Funcție pe grupuri filtrate
df[df['item'] == 'call'].groupby('network')['duration'].sum()
```

### Aggregation — `.agg()`
```python
# O funcție per coloană
df.groupby(['month', 'item']).agg({
    'duration': sum,
    'network_type': "count",
    'date': 'first'
})

# Mai multe funcții pe aceeași coloană
df.groupby(['month', 'item']).agg({
    'duration': [min, max, sum],
    'network_type': "count",
    'date': [min, 'first', 'nunique']
})
```

### Merge / Join
```python
# Inner join (implicit) — păstrează doar rândurile cu corespondent în AMBELE tabele
result = pd.merge(df1, df2[['use_id','platform','device']], on='use_id')

# Left join — păstrează TOATE rândurile din df1
result = pd.merge(df1, df2[['use_id','platform','device']], on='use_id', how='left')

# Right join — păstrează TOATE rândurile din df2
result = pd.merge(df1, df2[['use_id','platform','device']], on='use_id', how='right')

# Outer join — păstrează TOATE rândurile din ambele
result = pd.merge(df1, df2[['use_id','platform','device']], on='use_id', how='outer')

# Cu indicator (arată sursa fiecărui rând)
result = pd.merge(df1, df2, on='use_id', how='outer', indicator=True)

# Join pe coloane cu nume diferite
pd.merge(result, df3, left_on='device', right_on='Model', how='left')
```

### Vizualizare — matplotlib
```python
import matplotlib.pyplot as plt

# Bar chart
df['AGE'].plot(kind='bar')
plt.xlabel('ID_CLIENT'); plt.ylabel('AGE'); plt.show()

# Histogramă
plt.hist(df['Revenue'], bins=20, color='blue', edgecolor='black')
plt.title('...'); plt.xlabel('...'); plt.ylabel('Frequency'); plt.show()

# Pie chart
counts = df['Property'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.show()

# Bar plot agregat
df.groupby('Type')['Revenue'].mean().plot(kind='bar', color='skyblue', edgecolor='black')
plt.xticks(rotation=45); plt.show()

# Bar chart grupat (matplotlib direct)
df['AGE'].plot(kind='bar')
```

---

## SEMINAR 4 — PANDAS APLICAT (Stores Dataset)

### Date — StoresPrep.csv
Coloane: `Store_Number, AreaStore, Property, Type, Old/New, Checkout Number, Revenue`
- `Property`: Owned, Rental, Cooperate
- `Type`: Hyper, Extra, Express

### Operații de bază
```python
df.head()           # primele 5 rânduri
df.info()           # tipuri de date, valori non-null
df.describe()       # statistici descriptive
df.isnull().sum()   # valori lipsă
df['Property'].nunique()          # număr valori unice
df['Property'].unique()           # valorile unice
df.nunique()                      # unice pentru fiecare coloană
```

### GroupBy cu agg
```python
# Total revenue per tip magazin
df.groupby('Type')['Revenue'].sum()

# Medie checkout per categorie Old/New
df.groupby('Old/New')['Checkout Number'].mean()

# Total, medie, maxim revenue per tip
df.groupby('Type')['Revenue'].agg(['sum','mean','max'])

# Magazinul cu revenue maxim per tip
idx = df.groupby('Type')['Revenue'].idxmax()
df.loc[idx]
```

### pd.cut() — categorii personalizate
```python
# Categorii de vârstă la decade
df['Age_Group'] = pd.cut(df['Age'], bins=range(10, 71, 10), right=False)

# Categorii de venit cu etichete
df['Income_Category'] = pd.cut(df['Annual_Income_(k$)'],
                                bins=[0, 40, 70, 150],
                                labels=['Mic','Mediu','Mare'])
```

---

## SEMINAR 5 — EDA (Exploratory Data Analysis)

### Date — AB_NYC_2019.csv (Airbnb NYC)
48,895 înregistrări. Coloane cheie: `neighbourhood_group, room_type, price, minimum_nights, number_of_reviews, availability_365`

### Pași EDA standard
1. **Inspecție inițială:** `df.head()`, `df.info()`, `df.describe()`
2. **Valori lipsă:** `df.isnull().sum()`
3. **Distribuții:** histograme pentru variabile numerice
4. **Valori unice:** `df['col'].value_counts()`
5. **Corelații:** `df.corr()` + heatmap seaborn

```python
import seaborn as sns

# Distribuție cu KDE
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
sns.histplot(data['Age'], bins=20, kde=True, ax=axes[0,0])
axes[0,0].set_title('Age Distribution')
plt.tight_layout()
plt.show()
```

---

## SEMINAR 6 — K-MEANS CLUSTERING

### Date — Mall_Customers.csv
200 clienți. Coloane: `CustomerID, Genre, Age, Annual_Income_(k$), Spending_Score`

### Pași preprocessing (obligatorii înainte de K-Means)

```python
# 1. Verificare valori lipsă
data.isnull().sum()

# 2. Encodare variabile categorice
data['Genre'] = data['Genre'].map({'Male': 0, 'Female': 1})

# 3. Feature Scaling (StandardScaler)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = pd.DataFrame(
    scaler.fit_transform(data.drop(['CustomerID'], axis=1)),
    columns=data.columns[1:]
)

# 4. Detecție Outlieri — Boxplot
sns.boxplot(data=data_scaled)
plt.title('Boxplot for Outlier Detection')
plt.show()

# 5. Corelație — Heatmap
correlation_matrix = data_scaled.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()
```

### Algoritmul K-Means

```python
from sklearn.cluster import KMeans

X = data.iloc[:, [2, 3]].values   # Annual_Income + Spending_Score

# Metoda Elbow — găsim k optim
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

sns.lineplot(x=range(1, 11), y=wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.show()

# Aplicare K-Means cu k optim
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)
```

### Evaluare — Silhouette Score
```python
from sklearn.metrics import silhouette_score

sil_score = silhouette_score(X, y_kmeans)

# Interpretare:
# ~+1 → punctul este bine încadrat în cluster
# ~0  → punctul este la granița dintre clustere
# < 0 → punctul este probabil atribuit greșit
```

### Vizualizare clustere
```python
sns.scatterplot(x=X[y_kmeans==0, 0], y=X[y_kmeans==0, 1], color='yellow', label='Cluster 1')
sns.scatterplot(x=X[y_kmeans==1, 0], y=X[y_kmeans==1, 1], color='blue',   label='Cluster 2')
sns.scatterplot(x=X[y_kmeans==2, 0], y=X[y_kmeans==2, 1], color='green',  label='Cluster 3')
sns.scatterplot(x=kmeans.cluster_centers_[:,0], y=kmeans.cluster_centers_[:,1],
                color='red', label='Centroids', s=300, marker=',')
plt.show()
```

> **Concepte cheie K-Means:**
> - `init='k-means++'` → inițializare inteligentă a centroizilor (evită minime locale)
> - `inertia_` → WCSS (Within Cluster Sum of Squares) — suma distanțelor față de centroid
> - **Metoda Elbow** → punctul de „cot" din graficul WCSS indică k optim
> - **Silhouette Score** → valori între -1 și 1, mai mare = clustere mai bune

---

## SEMINAR 7 — CLASIFICARE

### Date — supplementary_demographics.csv

### Algoritmi de clasificare (sklearn)
- **Logistic Regression** — pentru clasificare binară/multiclasă
- **Decision Tree** — cascadă de întrebări da/nu
- **Random Forest** — bagging: mai mulți arbori votează
- **SVM** — hiperplan de separare

### Metrici evaluare clasificare
```python
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

accuracy_score(y_test, y_pred)
roc_auc_score(y_test, y_prob)
print(classification_report(y_test, y_pred))
```

---

## SEMINAR 8 — REGRESIE

### Tipuri de regresie
- **Liniară simplă:** o variabilă predictivă → `y = ax + b`
- **Liniară multiplă:** mai multe variabile predictive
- **Logistică:** variabilă dependentă categorică (clasificare)

### Metrici evaluare regresie
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

MSE  = mean_squared_error(y_test, y_pred)    # sensibil la outlieri
MAE  = mean_absolute_error(y_test, y_pred)   # mai robust
R2   = r2_score(y_test, y_pred)              # 0-1, mai mare = mai bun
```

---

## SEMINAR 9 — ALGORITMI PREDICTIVI

### Ierarhia algoritmilor (de la simplu la complex)

| Nivel | Algoritm | Idee cheie |
|---|---|---|
| 1 | **Linear Regression** | Formula simplă: `y = ax + b` |
| 2 | **Decision Tree** | Cascadă de întrebări da/nu |
| 3 | **Random Forest** | Bagging — mai mulți arbori votează |
| 4 | **Gradient Boosting** | Boosting — arbori secvențiali, fiecare corectează erorile precedentului |
| 5 | **Neural Networks** | Neuroni artificiali cu backpropagation |
| 6 | **Transformers** | Atenție globală — GPT, BERT, Claude |

### Cross-validation
```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
```

---

## REZUMAT RAPID — PANDAS CHEATSHEET

```python
# Citire
df = pd.read_csv('fisier.csv')
df.to_csv('output.csv')

# Inspecție
df.head(n)       # primele n rânduri
df.tail(n)       # ultimele n rânduri
df.shape         # (rânduri, coloane)
df.columns       # lista coloanelor
df.dtypes        # tipurile de date
df.info()        # info complet
df.describe()    # statistici

# Selecție
df['col']                    # o coloană
df[['col1','col2']]          # mai multe coloane
df.loc[idx, 'col']           # după etichetă
df.iloc[pos, col_pos]        # după poziție

# Filtrare
df[df['col'] > 5]
df[(cond1) & (cond2)]
df[(cond1) | (cond2)]

# Modificare
df['col_nou'] = valoare
df.loc[cond, 'col'] = valoare
df.rename(columns={'vechi':'nou'}, inplace=True)
df.drop(columns=['col'])
df.drop(index=[0,1])

# Valori lipsă
df.isnull().sum()
df.dropna()
df.fillna(valoare)

# GroupBy
df.groupby('col')['target'].sum()
df.groupby('col').agg({'col1': 'sum', 'col2': 'mean'})

# Merge
pd.merge(df1, df2, on='cheie', how='inner/left/right/outer')

# Sortare
df.sort_values('col', ascending=False)
```

---

## ÎNTREBĂRI FRECVENTE GRILĂ

**Q: Ce diferență este între `loc` și `iloc`?**
A: `loc` folosește etichete (labels), `iloc` folosește poziții numerice (0-indexed).

**Q: Ce returnează `df.iloc['banana']`?**
A: **EROARE** — iloc acceptă doar indici întregi.

**Q: Ce face `df.loc[2]` dacă indexul are duplicate (ex: `[1,2,2,3]`)?**
A: Returnează **toate rândurile** cu eticheta 2 (nu doar primul).

**Q: Ce este WCSS / inertia?**
A: Within Cluster Sum of Squares — suma pătratelor distanțelor fiecărui punct față de centroidul clusterului său. Mai mic = mai bun.

**Q: Ce indică Silhouette Score = -0.2?**
A: Punctul este **probabil atribuit greșit** unui cluster.

**Q: inner/left/right/outer join — ce păstrează?**
A: inner = intersecție; left = toate din stânga; right = toate din dreapta; outer = reuniune.

**Q: Ce face `st.session_state`?**
A: Păstrează valorile variabilelor între reîncărcările scriptului Streamlit.

**Q: Parametrii StandardScaler — ce face?**
A: Aduce datele la distribuție cu **media 0 și deviație standard 1** (standardizare Z-score).

**Q: `init='k-means++'` vs `init='random'` în K-Means?**
A: `k-means++` inițializează centroizii inteligent (distanțați), evitând minime locale.
