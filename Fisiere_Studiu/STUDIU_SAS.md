# FIȘIER DE STUDIU SAS — TEST GRILĂ
> Acoperă Seminarele SAS 1–4

---

## SEMINAR 1 — CITIREA DATELOR ȘI FORMATE

### Structura unui program SAS
```sas
DATA nume_set;
    INFILE 'cale/fisier.txt';
    INPUT variabile;
RUN;

PROC procedura DATA=nume_set;
    ...
RUN;
```

### Citirea fișierelor flat (text)

#### Delimitare prin SPAȚII (implicit)
```sas
data produse;
    infile '/home/user/produse.txt';
    input Nume $ Pret Categorie $;
run;
```
> `$` după un nume de variabilă = variabilă de tip **caracter**

#### Delimitare prin VIRGULĂ — opțiunea `dsd`
```sas
data produse;
    infile '/home/user/produse2.txt' dsd;
    input Nume $ Pret Categorie $;
run;
```
- `dsd` → delimitator = virgulă
- `dsd` tratează două virgule consecutive ca valoare lipsă
- `dsd` permite valori între ghilimele în fișierul sursă

#### Delimiter personalizat — `dlm=` sau `delimiter=`
```sas
infile '/home/user/produse3.txt' delimiter='/';
infile '/home/user/produse4.txt' dlm='/';
```

#### Date direct în program — `datalines`
```sas
data produse;
    input Nume $ Pret Categorie $;
datalines;
hartie 2 birotica
creione 10 birotica
apa 6 alimente
;
```

#### Date în coloane cu lățime fixă

**Metoda 1 — Column Input (poziție start-end)**
```sas
data produse;
    infile '/home/user/produse4.txt';
    input Nume $ 1-8 Pret 9-11 Categorie $ 12-19;
run;
```

**Metoda 2 — Formatted Input (@ + format)**
```sas
data produse;
    input @1 Nume $8. @9 Pret dollar4. @13 Categorie $8.;
    format Pret dollar6.0;
datalines;
hartie  $2 birotica
;
```

---

### Seturi de date permanente

#### Temporar (șters la închiderea sesiunii) — stocat în `Work`
```sas
data test;  /* → Work.test, șters la final de sesiune */
```

#### Permanent — cu `libname`
```sas
libname produse '/home/user';
data produse.date_test;
    input Nume $ 1-8 Pret 9-11;
    datalines;
    ...
run;
/* → creează fișierul date_test.sas7bdat pe disk */
```

---

### Proceduri de bază

#### PROC CONTENTS — descriere set de date
```sas
title "Descrierea datelor";
proc contents data=produse.date_test;
run;
```
Afișează: număr variabile, număr observații, nume/tip/dimensiuni variabile.

#### PROC PRINT — afișare date
```sas
title "Datele din fisier";
proc print data=produse.date_test;
run;
```

---

### Formate și Etichete

#### Etichete (LABEL)
```sas
DATA note;
    input cod $ Nota1-Nota3;
    label cod    = 'Cod Student'
          Nota1  = 'Nota PSW'
          Nota2  = 'Nota SGBD';
datalines;
1 10 10 8
;
```
- Etichete în secțiunea `DATA` → rămân asociate permanent
- Etichete în `PROC` → valabile **doar** în acea procedură

#### Formate definite de utilizator (PROC FORMAT)
```sas
proc format;
    value $gen
        'M' = 'Masculin'
        'F' = 'Feminin'
        other = 'necunoscut';
    value nota
        low-4.4 = 'Examen Picat'
        4.5-high = 'Promovat';
run;
```
> Formatele pentru variabile **caracter** → prefixate cu `$` (ex: `$gen`)
> Formatele pentru variabile **numerice** → fără `$` (ex: `nota`)

---

## SEMINAR 2 — OPERATORI, IF/WHERE, FUNCȚII

### Operatori de comparație SAS

| Operator | Simbol | Mnemonică SAS |
|---|---|---|
| Egal | `=` | `EQ` |
| Diferit | `^=` sau `~=` | `NE` |
| Mai mic | `<` | `LT` |
| Mai mic sau egal | `<=` | `LE` |
| Mai mare | `>` | `GT` |
| Mai mare sau egal | `>=` | `GE` |
| Într-o listă | — | `IN` |

#### Operatorul IN
```sas
Nota IN ('A' 'B-' 'B+')         /* caracter */
Nota IN (10 9 8 7)              /* numeric */
Valoare IN (10,15,20:30)        /* 20 până la 30 */
```

### Operatori logici — Precedența
`NOT` > `AND` > `OR`

```sas
if X and Y or Z;         /* ≡  if (X and Y) or Z; */
if X and (Y or Z);       /* forțăm OR să aibă prioritate */
if X and not y or z;     /* ≡  if (X and (not y)) or z; */
```

