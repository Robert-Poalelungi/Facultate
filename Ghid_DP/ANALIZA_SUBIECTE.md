# Analiza tuturor subiectelor — ce apare și cum recunoști

---

## Frecvența pattern-urilor în subiecte

| Pattern | Apare în | Frecvență |
|---------|----------|-----------|
| **COMPOSITE** | S7, S9(alt s1), alt s4 | ⭐⭐⭐⭐⭐ |
| **STRATEGY** | S8, S10, S11, alt s3 | ⭐⭐⭐⭐⭐ |
| **PROXY** | S7, S9, alt s1 | ⭐⭐⭐⭐ |
| **CHAIN OF RESPONSIBILITY** | S10, S11, alt s3 | ⭐⭐⭐⭐ |
| **OBSERVER** | S8 | ⭐⭐⭐ |
| **MEMENTO** | S9 | ⭐⭐⭐ |
| **DECORATOR** | alt s4 | ⭐⭐⭐ |
| **TEMPLATE METHOD** | alt s2 | ⭐⭐ |
| **FLYWEIGHT** | alt s2 | ⭐ |

> **Cele mai probabile la testul tău: COMPOSITE + STRATEGY sau PROXY + CoR**

---

## Fiecare subiect — ce pattern e și de ce

### S7 — Magazin online
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Discount 10% primă comandă, fără modificarea clasei Magazin | **PROXY** | „nu implică modificări în codul existent", „modul intermediar" |
| Vizualizare produse arborescent, categorii/subcategorii | **COMPOSITE** | „arborescent", „categorii", „minim 2 niveluri de agregare" |

### S8 — Magazin online
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Notificări clienți (email/telefon) la reduceri, dezabonare | **OBSERVER** | „notificări", „abonare/dezabonare", „email și/sau telefon" |
| Plată card sau virament bancar | **STRATEGY** | „poate alege", „modul de decizie a plății", două moduri diferite |

### S9 — Magazin online
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Autentificare securizată, blocare după 5 greșeli, fără modificare modul existent | **PROXY** | „nu trebuie să implice modificări", „modul intermediar securizat" |
| Revenire la stare anterioară coș cumpărături, salvare/restaurare | **MEMENTO** | „revenire la stare anterioară", „salvare", „restaurare" |

### S10 — Bancomat
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Retragere bancnote 50/20/10, adăugare noi tipuri ușor, schimbare ordine | **CHAIN OF RESPONSIBILITY** | „adăugare de noi tipuri cu minim de modificare", „schimba ordinea" |
| Client alege tipul de bancnote (toate sau personalizat) | **STRATEGY** | „poate alege", „utilizarea tuturor tipurilor sau o alegere personalizată" |

### S11 — Magazin online pantofi
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Filtrare produse după criterii, extindere cu noi criterii, rearanjare ordine, ignorat dacă nu parametrizat | **CHAIN OF RESPONSIBILITY** | „extindere prin adăugare noi criterii", „rearanjare ordine", „nu se ține cont dacă nu e parametrizat" |
| Client alege parametrizare implicită sau proprie | **STRATEGY** | „poate alege între", „parametrizare implicită sau proprie" |

### alt s1 — OMS / Spital
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Acces vizitatori cu restricții, modul intermediar, ISpital dată | **PROXY** | „modul intermediar", „conform noilor restricții", „interfața ISpital primită" |
| Gestiune arborescentă tulpini virusuri (continente > țări > tulpini) | **COMPOSITE** | „arborescent", „3 nivele", „număr total de cazuri" |

### alt s2 — Spital
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Protocol urgențe cu pași ficși, diferit spital stat vs privat | **TEMPLATE METHOD** | „protocol general valabil", „număr fix de pași", „diferit pentru privat" |
| Printare rețete cu recomandări generale, optimizare memorie (puține seturi, multe rețete) | **FLYWEIGHT** | „număr limitat de seturi", „număr mare de rețete", „optimizează spațiul de memorie" |

### alt s3 — Aplicație web
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Tehnici de vizualizare produse, noi tehnici adăugabile în timp | **STRATEGY** | „poate opta între", „noi tehnici adăugabile", „tehnica de vizualizare" |
| Filtrare elemente pagină web, etape interschimbabile, adăugare filtrări noi | **CHAIN OF RESPONSIBILITY** | „mai multe etape", „pot fi interschimbate", „adăugare filtrări suplimentare" |

### alt s4 — Restaurant
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Topping spaniol/italian adăugat la produse, fără modificare preț, adăugare noi specificuri | **DECORATOR** | „topping suplimentar", „fără modificare preț de bază", „adăugare noi specificuri" |
| Meniu restaurant arborescent (categorii > produse + meniuri zilei) | **COMPOSITE** | „arborescența meniului", „meniuri zilei formate din produse", „IProdus" |

---

## Fraze cheie → Pattern (pentru recunoaștere rapidă la test)

