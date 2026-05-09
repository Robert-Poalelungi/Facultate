# Grile Rezolvate — Tipare și Răspunsuri
## Condensat rapid pentru examen

---

## SECȚIUNEA 1: SAS — GRILE TIPICE

### G1. Sintaxă obligatorie SAS
```
Q: Ce caracter este obligatoriu la sfârșitul fiecărei instrucțiuni SAS?
A: ; (punct și virgulă)
   Fără ; → eroarea se propagă la instrucțiunea URMĂTOARE (nu la cea curentă)
```

### G2. WORK vs Permanent
```
Q: Unde se salvează dataseturile create fără LIBNAME?
A: În librăria temporară WORK (ștearsă la închiderea sesiunii)

Q: Cum se creează un dataset permanent?
A: LIBNAME mylib 'cale/folder';
   DATA mylib.date; ...   (cu prefixul libname)

Q: Ce conține WORK.SASMACR?
A: Macro-urile definite în sesiunea curentă (nu dataseturile obișnuite)
```

### G3. Tipuri de coloane
```
Q: Care este lungimea implicită a unei coloane numerice în SAS?
A: 8 bytes (stochează valori mari și zecimale)

Q: Care este lungimea implicită a unei coloane caracter?
A: 8 characters (dacă nu e specificat LENGTH sau $n în INPUT)

Q: Cum se declară o coloană caracter în INPUT?
A: INPUT nume $;     ($ după variabilă = caracter)
```

### G4. FORMAT vs INFORMAT
```
Q: FORMAT schimbă valorile stocate în dataset?
A: NU! FORMAT schimbă DOAR afișarea (valorile rămân 1, 2, 3...)

Q: Ce face INFORMAT?
A: Citește/convertește date la input (cum să interpreteze valoarea la citire)

Q: FORMAT DOLLAR12.2 ce face?
A: Afișează numărul cu simbol $ și 2 zecimale. Exemplu: $1,234.56
   Valoarea stocată rămâne 1234.56
```

### G5. WHERE vs IF
```
Q: Care operator se poate folosi ATÂT în DATA step CÂT ȘI în PROC?
A: WHERE

Q: Care operator funcționează în DATA step dar NU în PROC step?
A: IF

Q: Care operator citește TOATE rândurile din input (inclusiv cele eliminate)?
A: IF (citește toate, elimină unele înainte de output)
   WHERE (elimină înainte de citire — mai eficient!)

Q: WHERE $gen EQ 'M' — funcționează cu variabile create în DATA step curent?
A: NU! WHERE nu poate referi variabile create în același DATA step (nu există încă)
   IF trebuie folosit pentru variabile noi
```

### G6. MERGE vs SET
```
Q: Ce face MERGE fără BY?
A: One-to-one merge (combină rândul 1 cu rândul 1, rândul 2 cu rândul 2, etc.)

Q: MERGE cu BY — ce tip de join este implicit?
A: Full outer join (păstrează TOATE rândurile din AMBELE datasets)

Q: Ce trebuie să facă datasets înainte de MERGE BY?
A: SORTATE după variabila BY (PROC SORT BY var; înainte de MERGE)

Q: Care instrucțiune concatenează datasets (pune rând după rând)?
A: SET
   DATA all; SET ds1 ds2 ds3; RUN;
```

### G7. PROC SORT
```
Q: PROC SORT cu OUT= suprascrie dataset-ul original?
A: NU! Creează un dataset nou. Cel original rămâne NEMODIFICAT.

Q: Cum se sortează descrescător?
A: BY DESCENDING variabila;  (DESCENDING înainte de variabilă)

Q: PROC SORT elimină coloane?
A: NU! Menține TOATE coloanele. (Spre deosebire de DROP/KEEP)

Q: Se poate sorta după 2 variabile?
A: Da: BY var1 DESCENDING var2;
```

### G8. PROC PRINT
```
Q: Ce face NOOBS în PROC PRINT?
A: Elimină coloana "Obs" (numărul de observație) din output

Q: Ce face ID în PROC PRINT?
A: Înlocuiește coloana Obs cu variabila specificată ca identificator

Q: LABEL în PROC PRINT ce face?
A: Afișează ETICHETELE coloanelor în loc de numele variabilelor

Q: Ce trebuie să existe înaintea BY în PROC PRINT?
A: Datele SORTATE după variabila BY (altfel eroare sau rezultat incorect)

Q: SUM în PROC PRINT ce face?
A: Calculează și afișează suma la sfârșitul coloanei specificate
```

