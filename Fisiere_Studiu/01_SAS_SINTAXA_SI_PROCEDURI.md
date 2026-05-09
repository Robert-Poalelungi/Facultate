# SAS — SINTAXĂ, PROCEDURI, ENTERPRISE GUIDE
> Bazat pe toate grilele văzute. Cel mai testat capitol.

---

## 1. SINTAXA SAS — REGULI DE BAZĂ

### Singura cerință OBLIGATORIE de sintaxă:
> **Fiecare declarație se termină cu `;` (punct și virgulă)**

**Restul sunt opționale / false:**
- NU trebuie să începi în coloana 1
- NU trebuie o declarație pe fiecare rând
- NU trebuie linii libere între pași
- RUN nu este obligatoriu (dar e recomandat)

### Comentarii SAS
```sas
/* Acesta este un comentariu corect
   pe mai multe linii
   poate conține ; fără probleme */
proc print data=test; run;
```
> Comentariile `/* */` pot conține `;` fără eroare! ← întrebare grilă frecventă

### Structura unui program SAS
Un program SAS are 2 tipuri de pași:
- **Pasul DATA** → creează/modifică seturi de date
- **Pasul PROC** → generează rapoarte și analize

```sas
/* Pasul DATA */
data work.test;
    set biblioteca.sursa;
    variabila_noua = calcul;
run;

/* Pasul PROC */
proc print data=work.test;
run;
```

---

## 2. SETURI DE DATE SAS — STRUCTURĂ

### Cele două zone ale unui set de date SAS:
| Zonă | Conținut |
|---|---|
| **Zona descriptivă** | Numele setului, tipul variabilelor, data creării, lungimi |
| **Zona de date** | Valorile efective (observațiile) |

> **Grilă tipică:** "Unde se găsește tipul variabilei Salariu?" → **Zona descriptivă**

### Cele două tipuri de coloane (variabile) dintr-un set SAS:
> **Numeric** și **Caracter** ← răspuns corect la grilă
(Nu: integer/alfanumeric, data/bani, etc.)

### Lungimi implicite:
- **Variabile numerice** → **8 bytes** (implicit) ← grilă frecventă!
- **Variabile caracter** → definit de utilizator cu `LENGTH` sau prima valoare

---

## 3. BIBLIOTECI (LIBNAME) — TEMPORAR vs PERMANENT

```sas
/* Set de date TEMPORAR — șters la închiderea sesiunii */
data test;           /* stocat în biblioteca WORK */
data work.test;      /* echivalent */

/* Set de date PERMANENT — rămâne pe disc */
libname mylib '/home/user/';
data mylib.test;     /* stocat permanent ca mylib/test.sas7bdat */
```

> **Grilă:** "Ce se întâmplă cu un set creat cu 'data' fără bibliotecă?" → **Salvat automat în WORK (temporar)**

> **Grilă:** "Ce tip de set de date este `proc print data=order_fact`?" → **Temporar** (fără prefix de bibliotecă = WORK)

> **Grilă:** "Fisierele temporare SAS se salvează automat în libraria..." → **WORK**

---

## 4. CITIREA DATELOR — DATA STEP

### INPUT și tipuri de variabile
```sas
data clienti;
    infile '/path/fisier.txt';
    input Nume $ Pret Categorie $;
    /*    ^ caracter  ^ caracter */
    /*         ^ numeric (fără $) */
run;
```
> **Declarația INPUT** → **definește variabilele** (nu citește fișierul, nu asociază date) ← grilă!
> **Semnul `$`** → variabilă de tip **caracter** ← grilă frecventă!

### Citire cu delimitatori
```sas
/* Delimitator spațiu (implicit) */
infile 'fisier.txt';

/* Delimitator virgulă */
infile 'fisier.txt' dsd;          /* sau dlm=',' */

/* Delimitator personalizat */
infile 'fisier.txt' dlm='*';      /* sau delimiter='*' */
infile 'fisier.txt' dlm='/';
```

> **Grilă:** date separate prin `*` → `dlm='*'` ← nu `dlm*` și nu `dsd dlm='*'` (dsd e pentru virgulă!)

> **Grilă:** `infile 'sales.dat' dsd dlm='*'` → **CORECT** pentru fisier cu `*` dacă vrei și tratare ghilimele

### DATALINES — date direct în program
```sas
data produse;
    input Nume $ Pret Categorie $;
datalines;
hartie 2 birotica
apa 6 alimente
;
```
> **Grilă:** "Ce instrucțiune specifică liniile de date introduse direct?" → **DATALINES** (nu INFILE, nu INPUT)

### Citire coloane fixe
```sas
/* Column input */
input Nume $ 1-8 Pret 9-11 Categorie $ 12-19;

/* Formatted input */
input @1 Nume $8. @9 Pret dollar4. @13 Categorie $8.;
```

