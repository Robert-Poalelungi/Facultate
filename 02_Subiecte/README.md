# Analiza subiectelor — Design Patterns CTS

---

## Frecvența pattern-urilor în subiecte (S01–S14)

| Pattern | Apare în | Frecvență |
|---------|----------|-----------|
| **COMPOSITE** | S02, S06, S07, S10, S11, S12 | ⭐⭐⭐⭐⭐⭐ |
| **PROXY** | S01, S10, S11, S13, S14 | ⭐⭐⭐⭐⭐ |
| **STRATEGY** | S03, S04, S05, S09 | ⭐⭐⭐⭐ |
| **CHAIN OF RESPONSIBILITY** | S03, S04, S05 | ⭐⭐⭐ |
| **MEMENTO** | S01, S02, S14 | ⭐⭐⭐ |
| **FLYWEIGHT** | S08, S12, S13 | ⭐⭐⭐ |
| **TEMPLATE METHOD** | S07, S08 | ⭐⭐ |
| **DECORATOR** | S06 | ⭐ |
| **OBSERVER** | S09 | ⭐ |

> **Facade, Adapter, Command, State nu apar în niciun subiect.**
>
> **Cele mai probabile la testul tău: COMPOSITE + PROXY sau STRATEGY + CoR**

---

## Fiecare subiect — ce pattern e și de ce

### S01 — Spital | Proxy + Memento
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Acces vizitatori cu restricții, modul intermediar | **PROXY** | „modul intermediar ce gestionează noile restricții" |
| Revenire la stare anterioară, utilizatorul poate stoca o versiune | **MEMENTO** | „revenire la stare anterioară", „stocarea unei versiuni anterioare" |

### S02 — Restaurant | Composite + Memento
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Parsare recursivă cod, structură ierarhică Item | **COMPOSITE** | „parsare recursivă", „structură ierarhică", „analiza tuturor elementelor de tip Item" |
| Revenire la versiunea anterioară de afișare | **MEMENTO** | „versiune anterioară de afișare", „revenire la stare salvată" |

### S03 — Aplicație Web | Strategy + CoR
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Tehnici de vizualizare produse, noi tehnici adăugabile | **STRATEGY** | „selecta tehnica de vizualizare", „se pot adăuga noi tehnici în timp" |
| Filtrare în mai multe etape, interschimbabile, extensibile | **CHAIN OF RESPONSIBILITY** | „filtrarea este formată din mai multe etape", „etapele pot fi interschimbate", „adăugare filtrări suplimentare" |

### S04 — Magazin Pantofi Online | CoR + Strategy
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Filtrare produse după criterii, ordine schimbabilă, pași opționali | **CHAIN OF RESPONSIBILITY** | „extindere prin adăugarea de noi criterii", „rearanjare ordine", „dacă nu e parametrizat, nu se ține cont" |
| Client alege parametrizare implicită sau proprie | **STRATEGY** | „alege între parametrizare implicită sau setarea proprie" |

### S05 — Bancomat | CoR + Strategy
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Retragere bancnote 50/20/10, tipuri noi, ordine schimbabilă | **CHAIN OF RESPONSIBILITY** | „adăugare de noi tipuri cu minim de modificare", „schimba ordinea de preluare" |
| Client alege toate tipurile sau alegere personalizată | **STRATEGY** | „posibilitatea de a alege tipul de bancnote dorite sau toate tipurile" |

### S06 — Restaurant | Decorator + Composite
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Topping culinar adăugat fără modificarea prețului de bază, extensibil | **DECORATOR** | „topping suplimentar", „nu conduce la modificarea prețului de bază", „adăugare noi specificuri culinare" |
| Meniu arborescent (produse + meniuri zilei formate din produse) | **COMPOSITE** | „arborescența meniului", „meniurile zilei formate din mai multe componente de tip produs" |

### S07 — Referendum | Composite + Template Method
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Voturi pe secții → județe, afișare centralizată, interfața AbstractRezultat | **COMPOSITE** | „niveluri: secții → județe", „centralizarea rezultatelor", „interfața AbstractRezultat" |
| Procedură cu pași ficși, pași diferiți pentru secții din țară vs. străinătate | **TEMPLATE METHOD** | „procedura este aceeași", „unele etape pot fi diferite", „șablon cu pași comuni și pași diferiți" |