### G9. PROC MEANS
```
Q: Diferența BY vs CLASS în PROC MEANS?
A: BY: datele TREBUIE sortate, creează secțiuni separate în output
   CLASS: datele NU trebuie sortate, mai flexibil

Q: Cum se salvează rezultatele PROC MEANS?
A: OUTPUT OUT=numeDataset MEAN=medie STD=devStd;
   (cu NOPRINT pentru a nu afișa)

Q: Ce statistici calculează PROC MEANS implicit?
A: N, MIN, MAX, MEAN, STD (dacă nu se specifică altfel)

Q: CLM / ALPHA în PROC MEANS?
A: CLM = afișează intervalul de confidență
   ALPHA=0.05 = interval la 95% (implicit)
```

### G10. PROC UNIVARIATE
```
Q: Ce face NEXTROBS= în PROC UNIVARIATE?
A: Listează cele mai extreme N OBSERVAȚII (rânduri) — cu valorile tuturor variabilelor

Q: Ce face NEXTRVAL= în PROC UNIVARIATE?
A: Listează cele mai extreme N VALORI UNICE

Q: HISTOGRAM în PROC UNIVARIATE?
A: Creează histogramă pentru variabila analizată

Q: NORMAL în PROC UNIVARIATE?
A: Efectuează teste de normalitate (Shapiro-Wilk, Kolmogorov-Smirnov, etc.)
```

### G11. PROC CONTENTS
```
Q: PROC CONTENTS _ALL_ ce face?
A: Afișează conținutul TUTUROR datasets din librăria WORK
   (sau din librăria specificată cu DATA=libname._ALL_)

Q: Ce informații afișează PROC CONTENTS?
A: Număr observații, număr variabile, lungimi, tipuri, labels, formats
```

### G12. Formate dată SAS
```
Q: Cum se afișează o dată SAS în format zi/lună/an?
A: FORMAT data DDMMYY10.;  → 09/05/2026
   FORMAT data DATE9.;    → 09MAY2026
   FORMAT data MMDDYY10.; → 05/09/2026

Q: Ce stochează SAS intern pentru date calendaristice?
A: Numărul de zile de la 1 ianuarie 1960
   1 = 2 ianuarie 1960, 0 = 1 ianuarie 1960

Q: Funcțiile MONTH(), YEAR(), DAY() returnează?
A: MONTH(data): 1-12 (nu 0-11!)
   YEAR(data): anul (ex: 2026)
   DAY(data): 1-31
```

### G13. Funcții SAS
```
Q: INPUT('123', 8.) — ce face?
A: Convertește STRING '123' → NUMĂR 123
   (INPUT = caracter → numeric)

Q: PUT(123, 8.) — ce face?
A: Convertește NUMĂR 123 → STRING '123'
   (PUT = numeric → caracter)

Q: SUBSTR('ABCDE', 2, 3) — ce returnează?
A: 'BCD'  (pornește de la poziția 2, lungime 3)

Q: UPCASE('ana') — returnează?
A: 'ANA'

Q: TRIM('  hello  ') — returnează?
A: 'hello'  (elimină spații de la DREAPTA)
```

### G14. INFILE și opțiuni citire
```
Q: DLM=','  în INFILE ce face?
A: Specifică virgula ca delimitator (pentru CSV)

Q: DSD în INFILE ce face?
A: Permite valori lipsă consecutive (,,) și tratează valorile în ghilimele corect

Q: MISSOVER în INFILE ce face?
A: Dacă o linie se termină înaintea ultimei variabile → valorile rămase = MISSING
   (fără MISSOVER → trece la linia următoare)

Q: Diferența column input vs list input?
A: Column input: INPUT var 1-5 var2 7-10; (specifică coloanele exacte)
   List input: INPUT var1 var2 $;  (separate prin spații)
   Formatted input: INPUT var1 : $10.;  (cu informat)
```

### G15. TITLE
```
Q: TITLE;  (fără text) ce face?
A: Șterge TOATE titlurile (title1 prin title10)

Q: TITLE2 'text';  ce face?
A: Setează al doilea titlu. Titlurile 3-10 rămân.
   Titlul 1 rămâne dacă nu e modificat explicit.
```

### G16. DROP / KEEP
```
Q: DROP în DATA step — variabila eliminată poate fi folosită în calcule?
A: Da! DROP elimină variabila din OUTPUT (dataset final), 
   dar în DATA step poate fi folosită pentru calcule

Q: KEEP=  în opțiunile dataset ce face?
A: Menține DOAR variabilele specificate în output
   DATA out; SET in (KEEP=var1 var2); RUN;
```