---

## 5. INSTRUCȚIUNILE DROP și KEEP

```sas
data work.subset;
    set orion.sales;
    drop Salary;              /* elimină Salary din OUTPUT */
    Compensation = Salary * 2; /* dar Salary e DISPONIBIL în calcule! */
run;
```

> **Regulă critică:** `DROP` și `KEEP` elimină/păstrează variabilele **la OUTPUT**, nu pe parcursul execuției DATA step. Deci poți folosi o variabilă `drop`-ată în calcule!

> **Grilă:** Cei doi pași DATA cu DROP la început vs DROP la sfârșit → **produc ACELAȘI set** (răspuns: DA)

**Calcul număr variabile:**
```
data work.comp;
set orion.sales;         /* 9 variabile */
drop Gender Salary Birth_Date;  /* scade 3 */
run;
/* Rezultat: 9 - 3 = 6 variabile */
```
```
data work.comp;
set orion.sales;         /* 9 variabile */
drop Gender Salary Country;    /* scade 3 */
Compensation = sum(Salary, Bonus); /* ADAUGĂ 1 variabilă nouă */
run;
/* Rezultat: 9 - 3 + 1 = 7 variabile */
```

---

## 6. DO LOOPS și ARRAY
*(din `SAS/02_SAS_Seminar_2/` și `SAS/03_SAS_Seminar_3/`)*

### Grup DO (bloc condiționat)
```sas
/* Grup DO — execută mai multe instrucțiuni pe o ramură IF */
if Varsta le 39 then do;
    GrupVarsta = 'Grup1';
    Medie = 0.4*Proiect + 0.6*Examen;
end;
else if Varsta gt 39 then do;
    GrupVarsta = 'Grup2';
    Medie = (Proiect + Examen) / 2;
end;
```

### Bucla DO (număr cunoscut de iterații)
```sas
/* DO contor = start TO stop [BY increment]; */
data Dobanda;
    Dobanda = 0.0375;
    Total = 100;
    do An = 1 to 3;
        Total + Dobanda * Total;   /* Total + increment → reține + ignoră NULL */
        output;                    /* scrie o observație la fiecare iterație */
    end;
run;

/* BY negativ → iterare descrescătoare */
do i = 10 to 1 by -1;
    ...
end;
```

> **OUTPUT în DO loop:** când `output;` apare în DATA step, SAS NU mai face output automat la final — output are loc DOAR unde e specificat explicit.

### DO WHILE / DO UNTIL
```sas
/* DO WHILE — verificare ANTERIOARĂ (poate nu se executa deloc) */
do while (Total le 200);
    An + 1;
    Total = Total + Dobanda * Total;
    output;
end;

/* DO UNTIL — verificare POSTERIOARĂ (se execută cel puțin o dată) */
do until (Total ge 200);
    An + 1;
    Total = Total + Dobanda * Total;
    output;
end;
```

> **Diferența cheie:** WHILE verifică la ÎNCEPUT (poate să nu execute niciodată blocul), UNTIL verifică la SFÂRȘIT (execută cel puțin o dată).

### Operatorul SUM (acumulare)
```sas
/* Variabila + increment; — fără semnul = */
/* Reține valoarea între observații, ignoră NULL, inițializat cu 0 */
Total + Venit;   /* Total = Total + Venit, ignoră Venit=. */
```

### ARRAY (masiv de variabile)
```sas
/* Sintaxa */
ARRAY nume(n) lista_variabile;    /* numeric */
ARRAY nume(n) $ lista_variabile;  /* caracter — $ necesar dacă nu definite anterior */

/* Exemplu: înlocuiește 0 cu lipsă pentru 7 variabile */
DATA cursuri;
    INFILE '/home/.../cursuri.txt';
    INPUT Oras $ Varsta ECON MRKT FINA CONT STAT MATE INFO;
    ARRAY curs(7) ECON MRKT FINA CONT STAT MATE INFO;
    DO i = 1 TO 7;
        IF curs(i) = 0 THEN curs(i) = .;
    END;
RUN;
/* ATENȚIE: variabila contor 'i' este inclusă în setul de date — adaugă DROP=i dacă nu e necesară */

/* Două masive simultan */
ARRAY nou(7) Curs1-Curs7;
ARRAY vechi(7) ECON--INFO;    /* ECON--INFO = de la ECON la INFO în ordinea din INPUT */
DO i = 1 TO 7;
    IF vechi(i) = 0 THEN nou(i) = .;
    ELSE nou(i) = vechi(i);
END;
MedieCalif = MEAN(OF Curs1-Curs7);
```