### S08 — Spital | Template Method + Flyweight
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Protocol urgențe cu număr fix de pași, diferit spital stat vs. privat | **TEMPLATE METHOD** | „protocol general valabil format dintr-un număr fix de pași", „spital privat folosește echipă externă" |
| Printare rețete cu recomandări generale, optimizare memorie | **FLYWEIGHT** | „număr limitat de seturi de recomandări", „număr mare de rețete", „optimizează spațiul de memorie" |

### S09 — Magazin Online | Observer + Strategy
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Notificări clienți la reduceri, email/telefon, dezabonare | **OBSERVER** | „clienții pot fi informați", „email și/sau telefon", „dezabonare", „notificarea clienților abonați" |
| Plată card sau virament bancar | **STRATEGY** | „posibilitatea de a plăti prin card bancar sau prin virament bancar" |

### S10 — OMS / Spital | Proxy + Composite
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Acces vizitatori cu restricții, ISpital dată, fără modificare | **PROXY** | „modul intermediar", „conform noilor restricții", „interfața ISpital primită" |
| Gestiune arborescentă tulpini (continente → țări → tulpini) | **COMPOSITE** | „prezentare arborescentă", „continente → țări → tulpini", „număr total de cazuri" |

### S11 — Magazin Online | Proxy + Composite
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Discount 10% prima comandă, fără modificarea clasei Magazin | **PROXY** | „nu trebuie să implice modificări în codul existent", „modul intermediar" |
| Vizualizare produse arborescent, categorii/subcategorii | **COMPOSITE** | „manieră arborescentă", „minim două niveluri de agregare: categorii, subcategorii" |

### S12 — OMS | Flyweight + Composite
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Stocare centralizată virusuri unice, regăsire pe baza amprentei | **FLYWEIGHT** | „stochează la nivel centralizat virusurile unice", „regăsirea pe baza amprentei virusului" |
| Gestiune arborescentă tulpini (continente → țări → tulpini) | **COMPOSITE** | „gestiunea și prezentarea arborescentă", „afișarea numărului total de cazuri" |

### S13 — Spital | Proxy + Flyweight
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Acces restricționat certificat verde, modul intermediar | **PROXY** | „restricționat accesul", „modul intermediar ce gestionează noile restricții" |
| Recomandări diagnostice reutilizate la multe rețete, optimizare memorie | **FLYWEIGHT** | „număr limitat de diagnostice", „număr mare de rețete", „optimizează spațiul de memorie" |

### S14 — Magazin Online | Proxy + Memento
| Cerință | Pattern | Cuvinte cheie |
|---------|---------|---------------|
| Autentificare securizată, blocare după 5 greșeli, fără modificare modul existent | **PROXY** | „modul intermediar", „nu trebuie să implice modificări la nivelul actualului modul" |
| Revenire la stare anterioară coș cumpărături, salvare/restaurare | **MEMENTO** | „revenire la stare anterioară", „clientul poate stoca o versiune de coș", „reseta coșul curent pe baza coșului anterior" |

---

## Fraze cheie → Pattern (recunoaștere rapidă la test)

| Dacă citești... | Pattern |
|----------------|---------|
| „fără modificări în codul existent", „modul intermediar", „nu implică modificări" | **PROXY** |
| „arborescent", „minim 2-3 niveluri", „categorii și subcategorii", „număr total" | **COMPOSITE** |
| „poate alege între", „algoritm interschimbabil", „moduri diferite de..." | **STRATEGY** |
| „adăugare noi tipuri cu minim modificări", „rearanjare ordine", „ignorat dacă nu e setat" | **CHAIN OF RESPONSIBILITY** |
| „notificări", „abonare/dezabonare", „email și/sau telefon", „mai mulți clienți interesați" | **OBSERVER** |
| „revenire la stare anterioară", „salvare", „restaurare", „undo", „coș anterior salvat" | **MEMENTO** |
| „topping", „fără modificare preț de bază", „adăugare dinamic", „specificuri noi" | **DECORATOR** |
| „protocol fix de pași", „același algoritm, comportament diferit în subclase" | **TEMPLATE METHOD** |
| „optimizare memorie", „număr limitat de seturi reutilizate de N ori", „stocare centralizată" | **FLYWEIGHT** |