---

### Instrucțiunea WHERE

Folosită pentru **subseturi** în proceduri SAS (IF nu funcționează în PROC!).

```sas
proc print data=studenti;
    where Sex eq 'F' and (Proiect in (9 10) or Examen eq 10);
    var Sex Activitate Proiect Examen;
run;
```

#### Operatori speciali WHERE

| Operator | Descriere | Exemplu |
|---|---|---|
| `IS MISSING` | valoare lipsă | `where varsta is missing` |
| `IS NULL` | echivalent IS MISSING | `where varsta is null` |
| `BETWEEN AND` | interval închis | `where varsta between 20 and 40` |
| `CONTAINS` | conține un subșir | `where nume contains 'lex'` |
| `LIKE` | șablon: `_` = 1 car., `%` = orice | `where nume like 'A%'` |

---

### Instrucțiunea IF

```sas
IF conditie THEN actiune;
IF conditie THEN actiune1 ELSE actiune2;
```

**Selecție observații (IF fără THEN):**
```sas
data Femei;
    input Varsta Sex $ Nota;
    if Sex eq 'F';      /* păstrează DOAR femeile */
datalines;
...
;
```

**IF...ELSE...IF (recomandat față de IF multiple):**
```sas
data studenti;
    input Varsta Sex $ Nota;
    if Varsta lt 20 and not missing(Varsta) then GrupVarsta = 1;
    else if Varsta ge 20 and Varsta lt 40   then GrupVarsta = 2;
    else if Varsta ge 40 and Varsta lt 60   then GrupVarsta = 3;
    else if Varsta ge 60                    then GrupVarsta = 4;
datalines;
...
;
```

> **Atenție!** Valorile numerice lipsă (`.`) sunt tratate ca cel mai **negativ** număr posibil → un `IF Varsta < 20` va fi TRUE pentru missing! Folosiți `not missing(Varsta)`.

### Evitarea trunchierilor la variabile noi
SAS setează lățimea variabilei noi în funcție de **prima** valoare. Dacă valorile ulterioare sunt mai lungi → trunchiere!

```sas
data proiecte;
    set proiecte_in;
    length Raportare $8;   /* impunem lățimea dinainte */
    if Valoare le 10000 then Raportare = "Lunara";
    else                       Raportare = "Bilunara";
run;
```

### WHERE vs IF — Diferențe cheie

| Caracteristică | WHERE | IF |
|---|---|---|
| Funcționează în PROC | **DA** | NU |
| Poate folosi variabile create în DATA | NU | **DA** |
| Eficiență pe seturi indexate | Mai bun | Normal |
| Operatori speciali (BETWEEN, LIKE...) | **DA** | NU |

---

### Procesare iterativă — DO loops

```sas
/* DO simplu */
do i = 1 to 10;
    ...
end;

/* DO WHILE */
do while (conditie);
    ...
end;

/* DO cu bloc (pentru IF-THEN-DO) */
if Valoare le 10000 then do;
    Raportare = "Lunara";
    Prezentare = '17dec2018'd;   /* constantă dată SAS */
end;
else do;
    Raportare = "Bilunara";
    Prezentare = '20dec2018'd;
end;
```

---

## SEMINAR 3 — COMBINAREA SETURILOR DE DATE

### A. Concatenarea cu SET

Lipește observațiile unuia după celălalt (Union). Nr. obs. final = suma nr. obs. din input.

```sas
DATA concatenat;
    SET set1 set2;  /* ordinea contează! */
RUN;
```

**Dacă variabilele au nume diferite → RENAME:**
```sas
data angajati;
    set angajatiBV angajatiCJ (RENAME=(Zona=Judet));
run;

/* Mai multe redenumiri */
data angajati;
    set angajatiBV (RENAME=(Angajat=Nume Gen=Sex))
        angajatiCJ (RENAME=(Angajat=Nume Gen=Sex Zona=Judet));
run;
```

### B. Interclasarea (Merging sortat) cu SET + BY

Ca și concatenarea, DAR menține ordinea după variabila din BY. Datele trebuie **sortate în prealabil**!

```sas
PROC SORT DATA=set1; BY NrTichet; RUN;
PROC SORT DATA=set2; BY NrTichet; RUN;

DATA interclasare;
    SET set1 set2;
    BY NrTichet;
RUN;
```

### C. Fuziunea cu MERGE (JOIN-uri SAS)

#### Fuziune unu-la-unu
```sas
/* Datele TREBUIE sortate după variabila BY */
PROC SORT DATA=set1; BY Cod; RUN;
PROC SORT DATA=set2; BY Cod; RUN;

DATA rezultat;
    MERGE set1 set2;
    BY Cod;
RUN;
```
> **Atenție!** Dacă ambele seturi au variabile cu același nume (altele decât BY), valorile din **al doilea** set le suprascriu pe cele din primul!

