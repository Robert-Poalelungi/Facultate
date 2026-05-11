# Decorator

Pattern **structural** — adaugă dinamic funcționalitate unui obiect existent fără a-i modifica clasa. Decoratorul implementează aceeași interfață și delegă la obiectul decorat.

---

## Participanți (din seminar)

| Rol | Clasă |
|-----|-------|
| Interfață comună | `IComanda` |
| Implementare de bază | `Comanda` — logica de bază (adaugă produse, calculează total) |
| Decorator abstract | `DecoratorAbstract` — ține `IComanda comanda`, delegă toate metodele |
| Decorator concret | `DecoratorMartie` — suprascrie `getTotal()` și `printeazaBon()` cu comportament extra |
| Client | `Main` |

---

## Explicație pas cu pas

**Ideea în o propoziție:** „învelești" un obiect (`Comanda`) în altul (`DecoratorMartie`) care are aceeași interfață — decoratorul adaugă comportament înainte/după fără să modifice clasa de bază.

**Rețeta:**
1. Interfața comună (`IComanda`)
2. Implementarea de bază (`Comanda`) — logica normală
3. Decorator abstract — ține `private IComanda comanda`, delegă TOATE metodele
4. Decorator concret — extinde abstractul, suprascrie metodele de interes cu comportament extra + `super.metoda()`
5. Main — `new DecoratorX(new Comanda(...), parametri)`

**Pasul 1 — Interfața comună**

Toți participanții (baza și decoratorii) implementează aceeași interfață.

```java
public interface IComanda {
    void inchideComanda();
    void addProdus(float pret);
    void printeazaBon();
    double getTotal();
}
```

**Pasul 2 — Implementarea de bază**

Logica normală, fără niciun decorator. Calculează totalul, gestionează starea comenzii.

```java
public class Comanda implements IComanda {
    private int id;
    private List<Float> listaProduse = new ArrayList<>();
    private boolean esteInchisa = false;

    @Override public void addProdus(float pret) { listaProduse.add(pret); }

    @Override
    public void inchideComanda() {
        if (!esteInchisa) { esteInchisa = true; System.out.println("Comanda s-a inchis"); }
        else System.out.println("Comanda este deja inchisa.");
    }

    @Override
    public void printeazaBon() {
        if (esteInchisa) System.out.println("Comanda " + id + " | Total: " + getTotal());
        else System.out.println("Nu se poate printa bon pe comanda deschisa.");
    }

    @Override
    public double getTotal() {
        float sum = 0; for (Float f : listaProduse) sum += f; return sum;
    }
}
```

**Pasul 3 — Decoratorul abstract**

Ține `private IComanda comanda` (obiectul decorat). Delegă TOATE metodele — este esențial să le delegi pe toate, chiar dacă le suprascrii în concrete.

```java
public abstract class DecoratorAbstract implements IComanda {
    private IComanda comanda;   // obiectul decorat

    public DecoratorAbstract(IComanda comanda) { this.comanda = comanda; }

    // delegă totul la comanda decorată
    @Override public void inchideComanda() { this.comanda.inchideComanda(); }
    @Override public void addProdus(float pret) { this.comanda.addProdus(pret); }
    @Override public void printeazaBon() { this.comanda.printeazaBon(); }
    @Override public double getTotal() { return this.comanda.getTotal(); }
}
```

**Pasul 4 — Decoratorul concret**

Extinde abstractul. Suprascrie metodele de interes — adaugă comportament ÎNAINTE sau DUPĂ și apelează `super.metoda()` pentru a păstra comportamentul de bază.

```java
public class DecoratorMartie extends DecoratorAbstract {
    private boolean esteFemeie;

    public DecoratorMartie(IComanda comanda, boolean esteFemeie) {
        super(comanda);
        this.esteFemeie = esteFemeie;
    }

    @Override
    public void printeazaBon() {
        if (esteFemeie) System.out.println("** La multi ani! **");
        super.printeazaBon();  // delegă la comanda de bază
    }

    @Override
    public double getTotal() {
        if (esteFemeie) return 0.9 * super.getTotal();  // reducere 10%
        return super.getTotal();
    }
}
```

