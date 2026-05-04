# State — Ghid complet

## Ce este?

Un pattern **comportamental** care permite unui obiect să-și **schimbe comportamentul** când
starea sa internă se schimbă. Pare că obiectul și-a schimbat clasa.

În loc de if-else/switch gigant pe stări, fiecare stare e o clasă separată.

---

## Când se folosește?

- Obiect cu comportament diferit în funcție de stare
- Evitare if-else/switch mare cu state-uri
- Starea se schimbă la runtime
- Exemple: bancomat (idle/card introdus/pin introdus), comandă (nouă/procesată/livrată), semafor

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **IStare** | interfața comună pentru toate stările |
| **Stare concretă** | comportamentul specific stării respective |
| **Context** | ține starea curentă, delegă la ea, permite tranziții |

---

## Structura

```
Context
 - IStare stareCurenta
 + setStare()
 + actiune()  ──→ stareCurenta.actiune(context)
                      ↑         ↑          ↑
                  StareA     StareB     StareC
```

---

## Implementare pas cu pas

### Pasul 1 — Interfața State

Metodele pe care contextul le va delega. Contextul e primit ca parametru
pentru ca stările să poată face tranziții.

```java
public interface IStareBancomat {
    void introduceCard(Bancomat bancomat);
    void introducePin(Bancomat bancomat, String pin);
    void retrageBani(Bancomat bancomat, double suma);
    void ejectCard(Bancomat bancomat);
}
```

---

### Pasul 2 — Contextul

Ține starea curentă. Toate operațiile delegă la stare.

```java
public class Bancomat {
    private IStareBancomat stareCurenta;
    private double sold;

    public Bancomat(double sold) {
        this.sold = sold;
        this.stareCurenta = new StareAsteaptaCard();   // starea inițială
    }

    // tranziție de stare — apelat din stări
    public void setStare(IStareBancomat stareNoua) {
        System.out.println("  → Tranziție la starea: " + stareNoua.getClass().getSimpleName());
        this.stareCurenta = stareNoua;
    }

    public double getSold() { return sold; }
    public void setSold(double sold) { this.sold = sold; }

    // toate metodele delegă la starea curentă
    public void introduceCard() {
        stareCurenta.introduceCard(this);
    }

    public void introducePin(String pin) {
        stareCurenta.introducePin(this, pin);
    }

    public void retrageBani(double suma) {
        stareCurenta.retrageBani(this, suma);
    }

    public void ejectCard() {
        stareCurenta.ejectCard(this);
    }
}
```

---

### Pasul 3 — Stări concrete

Fiecare stare definește comportamentul și gestionează tranzițiile.

```java
// Starea 1: Așteaptă cardul
public class StareAsteaptaCard implements IStareBancomat {
    @Override
    public void introduceCard(Bancomat bancomat) {
        System.out.println("Card introdus. Introduceți PIN-ul.");
        bancomat.setStare(new StareAsteaptaPin());   // tranziție
    }

    @Override
    public void introducePin(Bancomat bancomat, String pin) {
        System.out.println("Eroare: introduceți cardul mai întâi.");
    }

    @Override
    public void retrageBani(Bancomat bancomat, double suma) {
        System.out.println("Eroare: introduceți cardul mai întâi.");
    }

    @Override
    public void ejectCard(Bancomat bancomat) {
        System.out.println("Niciun card de ejectat.");
    }
}

// Starea 2: Așteaptă PIN-ul
public class StareAsteaptaPin implements IStareBancomat {
    private static final String PIN_CORECT = "1234";

    @Override
    public void introduceCard(Bancomat bancomat) {
        System.out.println("Cardul e deja introdus.");
    }

    @Override
    public void introducePin(Bancomat bancomat, String pin) {
        if (PIN_CORECT.equals(pin)) {
            System.out.println("PIN corect. Puteți efectua operații.");
            bancomat.setStare(new StareAutentificat());   // tranziție
        } else {
            System.out.println("PIN incorect. Reîncercați.");
        }
    }

    @Override
    public void retrageBani(Bancomat bancomat, double suma) {
        System.out.println("Eroare: introduceți PIN-ul mai întâi.");
    }

    @Override
    public void ejectCard(Bancomat bancomat) {
        System.out.println("Card ejectat.");
        bancomat.setStare(new StareAsteaptaCard());   // tranziție
    }
}

// Starea 3: Autentificat
public class StareAutentificat implements IStareBancomat {
    @Override
    public void introduceCard(Bancomat bancomat) {
        System.out.println("Deja autentificat.");
    }

    @Override
    public void introducePin(Bancomat bancomat, String pin) {
        System.out.println("Deja autentificat.");
    }

    @Override
    public void retrageBani(Bancomat bancomat, double suma) {
        if (suma > bancomat.getSold()) {
            System.out.println("Fonduri insuficiente. Sold: " + bancomat.getSold());
        } else {
            bancomat.setSold(bancomat.getSold() - suma);
            System.out.printf("Retras %.2f RON. Sold rămas: %.2f RON%n",
                suma, bancomat.getSold());
        }
    }

    @Override
    public void ejectCard(Bancomat bancomat) {
        System.out.println("Card ejectat. La revedere!");
        bancomat.setStare(new StareAsteaptaCard());   // tranziție
    }
}
```

---

### Pasul 4 — Main

```java
public class Main {
    public static void main(String[] args) {
        Bancomat bancomat = new Bancomat(1000.0);

        System.out.println("=== Flux normal ===");
        bancomat.retrageBani(100);     // eroare: fără card
        bancomat.introduceCard();
        bancomat.introducePin("0000"); // PIN greșit
        bancomat.introducePin("1234"); // PIN corect
        bancomat.retrageBani(200);
        bancomat.retrageBani(900);     // fonduri insuficiente
        bancomat.ejectCard();

        System.out.println("\n=== Eject fără autentificare ===");
        bancomat.introduceCard();
        bancomat.ejectCard();          // abandon
    }
}
```

**Output:**
```
=== Flux normal ===
Eroare: introduceți cardul mai întâi.
Card introdus. Introduceți PIN-ul.
  → Tranziție la starea: StareAsteaptaPin
PIN incorect. Reîncercați.
PIN corect. Puteți efectua operații.
  → Tranziție la starea: StareAutentificat
Retras 200.00 RON. Sold rămas: 800.00 RON
Fonduri insuficiente. Sold: 800.0
Card ejectat. La revedere!
  → Tranziție la starea: StareAsteaptaCard

=== Eject fără autentificare ===
Card introdus. Introduceți PIN-ul.
  → Tranziție la starea: StareAsteaptaPin
Card ejectat.
  → Tranziție la starea: StareAsteaptaCard
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „stări" (idle, activ, blocat, etc.)
- „comportament diferit în funcție de stare"
- „tranziții între stări"
- „bancomat", „comandă", „semafor", „ușă"

**Structura răspunsului la examen:**
1. Interfață `IStare` cu toate operațiile posibile (chiar dacă unele sunt „eroare" în unele stări)
2. Câte o clasă per stare, implementează `IStare`, gestionează tranzițiile prin `context.setStare(...)`
3. Context (`Bancomat`) ține `private IStare stareCurenta`, toate metodele delegă la stare
4. `Main` interacționează DOAR cu contextul

> **Diferența față de Strategy:**
> - **Strategy**: clientul schimbă algoritmul explicit
> - **State**: obiectul se schimbă singur (intern) la tranziția de stare