### Liste abreviate SAS
| Sintaxă | Semnificație |
|---|---|
| `Var1-Var8` | variabile cu același prefix + numere consecutive |
| `s--p` | toate variabilele de la s la p (în ordinea din INPUT) |
| `_ALL_` | toate variabilele din setul de date |
| `_NUMERIC_` | toate variabilele numerice |
| `_CHARACTER_` | toate variabilele caracter |
| `SUM(OF Curs1-Curs7)` | suma variabilelor Curs1 până la Curs7 |

---

## 7. WHERE vs IF — DIFERENȚE CRITICE

| | WHERE | IF |
|---|---|---|
| **Funcționează în PROC** | **DA** | NU |
| **Poate folosi variabile create în DATA** | NU | **DA** |
| **Operatori speciali** | BETWEEN, LIKE, CONTAINS, IS MISSING | nu |
| **Eficiență pe seturi indexate** | mai bună | normală |

```sas
/* WHERE în PROC — CORECT */
proc print data=orion.sales;
    where Country = 'AU';
run;

/* WHERE cu operatori speciali */
where Job_Title contains 'I';    /* caută subșirul 'I' în Job_Title */
where varsta between 20 and 40;
where nume like 'A%';            /* % = orice caractere */
where varsta is missing;
```

> **Grilă:** `where Job_Title contains 'I'` pe valorile "Sales Rep I", "Sales Manager", "Insurance Sales" → **observațiile 1 și 3** (Sales Rep **I** și **I**nsurance Sales)

> **Grilă:** `proc print data=orion.sales; where Country='AU'; by Gender;` → afișează **NUMAI observațiile cu Country = 'AU'** (nu necesită sortare după Country pentru WHERE, dar BY necesită sortare!)

---

## 8. PROC SORT

```sas
proc sort data=orion.staff out=work.staffsort;
    by Gender Start_Date;   /* crescător implicit */
run;

/* Descrescător */
proc sort data=orion.staff out=work.staffsort;
    by descending Salary Manager_ID;
    /* Salary desc, Manager_ID CRESCĂTOR (fără descending înainte) */
run;

/* Ambele descrescător */
proc sort data=orion.staff out=work.staffsort;
    by descending Postal_Code descending Employee_ID;
run;
```

> **Grilă (sortare):** Postal_Code descrescător, Employee_ID descrescător → `by descending Postal_Code descending Employee_ID`

> **Grilă:** `out=work.staff` → setul sortat NU suprascrie intrarea; se salvează separat în `work.staff`

> **Grilă:** setul sortat conține **TOATE variabilele** (nu doar cele din BY)

### BY în PROC PRINT — condiție de sortare
```sas
/* Dacă PROC SORT sortează după Gender Start_Date: */
proc print data=work.staffsort;
    by Gender;           /* VALID — Gender e primul în sort */
    by Gender Start_Date; /* VALID — același ordin */
    by Start_Date Gender; /* INVALID — ordinea diferă */
    by descending Gender; /* INVALID — sort-ul nu e descrescător */
    by Start;            /* INVALID — NU se folosesc etichete, ci nume variabile */
run;
```

---

## 9. FORMAT

```sas
/* Formate SAS predefinite */
format Salary dollar12.2;    /* $108,255.00 — 12 caractere total, 2 zecimale */
format Salary dollar10.2;    /* $26,600.00 — 10 caractere total */
format DataVar date9.;       /* 17DEC2018 */
format DataVar ddmmyy10.;    /* 17/12/2018 */
format DataVar mmddyy8.;     /* 12/17/18 */
format DataVar monyy7.;      /* DEC2018 */
format Valoare comma8.;      /* 1,234,567 */
```

> **Regulă cheie:** Un format modifică **DOAR valoarea afișată**, NU valoarea stocată! ← grilă `False` la "format modifică atât valoarea stocată cât și afișată"

**Cum citești `dollar12.2`:** lățime totală = 12, zecimale = 2
- `$108,255.00` = 10 caractere → se potrivește în 10 sau mai mult

> **Grilă date:** `11JAN07`, `15JAN07`, `20JAN07` → format **`date7.`** (zi+lună3+an2 = 7 chars)

### PROC FORMAT — formate definite de utilizator
```sas
proc format;
    value $title                    /* $ = pentru variabile caracter */
        'Sales Manager',
        'Senior Sales Mrg' = 'Manager'
        'Sales Rep. I',
        'Sales Rep. II' = 'Rep';   /* 'Sales Rep II' (fără punct) NU va fi găsit! */
    
    value nota
        low-4.4 = 'Picat'
        4.5-high = 'Promovat';
    
    value $gen
        'M' = 'Masculin'
        'F' = 'Feminin'
        other = 'Necunoscut';     /* other = pentru valorile nedefinite */
run;
```

> **Grilă:** "Care NU este un format valid definit de utilizator?" → **`comma`** (este deja format de sistem!)

> **Grilă:** "Scopul clasei `other`" → **asigură tratarea valorilor nedefinite**

