# Identificare Design Patterns — Ghid rapid

Logica de identificare: citești cerința, cauți cuvintele cheie, mapezi la pattern.

---

## Metoda generală

1. **Câte patterns?** — de obicei 2 cerințe de câte 3p → 2 patterns distincte
2. **Ce interfață ți-a dat?** — numele metodelor din interfață îți confirmă pattern-ul
3. **Caută cuvintele cheie** din tabelul de mai jos
4. **Verifică** cu structura: câte clase ai nevoie și cum se leagă

---

## Tabel rapid — cuvinte cheie → pattern

| Cuvinte cheie în cerință | Pattern |
|--------------------------|---------|
| „structură ierarhică", „calcul recursiv", „element simplu și element compus tratate uniform", „grupuri care conțin alte grupuri" | **Composite** |
| „obiect intermediar", „control acces", „verifică înainte de a delega", „fără modificarea clasei reale" | **Proxy** |
| „algoritm schimbabil la rulare", „mai multe variante de calcul", „utilizatorul alege criteriul" | **Strategy** |
| „filtre succesive", „fiecare filtru decide dacă respinge sau pasează", „ordinea poate fi schimbată" | **Chain of Responsibility** |
| „obiecte costisitoare reutilizate", „stare partajată + informații variabile transmise separat", „reducerea numărului de instanțe" | **Flyweight** |
| „opțiuni adăugate dinamic", „combinare liberă fără explozie de clase", „același tip de referință înainte și după adăugare" | **Decorator** |
| „notificare automată la schimbare de stare", „componente care ascultă", „abonare/dezabonare dinamică" | **Observer** |
| „integrare fără modificarea clasei externe", „format diferit de la sistem extern", „același cod client pentru obiecte incompatibile" | **Adapter** |
| „acțiune ca obiect", „stocare și executare ulterioară", „listă de operații executate succesiv" | **Command** |
| „interfață simplificată peste mai multe subsisteme", „ascunde complexitatea" | **Facade** |

---

## Per pattern — logica de identificare detaliată

---

### COMPOSITE

**Întrebare cheie:** *Există un element simplu (frunză) și un element compus (container) care se comportă la fel?*

**Semnale:**
- Cerința menționează două tipuri de entități: una simplă și una care „poate conține" alte entități de același tip
- Se cere calcul recursiv (total pasageri, cost total, număr total)
- Interfața are metode ca `calculeaza...()`, `afiseaza...()` — fără parametri speciali

**Structura minimă:**
```
Interfata (frunza + nod au aceeași interfață)
  ├── ClasaFrunza   — implementează direct
  └── ClasaNod      — ține List<Interfata>, delegă recursiv
```

**Confirmare prin interfață:** metode de calcul/afișare fără parametri + metode `add/remove` pe nod

**Capcane:**
- Dacă se adaugă *comportament* (nu copii), nu e Composite → e **Decorator**
- Dacă elementele nu sunt de același tip cu containerul → nu e Composite

---

### PROXY

**Întrebare cheie:** *Există un obiect intermediar care controlează accesul la obiectul real?*

**Semnale:**
- Cuvântul „intermediar" apare explicit
- Se verifică o condiție (permisiuni, număr accese, cache) **înainte** de a apela obiectul real
- Interfața e aceeași pentru Proxy și obiectul real

**Structura minimă:**
```
Interfata
  ├── ClasaReala   — face treaba efectivă
  └── ProxyClasa   — conține ClasaReala, verifică, apoi delegă
```

**Linia care face Proxy:** `this.obiectReal.metoda(...)` — delegarea după verificare

**Capcane:**
- Proxy **nu modifică** rezultatul — doar controlează accesul → dacă modifică rezultatul e **Decorator**
- Proxy și obiectul real implementează **aceeași interfață** — obligatoriu

---

### STRATEGY

**Întrebare cheie:** *Există mai mulți algoritmi interschimbabili pentru aceeași operație?*

**Semnale:**
- Cerința listează variante: „timp minim SAU cost minim SAU număr minim de stații"
- „algoritmul poate fi schimbat la rulare" sau „utilizatorul alege"
- Contextul (clasa care folosește strategia) nu se modifică când schimbi algoritmul

**Structura minimă:**
```
InterfataStrategie
  ├── VariantaA implements InterfataStrategie
  ├── VariantaB implements InterfataStrategie
  └── VariantaC implements InterfataStrategie

ClasaContext — are private InterfataStrategie strategie + setter
```

**Confirmare prin interfață:** o singură metodă (ex: `calculeaza(...)`, `executa(...)`)

