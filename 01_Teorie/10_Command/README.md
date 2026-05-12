# Command

Pattern **comportamental** — acțiunea este împachetată într-un obiect. Comenzile pot fi puse în coadă și executate amânat, fără ca invoker-ul să știe ce face concret fiecare comandă.

---

## Participanți (din seminar — S12)

| Rol | Clasă |
|-----|-------|
| Interfață comandă | `IComanda` — `executa()` |
| Receiver | `ActiuneBursa` — face munca efectivă (buy/sell) |
| Comenzi concrete | `ComandaBuy`, `ComandaSell` — țin referința la receiver |
| Invoker | `Broker` — ține `List<IComanda>`, execută amânat cu `lansareIntarziata()` |
| Client | `Main` |

---

## Explicație pas cu pas

**Ideea în o propoziție:** brokerul nu știe cum se cumpără/vinde — el doar ține comenzile și le execută toate odată; fiecare comandă știe singură ce să facă.

**Rețeta:**
1. Interfața `IComanda` cu `executa()`
2. Receiver (`ActiuneBursa`) — face munca reală
3. Comenzi concrete (`ComandaBuy`, `ComandaSell`) — țin receiver + parametri, implementează `executa()`
4. Invoker (`Broker`) — `List<IComanda>`, `addComanda()`, `lansareIntarziata()`
5. Main — creează receiver, creează comenzi, le adaugă la invoker, declanșează execuția

**Pasul 1 — Interfața**

```java
public interface IComanda {
    void executa();
}
```

**Pasul 2 — Receiver**

Face munca efectivă. Nu știe nimic despre comenzi sau invoker.

```java
public class ActiuneBursa {
    private String ticker;
    private int stoc;

    public ActiuneBursa(String ticker, int stoc) {
        this.ticker = ticker;
        this.stoc = stoc;
    }

    public void buy(int cantitate) {
        this.stoc += cantitate;
        System.out.println("S-a cumparat " + cantitate + " pentru " + ticker);
    }

    public void sell(int cantitate) {
        if (this.stoc >= cantitate) {
            this.stoc -= cantitate;
            System.out.println("S-a vandut " + cantitate + " pentru " + ticker);
        } else {
            System.out.println("Stoc insuficient pentru vanzare " + ticker);
        }
    }
}
```

**Pasul 3 — Comenzi concrete**

Fiecare ține `private ActiuneBursa executant` + parametrii necesari. `executa()` apelează metoda corespunzătoare pe receiver.

```java
public class ComandaBuy implements IComanda {
    private ActiuneBursa executant;
    private int cantitate;

    public ComandaBuy(ActiuneBursa executant, int cantitate) {
        this.executant = executant;
        this.cantitate = cantitate;
    }

    @Override
    public void executa() { this.executant.buy(cantitate); }
}

public class ComandaSell implements IComanda {
    private ActiuneBursa executant;
    private int cantitate;

    public ComandaSell(ActiuneBursa executant, int cantitate) {
        this.executant = executant;
        this.cantitate = cantitate;
    }

    @Override
    public void executa() { this.executant.sell(cantitate); }
}
```

**Pasul 4 — Invoker (Broker)**

Ține lista de comenzi. Nu știe ce face fiecare — apelează doar `executa()`.

```java
public class Broker {
    private String nume;
    private List<IComanda> comenzi = new ArrayList<>();

    public Broker(String nume) { this.nume = nume; }

    public void addComanda(IComanda comanda) { this.comenzi.add(comanda); }

    public void lansareIntarziata() {
        for (IComanda comanda : comenzi) comanda.executa();
        comenzi.clear();
    }
}
```

**Pasul 5 — Main**

```java
ActiuneBursa a1 = new ActiuneBursa("AAPL", 500);
ActiuneBursa a2 = new ActiuneBursa("MSFT", 500);

Broker broker = new Broker("Broker");

broker.addComanda(new ComandaBuy(a1, 200));
broker.addComanda(new ComandaBuy(a2, 300));
broker.addComanda(new ComandaSell(a1, 1000)); // stoc insuficient
broker.addComanda(new ComandaSell(a1, 100));

broker.lansareIntarziata();
```

**Ce să ții minte:** invoker-ul (`Broker`) nu știe ce face comanda — apelează doar `executa()`; comanda concretă ține receiver-ul și parametrii; execuția e amânată până la `lansareIntarziata()`.

---

## Cod seminar (S12)

```java
public interface IComanda {
    void executa();
}

public class ActiuneBursa {
    private String ticker;
    private int stoc;

    public ActiuneBursa(String ticker, int stoc) { this.ticker = ticker; this.stoc = stoc; }

    public void buy(int cantitate) {
        this.stoc += cantitate;
        System.out.println("S-a cumparat " + cantitate + " pentru " + ticker);
    }

    public void sell(int cantitate) {
        if (this.stoc >= cantitate) { this.stoc -= cantitate; System.out.println("S-a vandut " + cantitate + " pentru " + ticker); }
        else System.out.println("Stoc insuficient pentru vanzare " + ticker);
    }
}

public class ComandaBuy implements IComanda {
    private ActiuneBursa executant;
    private int cantitate;

    public ComandaBuy(ActiuneBursa executant, int cantitate) { this.executant = executant; this.cantitate = cantitate; }

    @Override public void executa() { this.executant.buy(cantitate); }
}

public class ComandaSell implements IComanda {
    private ActiuneBursa executant;
    private int cantitate;

    public ComandaSell(ActiuneBursa executant, int cantitate) { this.executant = executant; this.cantitate = cantitate; }

    @Override public void executa() { this.executant.sell(cantitate); }
}

public class Broker {  // Invoker
    private String nume;
    private List<IComanda> comenzi = new ArrayList<>();

    public Broker(String nume) { this.nume = nume; }

    public void addComanda(IComanda comanda) { this.comenzi.add(comanda); }

    public void lansareIntarziata() {
        for (IComanda comanda : comenzi) comanda.executa();
        comenzi.clear();
    }
}

// Main
ActiuneBursa a1 = new ActiuneBursa("AAPL", 500);
ActiuneBursa a2 = new ActiuneBursa("MSFT", 500);
Broker broker = new Broker("Broker");

broker.addComanda(new ComandaBuy(a1, 200));
broker.addComanda(new ComandaBuy(a2, 300));
broker.addComanda(new ComandaSell(a1, 1000));
broker.addComanda(new ComandaSell(a1, 100));

broker.lansareIntarziata();
```

---

## Structura la examen

1. **Interfață** `IComanda` cu `executa()`
2. **Receiver** — clasa care face munca reală (nu știe de comenzi)
3. **Comenzi concrete** — fiecare ține `private Receiver r` + parametri, implementează `executa()` apelând receiver-ul
4. **Invoker** — `List<IComanda>`, `addComanda()`, metodă de execuție în masă
5. **Main** — creează receiver, creează comenzi cu receiver-ul, le adaugă la invoker

---

## Cum recunoști

- „coadă de comenzi", „execuție amânată"
- „obiectul care declanșează nu depinde de implementarea concretă"
- „ordine de cumpărare / vânzare", „acțiunile sunt obiecte care pot fi stocate"