> **Grilă:** "Ce afișează `$TITLE` pentru 'Sales Rep II'?" → **'Sales R'** (trunchiere! SAS trunchiază la lungimea primei valori 'Rep', dar de fapt 'Sales Rep. II' ≠ 'Sales Rep II' deci afișează valoarea originală trunchiată la lățimea formatului → depinde de lățime)

> **Grilă:** Formate caracter → prefix `$`; Formate numerice → fără `$`

### LENGTH pentru variabile caracter
```sas
data proiecte;
    set proiecte_in;
    length Raportare $8;   /* OBLIGATORIU dacă valorile au lungimi diferite */
    if Valoare le 10000 then Raportare = "Lunara";
    else Raportare = "Bilunara";
run;
```
> Fără `length`, SAS setează lățimea după PRIMA valoare → trunchiere pentru valori mai lungi!

---

## 10. PROC PRINT

```sas
proc print data=set NOOBS LABEL;
    by lista_var;       /* grupare — necesită sortare prealabilă */
    id var;             /* înlocuiește numărul obs cu o variabilă */
    sum lista_var;      /* afișează sume */
    var lista_var;      /* coloanele de afișat */
    where conditie;
    label Salary = 'Annual Salary';
    title 'Titlu raport';
run;
```

**Opțiuni cheie:**
- `NOOBS` → suprimă nr. observației ← grilă
- `LABEL` → afișează etichete în loc de nume variabile

> **Grilă:** dacă `proc print data=work.newsalesemps` și setul NU există → **mesaj de eroare în log**

> **Grilă:** `label Salary='Annual Salary'` → eticheta apare **în header-ul coloanei**, NU în "partea de sus"

---

## 11. PROC MEANS

```sas
proc means data=set MAX MIN MEAN N NMISS SUM RANGE;
    by lista_var;       /* necesită sortare! */
    class lista_var;    /* NU necesită sortare! */
    var lista_var;
    output out=set_iesire
        MEAN(col1 col2) = MedieCol1 MedieCol2
        SUM(col1) = SumaCol1;
run;
```

**Indicatori:**
| Indicator | Semnificație |
|---|---|
| MAX | Valoarea maximă |
| MIN | Valoarea minimă |
| MEAN | Media |
| N | Nr. valori nenule |
| NMISS | Nr. valori lipsă |
| SUM | Suma |
| RANGE | Max - Min |
| CLM | Limite interval de încredere |

> **Grilă:** `range mean nonobs maxdec=1` → afișează Range, Mean, fără coloana N, cu 1 zecimală

> **Grilă:** BY vs CLASS → BY necesită sortare, CLASS nu

**NOPRINT + OUTPUT:**
```sas
proc means NOPRINT data=set;
    by IDClient;
    var col1 col2;
    output out=totaluri MEAN(col1) = MedieCol1 SUM(col1) = SumaCol1;
run;
/* NOPRINT → nu afișează pe ecran, salvează în 'totaluri' */
```

---

## 12. PROC UNIVARIATE

```sas
proc univariate data=note NORMAL FREQ PLOT;
    var Punctaj;
    id NumeStudent;      /* identificator în loc de nr. obs */
    by Grupa;
    histogram Punctaj;
run;
```

| Opțiune | Efect |
|---|---|
| NORMAL | Teste normalitate |
| FREQ | Tabele de frecvență |
| PLOT | stem-leaf, boxplot, distribuție normală |
| NOPRINT | Fără output pe ecran |
| NEXTROBS=5 | 5 obs. extreme (cu număr) |
| NEXTRVAL=5 | 5 valori extreme distincte |
| NEXTROBS=0 | Suprimă tabelul cu obs. extreme |

---

## 13. PROC CONTENTS

```sas
proc contents data=mylib._all_ nods;   /* toate seturile din bibliotecă, fără descriere individuală */
run;

proc contents data=mylib.test;          /* un singur set */
run;
```

> **Grilă:** "Ce pas PROC listează TOATE seturile din biblioteca `orion` fără zone descriptor individuale?" → `proc contents data=orion._all_ nods;`

> **Lungime implicită variabilă numerică** → **8 bytes** ← grilă frecventă

---

## 14. COMBINAREA SETURILOR DE DATE

### A) Concatenare (SET cu 2+ seturi)
```sas
/* vanzari urmat de produse (ordinea contează!) */
data newsales;
    set sales products;   /* sales PRIMUL, products AL DOILEA */
run;
```
> Nr. obs. final = sum(obs. din fiecare set)

> **Grilă:** "Care program concatenează vânzările și produsele în acea ordine?" → `set sales products` (sales primul!)

### B) Interclasare (SET + BY)
```sas
/* Sortare obligatorie înainte */
proc sort data=set1; by NrTichet; run;
proc sort data=set2; by NrTichet; run;

data interclasare;
    set set1 set2;
    by NrTichet;
run;
```