---

## SECȚIUNEA 2: SAS ENTERPRISE GUIDE — GRILE TIPICE

### G17. Legătura dintre SAS EG și fișiere
```
Q: Când adăugăm un fișier Excel în SAS EG (Process Flow), ce se creează?
A: Un POINTER (referință) la fișier, nu o copie

Q: Dacă modificăm fișierul Excel extern, ce se întâmplă în SAS EG?
A: La re-rulare, SAS EG va citi datele actualizate (pointer, nu copie)
```

### G18. Format output implicit SAS EG
```
Q: Care este formatul implicit al output-ului în SAS EG?
A: HTML (se deschide în browser integrat)
```

### G19. Query Builder — Join-uri
```
Q: Query Builder — join implicit (Automatic) — cum se face?
A: Pe baza NUMELUI coloanei (dacă 2 tabele au coloană cu același nume)
   NU pe tip de date (poate genera erori dacă tipul diferă)

Q: Query Builder — ce tipuri de join-uri sunt disponibile?
A: Inner Join, Left Outer Join, Right Outer Join, Full Outer Join

Q: Care este join-ul implicit în Query Builder?
A: Inner Join (afișează doar rândurile cu corespondență în ambele tabele)
```

### G20. Tasks în SAS EG
```
Q: Care task generează statistici sumare (frecvențe pentru categoriale)?
A: One-Way Frequencies (sau Summary Tables pentru cross-tab)

Q: Care task listează datele (echivalent PROC PRINT)?
A: List Data

Q: Care task calculează statistici descriptive (mean, std, etc.)?
A: Summary Statistics (echivalent PROC MEANS/SUMMARY)
```

### G21. Parametrii în SAS EG
```
Q: Parametrii în SAS EG pot fi de tip list (dropdown)?
A: Da — utilizatorul alege dintr-o listă predefinită

Q: Parametrii pot fi de tip text liber?
A: Da

Q: Parametrii pot fi de tip "range/interval numeric"?
A: NU (nu există tip range direct ca parametru simplu)
```

### G22. Data View vs Dataset
```
Q: Ce este un Data View în SAS EG?
A: O vizualizare virtuală a datelor — nu stochează date fizic, 
   calculează la cerere din sursa originală
   Avantaj: Economisește spațiu pe disc/memorie

Q: Când e util Data View vs Dataset fizic?
A: Data View: când datele sursă se actualizează frecvent sau pentru economie de spațiu
   Dataset fizic: când datele sunt folosite des și viteza de acces e critică
```

---

## SECȚIUNEA 3: PYTHON — GRILE TIPICE

### G23. Output prediction — liste
```python
lst = [1, 2, 3, 4, 5]
print(lst[-2:])    # → [4, 5]
print(lst[::2])    # → [1, 3, 5]
print(lst[1:4])    # → [2, 3, 4]

result = lst.sort()
print(result)      # → None  (sort returnează None!)

lst2 = sorted(lst)
print(lst2)        # → [1, 2, 3, 4, 5]  (sorted returnează lista nouă)
```

### G24. Tuple — operații invalide
```python
t = (1, 2, 3)
t.append(4)  # → AttributeError: 'tuple' object has no attribute 'append'
t[0] = 99    # → TypeError: 'tuple' object does not support item assignment
del t[0]     # → TypeError
del t        # → OK! Șterge VARIABILA (nu elementul)
```

### G25. Dict — chei hashable
```python
d = {[1,2]: "val"}   # → TypeError: unhashable type: 'list'
d = {(1,2): "val"}   # → OK
d = {1: "val"}       # → OK
d = {"a": "val"}     # → OK
```

### G26. Comprehension output
```python
result = [x**2 for x in range(5) if x % 2 == 0]
# x: 0,1,2,3,4 → filtrat: 0,2,4 → x**2: 0,4,16
# → [0, 4, 16]

d = {k: v for k, v in [('a',1), ('b',2)]}
# → {'a': 1, 'b': 2}
```

### G27. Operatori aritmetici
```python
10 / 3    # → 3.3333...  (float!)
10 // 3   # → 3           (int, floor division)
10 % 3    # → 1           (rest)
2 ** 10   # → 1024        (putere)
10 / 2    # → 5.0         (FLOAT, chiar dacă exact!)
```

### G28. String slicing
```python
s = "Python"
s[0]      # → 'P'
s[-1]     # → 'n'
s[1:4]    # → 'yth'
s[::-1]   # → 'nohtyP'
s[::2]    # → 'Pto'  (pozițiile 0,2,4)
```

