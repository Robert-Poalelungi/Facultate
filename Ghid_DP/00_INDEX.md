# Ghid Design Patterns — Test 2 CTS

Toate pattern-urile structurale + comportamentale, cu cod Java explicat pas cu pas.

---

## Structurale

| # | Pattern | Idee principală | Când îl recunoști |
|---|---------|-----------------|-------------------|
| [03](03_Decorator.md) | **Decorator** | stivuiești „învelitori" peste un obiect | toppinguri, extras, prețul crește cu fiecare adăugire |
| [04](04_Facade.md) | **Facade** | o interfață simplă peste un subsistem complex | „simplifică", „un singur punct de intrare", mai multe subsisteme |
| [05](05_Proxy.md) | **Proxy** | intermediar cu aceeași interfață ca originalul | control acces, lazy loading, logging, cache |
| [06](06_Adapter.md) | **Adapter** | face două interfețe incompatibile să lucreze împreună | „legacy", „nu poți modifica clasa", „integrare" |
| [02](02_Composite.md) | **Composite** | structură arbore: frunze + noduri tratate uniform | ierarhii, departamente/angajați, foldere/fișiere |

---

## Comportamentale

| # | Pattern | Idee principală | Când îl recunoști |
|---|---------|-----------------|-------------------|
| [01](01_Chain_of_Responsibility.md) | **Chain of Responsibility** | cererea trece prin handlere în lanț | „verificatori succesivi", „pipeline", „aprobat/respins în trepte" |
| [09](09_Command.md) | **Command** | acțiunea e un obiect — se poate pune în coadă/undo | „coadă de comenzi", „execuție amânată", „undo" |
| [07](07_Observer.md) | **Observer** | mai mulți ascultători notificați la un eveniment | „notificare", „abonare", „subscripție" |
| [08](08_Strategy.md) | **Strategy** | algoritm interschimbabil la runtime | „mai mulți algoritmi pentru aceeași problemă", „selectare criteriu" |
| [10](10_State.md) | **State** | comportamentul se schimbă cu starea obiectului | „stări distincte", „bancomat", „comandă", „tranziții" |
| [11](11_Template_Method.md) | **Template Method** | scheletul algoritmului fix, pașii variabili în subclase | „pași comuni + pași diferiți", „preparare", „procesare" |
| [12](12_Memento.md) | **Memento** | salvează și restaurează starea anterioară | „undo", „rollback", „checkpoint", „stare anterioară" |

---

## Cum distingem pattern-urile similare

### Decorator vs Proxy
- **Decorator**: adaugă funcționalitate (`getPret() + 5`)
- **Proxy**: controlează accesul (`if (!arePermisiune()) return`)

### Strategy vs State
- **Strategy**: clientul schimbă algoritmul din exterior (`context.setStrategie(...)`)
- **State**: obiectul se schimbă singur intern (`context.setStare(new StareNoua())` din interiorul stărilor)

### Strategy vs Template Method
- **Strategy**: algoritmul întreg e interschimbabil (compoziție)
- **Template Method**: scheletul e fix, pașii variabili sunt în subclase (moștenire)

### Facade vs Adapter
- **Facade**: simplifică mai multe clase într-o interfață simplă
- **Adapter**: face o clasă incompatibilă să respecte o interfață cerută

### Command vs Strategy
- **Strategy**: un algoritm selectat, executat imediat
- **Command**: acțiuni împachetate, puse în coadă, executate mai târziu (sau undo)

---

## Structura comună la examen

### Orice pattern comportamental:
```
Interfață → Implementări concrete → Context/Client
```

### Orice pattern structural:
```
Componentă abstractă → Implementare simplă (Leaf/Real) + Implementare complexă (Composite/Proxy/Decorator)
```

---

## Template răspuns rapid la examen

**CoR**: `AHandler` cu `setUrmator()` + `pasezaMailDeparte()` → handlere concrete → Main leagă și trimite

**Composite**: `AComponenta` abstract + `Leaf` simplu + `Composite` cu `List<AComponenta>` recursiv

**Decorator**: `AComponenta` abstract + `ConcreteBase` + `ADecorator` (extinde AComponenta, ține AComponenta) + decoratori concreti cu `super.metoda() + adaos`

**Facade**: câteva clase subsistem + `Facade` care le orchestrează + Main apelează Facade

**Proxy**: interfață + RealSubject + Proxy (implementează interfața, ține RealSubject, adaugă logică)

**Adapter**: interfață target + Adaptee (existentă) + Adapter (implementează target, ține Adaptee, traduce)

**Observer**: `IObserver` + `ISubiect` + Subject concret (cu `List<IObserver>` + `notifyAll()`) + observatori

**Strategy**: `IStrategie` + strategii concrete + Context (ține IStrategie, delegă) + Main setează strategia

**Command**: `IComanda` + Receiver + comenzi concrete (țin Receiver) + Invoker (List<IComanda>) + Main

**State**: `IStare` + stări concrete (fac tranziții) + Context (delegă la stare) + Main

**Template Method**: clasă abstractă cu `final templateMethod()` + pași abstracti + subclase concrete

**Memento**: `Memento` (starea) + `Originator` (salvează/restaurează) + `Caretaker` (stiva de Memento)