### C) Fuziune (MERGE)
```sas
/* Sortare OBLIGATORIE după variabila BY */
proc sort data=set1; by ID; run;
proc sort data=set2; by ID; run;

data rezultat;
    merge set1 set2;
    by ID;
run;
```

> **Comportament MERGE (implicit):** include **TOATE observațiile din AMBELE seturi** (echivalent full outer join) ← grilă frecventă!

> **Grilă:** `merge managers staff; by EmplID;` → **toate obs. din staff și managers**, indiferent de corespondență

> **RENAME în MERGE:**
```sas
data angajati;
    set bv cj(RENAME=(Zona=Judet));
run;
```

> **Eroare la MERGE:** dacă seturile NU sunt sortate după BY → eroare (PROC SORT lipsă)

> **Grilă:** donors1 și donors2 nu sunt sortate → **pasul DATA produce erori**

---

## 15. FUNCTII SAS DATE

```sas
MONTH(data)    /* returnează 1-12 */  ← grilă: "returnează număr de la 1 la 12"
YEAR(data)     /* returnează anul */
DAY(data)      /* returnează ziua */
WEEKDAY(data)  /* returnează 1(duminică)-7(sâmbătă) */
TODAY()        /* data de azi (număr SAS) */
```

**Conversii:**
```sas
/* Caracter → Numeric */
numar = input(var_char, 8.);    /* funcția INPUT() */ ← grilă
var_char = put(numar, 8.);      /* Numeric → Caracter — funcția PUT() */
```

> **Grilă:** "Cum convertești caracter în numeric în SAS?" → **funcția INPUT()**

---

## 16. TITLURI ÎN SAS — COMPORTAMENT

```sas
title1 'RADIX Company';
title3 'DVD Sales';
proc print ...; run;

title2 'Best Sales';
title;           /* ȘTERGE TOATE titlurile de la nivelul curent în sus */
proc print ...; run;
/* Al doilea raport → NO titles */
```

> **Regulă:** `title;` (fără argument) → **șterge TOATE titlurile**
> Titlurile rămân active până sunt redefinite sau șterse

> **Grilă:** după `title;` al doilea raport are → **No titles**

---

## 17. DECLARAȚIA SET vs SETUL DE DATE DE INTRARE/IEȘIRE

```sas
data work.us;        /* set de date de IEȘIRE = work.us */
    set orion.sales; /* set de date de INTRARE = orion.sales */
    where Country = 'US';
run;
```

> **Grilă:** "Setul de date de intrare" → **orion.sales**
> **Grilă:** "Setul de date de ieșire" → **work.us**
> **Grilă:** "Ce declarație citește un set de date SAS într-un pas DATA?" → **SET statement**

---

## 18. SAS ENTERPRISE GUIDE (SAS EG) — CARACTERISTICI

### Deschiderea unui set de date SAS în SAS EG
> Un **pointer** (legătură) al setului de date este adăugat la proiect ← grilă
> NU se copiază, NU se incorporează, NU se deschide Import Wizard

### Formate de output SAS EG
- **Format implicit:** **HTML** ← grilă
- Stiluri personalizate se pot aplica: **HTML** ← grilă (nu PDF, nu Text în general)
- Un raport SAS poate fi exportat în: **SAS, HTML, XML, PDF** ← grilă

### Task-uri SAS EG
| Task | Utilizare |
|---|---|
| **List Data** | Raport detaliu (listare rânduri) |
| **Summary Report** | Vânzări totale și medii per regiune ← grilă |
| **One-Way Frequencies** | Frecvența valorilor (tabel cu Frequency, Cumulative Frequency) ← grilă |
| **Summary Tables** | Tabele de rezumat |

> **Grilă:** "Ce task pentru distribuția datelor?" → **Niciun răspuns nu este corect** (nici Summary Statistics, nici Summary Tables nu au această opțiune) ← verificat în 2 grile!

> **Grilă:** "Raport vânzări totale și medii per regiune?" → **Summary report**

### Filtre în SAS EG
> Se pot specifica **condiții multiple și condiții logice (AND sau OR)** ← grilă

### Query Builder
**Jonctiuni (joins) în Query Builder:**
- **Inner join** → NUMAI rândurile cu corespondent în AMBELE tabele
- **Left outer join** → toate rândurile din STÂNGA + corespondente din dreapta
- **Right outer join** → toate rândurile din DREAPTA + corespondente din stânga
- **Full outer join** → TOATE rândurile din ambele ← grilă

> **Grilă Query Builder:** Auto-combinare folosește **NUMELE coloanei** (nu tip, nu lungime) ← grilă

> **Grilă:** Combina manual → necesită **același nume și tip de date** ← grilă