**Pasul 5 — Main**

Creezi baza și o „învelești" în decorator. Clientul lucrează cu `IComanda` și nu știe dacă e baza sau decorator.

```java
IComanda comanda = new DecoratorMartie(new Comanda(1), true);
comanda.addProdus(1); comanda.addProdus(2); comanda.addProdus(4);
comanda.inchideComanda();
comanda.printeazaBon();                          // "** La multi ani! **" + bon
System.out.println("Total: " + comanda.getTotal()); // 6.3 (cu reducere 10%)
```

**Ce să ții minte:** decoratorul abstract ține `private IComanda comanda` și delegă TOATE metodele; concretul suprascrie metodele de interes cu `super.metoda()` pentru a păstra comportamentul de bază; în Main: `new Decorator(new Baza(...))`.

---

## Cod seminar

```java
public interface IComanda {
    void inchideComanda();
    void addProdus(float pret);
    void printeazaBon();
    double getTotal();
}

public class Comanda implements IComanda {
    private int id;
    private List<Float> listaProduse = new ArrayList<>();
    private boolean esteInchisa = false;

    @Override
    public void addProdus(float pret) { listaProduse.add(pret); }

    @Override
    public void inchideComanda() {
        if (!esteInchisa) { esteInchisa = true; System.out.println("Comanda s-a inchis"); }
        else System.out.println("Comanda este deja inchisa.");
    }

    @Override
    public void printeazaBon() {
        if (esteInchisa) {
            System.out.println("Comanda " + id + " | Total: " + getTotal());
        } else System.out.println("Nu se poate printa bon pe comanda deschisa.");
    }

    @Override
    public double getTotal() {
        float sum = 0; for (Float f : listaProduse) sum += f; return sum;
    }
}

public abstract class DecoratorAbstract implements IComanda {
    private IComanda comanda;   // obiectul decorat

    public DecoratorAbstract(IComanda comanda) { this.comanda = comanda; }

    // delegă totul la comanda decorată
    @Override public void inchideComanda() { this.comanda.inchideComanda(); }
    @Override public void addProdus(float pret) { this.comanda.addProdus(pret); }
    @Override public void printeazaBon() { this.comanda.printeazaBon(); }
    @Override public double getTotal() { return this.comanda.getTotal(); }
}

public class DecoratorMartie extends DecoratorAbstract {
    private boolean esteFemeie;

    public DecoratorMartie(IComanda comanda, boolean esteFemeie) {
        super(comanda);
        this.esteFemeie = esteFemeie;
    }

    @Override
    public void printeazaBon() {
        if (esteFemeie) System.out.println("** La multi ani! **");
        super.printeazaBon();  // delegă la comanda de bază
    }

    @Override
    public double getTotal() {
        if (esteFemeie) return 0.9 * super.getTotal();  // reducere 10%
        return super.getTotal();
    }
}

// Main — Comanda învelită în decorator
IComanda comanda = new DecoratorMartie(new Comanda(1), true);
comanda.addProdus(1); comanda.addProdus(2); comanda.addProdus(4);
comanda.inchideComanda();
comanda.printeazaBon();                          // "** La multi ani! **" + bon
System.out.println("Total: " + comanda.getTotal()); // 6.3 (cu reducere 10%)
```

---

## Structura la examen

1. **Interfață** `IComanda` cu toate metodele
2. **Implementare de bază** `Comanda` — logica normală
3. **Decorator abstract** `DecoratorAbstract` — ține `private IComanda comanda`, delegă toate metodele cu `this.comanda.metoda()`
4. **Decorator concret** `DecoratorMartie` — extinde `DecoratorAbstract`, suprascrie metodele adăugând comportament înainte/după `super.metoda()`
5. **Main** — `new DecoratorX(new Comanda(...), parametri)`

---

## Cum recunoști

- „topping suplimentar", „specificuri culinare", „reducere aplicată dinamic"
- „fără modificarea prețului / clasei de bază"
- „se pot adăuga noi decoratori / specificuri în timp"
