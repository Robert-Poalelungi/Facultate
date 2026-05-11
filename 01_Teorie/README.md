# Ghid Design Patterns — Test 2 CTS

Ordonate după probabilitatea de apariție la test (bazat pe S01–S14).
✅ = făcut la seminar | 📖 = doar curs/laborator

---

## Intră la test — prioritate înaltă

| Prob. | Seminar | Pattern | Fișier | Idee principală | Când îl recunoști |
|-------|---------|---------|--------|-----------------|-------------------|
| ⭐⭐⭐⭐⭐⭐ (6/14) | ✅ S02, S09 | **Composite** | [01](01_Composite/README.md) | structură arbore: frunze + noduri tratate uniform | „arborescent", „categorii/subcategorii", „număr total", ierarhii |
| ⭐⭐⭐⭐⭐ (5/14) | ✅ S08 | **Proxy** | [02](02_Proxy/README.md) | intermediar cu aceeași interfață ca originalul | „modul intermediar", „fără modificarea codului existent", control acces |
| ⭐⭐⭐⭐ (4/14) | ✅ S03, S10 | **Strategy** | [03](03_Strategy/README.md) | algoritm interschimbabil la runtime | „clientul poate alege între", „mai mulți algoritmi pentru aceeași problemă" |
| ⭐⭐⭐ (3/14) | ✅ S09 | **Chain of Responsibility** | [04](04_Chain_of_Responsibility/README.md) | cererea trece prin handlere în lanț | „adăugare noi tipuri cu minim modificare", „ordine schimbabilă", „etape înlănțuite" |
| ⭐⭐⭐ (3/14) | ✅ S11 | **Flyweight** | [05](05_Flyweight/README.md) | partajare obiecte pentru reducerea memoriei | „număr limitat de X reutilizat de N instanțe", „optimizare memorie", „stocare centralizată" |
| ⭐ (1/14) | ✅ S08 | **Decorator** | [06](06_Decorator/README.md) | stivuiești „învelitori" peste un obiect | „topping", „fără modificare preț de bază", „adăugare dinamică de specificuri" |
| ⭐ (1/14) | ✅ S10 | **Observer** | [07](07_Observer/README.md) | mai mulți ascultători notificați la un eveniment | „notificare", „abonare/dezabonare", „email și/sau telefon" |
| 0/14 | ✅ S10, S11 | **Adapter** | [08](08_Adapter/README.md) | face două interfețe incompatibile să lucreze împreună | „legacy", „nu poți modifica clasa", „integrare" |
| 0/14 | 📖 | **Facade** | [09](09_Facade/README.md) | o interfață simplă peste un subsistem complex | „simplifică", „un singur punct de intrare", mai multe subsisteme |
| 0/14 | 📖 | **Command** | [10](10_Command/README.md) | acțiunea e un obiect — se poate pune în coadă/undo | „coadă de comenzi", „execuție amânată", „undo" |

---

## Cum distingem pattern-urile similare

### Decorator vs Proxy
- **Decorator**: adaugă funcționalitate (`getPret() + 5`)
- **Proxy**: controlează accesul (`if (!arePermisiune()) return`)

### Facade vs Adapter
- **Facade**: simplifică mai multe clase într-o interfață simplă
- **Adapter**: face o clasă incompatibilă să respecte o interfață cerută

### Command vs Strategy
- **Strategy**: un algoritm selectat, executat imediat
- **Command**: acțiuni împachetate, puse în coadă, executate mai târziu (sau undo)

---

## Template răspuns rapid la examen

**Composite**: interfață comună + nod container (`List<INod>`, `for` recursiv) + frunză (returnează valoarea proprie, aruncă excepție la metodele de container)

**Proxy**: interfață + RealSubject + Proxy (implementează interfața, ține `private IReal real`, adaugă logică înainte de delegare)

**Strategy**: `IStrategie` + strategii concrete + Context (ține `private IStrategie s`, `setStrategie()`, delegă în metodă)

**CoR**: `IHandler` + `AbstractHandler` (ține `private IHandler next`) + handlere concrete (procesează, pasează la `getNextHandler()`) + Main leagă lanțul

**Flyweight**: `IFlyweight` + flyweight concret (stare intrinsecă) + `FabricaDeXxx` cu `static Map` + `static {}` + stare extrinsecă pasată la metodă

**Decorator**: interfață + bază concretă + decorator abstract (ține `private IComanda c`, delegă toate) + decorator concret (suprascrie cu `super.metoda()`)

**Observer**: `IObserver` + `ISubiect` + subiect concret (`List<IObserver>`, `for` în `notifica()`, notifică în setter) + observatori concreti

**Adapter**: interfață target + Adaptee (existentă) + Adapter (implementează target, traduce apelul spre Adaptee)

**Facade**: câteva clase subsistem + `Facade` care le orchestrează + Main apelează Facade

**Command**: `IComanda` + Receiver + comenzi concrete (țin Receiver) + Invoker (`List<IComanda>`) + Main