> **Grilă Q: Tabela1 are X={1,2,4}, Tabela2 are X={2,3,4} → inner join câte rânduri?**
> X comun: 2 și 4 → **2 rânduri**? Sau 1? Depinde exact de tabele. Verificați cu datele exacte din grilă.

> **Grilă clasică:** Tabela1 X={2,3,5} Cantitate, Tabela2 X={1,2,4} IdClient → Inner join → **1 rând** (X=2 e singurul comun)

### Parametrii în SAS EG
> Afirmație **falsă:** "Singurul tip de parametru este un element dintr-o listă" ← grilă (sunt mai multe tipuri)
> **Adevărat:** când creezi un parametru poți crea și un filtru; poți specifica valori la execuție; face filtrul dinamic

### Ce poate face SAS EG:
- Scrie și rula cod SAS
- Efectua prelucrări pentru analiză și raportare
- Permite exportul în alte aplicații (MS Excel) ← CORECT
- NU poate fi instalat pe mai multe sisteme de operare (funcționează pe Windows) ← verificați

> **Aplicația SAS EG:** 1+3+4 corect (permite scrierea codului, prelucrări, export Excel) ← grilă

### Flux de proces (Process Flow)
- Reprezintă **vizual relațiile dintre obiectele unui proiect** ← grilă
- NU afișează structura ierarhică (aceea e arborele proiectului)
- Un proiect poate conține **mai multe** fluxuri de proces

### Tabela virtuală (Data View)
- **Salvează spațiul de memorie** ← grilă
- NU este statică (se actualizează)
- SE pot efectua prelucrări asupra ei
- Conține date reactualizate

> **Grilă:** "Ce rezultate pot fi folosite ca intrări?" → **Tabelele de date și tabelele virtuale** (nu rapoartele!)

### Secțiunile PROC SAS — ce NU le caracterizează:
> **NU** au ca intrări **fișiere de date în orice format** ← grilă (au ca intrare SETURI DE DATE SAS, nu orice format)
> PROC: produc ieșiri informatii, definesc succesiuni de operații, folosesc seturi de date din secțiunea DATA

### Biblioteca SAS STAT
> Oferă facilități pentru **analiza statistică a datelor** ← grilă

### Format de citire SAS:
> **Trebuie să conțină punctul zecimal (.)** ← grilă (ex: `8.`, `date9.`, `dollar10.2`)

### Import Data task:
> Afirmație **falsă:** "Se poate specifica o expresie pentru a crea o coloană nouă" ← grilă (Import Data nu face asta)

### Documentele compuse:
> Afirmație **falsă:** "Sunt salvate cu ajutorul Document Builder" ← grilă (sunt CREATE, nu salvate astfel)

### Variabilă de tip calcul (Calculate):
> `medie = (nota1 + nota2) / 2` → **variabilă Calculate** ← grilă

### Edit Groups în interogare:
> Util când se creează **o variabilă agregată** ← grilă

### Identifying label în List Data:
> **Suprimă listarea repetată a variabilei de grupare** ← grilă

### Etapele procesului de selecție software (ce NU e etapă):
> **Implementarea algoritmilor specifici** ← NU este etapă de selecție ← grilă
> Etape reale: stabilirea candidatelor, tehnici de evaluare, testare

---

---

## 19. PROC FREQ — Distribuții de frecvențe
*(Seminar 4)*

Scopul principal: tabele cu distribuția valorilor datelor **categorice**.

```sas
PROC FREQ DATA=date_intrare <optiuni>;
    TABLES combinatii_variabile <optiuni>;
RUN;
```

### Declarația TABLES
- **Tabel unidimensional:** `TABLES var1;` — frecvențe pentru o singură variabilă
- **Tabel bidimensional:** `TABLES var1 * var2;` — tabel de contingență
- **Tabel multidimensional:** `TABLES var1 * var2 * var3;`

### Opțiuni TABLES
| Opțiune | Efect |
|---|---|
| `NOCUM` | Suprimă frecvențele și procentele cumulate |
| `NOROW` | Suprimă procentele rândurilor |
| `NOCOL` | Suprimă procentele coloanelor |
| `NOPERCENT` | Suprimă toate procentele |
| `MISSING` | Include valorile lipsă în statistici |
| `LIST` | Tabelele multidimensionale în format listă |
| `OUT=set_date` | Scrie frecvențele într-un set de date |

### Exemplu complet
```sas
PROC FORMAT;
    value nivel low-<40000='Mic'
                 40000-<60000='Mediu'
                 60000-100000='Mare'
                 other='Executiv';
RUN;

PROC FREQ DATA=sem4.angajati;
    TABLES Salariu / nocum;
    FORMAT Salariu nivel.;
    TITLE "Raport privind nivelul salariului anual";
RUN;

/* Tabel bidimensional: Departament x Salariu */
PROC FREQ DATA=sem4.angajati;
    TABLES Departament * Salariu / nocol norow nopercent;
    FORMAT Salariu nivel.;
RUN;
```