---

## Motivarea pattern-ului (1p la fiecare cerință — nu uita!)

### PROXY
> Am ales pattern-ul **Proxy** deoarece se dorește adăugarea unui comportament suplimentar (autentificare securizată / discount / acces restricționat) fără modificarea clasei existente. Proxy-ul implementează aceeași interfață ca obiectul real (`IAutentificare` / `IMagazin` / `ISpital`), interceptează apelurile și adaugă logica suplimentară înainte de a delega la obiectul real. Astfel, codul existent rămâne nemodificat (OCP).

### COMPOSITE
> Am ales pattern-ul **Composite** deoarece structura este arborescentă, cu noduri de tip container (categorii/departamente/județe) și frunze (produse/angajați/secții) tratate uniform prin interfața comună. Operațiile (afișare, calcul total) se propagă recursiv în arbore, permițând tratarea uniformă a elementelor individuale și a grupurilor.

### STRATEGY
> Am ales pattern-ul **Strategy** deoarece există mai mulți algoritmi interșanjabili pentru aceeași problemă (plată card/virament, vizualizare crescător/descrescător) și se dorește schimbarea lor la runtime fără modificarea contextului. Contextul delegă execuția strategiei curente, respectând OCP — noi strategii se adaugă fără modificări.

### CHAIN OF RESPONSIBILITY
> Am ales pattern-ul **Chain of Responsibility** deoarece cererea trebuie procesată de mai mulți handlere succesivi (tipuri de bancnote / criterii de filtrare), ordinea lor poate fi schimbată, și se pot adăuga noi handlere fără modificarea celor existente. Fiecare handler decide dacă procesează cererea sau o pasează mai departe.

### OBSERVER
> Am ales pattern-ul **Observer** deoarece există o relație one-to-many: un subiect (magazinul) trebuie să notifice automat mai mulți observatori (clienți prin email/telefon) la apariția unui eveniment (reducere de preț). Clienții se pot abona/dezabona dinamic fără modificarea subiectului.

### MEMENTO
> Am ales pattern-ul **Memento** deoarece se dorește salvarea și restaurarea stării anterioare a unui obiect (coș de cumpărături / afișare) fără a expune detaliile implementării. Originator-ul creează un Memento cu starea curentă, iar Caretaker-ul îl gestionează fără să cunoască conținutul.

### DECORATOR
> Am ales pattern-ul **Decorator** deoarece se dorește adăugarea dinamică de comportament (topping specific) unui obiect existent (produs), fără modificarea clasei de bază și fără explozie de subclase. Decoratorul implementează aceeași interfață `IProdus` și adaugă funcționalitate prin delegare.

### TEMPLATE METHOD
> Am ales pattern-ul **Template Method** deoarece există un algoritm cu structură fixă (protocol de urgențe / procedură de votare) în care anumiți pași diferă între implementări (spital stat vs. privat / secție în țară vs. în străinătate). Clasa abstractă definește scheletul (`final`), iar subclasele implementează doar pașii variabili.

### FLYWEIGHT
> Am ales pattern-ul **Flyweight** deoarece există un număr limitat de obiecte (seturi de recomandări / virusuri unice) care sunt reutilizate de un număr mare de instanțe (rețete / tulpini). Starea intrinsecă (comună, neschimbată) e stocată o singură dată în flyweight, iar starea extrinsecă (specifică fiecărei utilizări) e pasată ca parametru. Astfel se optimizează consumul de memorie.

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

## Cerinte_Diverse — cerințe suplimentare de la profesoară

Folderul `Cerinte_Diverse/` conține cerințe practice (nu subiecte de examen anterioare):

| Cerință | Pattern |
|---------|---------|
| Telecomandă universală (locuință inteligentă) | **Command** |
| Sistem tranzacționare bursă (cumpărare/vânzare) | **Command** |
| Telefon USB-C + încărcător MicroUSB | **Adapter** |
| Referendum (secții → județe → național) | **Composite** |
| Companie design interior (vizualizare 2D/3D/Detalii) | **Strategy** |
| Randări AI camere (bucătărie, baie, living, dining) | **Flyweight** |

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