### G29. Funcții care returnează None
```python
# Metodele IN PLACE returnează None:
lst.sort()      # → None
lst.reverse()   # → None
lst.append(x)   # → None
lst.extend([])  # → None
dct.update({})  # → None
random.shuffle(lst)  # → None

# Funcțiile care returnează rezultat NOU:
sorted(lst)     # → lista nouă
reversed(lst)   # → iterator
```

### G30. Lambda și funcții higher-order
```python
f = lambda x, y: x + y
f(3, 4)    # → 7

# filter
evens = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5]))
# → [2, 4]

# map
doubled = list(map(lambda x: x*2, [1,2,3]))
# → [2, 4, 6]

# sorted cu key
words = ["banana", "apple", "cherry"]
sorted(words, key=lambda w: len(w))
# → ['apple', 'banana', 'cherry']  (sortate după lungime)
```

---

## SECȚIUNEA 4: PANDAS — GRILE TIPICE

### G31. loc vs iloc slice
```python
# DataFrame cu index 0,1,2,3,4
df.loc[1:3]     # rândurile 1, 2, 3 (INCLUSIV capătul drept)
df.iloc[1:3]    # rândurile 1, 2 (EXCLUSIV capătul drept)

df.loc[:, 'Revenue']     # coloana Revenue (toate rândurile)
df.iloc[:, -1]           # ultima coloană (toate rândurile)
```

### G32. groupby + agg
```python
# Revenue total per Tip de store
df.groupby('Tip')['Revenue'].sum()

# Statistici multiple
df.groupby('Tip')['Revenue'].agg(['sum', 'mean', 'max'])

# Rândul cu Revenue maxim per Tip
idx = df.groupby('Tip')['Revenue'].idxmax()
df.loc[idx]
```

### G33. merge tipuri
```python
# INNER: doar id-uri comune
# LEFT: toate din stânga + matching din dreapta
# RIGHT: matching din stânga + toate din dreapta
# OUTER: toate din ambele, NaN unde nu e corespondență

pd.merge(df1, df2, on='id', how='left')
# Dacă id există în df1 dar nu în df2 → coloanele din df2 = NaN
```

### G34. Valori lipsă
```python
df.isnull().sum()    # NaN per coloană
df.dropna()          # șterge rânduri cu orice NaN
df.fillna(df.mean()) # înlocuiește NaN cu media (per coloană)
df.fillna(0)         # înlocuiește NaN cu 0
```

### G35. apply și map
```python
df['col'].map({'A': 1, 'B': 2})      # înlocuire valori (Series)
df['col'].apply(lambda x: x*2)       # funcție per element
df.apply(lambda col: col.max(), axis=0)  # per coloană
df.apply(lambda row: row.sum(), axis=1)  # per rând
```

---

## SECȚIUNEA 5: ML — GRILE TIPICE

### G36. K-Means
```
Q: K-Means este algoritm supervizat sau nesupervizat?
A: NESUPERVIZAT (nu are etichete/target)

Q: Ce măsoară WCSS (inertia)?
A: Suma distanțelor pătratice de la fiecare punct la centroidul clusterului său
   (mai mic = mai bun, dar scade mereu cu K mai mare)

Q: Ce este Elbow Method?
A: Alegerea K-ului optim unde curba WCSS vs K face "cotul" (inflexiune)

Q: Silhouette Score +1 înseamnă?
A: Punct perfect clasificat, bine separat de alte clustere

Q: Silhouette Score -1 înseamnă?
A: Punct clasificat greșit (ar trebui în alt cluster)

Q: Silhouette Score 0 înseamnă?
A: Punct pe granița dintre două clustere

Q: De ce silhouette începe de la K=2?
A: Necesită minim 2 clustere pentru comparație
```

### G37. Scalare
```
Q: StandardScaler transformă datele la ce interval?
A: Nu are interval fix! Produce medie=0, std=1 (poate fi -3 la +3 sau orice)

Q: MinMaxScaler transformă datele la ce interval?
A: [0, 1]

Q: De ce scalăm ÎNAINTE de K-Means?
A: K-Means folosește distanța Euclidiană — fără scalare, variabilele cu valori
   mari domină calculul distanței

Q: scaler.fit_transform(X_test) — de ce e greșit?
A: Data leakage! fit() calculează parametrii din test, "contaminând" evaluarea
   Corect: fit pe train, transform pe test
```