| Dacă citești... | Pattern |
|----------------|---------|
| „fără modificări în codul existent", „modul intermediar", „nu implică modificări" | **PROXY** |
| „arborescent", „minim 3 niveluri", „categorii și subcategorii", „număr total" | **COMPOSITE** |
| „poate alege între", „algoritm interschimbabil", „moduri diferite de..." | **STRATEGY** |
| „adăugare noi tipuri cu minim modificări", „rearanjare ordine", „ignorat dacă nu e setat" | **CHAIN OF RESPONSIBILITY** |
| „notificări", „abonare/dezabonare", „email și/sau telefon", „mai mulți clienți interesați" | **OBSERVER** |
| „revenire la stare anterioară", „salvare", „restaurare", „undo", „cos anterior salvat" | **MEMENTO** |
| „topping", „fără modificare preț de bază", „adăugare dinamic", „specificuri noi" | **DECORATOR** |
| „protocol fix de pași", „același algoritm, comportament diferit în subclase" | **TEMPLATE METHOD** |
| „optimizare memorie", „număr limitat de seturi refolosite de N ori" | **FLYWEIGHT** |

---

## Motivarea pattern-ului (1p la fiecare cerință — nu uita!)

Copiază și adaptează fraza de mai jos pentru fiecare pattern:

### PROXY
> Am ales pattern-ul **Proxy** deoarece se dorește adăugarea unui comportament suplimentar (autentificare securizată / discount / acces restricționat) fără modificarea clasei existente. Proxy-ul implementează aceeași interfață ca obiectul real (`IAutentificare` / `IMagazin` / `ISpital`), interceptează apelurile și adaugă logica suplimentară înainte de a delega la obiectul real. Astfel, codul existent rămâne nemodificat (OCP).

### COMPOSITE
> Am ales pattern-ul **Composite** deoarece structura este arborescentă, cu noduri de tip container (categorii/departamente) și frunze (produse/angajați) tratate uniform prin interfața `IProdus` / `IComponenta`. Operațiile (afișare, calcul total) se propagă recursiv în arbore, permițând tratarea uniformă a elementelor individuale și a grupurilor.

### STRATEGY
> Am ales pattern-ul **Strategy** deoarece există mai mulți algoritmi interșanjabili pentru aceeași problemă (plată card/virament, vizualizare crescător/descrescător) și se dorește schimbarea lor la runtime fără modificarea contextului. Contextul delegă execuția strategiei curente, respectând OCP — noi strategii se adaugă fără modificări.

### CHAIN OF RESPONSIBILITY
> Am ales pattern-ul **Chain of Responsibility** deoarece cererea trebuie procesată de mai mulți handlere succesivi (tipuri de bancnote / criterii de filtrare), ordinea lor poate fi schimbată, și se pot adăuga noi handlere fără modificarea celor existente. Fiecare handler decide dacă procesează cererea sau o pasează mai departe.

### OBSERVER
> Am ales pattern-ul **Observer** deoarece există o relație one-to-many: un subiect (magazinul) trebuie să notifice automat mai mulți observatori (clienți prin email/telefon) la apariția unui eveniment (reducere de preț). Clienții se pot abona/dezabona dinamic fără modificarea subiectului.

### MEMENTO
> Am ales pattern-ul **Memento** deoarece se dorește salvarea și restaurarea stării anterioare a unui obiect (coș de cumpărături) fără a expune detaliile implementării. Originator-ul (clientul) creează un Memento cu starea curentă, iar Caretaker-ul (managerul stărilor) îl gestionează fără să cunoască conținutul.

### DECORATOR
> Am ales pattern-ul **Decorator** deoarece se dorește adăugarea dinamică de comportament (topping specific) unui obiect existent (produs), fără modificarea clasei de bază și fără explozie de subclase. Decoratorul implementează aceeași interfață `IProdus` și adaugă funcționalitate prin delegare.

### TEMPLATE METHOD
> Am ales pattern-ul **Template Method** deoarece există un algoritm cu structură fixă (protocol de urgențe) în care anumiți pași diferă între implementări (spital stat vs privat). Clasa abstractă definește scheletul (`final`), iar subclasele implementează doar pașii variabili.

---

## OBLIGATORIU — Clean Code la test (pierde 2p per greșeală, max 8p)

### 1. Pachete — cel mai important!
```
cts.poalelungi.robert.g[NrGrupa].proxy
cts.poalelungi.robert.g[NrGrupa].composite
cts.poalelungi.robert.g[NrGrupa].strategy
cts.poalelungi.robert.g[NrGrupa].main
```

Fiecare pattern în pachet separat. Main în pachetul `.main`.

```java
package cts.poalelungi.robert.g1090.proxy;   // exemplu

public class ProxyAutentificare implements IAutentificare {
    ...
}
```

### 2. Denumiri legate de subiect — NU generice!
- ❌ `Handler`, `ConcreteStrategy`, `Leaf`
- ✅ `VerificatorBancnota50`, `StrategiePlataCuCard`, `ProdusIndividual`

### 3. Mesaje la consolă legate de context
```java
System.out.println("Clientul " + nume + " a primit notificare: " + mesaj);
// NU: System.out.println("notificare trimisa");
```

### 4. DIP — Dependency Inversion Principle
Depinde de interfețe, nu de implementări concrete:
```java
// ✅ corect
private IClient client;
private IStrategie strategie;

// ❌ greșit
private ClientConcret client;
private StrategieCard strategie;
```

---

## Structura unui fișier Main tipic

```java
package cts.poalelungi.robert.g1090.main;

import cts.poalelungi.robert.g1090.proxy.*;
import cts.poalelungi.robert.g1090.composite.*;

public class Main {
    public static void main(String[] args) {
        // === PROXY ===
        // setup
        // teste (minim cele cerute în subiect)

        System.out.println("===================");

        // === COMPOSITE ===
        // setup
        // teste
    }
}
```
