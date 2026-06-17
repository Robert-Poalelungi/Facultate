# CTS — Materie Completă pentru Examen (Calitate și Testare Software)
### Curs: lect. univ. dr. Mădălina Zurini — ASE București

> Document de sinteză construit pe baza `CTS_Cursuri_Complet.pdf` (cele 14 cursuri), `CTS_Curs_Complet.md` (cod sursă de curs), `CTS_Seminar_Complet.md` (cod sursă de seminar, grupele G1089–G1094) și grilele din `Grile_Examen2026_CTS.pdf` / `GrileTotTotTot.pdf`. Acoperă cele 3 mari domenii de examen: **Clean Code**, **Design Patterns (GoF)**, **Unit Testing cu JUnit**.

---

## CUPRINS

1. [Clean Code](#1-clean-code)
2. [Design Patterns — Creaționale](#2-design-patterns--creaționale)
3. [Design Patterns — Structurale](#3-design-patterns--structurale)
4. [Design Patterns — Comportamentale](#4-design-patterns--comportamentale)
5. [Unit Testing cu JUnit](#5-unit-testing-cu-junit)
6. [Dubluri de test (Test Doubles)](#6-dubluri-de-test-test-doubles)
7. [Git](#7-git)
8. [Cheat sheet — capcane frecvente la examen](#8-cheat-sheet--capcane-frecvente-la-examen)

---

## 1. CLEAN CODE

### 1.1 De ce Clean Code?

Ideea centrală predată la curs: **programarea nu constă în a spune computerului ce să facă, ci în a spune altui om ce vrem să facă un computer**. Practic, codul e citit de oameni mult mai des decât e scris, deci calitatea lecturii contează la fel de mult ca funcționarea corectă.

Câteva observații din curs care apar des în grile sub formă de „completări de frază":
- Programatorul e asemănat cu un **scriitor**.
- Când citim cod, **creierul nostru joacă rol de compilator**.
- Conform unor studii, oamenii pot reține simultan doar **7 elemente (±2)** în memorie — de aceea codul cu prea multe variabile/condiții simultane e greu de urmărit.
- **Rubber Duck Programming** = tehnică de debugging prin explicarea codului cu voce tare (chiar și unei rățuște de jucărie), pentru a-ți clarifica singur problema.

### 1.2 Ce înseamnă Clean Code

Clean Code înseamnă că codul trebuie să fie, **pentru oricine**:
- ușor de **citit**
- ușor de **înțeles**
- ușor de **modificat**

**CLEAN Code = GOOD Code** (sunt sinonime în terminologia cursului).

### 1.3 Bad Code

Bad Code este opusul — caracteristici (capcană de examen: o grilă cere "ce NU reprezintă o caracteristică a Clean Code"; răspunsul e una din aceste caracteristici de Bad Code):
- Greu de citit și înțeles
- Induce în eroare
- Se strică atunci când îl modifici
- Are dependințe în multe module externe
- Este **strâns legat (tight coupled)** de alte secvențe de cod

> **Glass Breaking Code** = cod care are dependințe în multe module externe (capcană: nu înseamnă „cod fragil care se rupe la prima modificare" ca termen separat, ci exact asta — dependențe excesive în module externe, conform feedback-ului din grile).

### 1.4 Principii: DRY, KISS, YAGNI, SOLID

#### DRY — Don't Repeat Yourself
Aplicabil ori de câte ori dăm Copy/Paste unei bucăți de cod, **sau** de fiecare dată când, fără să ne dăm seama, scriem două metode care fac același lucru.

#### KISS — Keep It Simple and Stupid
Se aplică ori de câte ori vrem ca **o metodă să facă de toate** (încălcarea KISS = o metodă cu prea multe funcționalități/scopuri multiple).

**Beneficiile KISS** (apar frecvent ca „alegeți una sau mai multe" / "toate variantele"):
- Permite rezolvarea rapidă de probleme
- Permite rezolvarea unor probleme complexe într-o manieră simplă
- Permite realizarea de produse complexe, ușor de întreținut
- Codul scris este mult mai flexibil
- Codul este mult mai ușor de extins și modificat dacă apar noi cerințe

#### YAGNI — You Ain't Gonna Need It
Nu scriem metode ce nu sunt necesare încă (poate nu vor fi necesare niciodată). **YAGNI este derivat din KISS** — întrebare clasică de grilă: „care principiu este derivat din KISS?" → YAGNI.

#### SOLID
Acronim pentru 5 principii de design orientat-obiect:

| Literă | Principiu | Esență |
|---|---|---|
| **S** | Single Responsibility (SRP) | O clasă trebuie să aibă întotdeauna **o singură responsabilitate și numai una**. „A class should have only one reason to change" (Robert C. Martin). |
| **O** | Open-Closed (OCP) | Clasele trebuie să fie **deschise (open)** pentru extensii, dar **închise (closed)** pentru modificări. |
| **L** | Liskov Substitution (LSP) | Obiectele pot fi înlocuite oricând cu instanțe ale claselor derivate (**subtipuri**) fără ca acest lucru să afecteze funcționalitatea. Cunoscut și ca **„Design by Contract"**. |
| **I** | Interface Segregation (ISP) | Mai multe interfețe specializate sunt oricând de preferat unei singure interfețe generale. Obiectele nu trebuie obligate să implementeze metode care nu le sunt utile. |
| **D** | Dependency Inversion (DIP) | „High-level modules should not depend on low-level modules. Both should depend on abstractions." Modulele de nivel înalt nu depind de cele de nivel jos — ambele depind de abstracții. |

**SRP — detaliu de scenariu din curs:** o clasă `Angajat` care depinde simultan de modificări venite din 2 zone diferite (ex. HR și Financiar / Director Financiar și Director General) încalcă SRP, fiindcă are mai mult de un „motiv de schimbare". Soluția standard predată: împărțirea clasei în două clase, fiecare răspunzând unui singur actor.

**Exemplu de cod SOLID din curs ([`Curs/src/cts/curs/c02/SOLID`](CTS_Curs_Complet.md#curssrcctscursc02soliddafteriworkerjava))** — fiecare principiu are o variantă `Before` (greșit) și `After` (corect):
- **S** — `Angajat` (Before, are atât logică de business cât și de taxare) vs. `CalculatorTaxe` + `ServiciiAngajat` separate (After)
- **O** — `CalculatorSalariu` cu `if`-uri pe tip de angajat (Before) vs. `RegulaSalarizare` ca interfață cu implementări `SalariuLucrator`/`SalariuManager` (After) — adăugarea unui nou tip de angajat NU mai necesită modificarea codului existent
- **L** — `Patrat extends Dreptunghi` cu `setLungime`/`setLatime` separate, ceea ce rupe contractul (Before) vs. `Forma` interfață cu `Dreptunghi` și `Patrat` independente, fiecare cu constructor imutabil (After)
- **I** — o interfață `Angajat` cu metode pentru toți (Before) vs. interfețe separate `Lucrator`/`Managerial` (After)
- **D** — `Manager` depinde direct de clasa concretă `Worker` (Before) vs. `Manager` depinde de interfața `IWorker` (After)

### 1.5 Convenții de nume

| Convenție | Descriere | Exemplu |
|---|---|---|
| **UpperCamelCase** | Pentru **clase și interfețe** | `PasaportPersoana` |
| **lowerCamelCase** | Pentru **metode și variabile** | `medieAritmetica` |
| **System Hungarian Notation** | Se introduce **tipul de dată** în numele variabilei | `strNume`, `iLength`, `bIsPresent`, `fpPercentage` |
| **Apps Hungarian Notation** | Se introduce **scopul/rolul** variabilei în nume (nu tipul) | `nButtonCount`, `btnSubmit`, `txtInput` |

**System Hungarian Notation — tabel de prefixe** (predat explicit la curs):

| Tip de dată | Prefix |
|---|---|
| Character | c sau ch |
| Boolean | b |
| Integer | i |
| Floating Point | f sau fp |
| String | str |
| Double precision floating point | d sau db |
| Pointer | p |
| Unsigned 32-bit integer | u32 |
| Function | fn |
| Long Integer | l |

Un nume bun trebuie să răspundă la 3 întrebări: **De ce există? (WHY?)**, **Ce face? (WHAT?)**, **Cum este folosit? (HOW?)**

### 1.6 Reguli de scriere a codului sursă

- Operatorii sunt separați de operanzi printr-un spațiu. **Excepție: operatorii unari** (nu se separă, ex: `-x`, nu `- x`).
- Acolada de închidere a unui corp de instrucțiuni este singură pe linie, **exceptând** situațiile cu `if-else` sau `try-catch`.
- Blocurile cu instrucțiuni sunt marcate și prin indentare.
- Parametrii sunt separați prin virgulă și spațiu.

### 1.7 Reguli în structuri condiționale

- **Evitați comparațiile cu `true`/`false`** — o variabilă booleană se poate instanția direct (`if(estePrezent)`, nu `if(estePrezent == true)`).
- Variabilele booleene pot fi instanțiate direct.
- **„Nu fiți negativiști!"** — evitați dublele negații.
- Folosiți operatorul **ternar** ori de câte ori este posibil (`int max = a > b ? a : b;`).
- Nu comparați direct cu stringuri — folosiți **enum** pentru astfel de situații.
- Constantele trebuie identificate și denumite (de obicei la începutul claselor).
- Condiții prea mari → indicate variabile intermediare.
- **Folosirea excesivă de enum poate denota un design greșit al claselor.**
- **Multe constante** indică nevoia de înglobare a lor într-o **tabelă din baza de date** (evită update-uri/versiuni dese ale aplicației).

### 1.8 Reguli pentru metode

- Maxim **3 niveluri de structuri imbricate** (arrow code) — peste asta, codul devine ilizibil.
- Ieșire **cât mai rapidă** din funcție (prin `return` sau excepție).
- Variabilele se declară **cât mai aproape de utilizare**.
- Folosiți `this` și o convenție de nume pentru parametrii constructorului.
- **Evitați metodele cu mai mult de 2 parametri.**
- **One Screen Rule**: evitați metodele cu peste **20 de linii de cod**.
- Complexitatea trebuie să fie **invers proporțională** cu numărul de linii de cod.
- Atenție la ordinea în care tratați excepțiile.

**Reguli SIMPLE pentru metode (acronim mnemonic din curs):**
- **S**ingle Responsibility (SRP)
- **I**ndiferent... (KISS aplicat la nivel de metodă)
- Keep It **S**imple & Stupid (KISS)
- Delegă prin pointeri/interfețe
- Folosește interfețe

*(Capcană de grilă: „evitarea interfețelor" este greșit — regula corectă e exact opusul, **folosirea** interfețelor.)*

### 1.9 Reguli pentru clase

- Toate metodele dintr-o clasă trebuie să aibă **legătură cu acea clasă**.
- Evitați clasele generale — mutați prelucrările ca metode statice în clasele aferente.
- Evitați **primitivele ca parametri** — folosiți clase **Wrapper** (Java) ori de câte ori e posibil.
- Atenție la primitive în prelucrări multi-thread.
- Folosiți fișiere de resurse pentru șirurile de caractere din GUI.
- Clasele ce conlucrează trebuie așezate una lângă alta.
- Folosiți design patterns acolo unde situația o cere.

### 1.10 Reguli pentru comentarii

- **Codul bine scris este auto-explicativ** — de cele mai multe ori comentariile nu își au locul.
- **Nu folosiți comentarii pentru a vă cere scuze** (ex: „// when I wrote this, only God and I understood what I was doing").
- **Nu comentați codul nefolosit** — devine **zombie code**. Există soluții de versionare (Git) pentru recuperare.
- Dacă simți nevoia de comentarii pentru a face o metodă lizibilă, probabil acea metodă trebuie **separată în două funcții**.
- **Evitați blocurile de comentarii introductive** — detaliile se găsesc în soluția de versionare.
- Comentarii acceptate doar pentru:
  - **TODO comments**
  - **Doc comments** pentru biblioteci ce vor fi refolosite de alți programatori

> **Zombie code** = cod sursă ce conține bucăți de cod comentate (nu cod vechi/legacy în sine — capcană de grilă).

### 1.11 Scurt dicționar de termeni (din curs)

| Termen | Definiție |
|---|---|
| **Code Review** | Revizuirea oricărei bucăți de cod scrise și de un alt programator |
| **Refactoring** | Rescrierea codului într-o manieră ce se adaptează mai bine noilor specificații |
| **Automatic Testing (= Unit Testing)** | Testarea automată a codului pe baza unor cazuri de utilizare |
| **Pair Programming** | Tehnica prin care doi programatori lucrează la aceeași sarcină (de obicei pentru task-uri complexe) |
| **Glass Breaking Code** | Cod care are dependințe în multe module externe |

---

## 2. DESIGN PATTERNS — CREAȚIONALE

### Context general despre Design Patterns

- Traducere RO: „șabloane de proiectare" / „tipare de proiectare" — ajută la rezolvarea unor probleme similare cu probleme deja rezolvate.
- Cartea de referință: **„Design Patterns: Elements of Reusable Object-Oriented Software"** (1994), cunoscută ca **„Gang of Four" (GoF)**.
- Categoriile GoF sunt **exact 3**: **Creaționale**, **Structurale**, **Comportamentale**. **NU există categoria „Arhitecturale"** — capcană foarte frecventă la examen (vezi capitolul cheat sheet).
- **Pașii de utilizare a unui Design Pattern** (ordine exactă, capcană pe „care e prima etapă"): **(1) Identificare problemă** → (2) Mapare Design Pattern–Problemă → (3) Identificare participanți → (4) Alegerea numelor participanților → (5) Implementarea interfețelor și claselor → (6) Implementarea metodelor.
- Un design pattern reprezintă: **o soluție la o problemă comună în POO** (NU un algoritm, NU o structură de date, NU o soluție universală).

**Cele 7 componente ale unui design pattern** (capcană frecventă — „refactoring" NU e o componentă a pattern-ului, ci o tehnică separată):
1. **Nume** — ajută la comunicarea între programatori, parte din vocabularul comun.
2. **Problemă** — descrie contextul pentru care se folosește pattern-ul.
3. **Structură** — diagrama UML a claselor pentru realizarea pattern-ului.
4. **Participanți** — clasele ce fac parte din structura pattern-ului.
5. **Implementare** — exemplu de cod sursă pentru problema rezolvată.
6. **Utilizări** — folosiri concrete și practice ale pattern-ului.
7. **Corelații** — relația cu alte design pattern-uri.

**Avantaje:** soluții folosite și testate de comunitate; module deja dezvoltate, integrabile facil în proiecte de anvergură; concepte universal cunoscute (vocabular comun); ajută comunicarea între programatori; permit înțelegerea mai facilă a codului/arhitecturii; conduc la evitarea rescrierii codului sursă (refactoring); permit reutilizarea soluțiilor standard; permit documentarea codului/arhitecturilor.

**Dezavantaje:** necunoașterea corectă a pattern-ului conduce la ambiguitate; din dorința de aplicare forțată se complică foarte mult codul sursă; **„irosirea timpului" cu etapa de analiză** (capcană: NU „timpul de analiză este redus" — de fapt analiza durează mai mult, ăsta e exact dezavantajul).

### Lista completă a pattern-urilor pe categorii (conform cursului)

> **Atenție:** cursul prof. Zurini enumeră teoretic și pattern-uri GoF care **NU au fost implementate explicit în cod** la curs/seminar (Bridge, Iterator, Interpreter, Mediator, Visitor) — pot apărea în grile ca „care din următoarele e de tip X" fără cod de exemplu asociat.

**Creaționale:** Singleton, Builder, Factory (Simple Factory), Factory Method, Abstract Factory, Prototype.

**Structurale** (contribuie la compoziția claselor și obiectelor, decuplând interfețele de clase): Adapter, **Bridge**, Composite, Decorator, Facade, Flyweight, Proxy.

**Comportamentale** (permit distribuția responsabilităților pe clase și descriu interacțiunea între clase și obiecte): Chain of Responsibility, Command, **Iterator**, **Interpreter**, **Mediator**, Memento, Observer, State, Strategy, **Visitor**, Template (Method).

> **Capcană de grilă frecventă:** „Chain of Responsibility NU e structural" (e Comportamental); „Bridge NU e comportamental" (e Structural); „Template NU e structural" (e Comportamental).

---

### 2.1 Singleton

**Sintagma cheie:** **instanță unică** / **o singură instanță**.

**Problemă tipică de curs:** un restaurant trebuie să gestioneze centralizat ocuparea meselor — toți ospătarii trebuie să vadă aceeași informație despre disponibilitatea meselor.

**Implementare generală:**
- Constructorul clasei este **privat**.
- Clasa conține o **instanță statică**.
- Crearea de obiecte se face printr-o **metodă statică** (`getInstance()`), care returnează instanța dacă a fost deja inițializată, sau o creează prin apelul constructorului privat.

**Tipuri de Singleton:**

| Tip | Caracteristică |
|---|---|
| **Eager Initialization** | Instanța e creată **la momentul declarării**, chiar dacă nu va fi folosită niciodată → ineficient. |
| **Static Block Initialization** | Similar Eager, dar permite **captarea excepțiilor** la inițializare. |
| **Lazy Initialization** | Cea mai implementată variantă. **Problemă**: în multithreading, metoda poate fi apelată simultan de două thread-uri → se pot crea **două instanțe diferite** (nu e thread-safe). |
| **Thread Safe Singleton** | Asigură că metoda nu va fi apelată de alt thread până nu termină thread-ul curent (sincronizare). |
| **Inner Static Helper Class** (Bill Pugh) | Conține o clasă imbricată (Helper) încărcată doar la apelul `getInstance()`. Combină: **Lazy initialization** + **Thread safe** + **Performanță** (fără blocuri de sincronizare). |
| **Enum Singleton** (Joshua Bloch) | Folosește o enumerare pentru crearea unică a instanței. Valorile enum sunt accesibile global. **NU permite Lazy initialization.** Testare dificilă (greu de înlocuit cu mock-uri). Nu poate extinde alte clase. |

**Singleton și serializarea:** dacă serializăm și deserializăm o instanță Singleton, se obțin **două instanțe** (una creată, una deserializată). Soluția: implementarea metodei **`readResolve()`**, care trebuie să returneze instanța deja creată.

**Singleton vs. clasă statică:**
- Singleton respectă principiile POO.
- Un obiect Singleton poate fi trimis ca parametru unei funcții — o clasă statică NU poate.
- O clasă Singleton poate implementa o interfață sau extinde altă clasă.

**Singleton Collection** (= Singleton registry) — gestiunea unor obiecte unice într-o colecție.

**Utilizări practice:** o singură instanță a aplicației; conexiune unică la baza de date; `SharedPreferences` în Android; `DocumentBuilderFactory`.

**Corelații:** Factory → o singură fabrică de obiecte; Builder → un singur obiect care construiește alte obiecte.

![Singleton](https://refactoring.guru/images/patterns/content/singleton/singleton.png?id=108a0b9b5ea5c4426e0afa4504491d6f)
![Singleton — Structură UML](https://refactoring.guru/images/patterns/diagrams/singleton/structure-en.png?id=4e4306d3a90f40d74c7a4d2d2506b8ec)

> **Analogie reală (refactoring.guru):** Guvernul unui stat este un exemplu clasic de Singleton. O țară poate avea un singur guvern oficial. Indiferent de identitatea persoanelor care îl compun, titlul „Guvernul lui X" este un punct global de acces care identifică grupul de oameni aflat la conducere.

**Cod relevant din proiect:** [`Curs/src/cts/curs/c03/Singleton/`](CTS_Curs_Complet.md#curssrcctscursc03singletoncollectionangajatjava) (toate cele 6+ variante), [`Curs/singleton.txt`](CTS_Curs_Complet.md#curssingletontxt) (problema restaurantului).

---

### 2.2 Simple Factory → Factory Method → Abstract Factory

**Simple Factory** (NU e pattern GoF oficial, dar e folosit intens în practică)
- O singură clasă Factory cu o metodă care primește un tip (string/enum) și returnează obiectul concret corespunzător, de regulă prin `if`/`switch`.
- **Capcană clasică de examen** (vezi imaginea cu `ShapeFactory`): o implementare Simple Factory cu mai multe `if(type.equals(...))` are aceste probleme:
  - **Încalcă OCP** — adăugarea unui nou tip necesită modificarea metodei `create()`.
  - **Adăugarea unui nou tip necesită modificarea fabricii** (consecință directă).
  - **Posibilitatea returnării valorii `null`** dacă tipul nu se potrivește cu niciun caz → risc de `NullPointerException`.
  - (DIP și ISP NU sunt relevante pentru această problemă specifică.)

**Factory Method** (= **Virtual Constructor**)
- Fiecare subclasă concretă de Factory decide ce obiect concret creează, prin polimorfism (nu prin `if`/`switch` ca la Simple Factory).
- Nu folosește structuri `switch` sau `if-else`.
- Pentru apeluri se folosesc **abstractizări**, nu obiecte concrete.

![Factory Method](https://refactoring.guru/images/patterns/content/factory-method/factory-method-en.png?id=cfa26f33dc8473e803fadae0d262100a)
![Factory Method — Structură UML](https://refactoring.guru/images/patterns/diagrams/factory-method/structure.png?id=4cba0803f42517cfe8548c9bc7dc4c9b)

> **Analogie reală (refactoring.guru):** Imaginează-ți o aplicație de logistică care inițial gestionează doar camioane. Pe măsură ce crește, apare nevoia de transport maritim. Dacă codul e cuplat strâns cu clasa `Camion`, adăugarea clasei `Vapor` necesită modificarea întregii baze de cod. Factory Method permite definirea unui contract (interfață) pentru crearea obiectului de transport, iar fiecare subclasă decide ce tip concret creează — fără a modifica codul existent.

**Abstract Factory**
- Creează o **familie de obiecte înrudite** fără a specifica clasele concrete.
- Avem o singură „fabrică-mamă" prin care obținem obiecte din toate familiile de obiecte dintr-o anumită categorie.
- Util când există o familie de obiecte într-o aplicație (ex. în cod: `RestaurantItalianFactory` produce `Pizza`+`VinRosu`, `RestaurantJaponezFactory` produce `Sushi`+`Matcha`).

![Abstract Factory](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-en.png?id=d0210ee255712a245fead94a3fafabe0)
![Abstract Factory — Structură UML](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure.png?id=a3112cdd98765406af94595a3c5e7762)

> **Analogie reală (refactoring.guru):** Un magazin de mobilă vinde familii de produse: `Scaun` + `Canapea` + `MăsuțăCafea`, disponibile în variantele `Modern`, `Victorian` și `ArtDeco`. Clienții se supără când primesc mobilă care nu se potrivește (un scaun Modern cu o canapea Victoriană). Abstract Factory garantează că toate obiectele create aparțin aceleiași familii, fără ca programul să cunoască clasele concrete.

**Cod relevant:** [`Curs/src/cts/curs/c05/factory/SimpleFactory`](CTS_Curs_Complet.md#curssrcctscursc05factorysimplefactoryimplementareetippizzajava), [`FactoryMethod`](CTS_Curs_Complet.md#curssrcctscursc05factoryfactorymethodimplementarefactorypizzanonvegetarianajava), [`AbstractFactory`](CTS_Curs_Complet.md#curssrcctscursc05factoryabstractfactoryimplementareabstractbauturajava).

---

### 2.3 Builder

**Utilizare:** pentru obiecte cu **multe atribute**, dintre care unele **opționale**, iar altele **obligatorii**.

- Are **2-3 variante de implementare** — a treia variantă folosește o **clasă imbricată (Inner class)**.
- Participanți: `IBuilder` (interfață), clasa Builder concretă, clasa Produs.
- **NU** este folosit pentru crearea de obiecte din aceeași familie (asta e Abstract Factory) — afirmație falsă frecventă în grile.
- Builder este un design pattern **creațional**.

![Builder](https://refactoring.guru/images/patterns/content/builder/builder-en.png?id=617612423ea3752477dc90929115b3ee)
![Builder — Structură UML](https://refactoring.guru/images/patterns/diagrams/builder/structure.png?id=fe9e23559923ea0657aa5fe75efef333)

> **Analogie reală (refactoring.guru):** Construirea unei case simple necesită fundație, pereți, ușă, ferestre și acoperiș. Dar dacă vrei o casă mai mare, cu piscină, sistem de încălzire și cablaj electric? În loc să creezi o subclasă pentru fiecare combinație posibilă, Builder-ul permite construcția pas cu pas: apelezi doar pașii de construcție necesari pentru varianta ta specifică.

**Cod relevant:** [`Curs/src/cts/curs/c05/builder/v1`](CTS_Curs_Complet.md#curssrcctscursc05builderv1implementareibuilderjava), [`v2`](CTS_Curs_Complet.md#curssrcctscursc05builderv2implementareibuilderjava), [`v3`](CTS_Curs_Complet.md#curssrcctscursc05builderv3implementareibuilderjava) (Petrecere/PetrecereBuilder).

---

### 2.4 Prototype

**Utilizare:** pentru obiecte a căror **construire durează foarte mult** sau **consumă foarte multe resurse** — ajută la crearea de **clone** în loc de creare costisitoare repetată.

**Participanți:** `Prototype` (interfață de clonare), `Concrete Prototype`, opțional `Prototype Factory`.

![Prototype](https://refactoring.guru/images/patterns/content/prototype/prototype.png?id=e912b1ada20bbf7b2ffc09e93b9fab20)
![Prototype — Structură UML](https://refactoring.guru/images/patterns/diagrams/prototype/structure.png?id=088102c5e9785ff45debbbce86f4df81)

> **Analogie reală (refactoring.guru):** Diviziunea mitotică celulară — după diviziune, se formează o pereche de celule identice. Celula originală acționează ca prototip și joacă un rol activ în crearea copiei. Spre deosebire de prototipurile industriale (care sunt pasive), celula biologică se reproduce singură, exact ca în pattern.

**Diferența cheie Prototype vs. Flyweight** (capcană foarte frecventă):
- **Prototype** → optimizează **VITEZA de creare** a obiectelor (prin clonare).
- **Flyweight** → optimizează **MEMORIA** necesară stocării obiectelor (prin reutilizare).
- Prin Prototype, crearea obiectelor se face prin **clonare**; prin Flyweight, obiectele sunt **reutilizate**.
- Prototype este **Creațional**, Flyweight este **Structural**.

**Cod relevant:** [`Curs/src/cts/curs/c04/Prototype/`](CTS_Curs_Complet.md#curssrcctscursc04prototypeimplementareabstractcontractjava) (ContractCorporate/ContractParty), și în seminar: [`CrocsPrototypeFactory`](CTS_Seminar_Complet.md#g1089s05srcctsg1089s05ex1implementareprototype2crocsprototypefactoryjava) (G1089/S05, G1092/S05, G1093/S05) — context Crocs personalizabile.

---

## 3. DESIGN PATTERNS — STRUCTURALE

> Contribuie la compoziția claselor și obiectelor, realizând **decuplarea interfețelor de clase**.

### 3.1 Adapter

**Problemă rezolvată:** utilizarea anumitor clase din framework-uri diferite, care **nu au o interfață comună**.

**Reguli esențiale:**
- Clasele existente **NU se modifică** — se adaugă noi clase (clasa **Wrapper**) pentru a realiza adaptarea.
- Utilizarea claselor existente se face **mascat**, prin intermediul adapterului.
- **Adapterul NU adaugă funcționalitate** — funcționalitatea e realizată tot de clasele existente (diferența cheie față de Decorator).

**Cele 2 tipuri de Adapter:**

| Tip | Implementare |
|---|---|
| **Adapter de clase** | Clasa Adapter **moștenește** clasa existentă și implementează interfața la care trebuie să facă adaptarea (apeluri prin `super`). |
| **Adapter de obiecte** | Clasa Adapter **conține o instanță** a clasei existente (compoziție) și implementează interfața la care trebuie să facă adaptarea — prin implementarea interfeței se asigură un set de metode care fac apeluri către metodele clasei existente prin intermediul instanței deținute. |

**Diferența Adapter vs. Decorator** (capcană foarte frecventă):
- Adapter NU adaugă funcționalitate nouă, doar schimbă interfața.
- Decorator adaugă funcționalitate nouă, păstrând interfața.

![Adapter](https://refactoring.guru/images/patterns/content/adapter/adapter-en.png?id=11ef6ae6177291834323e3f918c47cd2)
![Adapter — Structură UML](https://refactoring.guru/images/patterns/diagrams/adapter/structure-object-adapter.png?id=33dffbe3aece294162440c7ddd3d5d4f)

> **Analogie reală (refactoring.guru):** Când călătorești din SUA în Europa, constați că priza americană nu se potrivește în socketul german. Problema se rezolvă cu un adaptor de priză — care are socketul american pe o parte și ștecherul european pe cealaltă. Exact ca pattern-ul: adaptorul face ca două interfețe incompatibile să poată colabora.

**Cod relevant:** [`Curs/src/cts/curs/c08/adapter/clase/`](CTS_Curs_Complet.md#curssrcctscursc08adapterclaseimplementareadapterjava) și [`c08/adapter/obiecte/`](CTS_Curs_Complet.md#curssrcctscursc08adapterobiecteimplementareadapterjava) (context: `EvaluareClientFirmaA`/`EvaluareClientFirmaB`). În seminar: [`AdapterEuropaToAmerica`](CTS_Seminar_Complet.md#g1093s10srcctsg1093s10adapterimplementareadaptereuropatoamericajava) (priza Europa→America), [`Adaptor`](CTS_Seminar_Complet.md#g1093s11srcctss11adapterimplementareadaptorjava) (MicroUSB→USBc) — G1093.

---

### 3.2 Facade

**Problemă rezolvată:** ușurează lucrul cu **framework-uri foarte complexe**.

**Implementare:**
- Un subsistem format din mai multe clase/servicii.
- O clasă **Facade** care oferă o interfață unificată și simplificată.
- Facade deține/coordonează obiectele din subsistem și **delegă apelurile** către clasele potrivite.
- Clientul interacționează **doar cu Facade**, nu direct cu clasele interne.

**Asemănarea Facade ↔ Adapter:** **ambele sunt wrappere** (ambele „înfășoară" alt cod, fără a-l modifica).

![Facade](https://refactoring.guru/images/patterns/content/facade/facade.png?id=1f4be17305b6316fbd548edf1937ac3b)
![Facade — Structură UML](https://refactoring.guru/images/patterns/diagrams/facade/structure.png?id=258401362234ac77a2aaf1cde62339e7)

> **Analogie reală (refactoring.guru):** Când suni la un magazin pentru a plasa o comandă, operatorul telefonic este Facade-ul tău. El îți oferă o interfață simplă (vocea) către sistemul de comandă, gateway-urile de plată și diferitele servicii de livrare ale magazinului — tu nu interacționezi direct cu niciunul dintre acestea.

**Cod relevant:** [`Curs/src/cts/curs/c07/facade/`](CTS_Curs_Complet.md#curssrcctscursc07facadeimplementarebucatarjava) — context restaurant: `Facade` coordonează `GestiuneBucatari` și `GestiuneSali` pentru rezervarea unei petreceri.

---

### 3.3 Decorator

**Problemă rezolvată:** adaugă funcționalitate **fără a schimba** clasa originală.

**Participanți (4, EXACT):** `AbstractProduct`, `ConcreteProduct`, `AbstractDecorator`, `ConcreteDecorator`.

**Implementare:**
- Clasa abstractă (`AbstractDecorator`) implementează interfața produsului și ține o instanță a acelei interfețe.
- Pentru metoda din interfață se oferă o implementare, **dar nu se adaugă noi funcții abstracte** la nivelul decoratorului abstract.
- Decoratorii concreți implementează noile metode care extind funcționalitatea.

![Decorator](https://refactoring.guru/images/patterns/content/decorator/decorator.png?id=710c66670c7123e0928d3b3758aea79e)
![Decorator — Structură UML](https://refactoring.guru/images/patterns/diagrams/decorator/structure.png?id=8c95d894aecce5315cc1b12093a7ea0c)

> **Analogie reală (refactoring.guru):** Îmbrăcarea hainelor este un exemplu clasic de Decorator. Când ți-e frig, te înfășori într-un pulover. Dacă tot ți-e frig, pui o jachetă deasupra. Dacă plouă, adaugi o impermeabilă. Fiecare haină „extinde" comportamentul tău de bază, dar nu face parte din tine — și o poți da jos oricând.

**Cod relevant:** [`Curs/src/cts/curs/c07/decorator/`](CTS_Curs_Complet.md#curssrcctscursc07decoratorimplementareadecoratorpizzajava) — context pizza: `APizza` (abstract), `ADecoratorPizza`, `DecoratorCrown`, `DecoratorPicant`. Seminar: [`ABonDecorator`](CTS_Seminar_Complet.md#g1091s08srcctsmatracaruanamariag1091decoratorimplementareabondecoratorjava)/`DecoratorPrimavara` (bonuri cu reduceri sezoniere).

---

### 3.4 Composite

**Problemă rezolvată:** crearea unei **structuri ierarhice/arborescente** prin compunerea de obiecte. **NU este o structură de date** ca atare — e despre o relație **container-frunză**.

**Participanți:** o interfață/clasă abstractă comună + **Composite** (nod container) + **Frunză** (nod terminal).

**Implementare:**
- Clasele Composite (container) conțin o **listă** cu elemente de tipul componentei abstracte; permit `adaugaNod()`/`eliminaNod()`.
- Clasele Frunză **NU implementează** metodele de adăugare/ștergere a nodurilor (de obicei aruncă `UnsupportedOperationException`).

![Composite](https://refactoring.guru/images/patterns/content/composite/composite.png?id=73bcf0d94db360b636cd745f710d19db)
![Composite — Structură UML](https://refactoring.guru/images/patterns/diagrams/composite/structure-en.png?id=b7f114558b594dfb220d225398b2b744)

> **Analogie reală (refactoring.guru):** Ierarhia militară. O armată este compusă din divizii; o divizie e formată din brigăzi; o brigadă conține plutoane, care sunt alcătuite din echipe de soldați. Ordinele sunt date la vârful ierarhiei și transmise în jos, nivel cu nivel, până când fiecare soldat știe ce trebuie să facă — indiferent dacă ești la nivel de armată sau de soldat individual, interfața de „execută ordine" e aceeași.

**Utilizare practică:** meniurile aplicațiilor, meniurile de restaurant (structuri ierarhice de categorii/produse).

**Corelația Composite ↔ Decorator:** „Nodurile Composite pot fi privite ca Noduri Frunză decorate" — ambele „înfășoară" alte obiecte într-un mod recursiv/extensibil.

**Cod relevant:** [`Curs/src/cts/curs/c09/composite/`](CTS_Curs_Complet.md#curssrcctscursc09compositeimplementareanodjava) — context meniu restaurant: `ANod` (abstract), `Structura` (composite), `Produs` (frunză), folosit pentru `Meniu`/`Pizzeria ASE`.

---

### 3.5 Flyweight

**Problemă rezolvată:** optimizarea **memoriei** atunci când se construiesc foarte multe obiecte ale unei clase, obiecte ce au o **parte comună**.

**Concepte cheie:**
- **Stare intrinsecă** = stare partajată, comună mai multor obiecte (stocată în obiectul Flyweight reutilizat).
- **Stare extrinsecă** = stare specifică per-instanță, transmisă din exterior la apelul metodei.
- `FlyweightFactory` conține un **HashMap** pentru reținerea/reutilizarea obiectelor asemănătoare — evită crearea de noi obiecte identice.

**Asemănarea Flyweight ↔ Factory:** construirea de obiecte este gestionată de o clasă (factory pattern comun ca structură).

![Flyweight](https://refactoring.guru/images/patterns/content/flyweight/flyweight.png?id=e34fbacb847dd609b5e68aaf252c4db0)
![Flyweight — Structură UML](https://refactoring.guru/images/patterns/diagrams/flyweight/structure.png?id=c1e7e1748f957a4792822f902bc1d420)

> **Analogie reală (refactoring.guru):** Un joc video cu mii de particule/gloanțe/explozii pe ecran. Dacă fiecare particulă și-ar stoca toate datele (culoare, textură, formă), memoria RAM ar fi rapid epuizată. Flyweight separă starea comună (textura, culoarea — **intrinsecă**, stocată o singură dată și partajată) de starea unică per-instanță (poziție, viteză — **extrinsecă**, transmisă la apelul metodei). Astfel, mii de particule partajează același obiect Flyweight.

**Diferența cheie Flyweight vs. Prototype** (vezi și secțiunea Prototype): Flyweight optimizează **memoria** prin reutilizare; Prototype optimizează **viteza de creare** prin clonare.

**Cod relevant:** [`Curs/src/cts/curs/c08/flyweight/`](CTS_Curs_Complet.md#curssrcctscursc08flyweightimplementarebonjava) — `MesajPrintareFactory` (cu HashMap), `Bon`. Seminar: [`FabricaDeRecomandari`](CTS_Seminar_Complet.md#g1093s11srcctss11flyweightimplementarefabricaderecomandarijava)/`Recomandare` (G1093/S11), [`FlyweightFactory`](CTS_Seminar_Complet.md#g1093s12srcctss12g1093flyweightimplementareflyweightfactoryjava)/`Monstru`/`Vrajitor` (G1093/S12).

---

### 3.6 Proxy

**Problemă rezolvată:** controlul accesului la un obiect, **fără a-i modifica interfața**.

**Implementare:**
- O interfață comună pentru obiectul real și proxy.
- O clasă care implementează funcționalitatea efectivă (obiectul real).
- Un Proxy care implementează **aceeași interfață** ca obiectul real, deținând o referință către obiectul real (direct sau creat la nevoie).
- Clientul lucrează cu Proxy-ul **ca și cum ar fi obiectul real**.
- Metoda specifică instanței reale e apelată **doar dacă** condițiile sunt îndeplinite (control de acces).

**Problemă tipică de curs:** o petrecere de Crăciun cu vârstă minimă 18 ani — Proxy-ul verifică vârsta înainte de a permite înregistrarea efectivă.

**Diferența Proxy vs. Decorator** (capcană frecventă):
- **Proxy** → permite/restricționează accesul la funcționalități existente.
- **Decorator** → adaugă funcționalități noi.

![Proxy](https://refactoring.guru/images/patterns/content/proxy/proxy.png?id=efece4647fb11e3f7539291796327666)
![Proxy — Structură UML](https://refactoring.guru/images/patterns/diagrams/proxy/structure.png?id=f2478a82a84e1a1e512a8414bf1abd1c)

> **Analogie reală (refactoring.guru):** Un card de credit este un Proxy pentru un cont bancar, care la rândul lui este un Proxy pentru o sumă de bani fizică. Ambele implementează aceeași interfață: pot fi folosite pentru a face o plată. Cardul elimină necesitatea de a purta bani cash, iar magazinul beneficiază de securitatea tranzacțiilor electronice.

**Cod relevant:** [`Curs/src/cts/curs/c07/proxy/`](CTS_Curs_Complet.md#curssrcctscursc07proxyimplementareclientjava) — `Petrecere`/`PetrecereProxy` (verificare vârstă). Seminar: [`PesteraProxy`](CTS_Seminar_Complet.md#g1089s08srcpestera_proxyimplementare_proxypesteraproxyjava) (G1089/S08), [`SpitalProxy`](CTS_Seminar_Complet.md#g1090s08srcproxylayer_intermediarspitalproxyjava)/`ProxySpital` (G1090–G1094/S08).

---

## 4. DESIGN PATTERNS — COMPORTAMENTALE

> Furnizează soluții pentru o mai bună interacțiune între obiecte și clase; distribuie responsabilități și descriu interacțiunea dintre clase și obiecte.

### 4.1 Strategy

**Utilizare:** se dorește alegerea implementării pentru rezolvarea unei probleme pentru care există mai mulți algoritmi, cu **schimbare la runtime**.

**Participanți (EXACT 3 componente):**
1. O **interfață** ce definește algoritmul/strategia.
2. **Clase concrete** ce implementează interfața (algoritmi concreți interschimbabili).
3. O **clasă client/context** ce conține o **referință** de tipul interfeței (compoziție) și un mecanism pentru a schimba strategia.

**Diferența Strategy vs. State** (capcană extrem de frecventă — vezi cheat sheet): la **Strategy**, **clientul** alege explicit algoritmul; la **State**, schimbarea e **internă/automată**, declanșată de starea obiectului.

![Strategy](https://refactoring.guru/images/patterns/content/strategy/strategy.png?id=379bfba335380500375881a3da6507e0)
![Strategy — Structură UML](https://refactoring.guru/images/patterns/diagrams/strategy/structure.png?id=c6aa910c94960f35d100bfca02810ea1)

> **Analogie reală (refactoring.guru):** Vrei să ajungi la aeroport. Poți lua autobuzul, comanda un taxi sau merge cu bicicleta. Acestea sunt strategiile tale de transport. Alegi una în funcție de factori ca bugetul sau constrângerile de timp — scopul (ajungerea la aeroport) rămâne același, doar algoritmul (mijlocul de transport) se schimbă.

**Cod relevant:** [`Curs/src/cts/curs/c10/strategy/`](CTS_Curs_Complet.md#curssrcctscursc10strategyimplementareiprocesabiljava) — `IProcesabil`, `StrategieCaloriiMinim`, `StrategieCarbohidratiMinim`, client `MeniuRestaurant`/`OfertaMeniu`. Seminar: [`StrategiePlataCard`](CTS_Seminar_Complet.md#g1089s10srcctserculescuraresg1089strategyimplementarestrategieplatacardjava)/`StrategiePlataCash` (G1089, G1090, G1091, G1094 — plată cash vs. card), [`Vizualizare2D`](CTS_Seminar_Complet.md#g1090s10srcctss10strategyimplementarevizualizare2djava)/`Vizualizare3D` (G1090/S10).

---

### 4.2 Observer

**Utilizare:** atunci când anumite obiecte trebuie să fie **anunțate automat** la schimbarea stării altor obiecte.

**Relația este 1:n** (NU 1:1!) — un subiect notifică **mai mulți** observatori simultan.

![Observer](https://refactoring.guru/images/patterns/content/observer/observer.png?id=6088e31e1b0d4a417506a66614dcf065)
![Observer — Structură UML](https://refactoring.guru/images/patterns/diagrams/observer/structure.png?id=365b7e2b8fbecc8948f34b9f8f16f33c)

> **Analogie reală (refactoring.guru):** Abonamentele la reviste și ziare. În loc să mergi zilnic la chioșc să verifici dacă a apărut numărul nou, te abonezi și primești revista direct la cutia poștală după publicare. Editorul menține lista abonaților și știe interesele acestora; abonații pot renunța oricând la abonament.

**Participanți:**
- `ISubiect`/interfață observabilă — gestionează lista de observatori (clasa **ObservabilConcret** = clasa CONCRETĂ care gestionează lista de observatori — capcană: nu e clasa abstractă).
- `IObserver` — interfață abstractă pentru obiectele care vor fi notificate.
- **ObservatorConcret** = clasele concrete care definesc la nivel concret observatorii.

**Cod relevant:** [`Curs/src/cts/curs/c10/observer/`](CTS_Curs_Complet.md#curssrcctscursc10observerimplementareclientjava) — `Restaurant` (subiect) notifică `Client` (observer) la schimbări. Seminar: [`ServiciuMeteo`](CTS_Seminar_Complet.md#g1089s10srcctserculescuraresg1089observerimplementareserviciumeteojava)/`ServiciuPolitiaRomana` ca observeri (G1089, G1090, G1091, G1092, G1093/S10).

---

### 4.3 Chain of Responsibility

**Utilizare:** rezolvarea unei probleme când **nu se știe cu exactitate** cine o poate rezolva, dar există o listă de posibilități (un lanț de handlere).

**Implementare:**
- Cererea trece printr-un **lanț de handlere** până una o rezolvă.
- Dacă un handler concret **nu poate rezolva** problema, apelează la **următorul handler** din lanț.
- Participantul **Handler** = clasă abstractă care definește interfața obiectelor ce vor gestiona cererea de procesare/rezolvare.

![Chain of Responsibility](https://refactoring.guru/images/patterns/content/chain-of-responsibility/chain-of-responsibility.png?id=56c10d0dc712546cc283cfb3fb463458)
![Chain of Responsibility — Structură UML](https://refactoring.guru/images/patterns/diagrams/chain-of-responsibility/structure.png?id=848f0fc8dca57a44974d63f8181f5406)

> **Analogie reală (refactoring.guru):** Suportul tehnic telefonic. Când suni, apelul trece printr-un sistem automat, apoi la un operator general, și în final la un inginer specializat. Fiecare nivel încearcă să rezolve problema sau o transferă nivelului următor — exact ca un lanț de handlere care procesează sau pasează cererea.

**Cod relevant:** [`Curs/src/cts/curs/c09/chain_of_responsability/`](CTS_Curs_Complet.md#curssrcctscursc09chain_of_responsabilityimplementareahandlerjava) — `AHandler`, `Bucatar`/`BucatarSef` (escaladare comandă). Seminar: [`HandlerANAF`](CTS_Seminar_Complet.md#g1089s09srcchain_of_responsabilityimplementarehandleranafjava)/`HandlerVechime`/`HandlerNivelSalariu` (verificare eligibilitate credit, în majoritatea grupelor S09), [`FiltrarePret`](CTS_Seminar_Complet.md#g1093s09srcctss09g1093corimplementarefiltrarepretjava)/`FiltrareProcentReducere`/`FiltrareRecenzii` (G1093/S09).

---

### 4.4 Command

**Utilizare:** se dorește **decuplarea clientului** de cel ce execută o acțiune (loose coupling).

**Participanți (EXACT 4):**
1. `Command` — interfață care definește comanda în sens general.
2. Comenzi concrete — clase ce implementează `Command` (`ComandaPizza`, `ComandaPaste` etc.).
3. **Invoker** — clasa care gestionează/declanșează comenzile.
4. **Receiver** — obiectul responsabil cu **execuția efectivă** a acțiunilor.

**Caracteristici:** Command **nu ascunde** aplicarea de comenzi — se știe concret ce presupune acea comandă. Util la: macro-uri, lucrul cu fișiere, oriunde se dorește revenirea la o stare anterioară prin comenzi (deși Undo propriu-zis se face de regulă combinat cu Memento).

![Command](https://refactoring.guru/images/patterns/content/command/command-en.png?id=80fbadc666cf3b9b1958c546d2746ca4)
![Command — Structură UML](https://refactoring.guru/images/patterns/diagrams/command/structure.png?id=1cd7833638f4c43630f4a84017d31195)

> **Analogie reală (refactoring.guru):** Într-un restaurant, chelnerul preia comanda ta și o notează pe hârtie. Biletul de comandă este obiectul Command — conține toate detaliile necesare și rămâne în coadă până bucătarul este gata să prepare. Hârtia îi permite bucătarului să înceapă imediat, fără a necesita clarificări directe de la tine.

**Cod relevant:** [`Curs/src/cts/curs/c10/command/`](CTS_Curs_Complet.md#curssrcctscursc10commandimplementarebucatarjava) — `IComanda`, `ComandaPizza`/`ComandaPaste`, `Ospatar` (invoker), `Bucatar` (receiver). [`Curs/src/cts/curs/c11/Command_telecomanda/`](CTS_Curs_Complet.md#curssrcctscursc11command_telecomandaimplementarecomandacoboarajaluzelejava) — telecomandă TV/jaluzele (`Telecomanda` = invoker, `Televizor`/`Jaluzele` = receivers). Seminar: [`ComandaBuy`](CTS_Seminar_Complet.md#g1093s12srcctss12g1093commandimplementarecomandabuyjava)/[`ComandaSell`](CTS_Seminar_Complet.md#g1093s12srcctss12g1093commandimplementarecomandaselljava) cu `Broker` (G1093/S12, [`G1094/S11`](CTS_Seminar_Complet.md#g1094s11srcctscommandimplementareactiunebursajava) — tranzacții bursă).

---

### 4.5 Memento

**Utilizare:** realizarea de **backup-uri**, restaurarea unei stări anterioare a unui obiect.

**Participanți (EXACT 3, nu mai puțini/mulți):**
1. **Memento** — obiectul „instantaneu" care reține starea.
2. **Originator** — obiectul a cărui stare e salvată/restaurată.
3. **CareTaker** — gestionează/stochează colecția de Memento-uri (de regulă NU modifică conținutul lor).

**Detaliu de implementare:** clasa Memento poate fi inclusă (clasă imbricată) în cadrul clasei Originator, sau poate fi externă. Memento e folosit atât de Originator cât și de CareTaker.

![Memento](https://refactoring.guru/images/patterns/content/memento/memento-en.png?id=e51abf6a98a5b1f91e0f3a000f113e1a)
![Memento — Structură UML](https://refactoring.guru/images/patterns/diagrams/memento/structure1.png?id=4b4a42363a005b617d4df06689787385)

> **Analogie reală (refactoring.guru):** Un editor de text cu funcție Undo. Înainte de a efectua o operație, editorul salvează un „instantaneu" (snapshot) al stării curente. Dacă utilizatorul vrea să anuleze operația, editorul restaurează starea din snapshot. Provocarea e să nu expui detaliile interne ale editorului altor obiecte care gestionează istoricul.

**Cod relevant:** [`Curs/src/cts/curs/c12/memento/`](CTS_Curs_Complet.md#curssrcctscursc12mementoimplementarecontractjava) — `Contract` (Originator), `VersiuneContract` (Memento), `ManagerContracte` (CareTaker).

---

### 4.6 State

**Utilizare:** un obiect își schimbă **comportamentul** pe baza **stării interne** în care se află.

**Diferența State vs. Strategy** (capcană foarte frecventă — repetată intenționat aici): la **State**, schimbarea comportamentului e **internă/automată** (declanșată de tranziții de stare); la **Strategy**, clientul **alege explicit** algoritmul din exterior.

![State](https://refactoring.guru/images/patterns/content/state/state-en.png?id=c323fb8c54e2d57bebf4806c087afb07)
![State — Structură UML](https://refactoring.guru/images/patterns/diagrams/state/structure-en.png?id=caac48afbc4b2d95829cd7c7eb0dcacf)

> **Analogie reală (refactoring.guru):** Comportamentul unui smartphone în funcție de stare: când telefonul e deblocat, apăsarea butoanelor execută funcții diverse; când e blocat, orice buton duce la ecranul de deblocare; când bateria e descărcată, orice buton afișează ecranul de încărcare. Același obiect, comportament complet diferit în funcție de starea internă.

**Cod relevant:** [`Curs/src/cts/curs/c12/state/`](CTS_Curs_Complet.md#curssrcctscursc12stateimplementareastarejava) — `AStare` (interfață/abstract), `StareLiber`/`StareOcupat`, context `Bucatar` (comportament diferit în funcție de disponibilitate).

---

### 4.7 Template Method

**Utilizare:** este folosit atunci când un **algoritm este cunoscut** și urmează **anumiți pași preciși**, ficși, comuni mai multor implementări.

**Implementare:**
- În clasa abstractă, metoda template (ex. `generate()`) se declară **`final`** — astfel încât **NU poate fi suprascrisă** (împiedică subclasele să modifice **structura/ordinea** algoritmului).
- Pașii individuali (`loadData()`, `processData()`, `export()`) sunt declarați **`abstract`** — aceștia POT fi suprascriși de subclase, fiecare implementând propria logică pentru acel pas.
- Nu există nicio metodă separată care „apelează toate celelalte metode" altfel decât prin metoda template finală.

**De ce e `final` metoda template?** — Pentru a **împiedica modificarea structurii algoritmului** (a ordinii pașilor) de către subclase. Capcană: NU e despre performanță, NU e despre Singleton, ci strict despre protejarea secvenței de pași.

![Template Method](https://refactoring.guru/images/patterns/content/template-method/template-method.png?id=eee9461742f832814f19612ccf472819)
![Template Method — Structură UML](https://refactoring.guru/images/patterns/diagrams/template-method/structure.png?id=924692f994bff6578d8408d90f6fc459)

> **Analogie reală (refactoring.guru):** Construcția în serie a locuințelor. Un plan arhitectural tipic poate fi ușor modificat pentru a se potrivi nevoilor clientului. Fiecare fază — turnarea fundației, ridicarea structurii, construirea pereților, instalarea sistemelor — poate fi personalizată individual, dar ordinea și structura generală rămân fixe.

**Cod relevant:** [`Curs/src/cts/curs/c12/template/`](CTS_Curs_Complet.md#curssrcctscursc12templateimplementarepastejava) — `Preparat` (clasă abstractă cu metodă template), `Paste`/`Pizza` (subclase concrete care implementează pașii).

---

## 5. UNIT TESTING CU JUNIT

### 5.1 Concepte fundamentale

| Concept | Definiție |
|---|---|
| **Fixture** | Un **set de obiecte** utilizate în test. |
| **Setup** | Metoda/etapa de **definire** a fixture-ului, înainte de testare. |
| **Teardown** | Metoda/etapa de **distrugere** a fixture-ului, după terminarea testelor. |
| **Test Case** | O **clasă** ce definește fixture-ul pentru a rula mai multe teste. |
| **Test Suite** | O **colecție** de Test Cases. |
| **Assert** | O clasă **statică** ale cărei metode ajută la testarea codului. |
| **Test Runner** | **Instrument de rulare** a testelor (și de afișare a rezultatelor). |
| **Assertion** | Vezi Assert — clasă statică cu metode de testare (ex. `assertEquals`). |

**JUnit** = un framework ce permite realizarea și rularea de teste pentru diferite metode din cadrul proiectelor dezvoltate. Este cel mai folosit framework pentru testarea unitară a codului Java; reprezintă o **adaptare de la xUnit**. **JUnit 3** necesită JDK 1.2, **JUnit 4** necesită o versiune mai nouă decât JDK 5.

**Istoric JUnit** (din curs): Kent Beck a dezvoltat în anii '90 primul instrument de testare automată, **xUnit**, pentru Smalltalk. Beck și Gamma (unul din cei „Gang of Four") au dezvoltat **JUnit** în timpul unui zbor de la Zurich la Washington D.C. JUnit a devenit instrumentul standard pentru procesele **TDD** în Java și e componentă standard în multiple IDE-uri Java (Eclipse, BlueJ, JBuilder, DrJava, IntelliJ).

> **CORECȚIE IMPORTANTĂ — capcană frecventă de examen:** JUnit funcționează conform a **două design patterns: Composite și Command** (NU „Composite și Interpreter" — aceasta e o variantă-distractor greșită ce circulă). O clasă **TestCase reprezintă un obiect Command**, iar o clasă **TestSuite e compusă din mai multe instanțe TestCase sau TestSuite** (structură recursivă = Composite).

**Framework-uri de testare unitară pe limbaj** (tabel din curs — pot apărea în grile de tip „care framework e pentru Python/C++/etc."):

| Framework | Limbaj/scripting |
|---|---|
| JUnit | Java |
| PHPUnit | PHP |
| PyUnit | Python |
| CPPUnit | C++ |
| VBUnit | Visual Basic |
| DUnit | Delphi |
| cfcUnit | ColdFusion |
| HTMLUnit | HTML și JavaScript |
| JsUnit | JavaScript |
| dotUnit / NUnit | .NET / C#, ASP.NET |
| Ruby (framework nativ) | Ruby |
| XMLUnit | XML |
| ASPUnit | ASP |
| xUnit | C# |

**Motive pentru a folosi teste unitare** (din curs):
- Ușor de scris.
- Pot fi scrise **ad-hoc** atunci când ai nevoie de ele.
- Pe baza lor se pot defini colecții de teste — **Test Suites**.
- Pot fi rulate automat de fiecare dată când e nevoie — **„write once, use many times"**.
- Există multe framework-uri/instrumente ce simplifică scrierea și rularea.
- Reduc timpul pierdut pentru debugging și găsirea bug-urilor.
- Reduc numărul de bug-uri în codul livrat sau integrat.
- **Cresc rata bug-urilor identificate în faza de scriere a codului** (le prinzi mai devreme).

**Motive (greșite) pentru a NU folosi teste unitare** (capcană — aceste „motive" sunt prezentate critic în curs, nu sunt validate ca bune practici):
- „Codul scris de mine este corect!!!"
- „Nu am timp de teste, trebuie să implementez funcționalități, nu teste."
- „Nu e trecut în specificații că trebuie să facem teste." — *acesta e identificat explicit în grile ca „motivul pentru care NU folosești Unit Testing"*, fiind un răspuns greșit/o scuză, nu o practică validă.

### 5.2 Adnotări JUnit 4 vs. JUnit 5-Jupiter

| JUnit 4 | JUnit 5 (Jupiter) | Frecvență | Folosit pentru |
|---|---|---|---|
| `@Test` | `@Test` | per metodă | marchează o metodă ca test |
| `@Before` | `@BeforeEach` | înainte de **fiecare** test | setUp — pregătirea fixture-ului |
| `@After` | `@AfterEach` | după **fiecare** test | tearDown — distrugerea fixture-ului |
| `@BeforeClass` | `@BeforeAll` | **o singură dată**, înainte de toate testele clasei (metodă **static**) | setUpBeforeClass |
| `@AfterClass` | `@AfterAll` | **o singură dată**, după toate testele clasei (metodă **static**) | tearDownAfterClass |
| — | `@ParameterizedTest` | — | teste cu parametri multipli |
| — | `@RepeatedTest` | — | repetarea unui test de N ori |
| `try-catch` + `fail()` | `assertThrows` | — | testarea excepțiilor |

**Exemplu real din proiect (`UtilsTest.java`, stilul lui Robert):**
```java
@org.junit.Before
public void setUp() throws Exception {
    System.out.println("Apel setUp");
}

@org.junit.After
public void tearDown() throws Exception {
    System.out.println("Apel tearDown");
}

@BeforeClass
public static void setUpBeforeClass() throws Exception{
    System.out.println("Apel setupBeforeClass");
}

@AfterClass
public static void tearDownAfterClass() throws Exception{
    System.out.println("Apel tearDownAferClass");
}
```

### 5.3 Metode Assert frecvent testate la examen

**Lista completă de metode Assert din curs** (fiecare are și variantă cu parametru `message` opțional la început):

```
assertEquals(expected, actual)              assertEquals(message, expected, actual)
assertEquals(expected, actual, delta)       assertEquals(message, expected, actual, delta)
assertSame(expected, actual)                assertSame(message, expected, actual)
assertNotSame(expected, actual)             assertNotSame(message, expected, actual)
assertNull(object)                          assertNull(message, object)
assertNotNull(object)                       assertNotNull(message, object)
assertTrue(condition)                       assertTrue(message, condition)
assertFalse(condition)                      assertFalse(message, condition)
fail(message)
```

| Metodă | Verifică |
|---|---|
| `assertEquals(expected, actual)` | Egalitatea a două valori — compară prin **`.equals()`** |
| `assertEquals(message, expected, actual, delta)` | Egalitate pentru **valori reale** (double/float) — `delta` reprezintă **marja de eroare** (interval ±delta) |
| `assertNotNull(obj)` | Obiectul nu e null |
| `assertNull(obj)` | Obiectul **este** null |
| `assertTrue(condition)` / `assertFalse(condition)` | Condiție booleană |
| `assertSame(obj1, obj2)` | Cele **două obiecte se referă la aceeași instanță** — compară prin operatorul **`==`** (NU prin `.equals()` — aceasta e diferența exactă față de `assertEquals`) |
| `assertNotSame(obj1, obj2)` | Cele două obiecte **NU** sunt aceeași instanță |
| `assertArrayEquals(arr1, arr2)` | Testează **fiecare element din vector, unul câte unul**, prin metoda `.equals()` (NU doar dacă au aceeași lungime sau aceeași instanță) |
| `fail()` / `fail(message)` | Forțează eșecul testului (folosit când codul ajunge pe o ramură care NU ar trebui atinsă) |
| `@Test(timeout=100)` | Adnotare JUnit 4 pentru testarea **timpului** în care rulează o anumită metodă (în milisecunde) — folosită pentru testele de Performance |

**Tabel de corespondență JUnit ↔ NUnit** (apare în grile ca „echivalentul X din JUnit în NUnit este..."):

| JUnit | NUnit |
|---|---|
| `assertEquals` | `Assert.AreEqual` |
| (negația) | `Assert.AreNotEqual` |
| `assertSame` | `Assert.AreSame` |
| `assertNotSame` | `Assert.AreNotSame` |
| `assertNull` | `Assert.IsNull` |
| `assertNotNull` | `Assert.IsNotNull` |
| `assertTrue` | `Assert.IsTrue` |
| `assertFalse` | `Assert.IsFalse` |

> **Capcană de grilă:** `Assert.IsNotNull` NU există ca metodă **în JUnit/Java** (e sintaxă .NET/NUnit) — varianta corectă în Java e `assertNotNull`.
>
> **Capcană de grilă — diferența assertEquals vs. assertSame:** `assertEquals()` compară prin `.equals()`; `assertSame()` compară prin operatorul `==` (referință de obiect, nu valoare).

### 5.3bis Diferențe JUnit 3 vs. JUnit 4 (tabel complet din curs)

| Aspect | JUnit 3 | JUnit 4 |
|---|---|---|
| **Versiune JDK necesară** | Mai nouă decât JDK 1.2 | Mai nouă decât JDK 5 |
| **Moștenire obligatorie** | Clasele de test **trebuie** derivate din `TestCase` | **NU** e necesară moștenirea din `TestCase` |
| **Convenție de nume metode** | Metoda trebuie să respecte formatul **`testAAA`** (să conțină cuvântul „test" în nume) | Numele metodei **nu** e important — se marchează cu adnotarea **`@Test`** |
| **Timeout** | Nu există echivalent direct | `@Test(timeout=1000)` — valoarea e în **milisecunde** |
| **Excludere test din rulare** | Se șterge, comentează, sau se modifică numele să NU respecte `testAAA` | Se folosește adnotarea **`@Ignore`**, sau se șterge `@Test` |

**Adnotările exacte pentru skeleton JUnit 4** (corespondență metodă↔adnotare, capcană de grilă frecventă):
- `@BeforeClass` → pentru metoda `setUpBeforeClass()`
- `@AfterClass` → pentru metoda `tearDownAfterClass()`
- `@Before` → pentru metoda `setUp()`
- `@After` → pentru metoda `tearDown()`

> În JUnit 3, neexistând adnotări, numele metodelor `setUp()` și `tearDown()` erau **obligatorii** (convenție de nume, nu adnotare).

### 5.3ter Test Suite, Categorii și adnotări de grupare

- **Test Suite** = o **colecție de cazuri de testare (Test Cases)** destinate să fie folosite pentru a testa un program software (poate conține orice tip de teste, vizuale sau nefuncționale).
- Adnotările specifice unei suite JUnit 4: **`@RunWith(Suite.class)`**, **`@Suite.SuiteClasses({...})`**, și pentru filtrare pe categorii: **`@RunWith(Categories.class)`** + **`@Categories.IncludeCategory(X.class)`**.
- **`@Category(X.class)`** se aplică pe metode de test individuale, pentru a le grupa logic (ex: categoria `A` vs. categoria `B`), astfel încât o suită să poată rula **doar** testele dintr-o categorie specifică.

**Cod relevant din proiect:** [`Curs_JUnit/src/cts/junit/c14/suite/AllTestsSuita1.java`](CTS_Curs_Complet.md#curs_junitsrcctsjunitc14suitealltestssuita1java), `Suita2.java`, `categories/A.java`, `categories/AA.java`, `categories/B.java`, `testare/AutostradaTestMock.java` (folosește `@Category(A.class)` și `@Category(B.class)` pe metode diferite din aceeași clasă).

### 5.4 WhiteBox vs. BlackBox Testing

Citate din curs: *„Testarea este utilizată pentru a semnala prezența defectelor, dar nu garantează absența acestora"* (Dijkstra).

**Cauzele erorilor software** (procentaje exacte predate la curs):
- Erori de **specificații** — **55%** (cauza cu ponderea cea mai mare!)
- Erori de **proiectare** — **30%**
- Erori de **programare** — **15%**

> **Capcană de grilă frecventă:** „cauza erorilor software cu ponderea cea mai mare" → răspunsul corect e **erori de specificații (55%)**, NU erori de programare.

| | WhiteBox | BlackBox |
|---|---|---|
| **Alte denumiri** | Clear Box Testing, Code-Based Testing, **testare structurală** | **Testare comportamentală** |
| **Cunoștințe necesare** | Cunoști arhitectura/structura internă a aplicației | NU cunoști arhitectura internă — doar input/output |
| **Necesită programare?** | Da | **NU** — testerul nu trebuie să știe programare, limbajul de dezvoltare sau structura codului |
| **Profunzime** | Testare aprofundată, acoperă mai multe posibilități | Testare la nivel de utilizator final |

> **Capcană de grilă:** „Open Box Testing" și „Glass Box Testing" sunt **distractori** — singurele denumiri valide pentru WhiteBox sunt **Clear Box** și **Code-Based**.

### 5.5 Principii de testare: Right-BICEP

**Right-BICEP** este descris explicit în curs drept **„cel mai cunoscut principiu de testare"**.

| Literă | Sub-principiu | Detaliu |
|---|---|---|
| **R** | Right | **Primul lucru** care trebuie verificat când testăm o metodă: **oferă rezultatele corecte?** Această verificare se face **fără** a ține cont de specificațiile proiectului (verifică strict corectitudinea matematică/logică a output-ului). |
| **B** | Boundary | Testare **PE limitele** intervalelor — **verificarea corectitudinii valorilor limită** (nu „testarea pe interiorul" și nu „testarea în afara" intervalelor ca definiție separată — capcană frecventă, răspunsul corect e mereu strict despre limite). |
| **I** | Inverse relationship | Verificare **în mod invers, pornind de la rezultat** — se ajunge înapoi la aceeași intrare de la care s-a început (ex: alimentare + retragere = sold inițial). |
| **C** | Cross-check | Se poate utiliza **o altă metodă** pentru rezolvarea/verificarea problemei testate de metoda nou implementată — verificare **încrucișată** cu o sursă independentă. |
| **E** | Error conditions | Trebuie testate și **situațiile în care aplicația ar putea „crăpa"** — verifică dacă metodele **tratează o eroare** sau oferă o excepție corespunzătoare. |
| **P** | Performance | **Pe lângă** testarea corectitudinii rezultatelor, e important să se verifice **performanța procesării** — atât din punctul de vedere al **resurselor consumate**, cât și al **timpului necesar** pentru obținerea rezultatelor. Se efectuează când input-ul/rezultatul e o listă sau un număr foarte mare de elemente. În JUnit 4, se poate testa cu adnotarea **`@Test(timeout=100)`** (timeout în milisecunde). |

> **Capcană frecventă**: o variantă de răspuns afirmă greșit că „verificarea performanței se face DOAR din perspectiva resurselor, NU și a timpului" (sau invers) — corect e că performanța înglobează **ambele** aspecte simultan.

### 5.6 Principii de testare: CORRECT

Fiecare sub-principiu CORRECT are o întrebare-cheie pe care testerul trebuie să și-o pună. Acest principiu e folosit și pentru a stabili **condițiile limită** pentru testele de **Boundary** din Right-BICEP.

| Literă | Sub-principiu | Detaliu |
|---|---|---|
| **C** | Conformance | Cunoscut și ca **Compliance testing**, **Type testing**, **Conformity assessment** (capcană: „Structural Testing" NU e sinonim valid). Se aplică în domenii unde ceva trebuie să respecte **standarde/formate specifice**. Pentru orice intrare și ieșire trebuie verificată conformitatea cu un format/standard. Testele verifică: ce se întâmplă dacă datele de intrare NU sunt conforme cu formatul, și dacă rezultatul obținut e conform cu formatul specific proiectului. |
| **O** | Ordering | Specific **listelor, dar nu numai**. Verifică dacă **ordinea articolelor** este cea dorită; sau cum se comportă metoda dacă primește parametri într-o **altă ordine** decât cea așteptată. |
| **R** | Range | Pentru valorile de intrare/ieșire sunt setate **anumite intervale** — testat pentru toate aceste intervale. Pentru funcțiile cu **index**, trebuie verificat explicit: (1) valorile inițiale și finale ale indexului au aceeași valoare; (2) primul element e mai mare/mai mic decât ultimul; (3) ce se întâmplă dacă indicele e **negativ**; (4) ce se întâmplă dacă indicele e mai mare decât **limita superioară**; (5) numărul de articole nu corespunde cu dimensiunea dorită. |
| **R** | References | Metode care depind de lucruri/obiecte **externe** (precondiții) — ex: o aplicație web necesită conectarea utilizatorului; o extragere dintr-o stivă funcționează doar dacă există elemente în stivă. Aceste elemente externe se numesc **precondiții**/**condiții preliminare**. Testele de References se realizează **folosind dubluri de test** (stub, fake, dummy, mock). |
| **E** | Existence | Întrebarea cheie: **„does some given thing exist?"** — ce se întâmplă cu metoda dacă un parametru **nu există, e null sau e 0**? Pentru aplicații cu fișiere/conexiune la internet, se verifică existența fișierului/disponibilitatea conexiunii — aplicația NU trebuie să dea eroare necontrolată, ci să avertizeze utilizatorul normal. Citat din curs: **„Make sure your method can stand up to nothing."** Este **asemănătoare cu Error conditions din Right-BICEP**. |
| **C** | Cardinality | Regula **„0-1-n"**. Similar cu Existence și Range. Se verifică dacă metoda/lista/colecția are **0 elemente, 1 element sau n elemente**. Dacă funcționează pentru 2-3-4 elemente, se presupune că va funcționa pentru mai multe — dar nu trebuie ignorat testul de **Boundary superior**. |
| **T** | Time | **Similar cu testul de Performance din Right-BICEP.** Verifică dacă **șablonul de apeluri** e respectat — similar conceptual cu design pattern-ul **Template Method**. Exemplu din curs: pentru a apela `logout()`, trebuie mai întâi apelată `conectare()`. |

> **Diferența Time (CORRECT) vs. Performance (Right-BICEP)** — capcană foarte frecventă: Time verifică **apelarea metodelor la momentul/secvența potrivită** (ordinea corectă a apelurilor); Performance verifică **timpul necesar + resursele consumate** pentru a obține rezultatul (durată/eficiență), nu ordinea apelurilor.

> **Acronim complet CORRECT** (ordinea exactă cerută în grile): **C**onformance, **O**rdering, **R**ange, **R**eferences, **E**xistence, **C**ardinality, **T**ime.

### 5.7 Principiul FIRST

Citat din curs: *„Pentru ca testele unitare să fie utile și eficiente pentru echipa de programare, trebuie să vă amintiți să le faceți FIRST."*

| Literă | Înseamnă | Detaliu din curs |
|---|---|---|
| **F**ast | Rapid | Testul ar trebui să fie rapid — dacă avem prea multe teste, nu trebuie să așteptăm mult timp la execuție. |
| **I**solated (= **Independent**) | Izolat/Independent | Corespunde conceptului de **Single Responsibility din SOLID** — *„Each unit test should have a single reason to fail."* Când un test eșuează, dezvoltatorul **NU** trebuie să facă debug pentru a identifica ce e greșit — testul ar trebui să fie izolat și să spună **exact** unde și care e problema. |
| **R**epeatable | Repetabil | Rezultatele obținute ar trebui să fie **identice** indiferent de numărul de rulări. Testele se desfășoară repetat, **fără alte intervenții**. |
| **S**elf-Validating | Auto-validant | Vizează **încrederea** în testele implementate. Dacă testele trec, dezvoltatorul are mare încredere că codul e corect. **Dacă un test NU trece, dezvoltatorul trebuie să aibă încredere că METODA trebuie îmbunătățită — nu să considere că testul e greșit.** |
| **T**imely | La timp | Întrebări-cheie din curs: *„Când trebuie să punem în aplicare testele pentru metoda noastră? Când considerăm că am făcut toate testele?"* — testul se scrie la timp, nu mult după implementarea codului. |

> **Capcană de grilă pe Isolated**: „testul poate fi repetat și pentru alte metode" este FALS pentru Isolated (asta ar fi mai degrabă Repeatable) — Isolated e despre faptul că testul nu necesită debug, fiind clar și de sine stătător în identificarea problemei.

### 5.8 TDD — Test Driven Development

**Dezvoltarea pe baza testelor** — citat din curs: *„Este exact modul de gândire al oamenilor pentru realizarea metodelor."* **Testele se scriu ÎNAINTE de cod**, nu invers.

**Ciclul TDD (pașii exacți, capcană de grilă pe ordine/denumire):**
1. **Scrie și rulează testul** (care la început va pica, fiindcă codul încă nu există).
2. **Corectează/implementează metoda** astfel încât testul să treacă.
3. **Refactorizează** codul, păstrând testul verde.

> **Capcană de grilă:** „dacă testul generează `fail`, se corectează **testul**" este o afirmație **greșită** despre TDD — în TDD, dacă testul pică, se corectează/implementează **metoda** (codul), nu testul (vezi și principiul Self-Validating din FIRST, aceeași logică).

Beneficii: poate îmbunătăți design-ul codului (mai ales combinat cu TDD explicit), reduce nivelul de bug-uri din codul de producție, facilitează refactoring-ul/schimbarea codului mai ușor.

### 5.9 Avantajele testelor unitare

- Pot fi rulate automat de fiecare dată când e nevoie.
- Reduc timpul pierdut cu debugging-ul și găsirea bug-urilor.
- Pe baza lor se pot defini **suite de teste**.
- Respectă principiul **„write once, use many times"**.
- Fiecare test validează **un singur comportament** din aplicație.

### 5.10 Pattern de testare a excepțiilor (stilul exact din proiectul lui Robert)

```java
@Test
public void testCcSubLimita() {
    Masina masina = null;
    try {
        masina = new Masina("Dacia", 200, "Romania");
        fail("Nu aruncă excepție pe cc < 1000");
    } catch (ExceptieConstructor e) {
        assertTrue(true); // comportamentul așteptat
    }
}
```

**Capcana clasică de examen:** dacă blocul `catch` prinde un tip de excepție **diferit** de cel aruncat efectiv de metodă, testul **NU pică cu un `fail()` controlat** — pică cu o **eroare necontrolată** (excepția se propagă, fiindcă niciun catch nu o prinde). Exemplu real din `UtilsTest.java`:

```java
@org.junit.Test
public void maxPar2() {
    List<Integer> lista = null;
    try {
        int rezultat = Utils.maxPar(lista);
        fail("Nu arunca nicio exceptie cand lista e nula");
    } catch (ExceptieListaGoala e) {
        assertTrue("Arunca exceptie buna pe lista nula", true);
    } catch (ExceptieValoarePara e) {
        assertTrue("Arunca exceptie gresita pe lista nula", false);
    }
}
```
Aici sunt prinse **ambele** tipuri de excepție posibile, dar testul e scris să verifice explicit care din cele două a fost aruncată (succes doar dacă e `ExceptieListaGoala`).

---

## 6. DUBLURI DE TEST (TEST DOUBLES)

Citat din curs: *„În testarea automată este obișnuită folosirea obiectelor care arată și se comportă ca echivalentele lor de producție, dar sunt de fapt simplificate. Acest lucru reduce complexitatea, permite verificarea codului independent de restul sistemului."* O **dublură de testare** = un obiect care se potrivește cu interfața colaboratorului necesar și **poate fi trecut în locul său** (capcană: NU „nu poate fi trecut în locul său" — exact opusul e corect).

| Tip | Descriere exactă din curs |
|---|---|
| **Dummy Object** | Un obiect care **respectă interfața**, dar metodele **nu fac nimic** sau returnează `0`/`null`. Se folosește când avem nevoie de obiectul real ca parametru obligatoriu, dar **NU trebuie apelate metodele lui** — pentru că nu fac nimic relevant. |
| **Stub** | Spre deosebire de Dummy, metodele dintr-un Stub **întorc răspunsuri conservate/hardcodate** (comportament fix, predefinit). |
| **Spy** | Este un **Stub** (sau Fake) care **gestionează și contorizează numărul de apeluri** ale metodelor sale. |
| **Fake** | Un obiect care se comportă **asemănător cu unul real**, dar are o versiune **simplificată**, cu valori configurabile. |
| **Mock Object** | „Diferit de toate celelalte" — comportament **controlat**, folosit pentru **Mock Testing**: metoda testată NU trebuie să fie influențată de dependențe externe reale (bază de date, rețea, etc.). |

**Cod relevant din proiect:** [`Curs_JUnit/src/cts/junit/c14/mock/`](CTS_Curs_Complet.md#curs_junitsrcctsjunitc14mockautostradajava) — `MasinaMock`, `VremeMock`, `IMasina`/`IVreme` (interfețe), `TestareCuMock.java`, `AutostradaTestMock.java`.

---

## 7. GIT

### Comenzi esențiale

| Comandă | Etapă/Scop |
|---|---|
| `git init` | Inițializare repository |
| `git clone` | **Descărcare proiect** — crearea unei copii locale a proiectului de pe Repo-ul principal |
| `git add` | Adăugarea unui fișier nou în **track** |
| `git commit -m "..."` | Salvarea modificărilor (local) |
| `git push` | Trimiterea modificărilor spre server |
| `git pull` | **Copiază modificările** aflate pe server, pe mașina de lucru locală |
| `git status` | Starea curentă a proiectului |
| `git log` | Istoricul de commit-uri |
| `git branch` | Listă de ramuri (locale); `git branch -a` = **locale + remote** |
| `git checkout <branch>` | Schimbare branch; `git checkout -b <branch>` = creare + schimbare simultană |
| `git merge` | Unire versiuni |
| `git revert` | Revenire la o versiune anterioară (pe un fir de dezvoltare) |
| `git fetch` | Descărcare informații despre modificările de pe remote, fără a le aplica |

### Concepte

| Concept | Definiție |
|---|---|
| **Repository** | Arhiva (locală sau remote) a unui proiect și a istoricului de modificări |
| **Working Copy** | Copia locală de lucru a proiectului |
| **Branch** | Ramură secundară de dezvoltare, pe lângă `master`/`main` |
| **Stash** | „Sertar" temporar pentru modificări nesalvate definitiv |
| **Conflict** | Situație în care două modificări concurente nu pot fi unite automat |
| **Merge** | **Procesul de unire** a două sau mai multe versiuni de lucru |

---

## 8. CHEAT SHEET — CAPCANE FRECVENTE LA EXAMEN

Aceasta e o listă de distincții care apar constant ca întrebări „trick" în grile (`GrileTotTotTot.pdf` și `Grile_Examen2026_CTS.pdf`):

1. **GoF are EXACT 3 categorii**: Creaționale, Structurale, Comportamentale. „**Arhitecturale**" e răspunsul greșit clasic la „care categorie NU e prezentată în Cartea celor 4".

2. **Adapter vs. Decorator**: Adapter NU adaugă funcționalitate (doar schimbă interfața); Decorator adaugă funcționalitate (păstrând interfața).

3. **Proxy vs. Decorator**: Proxy controlează/restricționează accesul; Decorator adaugă funcționalitate.

4. **Prototype vs. Flyweight**: Prototype optimizează **viteza** (clonare); Flyweight optimizează **memoria** (reutilizare). Prototype = Creațional; Flyweight = Structural.

5. **Strategy vs. State**: la Strategy clientul **alege explicit** algoritmul; la State schimbarea e **internă/automată**, declanșată de starea obiectului.

6. **Template Method**: metoda template e `final` (NU poate fi suprascrisă — protejează ordinea pașilor); pașii individuali sunt `abstract` (POT fi suprascriși).

7. **Memento — exact 3 participanți**: Memento, Originator, CareTaker (nu mai puțini, nu „AbstractMemento" suplimentar).

8. **Command — exact 4 participanți**: Command (interfață), comenzi concrete, Invoker, Receiver.

9. **Decorator — exact 4 participanți**: AbstractProduct, ConcreteProduct, AbstractDecorator, ConcreteDecorator.

10. **Observer — relație 1:n, NU 1:1**. ObservabilConcret/ObservatorConcret = clasele CONCRETE (nu abstracte) care gestionează lista, respectiv definesc observatorii.

11. **WhiteBox = Clear Box / Code-Based** (testare structurală); **BlackBox** = testare comportamentală, NU necesită cunoștințe de programare.

12. **Time (din CORRECT)** ≠ **Performance (din Right-BICEP)**: Time = ordinea/secvența apelurilor; Performance = durata/resursele consumate.

13. **Singleton Lazy Initialization NU e thread-safe** by default — varianta thread-safe necesită sincronizare explicită sau Inner Static Helper Class.

14. **Enum Singleton NU permite Lazy initialization** și e dificil de testat/mock-uit.

15. **Excepția greșit prinsă în `catch`** la un test JUnit NU duce la un `fail()` controlat — duce la o **eroare necontrolată** (excepția se propagă nefiind prinsă).

16. **`assertSame`** verifică **aceeași referință de obiect**, NU doar egalitate de valoare (asta e `assertEquals`).

17. **System Hungarian Notation** = tipul de dată în nume (`strNume`); **Apps Hungarian Notation** = scopul/rolul în nume (`btnSubmit`) — NU invers.

18. **YAGNI e derivat din KISS** — întrebare frecventă „care principiu e derivat din KISS?" → YAGNI (NU DRY, NU SOLID).

19. **Zombie code** = cod comentat nefolosit (NU legacy code, NU cod cu TODO-uri).

20. **One Screen Rule** = evitarea metodelor cu peste 20 de linii de cod (NU despre numărul de parametri — aceea e altă regulă separată, max 2 parametri).

21. **Builder NU e despre familii de obiecte** (asta e Abstract Factory) — Builder e despre obiecte cu multe atribute opționale/obligatorii.

22. **Facade și Adapter — ambele sunt wrappere**, dar Facade simplifică un subsistem complex, în timp ce Adapter face compatibile interfețe incompatibile.

23. **Simple Factory cu `if`/`equals` în cascadă** → încalcă OCP, necesită modificarea fabricii la adăugare de tip nou, risc de `return null`.

24. **JUnit funcționează conform pattern-urilor Composite & Command** (NU „Composite & Interpreter" — capcană circulantă greșită; TestCase = obiect Command, TestSuite = structură Composite de TestCase/TestSuite).

25. **`@BeforeClass`/`@AfterClass`** sunt metode **`static`** și rulează **o singură dată** per clasă de test (nu per metodă de test, ca `@Before`/`@After`).

26. **Cauza erorilor software cu ponderea cea mai mare = erori de specificații (55%)**, NU erori de programare (15%) sau de proiectare (30%) — capcană frecventă care inversează ordinea.

27. **Time (CORRECT) vs. Existence (CORRECT) vs. Error Conditions (Right-BICEP)**: Existence e descrisă explicit în curs ca **„asemănătoare cu condiția de eroare din Right-BICEP"** — nu sunt identice, dar foarte înrudite conceptual (ambele despre „ce se întâmplă în cazuri degenerate/absente").

28. **Right-BICEP — primul pas de testare** = verificarea că metoda oferă rezultate corecte (litera R = Right), făcută **fără** a ține cont strict de specificațiile proiectului (verifică corectitudinea logică brută).

29. **Componentele unui design pattern sunt 7**: nume, problemă, structură, participanți, implementare, utilizări, corelații. „Refactoring" NU e o componentă a unui pattern — e o tehnică separată de Clean Code.

30. **Dezavantajul real al design patterns** e că „irosesc timp cu etapa de analiză" — NU că „timpul de analiză e redus" (capcană prin inversare de sens).

31. **TDD — la eșecul testului se corectează METODA (codul), nu testul** — exact ca la principiul Self-Validating din FIRST.

32. **Dubla de testare „poate fi trecută în locul colaboratorului real"** — definiția corectă include explicit această capacitate de substituire; varianta „NU poate fi trecută în locul său" e un distractor.

33. **Bridge e Structural** (nu Comportamental); **Chain of Responsibility e Comportamental** (nu Structural) — confuzii frecvente pe pattern-uri menționate teoretic dar fără cod de exemplu explicit (Bridge, Iterator, Interpreter, Mediator, Visitor).
