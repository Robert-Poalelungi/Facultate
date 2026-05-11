# Chain of Responsibility

Pattern **comportamental** — cererea trece printr-un lanț de handlere. Fiecare handler procesează și pasează mai departe (sau oprește lanțul).

---

## Participanți (din seminar)

| Rol | Clasă |
|-----|-------|
| Interfață handler | `IHandler` |
| Handler abstract | `AbstractHandler` — ține `IHandler nextHandler` |
| Handlere concrete | `FiltrarePret`, `FiltrareRecenzii`, `FiltrareProcentReducere` |
| Cerere | `ColectieProduse` + `Client` — ce se pasează prin lanț |
| Client | `Main` — leagă lanțul și trimite cererea |

---

## Explicație pas cu pas

**Ideea în o propoziție:** cererea (colecție de produse + preferințele clientului) trece prin mai mulți filtre unul după altul, fiecare elimină ce nu corespunde și pasează mai departe.

**Rețeta:**
1. Interfața handler-ului (`IHandler`) — metoda de procesare + `setNextHandler/getNextHandler`
2. Handler abstract (`AbstractHandler`) — gestionează `nextHandler`, lasă procesarea la concrete
3. Handlere concrete (`FiltrarePret` etc.) — procesează, apoi pasează la următor dacă există
4. Main — creează handlerele, leagă lanțul, trimite cererea primului

**Pasul 1 — Interfața**

Definești metoda de procesare (primește cererea) și metodele de gestionare a lanțului.

```java
public interface IHandler {
    ColectieProduse filtrareProduse(ColectieProduse colectie, Client client);
    void setNextHandler(IHandler nextHandler);
    IHandler getNextHandler();
}
```

**Pasul 2 — Handler-ul abstract**

Gestionează câmpul `nextHandler` și metodele aferente. Nu implementează logica de procesare — o lasă claselor concrete.

```java
public abstract class AbstractHandler implements IHandler {
    private IHandler nextHandler;

    @Override
    public void setNextHandler(IHandler nextHandler) { this.nextHandler = nextHandler; }

    @Override
    public IHandler getNextHandler() { return nextHandler; }
}
```

**Pasul 3 — Handler-ele concrete**

Fiecare extinde `AbstractHandler`, procesează cererea, apoi pasează la următor cu `getNextHandler()`. Dacă nu există următor, returnează rezultatul.

```java
public class FiltrarePret extends AbstractHandler {
    @Override
    public ColectieProduse filtrareProduse(ColectieProduse colectie, Client client) {
        // elimină produsele peste bugetul clientului
        for (var produs : colectie.getListaProduse()) {
            if (produs.getPret() > client.getBuget()) {
                colectie.removeProdus(produs);
            }
        }
        System.out.println("S-a filtrat dupa pret");
        // pasează mai departe dacă există următor
        if (this.getNextHandler() != null) {
            return this.getNextHandler().filtrareProduse(colectie, client);
        }
        return colectie;
    }
}
```

`FiltrareRecenzii` și `FiltrareProcentReducere` au aceeași structură — procesează după criteriul lor, apoi pasează.

**Pasul 4 — Main: leagă lanțul și pornește**

```java
IHandler f1 = new FiltrarePret();
IHandler f2 = new FiltrareRecenzii();
IHandler f3 = new FiltrareProcentReducere();

f1.setNextHandler(f2);   // f1 → f2 → f3
f2.setNextHandler(f3);

Client client = new Client("Gigel", 175, true, false);
ColectieProduse rezultat = f1.filtrareProduse(colectie, client); // pornește din f1
```

**Ce să ții minte:** `AbstractHandler` ține `private IHandler nextHandler`; concretele procesează și apoi apelează `getNextHandler().metoda()` dacă există următor; lanțul se leagă în Main cu `setNextHandler()`.

---

## Cod seminar

```java
public interface IHandler {
    ColectieProduse filtrareProduse(ColectieProduse colectie, Client client);
    void setNextHandler(IHandler nextHandler);
    IHandler getNextHandler();
}

public abstract class AbstractHandler implements IHandler {
    private IHandler nextHandler;

    @Override
    public void setNextHandler(IHandler nextHandler) { this.nextHandler = nextHandler; }

    @Override
    public IHandler getNextHandler() { return nextHandler; }
}

public class FiltrarePret extends AbstractHandler {
    @Override
    public ColectieProduse filtrareProduse(ColectieProduse colectie, Client client) {
        // procesare: elimină produsele peste buget
        for (var produs : colectie.getListaProduse()) {
            if (produs.getPret() > client.getBuget()) {
                colectie.removeProdus(produs);
            }
        }
        System.out.println("S-a filtrat dupa pret");
        // pasează mai departe dacă există următor
        if (this.getNextHandler() != null) {
            return this.getNextHandler().filtrareProduse(colectie, client);
        }
        return colectie;
    }
}

// FiltrareRecenzii și FiltrareProcentReducere — aceeași structură

// Main
IHandler f1 = new FiltrarePret();
IHandler f2 = new FiltrareRecenzii();
IHandler f3 = new FiltrareProcentReducere();

f1.setNextHandler(f2);   // leagă lanțul
f2.setNextHandler(f3);

Client client = new Client("Gigel", 175, true, false);
ColectieProduse rezultat = f1.filtrareProduse(colectie, client); // pornește din f1
```

---

## Structura la examen

1. **Interfață** `IHandler` cu metoda de procesare + `setNextHandler/getNextHandler`
2. **AbstractHandler** — implementează `setNextHandler/getNextHandler`, ține `private IHandler nextHandler`
3. **Handlere concrete** extind `AbstractHandler` — procesează, apoi `if (getNextHandler() != null) return getNextHandler().metoda(...)`
4. **Main** — creează handlerele, leagă lanțul cu `setNextHandler`, trimite cererea primului

---

## Cum recunoști

- „mai multe etape de filtrare / validare / procesare"
- „ordinea poate fi schimbată", „se pot adăuga noi filtre fără modificare"
- „dacă nu e parametrizat, nu se ține cont" — handlerul se poate sări