#### Fuziune unu-la-mulți (same syntax!)
```sas
PROC SORT DATA=set1; BY Sport; RUN;
PROC SORT DATA=set2; BY Sport; RUN;

DATA rezultat;
    MERGE set1 set2;
    BY Sport;
    Pret_Nou = ROUND(Pret - (Pret * Reducere), .01);
RUN;
```

---

## SEMINAR 4 — PROCEDURI STATISTICE ȘI RAPOARTE

### PROC PRINT — Rapoarte detaliate

```sas
PROC PRINT DATA=set_date NOOBS LABEL;
    BY lista_variabile;    /* grupare (necesită sortare prealabilă!) */
    ID variabila;          /* înlocuiește nr. obs. cu o variabilă */
    SUM lista_variabile;   /* afișează sume */
    VAR lista_variabile;   /* coloanele afișate și ordinea */
    TITLE 'Titlu raport';
RUN;
```

**Opțiuni PROC PRINT:**
- `NOOBS` → suprimă afișarea numărului observației
- `LABEL` → afișează etichetele în loc de numele variabilelor

**Opțiuni pentru sumlabel (etichete subtotaluri):**
```sas
proc print data=cititori sumlabel='Total #byval(Clasa)' grandtotal_label='Total';
    by Clasa;
    sum Castig;
run;
```

---

### PROC UNIVARIATE — Statistici descriptive + distribuție

```sas
PROC UNIVARIATE DATA=note NORMAL FREQ PLOT;
    VAR Punctaj;
    BY Grupa;           /* analize separate pe grupe */
    ID NumeStudent;     /* identificator în loc de nr. obs. */
    HISTOGRAM Punctaj;
    TITLE "Statistici";
RUN;
```

**Opțiuni cheie:**
| Opțiune | Efect |
|---|---|
| `NORMAL` | Teste de normalitate |
| `FREQ` | Tabele de frecvență |
| `PLOT` | Grafice: stem-leaf, boxplot, distribuție normală |
| `NOPRINT` | Nu afișează tabelele, trimite la OUTPUT |
| `NEXTROBS=5` | Afișează 5 obs. extreme (cu numărul lor) |
| `NEXTRVAL=5` | Afișează 5 valori extreme distincte |
| `NEXTROBS=0` | Suprimă tabelul cu observații extreme |

```sas
/* Histogramă fără tabele */
PROC UNIVARIATE DATA=set noprint;
    VAR Amenzi;
    HISTOGRAM Amenzi;
RUN;

/* Valori extreme distincte */
PROC UNIVARIATE DATA=set NEXTRVAL=5 NEXTROBS=0;
    VAR Amenzi;
    ID Stat;
RUN;
```

---

### PROC MEANS — Rapoarte agregate

```sas
PROC MEANS DATA=set MAX MIN MEAN N NMISS SUM;
    BY lista_variabile;    /* analize separate (necesită sortare!) */
    CLASS lista_variabile; /* analize separate (NU necesită sortare) */
    VAR lista_variabile;   /* variabilele analizate */
    OUTPUT OUT=set_iesire
        MEAN(Lalele Gladiole) = MedieLalele MedieGladiole
        SUM(Lalele Gladiole)  = Lalele Gladiole;
RUN;
```

**Indicatori disponibili:**
| Indicator | Semnificație |
|---|---|
| `MAX` | Valoarea maximă |
| `MIN` | Valoarea minimă |
| `MEAN` | Media |
| `N` | Numărul valorilor nenule |
| `NMISS` | Numărul valorilor lipsă |
| `SUM` | Suma |
| `STD` | Abaterea standard |
| `CLM` | Limitele intervalului de încredere |

**BY vs CLASS:**
- `BY` → necesită sortare prealabilă `PROC SORT`
- `CLASS` → **NU** necesită sortare, rezultate prezentate mai compact

**Salvare statistici într-un set de date:**
```sas
PROC MEANS NOPRINT DATA=vanzari;
    BY IDClient;
    VAR Lalele Gladiole Zambile;
    OUTPUT OUT=totaluri
        MEAN(Lalele Gladiole Zambile) = MedieLalele MedieGladiole MedieZambile
        SUM(Lalele Gladiole Zambile)  = Lalele Gladiole Zambile;
RUN;
```
> `NOPRINT` → nu afișează pe ecran, doar salvează în `OUT=`

**Interval de încredere:**
```sas
PROC MEANS DATA=set ALPHA=0.01 CLM;   /* interval 99% */
    VAR variabila;
RUN;
/* implicit → ALPHA=0.05 (interval 95%) */
```

---