> **PROC FREQ cu TABLES var /nocum** → creează tabel de frecvențe **unidimensional** (o singură variabilă)

---

## 20. PROC GCHART și PROC GPLOT — Grafice
*(Seminar 4)*

### PROC GCHART — Grafice cu bare, pie, stea

```sas
PROC GCHART DATA=set_date;
    VBAR  lista_var / <optiuni>;   /* bare verticale */
    HBAR  lista_var / <optiuni>;   /* bare orizontale */
    PIE   lista_var / <optiuni>;   /* grafic pie */
    VBAR3D lista_var;              /* 3D */
RUN;
QUIT;
```

#### Tipuri declarații grafice
| Declarație | Grafic |
|---|---|
| `VBAR` | Bare verticale |
| `HBAR` | Bare orizontale |
| `VBAR3D` / `HBAR3D` | Bare 3D |
| `PIE` / `PIE3D` | Grafic pie |
| `DONUT` | Grafic inel |
| `STAR` | Grafic stea |

#### Opțiuni VBAR/HBAR
```sas
/* Grafic de frecvențe simple */
PROC GCHART DATA=ad_data.biciclete;
    VBAR Model Tara;
RUN; QUIT;

/* Bare care reprezintă sume */
PROC GCHART DATA=ad_data.biciclete;
    VBAR Tara / sumvar=VanzariTotale  /* variabila pentru indicator */
                type=sum              /* tipul indicatorului: sum, mean, etc. */
                maxis=axis1;
RUN; QUIT;

/* A doua variabilă ca subgrup în bare */
PROC GCHART DATA=ad_data.Biciclete;
    VBAR Tara / subgroup=Model;       /* culori diferite per Model în fiecare bară */
RUN; QUIT;

/* Midpoints pentru variabile continue */
PROC GCHART DATA=ad_data.biciclete;
    VBAR VanzariTotale / midpoints=0 to 12000 by 2000;
RUN; QUIT;
```

### PROC GPLOT — Diagrame de corelație (scatter plot)

```sas
PROC GPLOT DATA=set_date;
    PLOT variabila_Y * variabila_X / <optiuni>;
RUN; QUIT;
```

#### Opțiuni SYMBOL
```sas
SYMBOL value=dot;                   /* puncte */
SYMBOL value=dot i=sm;              /* puncte + linie continuă */
SYMBOL value=dot i=join width=2;    /* puncte + linii drepte, grosime 2 */
```

- `INTERPOL=` (prescurtat `I=`): `join` = linii drepte, `sm` = linie netedă
- `WIDTH=`: grosimea liniei
- `VALUE=`: simbolul punctului

---

## 21. PROC CORR — Analiza de corelație
*(Seminar 4)*

Calculează coeficienți de corelație între variabile numerice.

```sas
PROC CORR DATA=set_date <optiuni>;
    VAR lista_variabile;    /* variabile pe axa orizontală (top) */
    WITH lista_variabile;   /* variabile pe axa verticală (stânga) */
RUN;
```

- Fără `VAR` și `WITH` → calculează corelații între **toate variabilele numerice**
- Implicit: coeficientul **Pearson**
- Opțiuni pentru alți coeficienți: `SPEARMAN`, `KENDALL`

```sas
/* Exemplu: influența TV și exerciții asupra notei */
DATA grupa_studenti;
    INPUT Punctaj Televiziune Exercitii @@;
DATALINES;
56 6 2   78 7 4   84 5 5   73 4 0
;
RUN;

PROC CORR DATA=grupa_studenti;
    VAR Televiziune Exercitii;
    WITH Punctaj;
RUN;
```

---

## 22. GRILE TRICKY — CAPCANE FRECVENTE

**1. DROP disponibil în calcule:**
```sas
drop Salary;
Comp = Salary * 2;  /* VALID! Salary e eliminată la output, nu în execuție */
```

**2. MERGE implicit = full outer join** (toate obs. din ambele seturi)

**3. `proc contents data=orion._all_ nods`** ← exact această sintaxă

**4. Format modifică DOAR afișarea** (False că modifică și stocarea)

**5. Variabile numerice: lungime implicită = 8 bytes**

**6. Set de date fără bibliotecă → WORK (temporar)**

**7. Sortare OBLIGATORIE înainte de BY în DATA step (MERGE/SET interclasare)**

**8. `title;` șterge TOATE titlurile**

**9. Deschiderea unui set SAS în EG → POINTER, nu copie**

**10. Format de citire SAS → OBLIGATORIU punctul (.)**


---

## 23. INTERPRETAREA OUTPUTURILOR SAS

### PROC PRINT