**Capcane:**
- Dacă variantele se aplică *succesiv* (una după alta) → **Chain of Responsibility**
- Dacă e o singură variantă cu pași diferiți → **Template Method**

---

### CHAIN OF RESPONSIBILITY

**Întrebare cheie:** *Există mai mulți handlere/filtre care procesează același input succesiv?*

**Semnale:**
- „filtrare succesivă după mai multe criterii"
- „fiecare handler decide dacă oprește sau pasează mai departe"
- „ordinea poate fi schimbată ușor"
- Abstracta are câmpul `urmator` (next handler) și metoda `seteazaUrmator()`

**Structura minimă:**
```
AbstractHandler — are protected AbstractHandler urmator
  ├── Handler1 extends AbstractHandler — procesează, apoi apelează urmator
  ├── Handler2 extends AbstractHandler
  └── Handler3 extends AbstractHandler

// Main: h1.setNext(h2); h2.setNext(h3); h1.proceseaza(input);
```

**Linia care face CoR:** `if (urmator != null) return urmator.proceseaza(input);`

**Capcane:**
- Dacă toate variantele sunt independente (nu se înlănțuie) → **Strategy**
- Dacă clasa abstractă e dată cu câmpul `urmator` deja — e sigur **CoR**

---

### FLYWEIGHT

**Întrebare cheie:** *Există obiecte costisitoare care se repetă în multe contexte cu mici variații?*

**Semnale:**
- „resursele sunt mari/costisitoare și se reutilizează"
- „aceleași obiecte apar în zeci/sute de locuri"
- „stare partajată (intrinsecă) + informații variabile (extrinsecă) transmise separat"
- Metoda interfaței primește parametrii variabili: `afiseaza(int x, int y, String eticheta)`

**Structura minimă:**
```
InterfataFlyweight — metodă cu parametrii extrinseci
  └── ClasaFlyweight — conține doar starea intrinsecă (partajată)

FabricaFlyweight — HashMap<String, InterfataFlyweight>, returnează același obiect
```

**Linia care face Flyweight:** `return cache.get(cheie);` — returnează instanță existentă

**Capcane:**
- Dacă nu există fabrică/cache → nu e Flyweight
- Parametrii extrinseci NU se stochează în obiect — se primesc la fiecare apel al metodei

---

### DECORATOR

**Întrebare cheie:** *Se adaugă comportament dinamic peste un obiect, fără a-i schimba tipul?*

**Semnale:**
- „opțiuni suplimentare adăugate dinamic" (ex: topping pe pizza, extensii pe fișă)
- „combinare liberă fără explozie de clase"
- „adăugare succesivă" — învelire strat cu strat
- Interfața e aceeași pentru obiectul de bază și pentru decorator

**Structura minimă:**
```
Interfata
  ├── ClasaBaza          — implementare simplă
  └── DecoratorAbstract  — implements Interfata, conține private Interfata obiect
        └── DecoratorConcret — suprascrie metoda, adaugă comportament + apelează super/obiect
```

**Linia care face Decorator:** `super.metoda()` sau `this.obiect.metoda()` — delegare + adăugare

**Capcane:**
- Decorator vs Composite: Decorator adaugă *comportament*, Composite adaugă *copii*
- Decorator vs Proxy: Decorator modifică rezultatul, Proxy doar controlează accesul

---

### OBSERVER

**Întrebare cheie:** *Mai multe obiecte trebuie notificate automat când se schimbă starea unui obiect central?*

**Semnale:**
- „module/componente notificate la schimbarea stării"
- „abonare și dezabonare dinamică"
- „fără modificarea clasei care gestionează subiectul"
- Interfața subiectului are: `adauga(Observer)`, `elimina(Observer)`, `notifica()`
- Interfața observatorului are: `actualizeaza(...)` / `mesaj(...)`

**Structura minimă:**
```
InterfataObserver — actualizeaza(...)
  └── ObservatorConcret — ce face cu notificarea

InterfataSubiect — adauga, elimina, notifica
  └── SubiectConcret — List<InterfataObserver>, apelează actualizeaza pe toți la schimbare
```

**Linia care face Observer:** `for (Observer o : lista) o.actualizeaza(stare);`

**Capcane:**
- Dacă există un singur „ascultător" hardcodat → nu e Observer
- Subiectul nu știe concret cine sunt observatorii — depinde de interfață

---

### ADAPTER

**Întrebare cheie:** *Există o clasă externă incompatibilă pe care trebuie să o integrezi fără s-o modifici?*