### G38. Metrici clasificare
```
Q: Accuracy e metrică bună când datele sunt dezechilibrate?
A: NU! Ex: 95% clasa A, 5% clasa B → prezic mereu A → accuracy=95% dar e inutil

Q: Care metrică e mai bună pentru date dezechilibrate?
A: F1-Score (combină Precision și Recall)

Q: ROC-AUC = 0.5 înseamnă?
A: Clasificator aleatoriu (nu mai bun decât ghicitul)

Q: ROC-AUC = 1.0 înseamnă?
A: Clasificator perfect
```

---

## SECȚIUNEA 6: TEORIE SOFTWARE — GRILE TIPICE

### G39. Licențe software
```
Q: Ce tip de licență permite utilizatorului să modifice și redistribuie codul?
A: Free Software / Open Source

Q: Freeware înseamnă că software-ul are codul sursă disponibil?
A: Nu! Freeware = gratuit, codul poate fi proprietar (închis)

Q: Ce tip de software este distribuit gratuit cu scop comercial/de marketing?
A: Shareware

Q: Câte libertăți are Free Software (FSF)?
A: 4 libertăți (numerotate 0, 1, 2, 3)

Q: "Free" în Free Software înseamnă?
A: Libertate (freedom), NU gratuit (gratis/free of charge)
```

### G40. Cloud computing
```
Q: Care model cloud oferă aplicații complete accesate prin browser?
A: SaaS (Software as a Service) — Gmail, Docs, etc.

Q: Care model cloud oferă mașini virtuale și stocare?
A: IaaS (Infrastructure as a Service)

Q: Care model cloud este cel mai potrivit pentru developeri?
A: PaaS (Platform as a Service) — oferă platforma de deployment

Q: Cloud privat (private cloud) ce caracteristici are?
A: Infrastructură dedicată unei singure organizații, cel mai sigur, cel mai scump

Q: Care deployment model combină avantajele public + private?
A: Hybrid Cloud

Q: Mai multe spitale care împart o infrastructură cloud = ?
A: Community Cloud
```

### G41. Criterii de selecție
```
Q: Criteriile din "clasa funcțională" au răspuns de tip?
A: Da/Nu (binare) — software-ul fie are funcționalitatea, fie nu

Q: Criteriile din "clasa de utilizabilitate" au răspuns de tip?
A: Gradual/Scale — mai bun sau mai puțin bun, nu Da/Nu

Q: "Software-ul suportă import din Excel" este criteriu?
A: Funcțional

Q: "Interfața este intuitivă" este criteriu?
A: Utilizabilitate
```

---

## REZUMAT ULTRA-RAPID (Ultima oră înainte de test)

### SAS
- `;` = obligatoriu la orice instrucțiune
- WORK = temporar, LIBNAME = permanent
- FORMAT = afișare (NU schimbă valori)
- WHERE = PROCs + DATA step, IF = doar DATA step
- MERGE = full outer join implicit, necesită sortare BY
- PROC SORT + OUT= = nu suprascrie originalul
- PROC PRINT + NOOBS = elimină coloana Obs
- BY vs CLASS în PROC MEANS: BY necesită sortare, CLASS nu
- NEXTROBS = extreme observații, NEXTRVAL = extreme valori unice
- SAS EG = pointer (nu copie), output HTML implicit

### Python
- Tuple = imutabil, `del t[0]` → TypeError, `del t` → OK
- sort() returnează None, sorted() returnează lista nouă
- Dict keys = hashable (nu liste!)
- `10/2 = 5.0` (float!), `10//2 = 5` (int)
- List comprehension: `[expr for x in iter if cond]`

### Pandas
- loc = label, iloc = poziție
- loc[a:b] = INCLUSIV b, iloc[a:b] = EXCLUSIV b
- groupby().agg() = multiple statistici simultan
- merge how='inner/left/right/outer'
- fit_transform pe TRAIN, transform pe TEST

### ML
- K-Means = NESUPERVIZAT
- WCSS/inertia = mai mic = mai compact
- Silhouette: -1=greșit, 0=graniță, +1=perfect
- StandardScaler → medie=0, std=1 (nu e limitat)
- MinMaxScaler → [0,1]
- F1 = metric bun pentru date dezechilibrate
- ROC-AUC 0.5 = aleatoriu, 1.0 = perfect

### Teorie
- Freeware ≠ Free Software (freeware=gratuit, free software=libertăți)
- Shareware = proprietar + demo gratuit + limitat
- IaaS/PaaS/SaaS (infrastructură/platformă/software)
- Private/Public/Hybrid/Community (deployment models)
- Funcțional = Da/Nu, Utilizabilitate = gradual
