# Adapter

Pattern **structural** — face două interfețe incompatibile să lucreze împreună. Adaptorul implementează interfața cerută și traduce apelurile spre clasa existentă.

---

## Participanți (din seminar — exemplul priza)

| Rol | Clasă |
|-----|-------|
| Interfață cerută (target) | `IPrizaAmerica` — `incarcaLa110V()` |
| Interfață existentă (adaptee) | `IPrizaEuropa` — `incarcaLa230V()` |
| Implementare existentă | `PrizaEuropa implements IPrizaEuropa` |
| Adapter | `AdapterEuropaToAmerica extends PrizaEuropa implements IPrizaAmerica` |
| Client | `Laptop` — acceptă `IPrizaAmerica` |

---

## Explicație pas cu pas

**Ideea în o propoziție:** clientul vrea `IPrizaAmerica` (110V), tu ai `PrizaEuropa` (230V) — adaptorul implementează ce vrea clientul și traduce intern apelul spre ce ai.

**Rețeta:**
1. Identifici interfața cerută (ce vrea clientul) și clasa existentă (ce ai)
2. Creezi adaptorul care implementează interfața cerută
3. Adaptorul „traduce" apelul spre clasa existentă
4. Main — clientul primește adaptorul, nu știe de clasa existentă

**Pasul 1 — Interfețele (cerută și existentă)**

```java
public interface IPrizaAmerica {
    void incarcaLa110V();  // interfața cerută de client
}

public interface IPrizaEuropa {
    void incarcaLa230V();  // interfața existentă
}

public class PrizaEuropa implements IPrizaEuropa {
    @Override
    public void incarcaLa230V() { System.out.println("Priza ofera flux 230V...."); }
}
```

**Pasul 2 — Class Adapter (prin moștenire)**

Extinde clasa existentă și implementează interfața cerută. Traduce apelul intern.

```java
public class AdapterEuropaToAmerica extends PrizaEuropa implements IPrizaAmerica {
    @Override
    public void incarcaLa110V() {
        this.incarcaLa230V();  // moștenit din PrizaEuropa
        System.out.println("Adaptor care face conversie de la 230V la 110V.");
    }
}
```

Clientul vrea `IPrizaAmerica` → adaptorul moștenește `PrizaEuropa` → apelează `incarcaLa230V()` intern.

**Pasul 3 — Object Adapter (prin compoziție)**

Ține o referință la clasa existentă în loc să o extindă. Mai flexibil când nu poți moșteni.

```java
public class Adaptor implements IUSBcIncarcator {
    private IMicroUSBIncarcator incarcatorVechi;  // compoziție, nu moștenire

    public Adaptor(IMicroUSBIncarcator incarcatorVechi) {
        this.incarcatorVechi = incarcatorVechi;
    }

    @Override
    public void incarcaUSBc() {
        incarcatorVechi.incarcaMicroUSB(); // traduce apelul
    }
}
```

**Pasul 4 — Main**

```java
// Class adapter (priză)
Laptop laptop = new Laptop("Dell", 60);
laptop.incarca(new AdapterEuropaToAmerica()); // adaptorul face trecerea

// Object adapter (USB)
Telefon telefon = new Telefon("Huawei p20", 60);
IMicroUSBIncarcator incarcatorVechi = new MicroUSB();
telefon.chargeUSBc(new Adaptor(incarcatorVechi));
```

**Ce să ții minte:**
- **Class adapter**: `Adapter extends Adaptee implements ITarget` — moștenire
- **Object adapter**: `Adapter implements ITarget` + `private Adaptee adaptee` — compoziție
- Adaptorul NU modifică clasa existentă; traduce apelurile spre ea

---

## Cod seminar (exemplul 1 — priză)

```java
public interface IPrizaAmerica {
    void incarcaLa110V();  // interfața cerută de client
}

public interface IPrizaEuropa {
    void incarcaLa230V();  // interfața existentă
}

public class PrizaEuropa implements IPrizaEuropa {
    @Override
    public void incarcaLa230V() { System.out.println("Priza ofera flux 230V...."); }
}

// Adapter prin moștenire (class adapter)
public class AdapterEuropaToAmerica extends PrizaEuropa implements IPrizaAmerica {
    @Override
    public void incarcaLa110V() {
        this.incarcaLa230V();  // folosește ce există
        System.out.println("Adaptor care face conversie de la 230V la 110V.");
    }
}

public class Laptop {
    public void incarca(IPrizaAmerica priza) {  // vrea IPrizaAmerica
        priza.incarcaLa110V();
    }
}

// Main
Laptop laptop = new Laptop("Dell", 60);
laptop.incarca(new AdapterEuropaToAmerica()); // adaptorul face trecerea
```

---

## Cod seminar (exemplul 2 — USB-C / MicroUSB)

```java
// Client vrea IUSBcIncarcator, dispunem de IMicroUSBIncarcator
public class Adaptor implements IUSBcIncarcator {
    private IMicroUSBIncarcator incarcatorVechi;

    public Adaptor(IMicroUSBIncarcator incarcatorVechi) {
        this.incarcatorVechi = incarcatorVechi;
    }

    @Override
    public void incarcaUSBc() {
        incarcatorVechi.incarcaMicroUSB(); // traduce apelul
    }
}

// Main
Telefon telefon = new Telefon("Huawei p20", 60);
IMicroUSBIncarcator incarcatorVechi = new MicroUSB();
telefon.chargeUSBc(new Adaptor(incarcatorVechi));
```

---

## Structura la examen

1. **Interfață cerută** (target) — ce vrea clientul
2. **Clasa existentă** (adaptee) — ce avem deja, nu o modificăm
3. **Adapter** — implementează interfața cerută, ține referința la adaptee, traduce apelurile
4. **Main** — clientul primește Adapter, nu știe de adaptee

**Două variante:**
- **Class adapter**: `Adapter extends Adaptee implements ITarget`
- **Object adapter**: `Adapter implements ITarget` + `private Adaptee adaptee` (compoziție)

---

## Cum recunoști

- „legacy", „nu poți modifica clasa existentă", „integrare cu sistem extern"
- Două interfețe incompatibile care trebuie să lucreze împreună