**Semnale:**
- „integrare fără modificarea clasei externe"
- „format diferit de la parteneri/sisteme externe"
- „același cod/evaluator pentru obiecte interne și externe"
- Există o interfață internă (target) și o clasă externă (adaptee) cu metode diferite

**Structura minimă:**
```
InterfataInterna (target) — ce vrea clientul
ClasaExterna (adaptee)   — ce există deja, nu o modifici

// Object Adapter (compoziție — preferată):
AdaptorClasa implements InterfataInterna {
    private ClasaExterna obiectExtern;
    @Override public void metodaInterna() { obiectExtern.metodaExterna(); }
}

// Class Adapter (moștenire):
AdaptorClasa extends ClasaExterna implements InterfataInterna { ... }
```

**Linia care face Adapter:** `obiectExtern.metodaExterna()` — apel pe adaptee din metodele target

**Capcane:**
- Dacă modifici clasa externă → nu mai e Adapter
- Dacă adaugi logică intermediară (nu doar traducere) → poate fi **Proxy**

---

### COMMAND

**Întrebare cheie:** *O acțiune trebuie reprezentată ca obiect pentru a fi stocată, amânată sau combinată?*

**Semnale:**
- „fiecare acțiune reprezentată printr-un obiect separat"
- „stocare și executare ulterioară"
- „listă de comenzi executate succesiv"
- Interfața are o singură metodă: `executa()` / `execute()`

**Structura minimă:**
```
InterfataComanda — executa()
  ├── ComandaConcreta1 — conține Receiver, apelează metoda lui în executa()
  └── ComandaConcreta2

Invoker — List<InterfataComanda>, execută toate
Receiver — clasa care face treaba efectivă (ex: Bucatarie, Lumina)
```

**Linia care face Command:** `receiver.actiune()` — în interiorul lui `executa()`

**Capcane:**
- Command vs Strategy: Strategy schimbă *cum* se face ceva, Command *ce* să se facă și *când*
- Dacă interfața are `executa()` și se vorbește de liste/stocare → sigur **Command**

---

## Flowchart de identificare rapidă

```
Cerința menționează...

structură arborescentă / calcul recursiv pe ierarhie?
  → COMPOSITE

obiect intermediar / control acces / verificare înainte de delegare?
  → PROXY

mai mulți algoritmi interschimbabili la rulare?
  → STRATEGY

filtre/handlere succesive, fiecare pasează mai departe?
  → CHAIN OF RESPONSIBILITY

obiecte costisitoare reutilizate, stare partajată + variabile separate?
  → FLYWEIGHT

opțiuni adăugate dinamic peste un obiect, fără explozie de clase?
  → DECORATOR

notificare automată a mai multor componente la schimbare de stare?
  → OBSERVER

clasă externă incompatibilă, integrare fără modificare?
  → ADAPTER

acțiune ca obiect, stocare și executare ulterioară?
  → COMMAND

interfață simplificată peste mai multe subsisteme complexe?
  → FACADE
```

---

## Perechi frecvente la subiecte

| Subiect | Pattern 1 | Pattern 2 | Logica perechii |
|---------|-----------|-----------|-----------------|
| Spital / OMS | Proxy | Composite / Memento | acces controlat + structură ierarhică |
| Restaurant | Decorator | Command / Composite | extensii produs + acțiuni comenzi |
| Magazin online | Observer | Strategy / Proxy | notificare stoc + filtrare produse |
| Platformă | Adapter | Proxy / CoR | integrare externă + control acces |
| Transport | Strategy | Composite | algoritm rută + structură stații |
| Hotel | Composite | Flyweight | structură camere + pictograme partajate |

---

## Greșeli comune

| Greșeală | Cum o eviți |
|----------|-------------|
| Confunzi Decorator cu Composite | Decorator = adaugă comportament. Composite = adaugă copii într-un arbore |
| Confunzi Proxy cu Decorator | Proxy = nu modifică rezultatul, doar controlează accesul. Decorator = modifică rezultatul |
| Confunzi Strategy cu CoR | Strategy = alegi O variantă. CoR = treci prin TOATE filtrele succesiv |
| Confunzi Adapter cu Facade | Adapter = interfață incompatibilă existentă. Facade = simplifici un sistem complex |
| Flyweight fără fabrică | Fără HashMap/cache nu e Flyweight — trebuie să returnezi aceeași instanță |
| Observer cu un singur ascultător hardcodat | Observer presupune listă dinamică — dacă e fix, nu e Observer |
