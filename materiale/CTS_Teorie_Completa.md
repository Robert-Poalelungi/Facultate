# 📚 CTS — Teorie Completă pentru Examen
### Calitate și Testare Software — ASE București
> Acoperă 100% din grilele din fișierul de examen

---

## CUPRINS

1. [Unit Testing — Concepte de bază](#1-unit-testing--concepte-de-bază)
2. [JUnit — Framework de testare](#2-junit--framework-de-testare)
3. [Tipuri de testare: BlackBox vs WhiteBox](#3-tipuri-de-testare-blackbox-vs-whitebox)
4. [Right-BICEP](#4-right-bicep)
5. [CORRECT — Condiții limită](#5-correct--condiții-limită)
6. [Dubluri de testare (Test Doubles)](#6-dubluri-de-testare-test-doubles)
7. [Principiul FIRST](#7-principiul-first)
8. [TDD — Test Driven Development](#8-tdd--test-driven-development)
9. [Clean Code](#9-clean-code)
10. [Design Patterns — Introducere](#10-design-patterns--introducere)
11. [Design Patterns Creaționale](#11-design-patterns-creaționale)
12. [Design Patterns Structurale](#12-design-patterns-structurale)
13. [Design Patterns Comportamentale](#13-design-patterns-comportamentale)
14. [GIT — Control versiuni](#14-git--control-versiuni)

---

## 1. Unit Testing — Concepte de bază

### Ce este Unit Testing?
- O **secvență de cod** scrisă de un programator pentru a evalua o clasă sau o metodă
- Testează **individual** o componentă, parte de cod, clasă sau metodă
- Se realizează **în faza de dezvoltare** și este un instrument destinat programatorilor
- Evaluează modul de funcționare al unei metode **într-un context bine definit**
- Metodă **simplă și rapidă** de testare a codului sursă

### De ce folosim Unit Testing?
- Testele pot fi **rulate automat** de fiecare dată când e nevoie
- **Reduc timpul** pierdut pentru debugging și găsirea bug-urilor
- Testele sunt **ușor de scris**
- Se pot defini **suite de teste**
- Respectă principiul **write once, use many times**
- Pe baza lor se pot defini **colecții de teste**

### Ce este testarea?
- Este utilizată pentru a **semnala prezența defectelor**
- NU garantează **absența defectelor**
- NU este procesul de modificare a erorilor și defectelor

### Concepte fundamentale

| Concept | Definiție |
|---------|-----------|
| **Fixture** | Set de obiecte utilizate în test |
| **Setup** | Metodă/etapă de definire a setului de obiecte utilizate (Fixture) **înainte** de testare |
| **Teardown** | Metodă/etapă de **distrugere** a obiectelor (Fixture) după terminarea testelor |
| **Test Case** | Clasă ce definește setul de obiecte (Fixture) pentru a rula mai multe teste |
| **Test Runner** | Instrument de rulare al testelor |
| **Test Suite** | Colecție de cazuri de testare (TestCase-uri grupate și rulate împreună) |
| **Assertion** | Clasă statică ale cărei metode ajută la testarea codului |

### Cauza erorilor software
- **Ponderea cea mai mare**: erori de **specificații**
- Urmate de: erori de proiectare, erori de programare

---

## 2. JUnit — Framework de testare

### Ce este JUnit?
- **Framework** ce permite realizarea și rularea de teste pentru diferite metode din cadrul proiectelor
- Cel mai folosit framework pentru testarea unitară a codului scris în **Java**
- Reprezintă o adaptare de la **xUnit** (NU invers — xUnit NU este adaptare la JUnit!)
- Funcționează conform a două design patterns: **Composite** și **Command**
- O clasă TestCase reprezintă un obiect al design pattern-ului **Command**

### Structura unui test JUnit — Pattern AAA
```java
@Test
public void numeTest() throws ExceptieChecked {
    // ARRANGE — pregătești datele
    Masina masina = new Masina("BMW", 2000, "Germania");

    // ACT + ASSERT
    assertEquals("Mesaj eroare", valoareAsteptata, valoareReala);
}
```

### Adnotări JUnit 4 (cele din fișierele de laborator)

| Adnotare JUnit 4 | Când rulează | De câte ori | static? |
|-----------------|--------------|-------------|---------|
| `@BeforeClass` | Înainte de TOATE testele | 1 | ✅ DA |
| `@Before` | Înainte de FIECARE test | N | ❌ NU |
| `@Test` | Marchează metoda ca test | — | ❌ NU |
| `@After` | După FIECARE test | N | ❌ NU |
| `@AfterClass` | După TOATE testele | 1 | ✅ DA |

**Metode automate skeleton:**
- `@BeforeClass` → `setUpBeforeClass()`
- `@Before` → `setUp()`
- `@After` → `tearDown()`
- `@AfterClass` → `tearDownAfterClass()`

### Adnotări JUnit 5 — Jupiter (echivalente)

| JUnit 4 | JUnit 5 (Jupiter) |
|---------|-------------------|
| `@BeforeClass` | `@BeforeAll` |
| `@Before` | `@BeforeEach` |
| `@After` | `@AfterEach` |
| `@AfterClass` | `@AfterAll` |

**Adnotare prezentă în JUnit5 dar NU în JUnit4:** `@AfterEach`

**`@BeforeAll` trebuie executată înainte de:** `@Test`, `@RepeatedTest`, `@ParameterizedTest`, `@TestFactory`

### Adnotări pentru TestSuite (JUnit 4)
- `@RunWith`
- `@SuiteClasses`
- `@Category`

### Metode Assert

| Metodă | Ce face |
|--------|---------|
| `assertEquals(asteptat, real)` | Verifică egalitate prin `.equals()` |
| `assertSame(obj1, obj2)` | Verifică dacă 2 obiecte referă același obiect (operator `==`) |
| `assertTrue(conditie)` | Verifică că e `true` |
| `assertFalse(conditie)` | Verifică că e `false` |
| `assertNotNull(obiect)` | Verifică că nu e `null` |
| `assertNull(obiect)` | Verifică că e `null` |
| `assertArrayEquals(arr1, arr2)` | Testează fiecare element din vector prin `.equals()` |
| `fail(mesaj)` | Forțează picarea testului |

> ⚠️ **assertEquals vs assertSame:** `assertEquals` compară prin `.equals()`, `assertSame` compară prin `==`

> ⚠️ **assertEquals(message, expected, actual, delta):** `delta` = marja de eroare pentru valori reale (interval ±delta)

> ⚠️ **NU există în JUnit:** `Assert.IsNotNull` (aceasta e din .NET)

> ⚠️ **Ordinea parametrilor:** `assertEquals(ASTEPTAT, REAL)` — primul e așteptat, al doilea e real!

### @Test(timeout=100)
- Folosit pentru **testarea timpului** în care rulează o anumită metodă (în milisecunde)
- NU oprește metoda la 100ms — **testează** dacă se termină în 100ms

### Testarea excepțiilor (JUnit 5)
- `assertThrows` — pentru testarea condițiilor de eroare în JUnit 5

### Ordinea execuției lifecycle (exemplu cu 2 teste):
```
setUpBeforeClass()     ← @BeforeClass (o dată)
setUp()                ← @Before (test 1)
test1()
tearDown()             ← @After (test 1)
setUp()                ← @Before (test 2)
test2()
tearDown()             ← @After (test 2)
tearDownAfterClass()   ← @AfterClass (o dată)
```

### Complexitatea ciclomatică
Formula: **M = A - N + 2**
- A = numărul de muchii (arce)
- N = numărul de noduri

---

## 3. Tipuri de testare: BlackBox vs WhiteBox

### BlackBox Testing

**Ce este:**
- Testarea **comportamentală** (mai este numită testare comportamentală)
- Testerul cunoaște **doar datele de intrare și datele de ieșire** ale aplicației
- Persoanele care testează **nu cunosc arhitectura internă** a aplicației testate
- Mai este cunoscută ca: **Glass Box Testing** ❌ (NU — asta e WhiteBox!)

**Avantaje BlackBox:**
- Testerul nu trebuie să știe **programare, limbajul folosit sau structura de cod**
- Testele sunt realizate din **punctul de vedere al utilizatorului**
- Testerul cunoaște doar datele de intrare și ieșire

**Dezavantaje BlackBox:**
- Testele vor avea un număr **mare** de intrări
- Testele pot fi **redundante** cu alte teste realizate de dezvoltator

### WhiteBox Testing

**Ce este:**
- Mai este cunoscut și sub numele de: **Structural Testing**, **Clear Box Testing**, **Open Box Testing**, **Glass Box Testing** (toate sunt corecte!)
- Testarea **structurală**
- Persoanele care testează **cunosc arhitectura internă** a aplicației

**Avantaje WhiteBox:**
- Testarea este mai **aprofundată**, cu posibilitatea de a acoperi cele mai multe cazuri
- Poate fi efectuată **într-o etapă anterioară** punerii în funcțiune a aplicației

**Dezavantaje WhiteBox:**
- Sunt necesare **resurse de înaltă calificare**, cu cunoaștere aprofundată a programării
- Testele pot fi redundante cu alte teste

### Tabel comparativ

| | BlackBox | WhiteBox |
|---|---|---|
| **Cunoaște arhitectura** | NU | DA |
| **Perspectivă** | Utilizator | Dezvoltator |
| **Alt nume** | Comportamentală | Structurală / Clear Box / Open Box / Glass Box |
| **Număr intrări** | Mare | Mic (mai controlat) |
| **Poate începe înainte de finalizare** | NU | DA |

> **Open Box Testing** = altă denumire pentru **WhiteBox Testing**

---

## 4. Right-BICEP

### Ce este Right-BICEP?
- **Cel mai cunoscut principiu de testare** (NU "cel mai urât scenariu")
- Este un **principiu de testare** (nu suite case, nu tipuri de teste, nu reguli de programare)
- Acronim pentru 6 principii de testare

### Cele 6 principii

| Literă | Principiu | Ce verifică |
|--------|-----------|-------------|
| **R** (Right) | **Corectitudinea** | Dacă rezultatele furnizate de metodă sunt corecte. **Primul lucru** de verificat când testăm o metodă |
| **B** (Boundary) | **Limitele** | Testele pe limitele intervalelor (boundary test) |
| **I** (Inverse Relationship) | **Relații inverse** | Pornind de la rezultat, trebuie să se ajungă la aceeași intrare inițială |
| **C** (Cross-Check) | **Verificare încrucișată** | Utilizarea altei metode pentru testarea/verificarea metodei nou implementate |
| **E** (Error Conditions) | **Condiții de eroare** | Simularea și forțarea obținerii erorilor; testarea dacă metodele tratează o eroare sau oferă o excepție |
| **P** (Performance) | **Performanță** | Verificarea performanței procesării (timp + resurse consumate) |

### Detalii pe principii

**RIGHT:**
- Primul lucru pe care trebuie să-l facem când testăm o metodă = verificăm că metoda oferă **rezultatele corecte**

**BOUNDARY:**
- Testele pe **limitele intervalelor** (nu în interior, nu în afara)
- Se determină intervalul în care pot fi valorile parametrilor de intrare
- Testele se fac pentru limitele inferioare și superioare
- ❌ NU: "testele pe limitele intervalelor și în afara acestora" (aceea e Range din CORRECT)

**INVERSE RELATIONSHIP (I):**
- Anumite metode pot fi testate prin aplicarea **regulii inverse**
- Ex: dacă testezi `sqrt(x)`, verifici că `rezultat² = x`

**CROSS-CHECK (C):**
- Se poate utiliza o **altă metodă** pentru rezolvarea problemei, pentru verificarea metodei nou implementate
- Se aplică când metoda implementată a fost concepută pentru a crește productivitatea
- ❌ NU confunda cu Inverse Relationship!

**ERROR CONDITIONS (E):**
- Trebuie să testăm și situațiile în care **aplicația ar putea crăpa**
- Testarea realizată pentru a verifica dacă metodele **tratează o eroare sau oferă o excepție**
- Testarea de forțare a erorilor se face pentru **toate metodele** (nu doar pentru unele)

**PERFORMANCE (P):**
- Verificarea se face din punctul de vedere al **resurselor consumate** și **timpului** necesar
- Se aplică metodelor cu input/output reprezentat de o listă sau număr **foarte mare** de elemente

### Exemplu Fibonacci și Right-BICEP
- Test pentru `getFibonacciNumber(2)` → test de tip **Right**
- Test folosind funcția inversă (dacă fib(n-1) + fib(n-2) = fib(n)) → test de tip **Inverse Relationship**
- Test folosind altă librărie pentru verificare → **Cross-Check**

---

## 5. CORRECT — Condiții limită

### Ce este CORRECT?
Acronim pentru: **Conformance, Ordering, Range, References, Existence, Cardinality, Time**

> ⚠️ **NU este:** Cross-check, Errors, Experience, Cleanliness, Rapidity

### Cele 7 sub-principii

| Literă | Principiu | Ce verifică |
|--------|-----------|-------------|
| **C** | Conformance | Conformitatea cu un format/standard |
| **O** | Ordering | Ordinea elementelor (pentru liste) |
| **R** | Range | Intervalele valorilor de intrare și ieșire |
| **R** | References | Dependențele externe ale metodei |
| **E** | Existence | Existența parametrilor (null, 0) |
| **C** | Cardinality | Numărul de elemente (0, 1 sau n) |
| **T** | Time | Momentul și ordinea apelurilor |

### Detalii pe sub-principii

**CONFORMANCE (C):**
- Mai este cunoscut și sub numele de **Compliance testing**
- Verifică dacă datele trebuie să îndeplinească anumite **standarde sau formate**
- Pentru orice intrare și ieșire, trebuie să se verifice **conformitatea cu un format**
- Testele verifică și ce se întâmplă dacă datele de intrare **nu sunt conforme** cu formatul

**ORDERING (O):**
- Specific în special **listelor**
- Verifică dacă **ordinea** articolelor este cea dorită (ex: sortare crescătoare)

**RANGE (R):**
- Pentru valorile de intrare și de ieșire sunt setate anumite **intervale**
- Testele Range implică testarea pe **limitele intervalelor, în interiorul acestora și în afara lor** (toate 3!)
- Toate funcțiile cu **index** trebuie testate pentru interval
- Se verifică: dacă primul element e mai mic/mare decât ultimul, dacă valorile inițiale/finale pentru index au aceeași valoare

**REFERENCES (R):**
- Anumite metode depind de **lucruri externe / obiecte externe** metodei testate
- Acestea trebuie **verificate și controlate** (sunt precondițiile)
- Testele Reference se realizează prin **dubluri de test** (stub, fake, dummy, mock)
- Ex: extragerea dintr-o stivă → trebuie verificat dacă există **elemente în stivă**

**EXISTENCE (E):**
- Trebuie să ne întrebăm ce se întâmplă cu metoda dacă un parametru **nu există, este null sau este 0**
- Cel mai asemănător cu **Error Conditions** din Right-BICEP
- Ex: metodă pe String → test pentru null, sir vid, sir normal

**CARDINALITY (C):**
- Verifică dacă metoda/lista/colecția are **0 elemente, 1 element sau n elemente**
- Regula **0-1-n**: testezi cu 0, cu 1 și cu mai multe

**TIME (T):**
- Similar cu testul de Performance din Right-BICEP, **plus** testează:
  - **Momentul** în care este apelată metoda (sablonul de apeluri)
  - Dacă pentru a apela o metodă trebuie apelată mai întâi alta
- `@Test(timeout=100)` → testarea timpului de execuție

### Comparație Right-BICEP vs CORRECT

| Right-BICEP | CORRECT echivalent |
|-------------|-------------------|
| Error Conditions | **Existence** (cel mai asemănător) |
| Performance | **Time** (Time e similar, plus verifică momentul apelului) |
| Boundary | **Range** (Range e mai cuprinzător: interior + exterior + limite) |

---

## 6. Dubluri de testare (Test Doubles)

### Ce este o dublură de testare?
- Un **alt obiect** care se potrivește cu interfața colaboratorului necesar și poate fi trecut în locul său
- Un obiect care reduce complexitatea, permite verificarea codului **independent de restul sistemului**
- Folosit când dorim ca metoda testată să **nu fie influențată de referințe externe** (Mock testing)

### Tipurile de dubluri

| Tip | Ce face | Metodele returnează | Gestionează apeluri? |
|-----|---------|---------------------|----------------------|
| **Dummy** | Respectă interfața, metodele nu fac nimic | `null` sau `0` | ❌ |
| **Stub** | Returnează răspunsuri conservate/hardcodate | Valori hardcodate | ❌ |
| **Fake** | Se comportă ca un obiect real, versiune simplificată | Valori pe care le putem stabili | ❌ |
| **Spy** | Stub sau Fake + gestionează numărul de apeluri | Valori hardcodate/conservate | ✅ |
| **Mock** | Simulează comportamentul altui obiect în mod controlat | Controlate | ✅ |

### Detalii pe fiecare tip

**DUMMY:**
- Respectă interfața, dar metodele **nu fac nimic sau returnează 0 sau null**
- Folosit când **nu trebuie să apelăm metodele** din acel obiect
- Atunci când trebuie să folosim obiectul real, de fapt folosim un **dummy**

**STUB:**
- Metodele returnează **răspunsuri conservate/hardcodate**
- NU gestionează numărul de apeluri
- Diferența față de Dummy: Stub returnează hardcoded, Dummy returnează null/0

**FAKE:**
- Se comportă ca **unul real**, dar are o versiune **simplificată**
- Putem stabili ce valoare să întoarcă
- Diferența față de Stub: Fake are logică simplificată, Stub returnează fix hardcoded

**SPY:**
- Este un **Stub sau Fake** care gestionează și **contorizează** numărul de apeluri realizate pentru metode
- Poate fi un Stub → ✅
- Poate fi un Fake → ✅

**MOCK:**
- Simulează comportamentul unui alt obiect **în mod controlat**
- Creat pe baza **unei interfețe** (nu a unei clase reale)
- Mock testing se utilizează când dorim că metoda testată să nu fie influențată de **referințe externe**

### Când folosim fiecare?

| Situație | Dublura potrivită |
|----------|------------------|
| Nu trebuie să apelăm metodele | **Dummy** |
| Vrem răspunsuri hardcodate | **Stub** |
| Vrem o versiune simplificată a unui obiect real | **Fake** |
| Vrem să contorizăm apelurile | **Spy** |
| Vrem să testăm fără referințe externe | **Mock** |

### Diferențe cheie (frecvente la grile)

- **Dummy vs Stub:** Dummy → null/0; Stub → hardcoded
- **Stub vs Spy:** Spy = Stub + contorizare apeluri
- **Stub vs Fake:** Fake are versiune simplificată reală; Stub are hardcoded fix
- **Mock vs Dummy:** Mock simulează comportament controlat; Dummy nu face nimic

---

## 7. Principiul FIRST

### Ce înseamnă FIRST?
**F**ast, **I**solated, **R**epeatable, **S**elf-Validating, **T**imely

| Literă | Principiu | Ce presupune |
|--------|-----------|--------------|
| **F** | Fast | Testele trebuie să ruleze rapid |
| **I** | Isolated / Independent | Când un test eșuează, dezvoltatorul **nu trebuie să facă debug** pentru a identifica ce e greșit și unde |
| **R** | Repeatable | Testele ar trebui să se desfășoare **în mod repetat**, fără alte intervenții; rezultatele identice indiferent de numărul de rulări |
| **S** | Self-Validating | Dacă un test nu reușește, dezvoltatorul trebuie să aibă **încredere** că metoda trebuie îmbunătățită, nu testul |
| **T** | Timely | Testele se scriu **înainte** de cod (legat de TDD) |

### Detalii importante

**ISOLATED:**
- Testul ar trebui să fie izolat și să spună exact **unde** este problema și **ce** problemă există
- Orice test trebuie să aibă un **singur motiv să eșueze**
- ❌ NU: "Testul poate fi repetat și pentru alte metode"

**SELF-VALIDATING:**
- Dacă un test nu reușește → metoda trebuie îmbunătățită, **nu testul**
- Atunci când un test eșuează, dezvoltatorul **nu trebuie să facă debug**

**I din FIRST = Isolated = Independent** (toate variantele sunt corecte)

---

## 8. TDD — Test Driven Development

### Ce este TDD?
- **Testele sunt scrise ÎNAINTE de cod** (nu invers!)
- Se bazează pe repetarea unui **ciclu de dezvoltare simplu**
- Descrie conceptul de **Test Driven Development**

### Pașii din TDD:
1. **Scrie și rulează** testele (vor eșua — RED)
2. **Corectează metoda** (fă testele să treacă — GREEN)
3. **Refactorizează** codul — REFACTOR

> ⚠️ **În TDD**: dacă testul generează fails → se corectează **metoda**, NU testul!

---

## 9. Clean Code

### Ce este Clean Code?
Codul trebuie să fie:
- Ușor de **citit**
- Ușor de **înțeles**
- Ușor de **modificat**

### Ce este Bad Code?
- Greu de citit și înțeles
- Se strică atunci când îl **modifici**
- Are dependințe în **multe module externe** ("glass breaking code")
- Cod strans legat de alte secvențe de cod

### Principii Clean Code

---

#### 9.1 KISS — Keep It Simple and Stupid

**Ce este:** Metodele trebuie să facă **un singur lucru**

**Este încălcat când:** O metodă **are prea multe funcționalități** / face prea multe lucruri

**Beneficii KISS:**
- Codul scris este mai **flexibil**
- Realizarea unor produse ușor de **întreținut**
- Rezolvarea facilă a unor probleme **complexe**
- Toate variantele sunt corecte → răspuns: **Toate variantele**

**Derivat din KISS: YAGNI**

---

#### 9.2 DRY — Don't Repeat Yourself

**Ce este:** Nu repeta cod; nu scrie două metode care fac același lucru

**Este aplicabil când:**
- Dăm **Copy/Paste** unei bucăți de cod
- Două metode **fac același lucru**

**Este încălcat când:** Aceeași bucată de cod se găsește în două metode

---

#### 9.3 YAGNI — You Ain't Gonna Need It

**Ce este:** Dacă nu e nevoie de o metodă, **nu o scriem**

**Derivat din:** KISS

**Este încălcat când:** Scriem metode care **nu sunt necesare**

**NU se confundă cu:** DRY (care e despre duplicare de cod)

---

#### 9.4 SOLID

**S** — Single Responsibility Principle  
**O** — Open-Closed Principle  
**L** — Liskov Substitution Principle  
**I** — Interface Segregation Principle  
**D** — Dependency Inversion Principle

---

**S — Single Responsibility Principle (SRP):**
- O clasă trebuie să aibă **întotdeauna o singură responsabilitate și numai una**
- Aplicat metodelor: funcția să calculeze/să facă **un singur lucru**

---

**O — Open-Closed Principle (OCP):**
- Clasele trebuie să fie **deschise (open) pentru extensii**, dar **închise (closed) pentru modificări**
- "Open" din Open-Closed = **Open for extension**
- NU: "Open for modification"

---

**L — Liskov Substitution Principle (LSP):**
- Obiectele pot fi înlocuite oricând cu **instanțe ale claselor derivate** fără ca acest lucru să afecteze funcționalitatea
- Mai este întâlnit sub denumirea de **Design by Contract**
- L din SOLID = **Liskov substitution** (nu responsibility, nu segregation, nu inversion)

---

**I — Interface Segregation Principle (ISP):**
- Mai multe **interfețe specializabile** sunt oricând de preferat unei singure interfețe generale
- Obiectele nu trebuie obligate să implementeze **metode care nu sunt utile**
- Nu riscăm că prin modificarea "contractului" unui client să modificăm și contractele altor clienți

---

**D — Dependency Inversion Principle (DIP):**
- Programarea se realizează folosind **interfețe, abstractizări** și nu clasele concrete
- Inspirat de principiul Hollywood: **"Don't call us, we'll call you"**
- Modulele de nivel înalt **NU trebuie să depindă** de modulele de nivel jos (ci invers — ambele depind de abstractizări)

---

### Convenții de nume

| Convenție | Unde se folosește | Exemplu |
|-----------|-------------------|---------|
| **UpperCamelCase** | Clase și interfețe | `PasaportPersoana` |
| **lowerCamelCase** | Variabile și metode | `medieAritmetica`, `nrStudenti` |
| **System Hungarian Notation** | Se introduce **tipul** variabilei în denumire | `boolEstePrezent`, `intVarsta` |
| **Apps Hungarian Notation** | Se introduce **modulul** din care vine variabila | — |

**CapitalizationCamelCase NU este o convenție de nume!**

---

### Reguli Clean Code în cod

**În metode:**
- Variabilele vor fi declarate **cât mai aproape** de utilizarea lor
- Întotdeauna se va încerca ieșirea din funcție **cât mai repede posibil** (prin return sau excepție)
- Orice metodă e indicat să aibă cel mult **3 niveluri** de structuri imbricate
- **One Screen Rule:** evitarea metodelor cu mai mult de **20 de linii** de cod
- Funcțiile nu ar trebui să aibă mai mult de **3 argumente**

**În comentarii:**
- Codul bine scris este **auto-explicativ**
- Comentariile sunt indicate doar pentru:
  - **ToDo comments**
  - **Doc comments** (biblioteci refolosite de alți programatori)
- NU se comentează codul nefolosit (**zombie code** = cod sursă comentat)
- NU se folosesc blocuri de comentarii introductive

**În structuri condiționale:**
- Folosirea **operatorului ternar** ori de câte ori e posibil
- **Instantierea directă** a variabilelor boolean
- **Evitarea comparațiilor** cu `true` și `false`

**Scrierea codului sursă:**
- Acolada de închidere este **singură pe linie** (excepție: if-else, try-catch)
- Blocurile de cod încep cu `{` și se termină cu `}`
- Blocurile cu instrucțiuni sunt marcate și prin **indentare**
- Metodele sunt separate printr-o **singură linie goală** (NU oricâte!)
- Parametrii sunt separați prin **virgulă și spațiu**
- Operanzii sunt separați de operatori printr-un spațiu (excepție: **operatori unari**)

**Alte concepte:**
- **Zombie code** = codul sursă ce conține bucăți de cod comentate (cod nefolosit comentat)
- **Code Review** = revizuirea oricărei bucăți de cod scrise și de un alt programator
- **Refactoring** = rescrierea codului într-o manieră ce se adaptează mai bine noilor specificații
- **Automatic Testing** = testarea automată a codului pe baza unor cazuri de utilizare
- **Clasa Utils** = "este ca un magnet" (poate conține diverse metode statice)
- **Complexitatea ciclomatică** = calculată cu formula M = A - N + 2

---

## 10. Design Patterns — Introducere

### Ce este un Design Pattern?
- O **soluție la o problemă comună** în OOP (Programare Orientată Obiect)
- NU: algoritm, structură de date, schemă pentru un tip particular de clasă, soluție universală

### Componentele unui Design Pattern (obligatorii):
1. **Numele** pattern-ului
2. **Problema** pentru care pattern-ul oferă soluție
3. **Soluția** oferită de pattern, descrisă prin diagrame sau pseudo-cod
4. **Avantajele și dezavantajele** oferite de pattern

> ⚠️ **NU este componentă obligatorie:** Implementarea pattern-ului în Java

### Categorii de Design Patterns (GoF — Gang of Four):
- **Creaționale** — ajută la inițializarea și configurarea claselor și obiectelor; separă crearea obiectelor de utilizarea lor
- **Structurale** — controlează relațiile complexe dintre clase; compunerea claselor
- **Comportamentale** — permit distribuția responsabilităților pe clase; descrie interacțiunea între clase și obiecte; furnizează soluții pentru o mai bună interacțiune

> **Combinații corecte:** Creaționale, Structurale, Comportamentale

### Avantajele Design Patterns:
- Permit înțelegerea mai facilă a codului sursă și refactoring
- Ajută la comunicarea între programatori
- Reprezintă soluții folosite și testate de comunitate
- Conduc la evitarea rescrierii codului sursă

> ⚠️ **NU este avantaj:** "Timpul de analiză este lung" / "Timpul petrecut pentru analiză este redus"

### Clasificare pattern-uri (tabel complet)

| Pattern | Categorie |
|---------|-----------|
| Singleton | Creational |
| Simple Factory | Creational |
| Factory Method | Creational |
| Abstract Factory | Creational |
| Builder | Creational |
| Prototype | Creational |
| Adapter | Structural |
| Facade | Structural |
| Decorator | Structural |
| Composite | Structural |
| Proxy | Structural |
| Flyweight | Structural |
| Bridge | Structural |
| Strategy | Comportamental |
| Observer | Comportamental |
| Command | Comportamental |
| State | Comportamental |
| Memento | Comportamental |
| Chain of Responsibility | Comportamental |
| Template Method | Comportamental |

### Etapele utilizării unui Design Pattern:
1. **Identificarea problemei** (prima etapă!)
2. Maparea design pattern — problemă
3. Identificarea participanților
4. Implementarea metodelor

### Clasele în structura unui Design Pattern = **participanții**

---

## 11. Design Patterns Creaționale

### 11.1 SINGLETON

**Ce este:** Pattern creational care asigură existența **unei singure instanțe** a unui obiect

**Sintagma cheie:** "instanță unică"

**Când se utilizează:**
- Conexiune unică la baza de date
- Accesarea resurselor dispozitivelor mobile (SharedPreferences în Android)
- Deschiderea unei singure instanțe ale unei aplicații
- Gestiunea centralizată a unei resurse printr-o singură instanță

**Implementare — componente obligatorii:**
- Constructor **privat** (apelabil doar în clasă)
- **Instanță statică** de tip volatile
- **Metodă publică statică** care oferă acces la instanță
- Crearea obiectelor se face **prin intermediul unei funcții statice**
- Restricționarea creării de mai multe instanțe se face **din interiorul clasei**

**Tipuri de implementare Singleton:**
1. **Eager Initialization** — inițializează instanța chiar dacă nu e folosită; NU e eficientă
2. **Lazy Initialization** — creează instanța **la momentul folosirii** (doar când e folosită)
3. **Thread Safe Singleton** — metoda nu o să fie apelată de un alt fir de execuție până nu se termină cea curentă; **cea mai recomandată**
4. **Static block initialization** — asemănătoare cu Eager Init; utilă dacă constructorul aruncă excepții; furnizează posibilitatea de captare a excepțiilor
5. **Inner Static Helper Class** — îmbină **Eager Initialization cu Lazy Initialization**; clasa Helper imbricată e încărcată doar când e apelată funcția de creare a instanței
6. **Enum Singleton** — utilizează o enumerare pentru crearea unică a instanței; NU permite Lazy initialization

**Ordinea recomandată:** Thread Safe > Inner Static Helper Class > Static Block > Lazy > Eager > Enum

> ⚠️ **NU este tip de Singleton:** Conformity Assessment, Base Component, Singleton Collection

**Singleton vs Clasă statică:**
- Un obiect Singleton **poate fi trimis ca parametru** unei funcții; o clasă statică NU
- Singleton **poate implementa o interfață sau extinde** o altă clasă
- Singleton **respectă principiile POO**

**Problema serializării:** Se rezolvă implementând metoda **readResolve()**

**Corelație cu Factory:** Fabrica poate fi unică (Singleton)

---

### 11.2 SIMPLE FACTORY

**Ce este:** Pattern creational pentru crearea de obiecte dintr-o familie; creează obiecte concrete fără a cunoaște tipul concret

**Sintagma cheie:** "familie de obiecte" sau "obiecte din aceeași familie"

**NU este prezentat în cartea GoF**, dar este folosit în practică deoarece este ușor de implementat

**Componente (participanți):**
- Interfață/clasă abstractă comună pentru obiectele create
- Clasele concrete care implementează interfața
- Clasa care încapsulează procesul de creare a obiectelor (fabrica)
- Metoda `createInstance()` — primește tipul de obiect dorit și returnează tipul concret

> ⚠️ **NU este componentă Simple Factory:** "O metodă publică ce dă acces la o instanță unică" (aceea e Singleton)

**Dezavantaje:** Când adăugăm un nou tip de produs trebuie să modificăm în mai multe locuri, inclusiv fabrica

**Utilizare:** Când vrem să construim obiecte **din aceeași familie**

---

### 11.3 FACTORY METHOD

**Ce este:** Similar cu Simple Factory, dar NU mai folosește enum; abstractizează nivelul de creare

**Alt nume:** **Virtual Constructor**

**Caracteristici:**
- NU folosește structuri switch sau if-else
- Folosește abstractizări (nu clase concrete) pentru apeluri
- Poate fi găsit și sub denumirea de "Virtual Constructor"

**Dezavantaje:** Constructorii sunt privați, **clasele nu pot fi extinse**

**Principii SOLID respectate de Factory prin `createInstance()`:** Dependency Inversion + Liskov Substitution

**Tip de Factory bazat pe compunere:** **Abstract Factory**

---

### 11.4 ABSTRACT FACTORY

**Ce este:** Introduce un **nou nivel de abstractizare** față de Factory Method

**Implementare:**
- Fiecare factory va crea **două sau mai multe tipuri** de obiecte
- Avem o singură fabrică cu ajutorul căreia obținem obiecte din toate familiile dintr-o categorie
- Pentru fiecare obiect există o metodă

**Tip:** Creational; bazat pe **compunere**

---

### 11.5 BUILDER

**Ce este:** Pattern pentru crearea în mod structurat de obiecte complexe printr-un mecanism **independent** de procesul de realizare efectivă a obiectelor, astfel că **clientul nu cunoaște detaliile interne** ale obiectului

**Sintagma cheie:** "obiecte complexe cu foarte multe atribute", "atribute opționale"

**Când se utilizează:**
- Obiecte cu **multe atribute** din care unele sunt opționale, iar altele obligatorii

**Participanți:**
- **AbstractBuilder** — interfața care definește metodele de construire
- **ConcreteBuilder** — clasa care implementează interfața
- **Produs** — obiectul complex construit

**Variante de implementare (toate 3 sunt corecte):**
1. Crearea obiectului complex în **constructorul** clasei Builder
2. Crearea obiectului complex în **metoda build()**
3. Utilizarea unei **clase imbricate** (Inner class)

**Avantaje:** Flexibilitatea algoritmului de creare (clientul alege ce părți să fie create)

**Dezavantaje:** La crearea de obiecte, pot fi **omise atribute**

> ⚠️ **NU este caracteristic Builder:** "Asigură un singur punct de acces, vizibil global, la o instanță unică" (aceea e Singleton!)

> ⚠️ **NU este componentă Builder:** Interfața Factory

**Corelație cu Singleton:** Builder poate fi unic (Singleton)

---

### 11.6 PROTOTYPE

**Ce este:** Pattern creational bazat pe **clonarea** unor instanțe ale unui prototip existent

**Sintagma cheie:** "evitarea consumului mare de resurse" / "clonare"

**Când se utilizează:**
- Crearea unui obiect durează **foarte mult**
- Crearea unui obiect consumă **foarte multe resurse**
- Obiectele create seamănă între ele
- Folosim `clone()`

**Participanți:**
- Interfața care anunță metoda de copiere (**Interfața Prototype** — anunță, nu implementează!)
- Clasa concretă care **implementează** metoda de copiere sau de clonare

**Interfața Prototype:** **Anunță** metoda de copiere (NU implementează!)

**Implementare:**
- Prin intermediul design pattern-ului se creează un **obiect considerat prototip**
- Prototipul urmează să fie clonat pentru următoarele instanțe

**Corelație cu Composite:** Elementele de pe același nivel pot fi clonate

**Corelație cu Decorator:** Se clonează obiectele și apoi se modifică

**Diferență Prototype vs Flyweight:**
- Prototype: crearea obiectelor se face prin clonare
- Flyweight: obiectele sunt **reutilizate**
- Prototype tip Creational; Flyweight tip Structural
- Prototype = optimizează viteza de creare; Flyweight = optimizează memoria

---

## 12. Design Patterns Structurale

### 12.1 ADAPTER

**Ce este:** Pattern structural care rezolvă problema utilizării anumitor clase din **framework-uri diferite** care nu au o interfață comună

**Sintagma cheie:** "utilizarea unor clase din framework-uri diferite care nu au o interfață comună"

**Caracteristici:**
- Clasele existente **nu se vor modifica**; se adaugă clase noi (clase Wrapper)
- Utilizarea claselor existente se va face **mascat** prin intermediul adapterului creat
- Adapterul **NU adaugă funcționalitate** (o face Decorator!)

**Participanți:**
- Clasa existentă (Adaptee)
- Clasa utilizată (Target — interfața)
- **Adapterul**

**Cele 2 tipuri de Adapter:**
1. **Adapter de obiecte** — Clasa Adapter **conține o instanță** a clasei existente și implementează interfața
2. **Adapter de clase** — Clasa Adapter **moștenește** clasa existentă și implementează interfața

**Structura:** Target → Adapter → Adaptee

**Asemănare cu Facade:** Ambele sunt **wrappere**

**Asemănare cu Proxy:** Ambele **ascund, într-un fel, clasa existentă**

**Deosebire față de Decorator:** Decorator adaugă funcționalități noi; Adapter NU

**Când se utilizează:**
- Ori de câte ori nu se dorește **modificarea codului existent**
- Ori de câte ori este necesară conlucrarea mai multor framework-uri

---

### 12.2 FACADE

**Ce este:** Pattern structural care usurează lucrul cu **framework-uri foarte complexe**

**Sintagma cheie:** "simplificarea unui proces"

**Caracteristici:**
- Realizează o **fatadă** pentru framework-urile complexe
- Clasa Facade cuprinde metode care utilizează metodele din clasele framework-ului
- Clasa Facade **ascunde complexitatea** prin apelurile sale
- Nu e nevoie să cunoaștem toate clasele, metodele și atributele din framework

**Participanți:**
- Clasele **din cadrul** framework-ului folosit
- Clasa care **ascunde complexitatea** framework-ului (Facade)

**Asemănare cu Adapter:** Ambele sunt wrappere

**Când se utilizează:** Se dorește **simplificarea** unui proces

> ⚠️ **NU pentru:** "Se dorește adăugarea de funcționalități" (aceea e Decorator)

---

### 12.3 DECORATOR

**Ce este:** Pattern structural folosit pentru **adăugarea de noi funcționalități** unui obiect la runtime, fără modificarea clasei

**Sintagma cheie:** "noi funcționalități"

**Caracteristici:**
- Poate modifica comportamentul unui obiect **la run-time**
- Decorarea poate fi **multiplă** (prin moștenire continuă)
- Decorarea este transparentă deoarece **moștenește interfața** specifică obiectului

**Participanți:**
- **AbstractProduct** (interfața)
- **ConcreteProduct** (clasa concretă)
- **AbstractDecorator** (decorator abstract)
- **ConcreteDecorator** (decorator concret)

**Avantaj:** Decorarea se poate face pe mai multe niveluri, transparent pentru utilizator

**Dezavantaj:** ❌ Nu există — Decorator poate modifica sau adăuga funcționalități

**Implementare:**
- În clasa abstractă: se implementează interfața și se creează o instanță de tipul acelei interfețe
- În clasa decorator concret: se implementează noile metode

**Deosebire față de Adapter:** Decorator adaugă funcționalități; Adapter NU

**Deosebire față de Proxy:** Proxy = control acces; Decorator = adăugare funcționalități

**Deosebire față de Strategy:** Decorator modifică întreaga clasă; Strategy modifică comportamentul

**Corelație cu Composite:** Nodurile Composite pot fi privite ca Noduri Frunză decorate

**Când se utilizează:** Se dorește adăugarea de funcționalități claselor existente

---

### 12.4 COMPOSITE

**Ce este:** Pattern structural folosit când este necesară crearea unei **structuri ierarhice** prin compunerea de obiecte

**Sintagma cheie:** "structură ierarhică sau arborescentă"

**Participanți:**
- **Componenta abstractă** (interfața/clasa abstractă)
- **Composite** (nod container — conține o listă cu elemente de tip ComponentaAbstractă)
- **NodFrunza** (nu implementează metodele de adăugare și ștergere!)

> ⚠️ NU: NodRadacina! Participantul corect este **NodFrunza**

**Caracteristici:**
- Clasele Composite conțin o **listă** cu elemente de tip ComponentaAbstractă
- În lista de obiecte se pot **adăuga și șterge** noduri
- **Clasele NodFrunza NU implementează** metodele de adăugare și ștergere

**Principiu Clean Code încălcat:** **YAGNI** (metodele de adăugare/ștergere în NodFrunza sunt inutile)

**Utilizări:** Meniurile aplicațiilor, meniurile de la restaurant, orice arborescentă

**Asemănare cu Decorator:** Nodurile Composite pot fi privite ca Noduri Frunză decorate

---

### 12.5 PROXY

**Ce este:** Pattern structural care oferă acces controlat la un obiect

**Sintagma cheie:** "control acces", "permisiuni"

**Participanți:**
- O interfată
- Clasa concretă **Entitate** (obiectul gestionat)
- Clasa concretă **Proxy**

> ⚠️ NU abstracte! Sunt **clase concrete**

**Implementare:**
- Clasa Proxy implementează interfata InterfataEntitate
- Clasa Proxy are un atribut de tipul Entitate (obiectul gestionat)
- Metoda va fi apelată **doar dacă condițiile sunt îndeplinite**

**Asemănare cu Adapter:** Ambele ascund, într-un fel, clasa existentă

**Deosebire față de Decorator:** Proxy = control acces; Decorator = funcționalități noi

**Când se utilizează:** Ori de câte ori se dorește realizarea de **permisiuni** pentru anumite obiecte sau accesul la anumite funcționalități ale obiectelor

---

### 12.6 FLYWEIGHT

**Ce este:** Pattern structural care reduce **consumul de memorie** prin reutilizarea obiectelor similare

**Sintagma cheie:** "foarte multe obiecte similare", "optimizare memorie"

**Caracteristici:**
- Una din clase (**FlyweightFactory**) conține un **HashMap** pentru reținerea obiectelor asemănătoare
- NU consumă multă memorie — dimpotrivă, **reduce** consumul!
- Obiectele create NU sunt identice — au o **parte comună** și diferă prin alte atribute

**Participanți:**
- **Flyweight** (interfața)
- **ConcreteFlyweight** (obiectele cu parte comună)
- **UnsharedConcreteFlyweight** (obiecte care nu sunt partajate)
- **FlyweightFactory** (gestionează crearea/reutilizarea)

**Asemănare cu Factory:** Construirea de obiecte este gestionată de o clasă

**Avantaj:** **Reducerea consumului de memorie**

**Context utilizare:** În jocuri când foarte multe modele seamănă, dar diferă prin culoare sau poziție

**Diferență față de Prototype:**
- Flyweight = obiecte **reutilizate** (nu clonate)
- Prototype = obiecte **clonate**

---

## 13. Design Patterns Comportamentale

### 13.1 STRATEGY

**Ce este:** Pattern comportamental care permite alegerea la **run-time** a algoritmului/funcției necesare procesării unui set de date

**Sintagma cheie:** "mai mulți algoritmi", "alegerea la run-time"

**Caracteristici:**
- Definește strategia adoptată la **run-time** (nu la compilare!)
- Alegerea implementării se face la **runtime**
- Permite modificarea librăriei de funcții dar **nu a clasei** care gestionează datele

**Participanți:**
- O **interfață** (definește metoda de procesare)
- **Clase concrete** ce implementează interfața (algoritmii)
- **Clasa concretă** ce conține o referință de tipul interfeței (contextul)

**Când se utilizează:** Avem **mai mulți algoritmi** pentru rezolvarea unei probleme, iar alegerea se face la runtime

**Utilizări practice:** Validatoare pentru anumite controale; compresie/decompresie cu formate diferite

**Diferență față de State:**
- La Strategy = **strategia este dată ca parametru**
- La State = **trecerea de la o stare la alta se face controlat**

---

### 13.2 OBSERVER

**Ce este:** Pattern comportamental care definește o relație **1:n** între obiecte, unde un subiect notifică mai mulți observatori

**Sintagma cheie:** "notificare la schimbare de stare"

**Caracteristici:**
- Definește o relație de **1:n** (NU 1:1, NU n:1)
- Atunci când starea subiectului se schimbă, toți observatorii sunt notificați
- ❌ Observer NU permite instanțierea unui singur obiect (aceea e Singleton)

**Participanți:**
- **Interfețe** pentru observer și observabil
- **Clase concrete** pentru observer și observabil

**Clase din Observer:**
- **ObservabilConcret** = clasa concretă care **gestionează lista de observatori**
- **ObservatorConcret** = clasele care definesc la nivel concret observatorii

**Context utilizare:** **Model View Controller (MVC)** — NU DNS Resolver (aceea e Chain of Responsibility)

**Când se utilizează:** Este necesar ca un subiect să notifice mai mulți observatori

**Smart home exemplu:** Senzori → notifică mai mulți observatori pe GUI → **Observer**

---

### 13.3 COMMAND

**Ce este:** Pattern comportamental folosit pentru implementarea **loose coupling** (decuplare)

**Sintagma cheie:** "decuplarea clientului de cel ce execută o acțiune", "lose coupling"

**Caracteristici:**
- Command este folosit pentru implementarea **lose coupling**
- Clientul este decuplat de cel ce execută acțiunea
- Invoker-ul poate salva comenzile invocate
- Invoker-ul poate fi folosit pentru a invoca comenzile

**Participanți:**
- **Command** (interfața care definește comanda la nivel abstract)
- **Comenzile concrete** (clasele concrete pentru fiecare comandă)
- **Receiver** — **obiectul responsabil cu execuția acțiunilor**
- **Invoker** — **clasa care se ocupă cu gestiunea comenzilor**

**O clasă TestCase** este un obiect al pattern-ului **Command**

**Asemănare cu Adapter:** Ambele folosesc funcționalități deja existente

**Când se utilizează:**
- Implementarea lose coupling
- Lucrul cu fișiere
- Macro-uri
- Oriunde se dorește revenirea la o stare anterioară prin intermediul comenzilor

---

### 13.4 STATE

**Ce este:** Pattern comportamental folosit când un obiect **își schimbă comportamentul** pe baza stării în care se află

**Sintagma cheie:** "schimbare comportament în funcție de stare"

**Participanți:**
- O **interfață** (sau clasă abstractă)
- **Clase concrete** ce definesc starile obiectului (ConcreteState)
- **Clasa concretă** ce definește obiectul (care va trece prin stări)

**Clase din State:**
- **ConcreteState** = **starile concrete** în care poate fi un obiect (NU abstractizarea, NU interfata)

**Diferență față de Strategy:**
- Strategy = strategia dată ca parametru
- State = trecerea de la o stare la alta se face **controlat**

**Când se utilizează:** Un obiect își schimbă comportamentul pe baza stării în care se află

---

### 13.5 MEMENTO

**Ce este:** Pattern comportamental folosit pentru **salvarea și revenirea** la stări anterioare ale obiectelor

**Sintagma cheie:** "salvarea stărilor", "backup", "revenire"

**Participanți:**
- **Memento** — stochează starea
- **Originator** — **clasa care are obiecte pentru care se vor salva stări intermediare**
- **CareTaker** — **clasa care gestionează obiectele de tip Memento**

**Implementare:** Clasa Memento poate fi una **externă** (ocupându-se de atributele pentru care se realizează imaginea intermediară)

**Utilizări:**
- Realizarea de **backup-uri**
- Backtracking
- ❌ NU: evitarea structurii switch/if-else (aceea e Strategy)

---

### 13.6 CHAIN OF RESPONSIBILITY

**Ce este:** Pattern comportamental folosit când se dorește rezolvarea unei probleme când **nu se știe cu exactitate** cine o poate rezolva, dar există o listă de posibilități

**Sintagma cheie:** "listă de posibili rezolvatori", "nu știm cine poate rezolva"

**Implementare:**
- Obiectele posibile se ordonează **într-un lanț**
- Cel care are problema apelează primul din lanț
- Dacă un handler concret NU poate rezolva problema → apelează la **următorul handler**
- Ultimul handler din lanț NU apelează la altul (întoarce eroare sau nimic)

**Participanți:**
- **Handler** (abstract) — clasa abstractă care definește interfața obiectelor ce vor gestiona cererea
- **Clase concrete** — obiectele care vor forma lanțul

**Context utilizare:** **DNS Resolver** — NU MVC (aceea e Observer)

---

### 13.7 TEMPLATE METHOD

**Ce este:** Pattern comportamental folosit când un algoritm este **cunoscut** și urmează anumiți pași precisi

**Sintagma cheie:** "algoritm cu pași precisi"

**Participanți:**
- **Template** (clasa abstractă cu metoda template)
- **ConcreteTemplate** (clasele concrete care implementează pașii)

> ⚠️ NU: Template, ConcreteTemplate, ConcreteClass

**Implementare:**
- În clasa abstractă, metoda template se declară **finală** (astfel încât să NU poată fi suprascrisă)
- În clasele concrete sunt implementate metodele folosite în metoda template

**Când se utilizează:**
- Modul de rezolvare urmează un **număr cunoscut de pași**
- Modul de procesare urmează un număr finit de pași
- Backtracking

---

## 14. GIT — Control Versiuni

### Ce este GIT?
- Sistem **distribuit** de versionare (NU centralizat!)
- Publicat în 2005 de **Linus Torvalds** (care a creat și sistemul de operare **Linux**)
- Toți programatorii au acces la **istoricul modificărilor**
- Fiecare programator lucrează pe mașina sa și are **o copie a repository-ului**

### Necesitățile versionării:
- **Backup** pentru codul scris
- **Caracter colaborativ** al proiectelor
- **Istoricul modificărilor** — toți programatorii au acces
- ❌ NU: "semnalează automat erorile din liniile de cod"

### Caracteristici GIT (false):
- ❌ "Doar unii programatori au acces la istoricul modificărilor"
- ❌ "Este un sistem centralizat de versionare"
- ❌ "Programatorii lucrează numai pe branch-ul principal (master)"

### Concepte cheie

| Concept | Definiție |
|---------|-----------|
| **Repository** | Componenta server ce conține informații privind ierarhia de fișiere și reviziile asupra acestora (NU versiunea locală!) |
| **Working copy** | Versiunea **locală** a proiectului, versiunea în care lucrează programatorul |
| **Branch** | Bifurcarea unui set de fișiere în două căi de dezvoltare distincte |
| **Commit** | Cerere de publicare în repository-ul local a unor modificări realizate în working copy |
| **Merge** | Procesul de **unire** a două sau mai multe versiuni de lucru |
| **Conflict** | Apare când mai mulți utilizatori au realizat modificări în **aceleași fișiere** din proiect |
| **Revert** | Revenirea la o versiune anterioară pe un anume fir de dezvoltare (branch) |
| **Stash** | Arhivă locală pentru un set de modificări |
| **Checkout** | Preluarea în mediul local a unei anumite revizii publicate pe server |

### Comenzi GIT

| Comandă | Ce face |
|---------|---------|
| `git init` | **Inițializarea** unui repository (crearea unui proiect nou) |
| `git clone` | **Descărcarea** proiectului (repository) pe computer |
| `git add <fisier>` | Adăugarea unui nou fișier în **track** |
| `git add app.js` | Adăugarea modificărilor din fișierul app.js |
| `git status` | Verificarea **stării** proiectului / repository-ului local |
| `git commit -m "mesaj"` | **Salvarea** modificărilor (publicare în repo local) |
| `git push` | **Trimiterea** modificărilor în repository-ul central (opus lui clone) |
| `git pull` | **Actualizarea** versiunii curente (actualizare informații locale cu cele de pe server) |
| `git fetch` | Importarea commit-urilor de pe repo-ul remote în repo-ul local |
| `git merge` | **Unirea** a două sau mai multe versiuni de lucru |
| `git log` | Afișarea tuturor commit-urilor care au fost făcute |
| `git diff` | Verificarea stării repo-ului local față de ultimul commit |

### Comenzi pentru Branch-uri

| Comandă | Ce face |
|---------|---------|
| `git branch` | Afișează branch-urile **locale** |
| `git branch -a` | Afișează branch-urile **locale și de pe repository** |
| `git branch -b <<new_branch>>` | Creează un **nou branch** pe baza celui curent |
| `git branch -b <<new_branch>> <<branch_sursa>>` | Creează un nou branch sincronizat cu branch-ul sursă din repository |
| `git checkout <<branch_local>>` | **Schimbă** branch-ul pe care se lucrează |
| `git branch -d <<branch>>` | Șterge branch-ul local și de pe repository; dacă există modificări ne-merge-uite, **ștergerea NU se face** |
| `git branch -D <<branch>>` | Șterge branch-ul local și de pe repository **chiar dacă există modificări** ne-merge-uite |

### Etapele standard în GIT:
1. `git clone` → Descărcare proiect
2. Lucru în proiect
3. `git add` → Adăugare fișiere în track
4. `git commit -m "mesaj"` → Commit modificări (corect: `git commit -m "message"`)
5. `git push` → Publicare pe server

### Situații la grile:

**Conflict:** Apare când un coleg a făcut modificări pe care NU le-ai integrat local și tu vrei să dai push → **Conflict**

**Soluție conflict:** `git stash` (salvezi modificările tale) → `git pull` → rezolvare conflict → `git push`

**Opusul lui git clone:** `git push`

**`git fetch` vs `git pull`:** `fetch` = importă commit-urile local (fără merge); `pull` = fetch + merge (actualizează direct)

---

## ⚡ CHEAT SHEET — Răspunsuri capcană la grile

### Design Patterns — Capcane frecvente

| Întrebare | Răspuns corect | Greșeală frecventă |
|-----------|---------------|-------------------|
| Simple Factory în GoF? | **NU** | Confundat cu Factory Method |
| xUnit vs JUnit | **xUnit NU este adaptare la JUnit** — JUnit e adaptare de la xUnit | Invers |
| JUnit pattern-uri | **Composite + Command** | Adapter, Builder etc. |
| Adnotare lipsă în JUnit 4 | **@AfterEach** | @AfterClass, @Before |
| Tip Singleton recomandat | **Thread Safe** (sau Inner Static Helper Class) | Eager Initialization |
| Inner Static Helper Class îmbină | **Eager + Lazy** | Thread Safe + Eager |
| L din SOLID | **Liskov substitution** | Liskov responsibility/segregation |
| Design by Contract | **Liskov Substitution** | Open-Closed |
| YAGNI derivat din | **KISS** | DRY, SOLID |
| NU convenție de nume | **CapitalizationCamelCase** | System Hungarian |
| Observer relație | **1:n** | 1:1, n:1 |
| Observer context | **Model View Controller** | DNS Resolver |
| Chain of Responsibility context | **DNS Resolver** | MVC |
| Composite principiu încălcat | **YAGNI** | DRY, KISS |
| Template Method declarat | **final** (nu abstract!) | abstract |
| ObservabilConcret | Gestionează lista de observatori | Definește observatorii |
| ObservatorConcret | Definește observatorii | Gestionează lista |
| Facade vs Adapter asemanare | **Ambele sunt wrappere** | Fac același lucru |
| Proxy vs Adapter asemanare | **Ambele ascund clasa existentă** | Sunt wrappere |
| Decorator vs Adapter deosebire | **Decorator adaugă funcționalități, Adapter NU** | — |
| Flyweight consumă memorie? | **NU** — reduce consumul | DA |
| Prototype vs Flyweight | Prototype = clonare; Flyweight = reutilizare | Inversate |

### Right-BICEP / CORRECT — Capcane

| Întrebare | Răspuns corect |
|-----------|---------------|
| CORRECT acronim | Conformance, **O**rdering, **R**ange, **R**eferences, **E**xistence, **C**ardinality, **T**ime |
| Asemănător Error Conditions din BICEP | **Existence** din CORRECT |
| Compliance testing = | **Conformance** |
| Time vs Performance | Time = Performance **+** momentul apelării metodei |
| Boundary vs Range | Boundary = pe limite; Range = limite + interior + exterior |
| Testul Reference se face cu | **Dubluri de test** |
| Extragere din stivă → Reference → verificăm | **Dacă există elemente în stivă** |
| Test Fibonacci cu altă funcție | **Cross-Check** |
| Test Fibonacci invers | **Inverse Relationship** |

### GIT — Capcane

| Întrebare | Răspuns corect |
|-----------|---------------|
| Repository = | Componenta server (NU versiunea locală) |
| Working copy = | Versiunea **locală** |
| Opusul git clone | **git push** (NU git upload) |
| git fetch = | Importarea commit-urilor (NU actualizarea directă) |
| git branch -D vs -d | -D = forțat chiar cu modificări; -d = nu șterge dacă sunt modificări |
| Linus Torvalds a creat și | **Linux** |
| GIT este distribuit sau centralizat? | **Distribuit** |

---

*Fișier creat pentru pregătirea examenului CTS — ASE București*  
*Bazat pe grilele din fișierul GrileTotTotTot și laboratoarele din proiect*