```
Obs  Varsta  Sex  Proiect  Examen
  1    21     M      8       8
  2     .     F      9       9
  3    35     M      8       8
```
- **Obs** = numarul observatiei (adaugat automat, nu e variabila in dataset)
- **NOOBS** = elimina coloana Obs
- Valori lipsa = punct `.` la numeric, spatiu la caracter
- Variabilele apar in ordinea din dataset daca nu e specificat VAR

---

### PROC MEANS

```
Variable    N      Mean    Std Dev    Minimum    Maximum
Varsta      8    37.625    16.021     15.000     67.000
Proiect     9     7.778     1.202      5.000      9.000
Examen     10     7.800     0.919      6.000      9.000
```
- **N** = observatii NON-LIPSA (poate fi < total randuri daca exista valori lipsa!)
- **Mean** = media aritmetica
- **Std Dev** = deviatia standard
- **Minimum / Maximum** = valorile extreme
- Valorile lipsa sunt EXCLUSE automat din calcule

---

### PROC UNIVARIATE

```
Moments
N                  10    Mean              7.800
Std Deviation   0.919    Variance          0.844
Skewness       -0.817    Kurtosis          0.103

Quantiles
100% Max    9
 75% Q3     9
 50% Median 8
 25% Q1     7
  0% Min    6

Extreme Observations
Lowest        Highest
Value  Obs    Value  Obs
    6   10        9    2
    7    4        9    5
```
- **Skewness > 0** = distributie right-skewed (coada la dreapta, mean > median)
- **Skewness < 0** = distributie left-skewed (coada la stanga, mean < median)
- **Skewness = 0** = distributie simetrica (normala)
- **Quantiles**: Min = 0%, Q1 = 25%, Median = 50%, Q3 = 75%, Max = 100%

---

### PROC FREQ — tabel unidimensional

```
Cafea       Frequency  Percent  Cumulative  Cumulative
                                Frequency   Percent
cappuccino     12       30.00      12         30.00
espresso        8       20.00      20         50.00
frappe         10       25.00      30         75.00
latte          10       25.00      40        100.00
```
- **Frequency** = numarul de aparitii
- **Percent** = procentul din total
- **Cumulative Frequency** = suma frecventelor de la inceput pana la randul curent
- **Cumulative Percent** = suma procentelor cumulate
- NOCUM = elimina coloanele Cumulative
- NOPERCENT = elimina toate procentele

### PROC FREQ — tabel bidimensional (Cafea * Zona)

```
Cafea      |exterior |interior |  Total
-----------+---------+---------+-------
cappuccino | 5       | 7       |   12
           | 12.50   | 17.50   | 30.00   <- Percent (din total general)
           | 41.67   | 58.33   |         <- Row Pct (din totalul randului)
           | 27.78   | 31.82   |         <- Col Pct (din totalul coloanei)
-----------+---------+---------+-------
Total        18        22         40
```
- Fiecare celula are 4 randuri: Frequency / Percent / Row Pct / Col Pct
- NOROW = elimina Row Pct
- NOCOL = elimina Col Pct
- NOPERCENT = elimina Percent

---

### PROC CORR

```
Pearson Correlation Coefficients, N = 30

              Televiziune   Exercitii
Punctaj
  Televiziune   -0.75432      0.65218
               (<.0001)     (<.0001)
  Exercitii      0.65218      1.00000
               (<.0001)
```
- Valoarea coeficientului: intre -1 si +1
  - aproape de +1 = corelatie pozitiva puternica
  - aproape de -1 = corelatie negativa puternica
  - aproape de 0 = fara corelatie liniara
- **Prob > |r|** (valoarea sub coeficient) = p-value:
  - < 0.05 = corelatie semnificativa statistic
  - < 0.0001 afisat ca `<.0001`
- Diagonala principala = 1.00000 (variabila cu ea insasi)
- Matricea este simetrica: corel(A,B) = corel(B,A)

---

### PROC GCHART — interpretare vizuala
| Declaratie | Ce arata |
|---|---|
| VBAR Var | Bare verticale, inaltime = frecventa categoriei |
| HBAR Var | Bare orizontale |
| PIE Var | Grafic circular, fiecare felie = o categorie |
| subgroup=Var2 | Barele sunt impartite pe sub-categorii (colorate) |
| sumvar=VarNum | Inaltimea = SUMA valorii numerice (nu frecventa!) |
| type=mean | Inaltimea = MEDIA (nu suma, nu frecventa) |
| midpoints= | Specifica valorile afisate pe axa X |

### PROC GPLOT — interpretare vizuala
| Element | Semnificatie |
|---|---|
| PLOT Y * X | Scatter plot: X pe orizontala, Y pe verticala |
| SYMBOL value=dot | Punctele sunt reprezentate ca puncte |
| SYMBOL i=sm | Linie de tendinta smooth prin puncte |
| SYMBOL i=join | Linie dreapta care uneste punctele in ordine |
| SYMBOL width=2 | Grosimea liniei |
