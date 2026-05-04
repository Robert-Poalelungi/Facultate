# Materiale CTS — Design Patterns

Implementări pentru testul 2: **Chain of Responsibility** (comportamental) + **Composite** (structural).

```
CoR/
├── Problema1_CreditBoolean/     Chain of Responsibility — decizie boolean (credit aprobat/respins)
│   ├── Persoana.java
│   ├── AVerificator.java        handler abstract
│   ├── VerificatorBirouCredit.java
│   ├── VerificatorVechime.java
│   ├── VerificatorGradIndatorare.java
│   └── Main.java
│
├── Problema2_CreditMaxim/       Chain of Responsibility — suma maxima eligibila sau exceptie
│   ├── Persoana.java
│   ├── CreditRefuzatException.java
│   ├── ALimitator.java          handler abstract
│   ├── VerificatorEligibilitateMinima.java
│   ├── LimitatorVechime.java
│   ├── LimitatorVenit.java
│   ├── LimitatorScorCredit.java
│   └── Main.java
│
└── Problema3_PreproText/        Chain of Responsibility — preprocesare text prin filtre
    ├── AFiltru.java             handler abstract
    ├── LowerCaseFilter.java
    ├── RemoveExtraSpacesFilter.java
    ├── TrimFilter.java
    ├── RemovePunctuationFilter.java
    ├── ReplaceDiacriticsFilter.java
    ├── StopWordsFilter.java
    ├── ShortWordFilter.java
    ├── DuplicateWordRemover.java
    └── Main.java

Composite/
├── Problema4_OrgStructura/      Composite — ierarhie companie (departamente + angajati)
│   ├── AComponenta.java         nod abstract
│   ├── Angajat.java             leaf
│   ├── Departament.java         composite
│   └── Main.java
│
└── Problema5_FileSystem/        Composite — sistem de fisiere (foldere + fisiere)
    ├── AElementSistem.java      nod abstract
    ├── Fisier.java              leaf
    ├── Folder.java              composite
    └── Main.java
```

## Pattern-uri

### Chain of Responsibility
- Handler abstract cu `setUrmator()` care returneaza handlerul urmator (permite chaining fluent)
- `pasezaMailDeparte()` delegheaza daca exista urmator
- **P1**: returneaza `boolean` — lanțul se opreste la primul `false`
- **P2**: returneaza `double` (suma maxima), aruncă `CreditRefuzatException` dacă nu e eligibil
- **P3**: returneaza `String` modificat progresiv

### Composite
- Nod abstract cu operatiile comune + `adauga/elimina/cauta` care arunca `UnsupportedOperationException` in leaf
- **Leaf** (Angajat, Fisier): implementeaza operatiile pe element simplu
- **Composite** (Departament, Folder): agrega recursiv valorile din copii

## Compilare si rulare (fara IDE)

```bash
cd CoR/Problema1_CreditBoolean
javac *.java
java Main
```
