# Adapter — Ghid complet

## Ce este?

Un pattern **structural** care permite cooperarea a două interfețe **incompatibile**.

Adapter-ul „traduce" apelurile dintr-o interfață în alta — ca un adaptor de priză.
Clientul apelează interfața așteptată, Adapter-ul convertește apelul pentru clasa incompatibilă.

---

## Când se folosește?

- Vrei să folosești o clasă existentă dar interfața ei nu se potrivește
- Integrezi o librărie externă cu interfața ta
- Ai cod legacy pe care nu îl poți modifica

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **Target** (interfață) | interfața așteptată de client |
| **Adaptee** | clasa existentă cu interfața incompatibilă |
| **Adapter** | implementează Target, ține Adaptee, traduce apelurile |
| **Client** | lucrează cu Target |

---

## Structura (Object Adapter)

```
Client → «interface» ITarget
                        ↑
                     Adapter ──→ Adaptee
                  (traduce)    (incompatibil)
```

---

## Implementare pas cu pas

### Pasul 1 — Interfața așteptată de client (Target)

Ce vrea clientul să folosească.

```java
public interface IPlataModerna {
    void plateste(String destinatar, double suma, String moneda);
    double getSoldDisponibil();
}
```

---

### Pasul 2 — Clasa existentă incompatibilă (Adaptee)

Există deja, nu o poți modifica (ex: librărie externă, sistem legacy).

```java
public class SistemBancarVechi {
    private double cont;

    public SistemBancarVechi(double soldInitial) {
        this.cont = soldInitial;
    }

    // metode cu semnătură diferită față de IPlataModerna
    public void transferBani(int sumaCenti, String beneficiar) {
        double suma = sumaCenti / 100.0;
        System.out.printf("Transfer legacy: %.2f RON → %s%n", suma, beneficiar);
        this.cont -= suma;
    }

    public int getSoldCenti() {
        return (int)(cont * 100);
    }
}
```

---

### Pasul 3 — Adapter

Implementează interfața așteptată (Target), ține Adaptee-ul și traduce apelurile.

```java
public class AdapterBancarVechi implements IPlataModerna {
    private SistemBancarVechi sistemVechi;   // adaptee

    public AdapterBancarVechi(SistemBancarVechi sistemVechi) {
        this.sistemVechi = sistemVechi;
    }

    @Override
    public void plateste(String destinatar, double suma, String moneda) {
        // conversia interfețelor:
        // IPlataModerna: (String destinatar, double suma, String moneda)
        // SistemBancarVechi: (int sumaCenti, String beneficiar)

        double sumaRON = suma;
        if ("EUR".equals(moneda)) sumaRON = suma * 5.0;   // conversie valutară
        if ("USD".equals(moneda)) sumaRON = suma * 4.6;

        int sumaCenti = (int)(sumaRON * 100);

        System.out.printf("Adapter: convertesc %.2f %s → %d centi%n", suma, moneda, sumaCenti);
        sistemVechi.transferBani(sumaCenti, destinatar);   // apel tradus
    }

    @Override
    public double getSoldDisponibil() {
        // traduce getSoldCenti() → double în RON
        return sistemVechi.getSoldCenti() / 100.0;
    }
}
```

---

### Pasul 4 — Client

Clientul lucrează cu interfața modernă — nu știe de sistemul vechi.

```java
public class Main {
    public static void main(String[] args) {
        // sistemul vechi (nu îl putem modifica)
        SistemBancarVechi sistemVechi = new SistemBancarVechi(1000.0);

        // adapter face sistemul vechi compatibil cu interfața modernă
        IPlataModerna plata = new AdapterBancarVechi(sistemVechi);

        System.out.println("Sold disponibil: " + plata.getSoldDisponibil() + " RON");

        plata.plateste("Ion Popescu", 100.0, "RON");
        plata.plateste("Maria Ionescu", 50.0, "EUR");

        System.out.println("Sold rămas: " + plata.getSoldDisponibil() + " RON");
    }
}
```

**Output:**
```
Sold disponibil: 1000.0 RON
Adapter: convertesc 100.00 RON → 10000 centi
Transfer legacy: 100.00 RON → Ion Popescu
Adapter: convertesc 50.00 EUR → 25000 centi
Transfer legacy: 250.00 RON → Maria Ionescu
Sold rămas: 650.0 RON
```

---

## Variantă: Adapter pentru format date

```java
// ce vrea clientul
public interface IAfisabilDate {
    String getDateFormatat();   // "DD/MM/YYYY"
}

// clasă existentă cu format diferit
public class SursaDate {
    public String getData() { return "2025-05-04"; }  // "YYYY-MM-DD"
}

// adapter
public class AdapterFormatData implements IAfisabilDate {
    private SursaDate sursa;

    public AdapterFormatData(SursaDate sursa) {
        this.sursa = sursa;
    }

    @Override
    public String getDateFormatat() {
        String data = sursa.getData();           // "2025-05-04"
        String[] parts = data.split("-");
        return parts[2] + "/" + parts[1] + "/" + parts[0];   // "04/05/2025"
    }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „interfețe incompatibile"
- „clasă existentă / legacy pe care nu o poți modifica"
- „adaptezi", „convertiți"
- „integrare"

**Structura răspunsului la examen:**
1. Interfață `ITarget` — ce vrea clientul
2. Clasa `Adaptee` — există, nu se modifică, interfață diferită
3. Clasa `Adapter implements ITarget` — ține `private Adaptee adaptee`, traduce apelurile
4. `Main` creează `ITarget target = new Adapter(new Adaptee())`

> **Diferența față de Facade:**
> - Facade simplifică mai multe clase într-una
> - Adapter face o clasă compatibilă cu o altă interfață