### Funcții SAS utile

```sas
/* Matematice */
ROUND(valoare, .01)     /* rotunjire la 2 zecimale */
ABS(x)                  /* valoare absolută */
SQRT(x)                 /* radical */

/* Date calendaristice */
MONTH(data)             /* luna (1-12) */
YEAR(data)              /* anul */
DAY(data)               /* ziua */
'17dec2018'd            /* constantă dată SAS */

/* Caractere */
UPCASE(sir)             /* majuscule */
LOWCASE(sir)            /* minuscule */
LENGTH(sir)             /* lungimea șirului */
SUBSTR(sir, start, len) /* subșir */

/* Verificare */
MISSING(var)            /* TRUE dacă valoarea lipsă */
```

### Formate de dată SAS

```sas
format DataVar DDMMYY10.;    /* 17/12/2018 */
format DataVar DATE9.;       /* 17DEC2018 */
format DataVar MMDDYY10.;    /* 12/17/2018 */
format Valoare COMMA8.;      /* 1,234,567 */
format Pret DOLLAR6.0;       /* $1,235 */
```

---

## REZUMAT RAPID — SAS CHEATSHEET

```sas
/* Structură program */
DATA set;
    INFILE 'fisier' <optiuni>;
    INPUT var1 $ var2 var3;
    /* declarații de calcul */
RUN;

PROC procedura DATA=set <optiuni>;
    BY var;   /* necesită PROC SORT DATA=set; BY var; RUN; */
    VAR var;
RUN;

/* Bibliotecă permanentă */
LIBNAME alias 'cale';
DATA alias.set;  ...

/* Concatenare */
DATA nou; SET set1 set2; RUN;

/* Interclasare */
DATA nou; SET set1 set2; BY var; RUN;  /* cu sortare prealabilă */

/* Fuziune */
DATA nou; MERGE set1 set2; BY var; RUN;  /* cu sortare prealabilă */

/* Rename în SET/MERGE */
SET set (RENAME=(vechi=nou))

/* Subseturi */
IF conditie;              /* în DATA */
WHERE conditie;           /* în DATA sau PROC */

/* DO bloc */
if cond then do; ...; end;
else do; ...; end;

/* length pentru variabile caracter */
length Var $8;
```

---

## ÎNTREBĂRI FRECVENTE GRILĂ — SAS

**Q: Care este diferența dintre `WHERE` și `IF`?**
A: WHERE funcționează și în **PROC** (IF nu), are operatori speciali (BETWEEN, LIKE, CONTAINS), dar nu poate folosi variabile create în secțiunea DATA. IF poate folosi variabile noi create în DATA.

**Q: Ce face opțiunea `dsd` la `INFILE`?**
A: Schimbă delimitatorul din spațiu în **virgulă**, tratează două virgule consecutive ca valoare lipsă, permite valori între ghilimele.

**Q: Ce se întâmplă cu o variabilă lipsă (`.`) într-un `IF Varsta < 20`?**
A: **Condiția este TRUE!** Valorile numerice lipsă sunt tratate ca cel mai negativ număr. Soluție: `if Varsta lt 20 and not missing(Varsta)`.

**Q: Ce diferență este între `BY` și `CLASS` în PROC MEANS?**
A: `BY` → necesită sortare prealabilă; `CLASS` → NU necesită sortare.

**Q: Concatenare vs Fuziune (MERGE)?**
A: SET (concatenare) → lipește rândurile unuia după altul; MERGE → combină pe coloane, rând cu rând, pe baza unei variabile comune (BY).

**Q: Ce face `NOOBS` în PROC PRINT?**
A: Suprimă afișarea numărului de ordine al observației.

**Q: Ce face `NOPRINT` în PROC MEANS?**
A: Nu afișează rezultatele pe ecran — le trimite doar în setul de date specificat la `OUTPUT OUT=`.

**Q: Formate permanente vs temporare în PROC?**
A: Etichete/formate în `DATA` → rămân asociate permanent. În `PROC` → valabile **doar** în acea procedură.

**Q: Ce extensie au fișierele SAS permanente?**
A: `.sas7bdat`

**Q: Ce face `PROC SORT DATA=set; BY var; RUN;` înainte de MERGE?**
A: Sortează setul de date după variabila din BY — **obligatoriu** înainte de MERGE și interclasare!

**Q: Dacă în MERGE două seturi au o variabilă cu același nume (alta decât BY), care valoare câștigă?**
A: Valorile din **al doilea** set de date le suprascriu pe cele din primul.

**Q: Ce sunt WCSS și Silhouette Score?**
A: WCSS = suma pătratelor distanțelor față de centroid (mai mic = mai bun). Silhouette: +1 = bine încadrat, 0 = la granița, <0 = greșit atribuit.
