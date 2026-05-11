# Strategy

Pattern **comportamental** — algoritmul este interschimbabil la runtime. Contextul delegă execuția strategiei curente.

---

## Participanți (din seminar)

| Rol | Clasă |
|-----|-------|
| Interfață strategie | `IStrategy` |
| Strategii concrete | `PlataCard`, `PlataCash` |
| Context | `Bon` — ține `IStrategy strategie`, apelează `strategie.plata()` |
| Client | `Main` — setează strategia pe context |

---

## Explicație pas cu pas

**Ideea în o propoziție:** contextul (Bon) nu știe CUM se face plata — delegă la strategia curentă care poate fi schimbată oricând la runtime.

**Rețeta:**
1. Interfața strategiei (`IStrategy`) cu metoda algoritmului
2. Strategii concrete (`PlataCard`, `PlataCash`) — fiecare cu logica proprie
3. Context (`Bon`) — ține `private IStrategy strategie`, are `setStrategie()`, delegă
4. Main — creează contextul, setează strategia, apelează

**Pasul 1 — Interfața strategiei**

Definești metoda pe care toate strategiile trebuie să o implementeze.

```java
public interface IStrategy {
    void plata(int suma);
}
```

**Pasul 2 — Strategii concrete**

Fiecare implementează logica proprie. Nu știu nimic despre context.

```java
public class PlataCard implements IStrategy {
    @Override
    public void plata(int suma) {
        System.out.println("Plata card " + suma);
    }
}

public class PlataCash implements IStrategy {
    @Override
    public void plata(int suma) {
        System.out.println("Plata cash " + suma);
    }
}
```

**Pasul 3 — Contextul (Bon)**

Ține `private IStrategy strategie`. Metoda `setStrategie()` permite schimbarea la runtime. Metoda de business (`inchideBon()`) delegă la strategie.

```java
public class Bon {
    private IStrategy strategie;
    private float total;

    public Bon(float total) { this.total = total; }

    public void setStrategie(IStrategy strategie) { this.strategie = strategie; }

    public void inchideBon() {
        if (this.strategie != null) {
            this.strategie.plata((int) total); // delegă la strategie
        }
    }
}
```

**Pasul 4 — Main**

Creezi contextul, setezi strategia (poate fi schimbată oricând), apelezi metoda.

```java
Bon bon = new Bon(100f);
bon.setStrategie(new PlataCash());
bon.inchideBon();   // "Plata cash 100"

bon.setStrategie(new PlataCard());
bon.inchideBon();   // "Plata card 100"
```

**Ce să ții minte:** contextul are `private IStrategy strategie` + `setStrategie()`; metoda de business delegă la `strategie.metoda()`; strategia poate fi schimbată la runtime fără a modifica contextul.

---

## Cod seminar

```java
public interface IStrategy {
    void plata(int suma);
}

public class PlataCard implements IStrategy {
    @Override
    public void plata(int suma) {
        System.out.println("Plata card " + suma);
    }
}

public class PlataCash implements IStrategy {
    @Override
    public void plata(int suma) {
        System.out.println("Plata cash " + suma);
    }
}

public class Bon {                         // Context
    private IStrategy strategie;
    private float total;

    public Bon(float total) { this.total = total; }

    public void setStrategie(IStrategy strategie) { this.strategie = strategie; }

    public void inchideBon() {
        if (this.strategie != null) {
            this.strategie.plata((int) total); // delegă la strategie
        }
    }
}

// Main
Bon bon = new Bon(100f);
bon.setStrategie(new PlataCash());
bon.inchideBon();   // "Plata cash 100"

bon.setStrategie(new PlataCard());
bon.inchideBon();   // "Plata card 100"
```

---

## Structura la examen

1. **Interfață** `IStrategy` cu metoda algoritmului (ex. `plata`, `filtrare`, `vizualizare`)
2. **Strategii concrete** implementează `IStrategy` — fiecare cu logica proprie
3. **Context** `Bon` — câmp `private IStrategy strategie`, metodă `setStrategie()`, metodă care delegă
4. **Main** — creează contextul, setează strategia, apelează metoda

---

## Cum recunoști

- „clientul poate alege între X, Y, Z moduri de a face același lucru"
- „plată card sau virament", „vizualizare crescător sau descrescător"
- Comportament ales la runtime, schimbabil fără modificarea contextului
