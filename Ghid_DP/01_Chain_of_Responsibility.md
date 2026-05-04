# Chain of Responsibility — Ghid complet

## Ce este?

Un pattern **comportamental** care leagă o serie de handlere (responsabili) în lanț.
Fiecare handler decide: **îl procesează el** sau **îl pasează mai departe**.

Clientul nu știe cine va rezolva cererea — trimite la primul din lanț și gata.

---

## Când se folosește?

- Când mai mulți pași trebuie aplicați succesiv pe o cerere
- Când vrei să poți adăuga/scoate pași fără să modifici restul codului
- Exemple clasice: validare formular, pipeline de filtre, sistem de aprobare

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **Handler abstract** | definește interfața + ține referința la următor |
| **Handler concret** | implementează logica proprie, pasează dacă e cazul |
| **Client** | construiește lanțul și trimite cererea la primul |

---

## Structura

```
Client → [Handler1] → [Handler2] → [Handler3] → null
              ↓            ↓            ↓
           procesează   pasează     procesează
           sau pasează  mai dep.    sau returnează
```

---

## Implementare pas cu pas

### Pasul 1 — Creează handler-ul abstract

Reține referința la următorul handler. Metoda `setUrmator()` returnează handlerul setat
ca să poți construi lanțul fluent: `h1.setUrmator(h2).setUrmator(h3)`.

```java
public abstract class AHandler {
    private AHandler urmator;

    // returnează următorul ca să poți face chaining: h1.setUrmator(h2).setUrmator(h3)
    public AHandler setUrmator(AHandler urmator) {
        this.urmator = urmator;
        return urmator;        // <-- cheia: returnează ce a setat, nu this
    }

    // apelat de subclase când vor să paseze mai departe
    protected void pasezaMailDeparte(Cerere cerere) {
        if (urmator != null)
            urmator.proceseaza(cerere);
        // dacă nu e următor, lanțul s-a terminat
    }

    // fiecare handler concret implementează asta
    public abstract void proceseaza(Cerere cerere);
}
```

> **De ce `return urmator` și nu `return this`?**
> Ca să poți scrie `h1.setUrmator(h2).setUrmator(h3)` — fiecare apel
> returnează ultimul setat, pe care apelezi imediat `setUrmator` din nou.

---

### Pasul 2 — Creează clasa cu datele cererii

```java
public class Cerere {
    private String tip;
    private int valoare;

    public Cerere(String tip, int valoare) {
        this.tip = tip;
        this.valoare = valoare;
    }

    public String getTip() { return tip; }
    public int getValoare() { return valoare; }
}
```

---

### Pasul 3 — Creează handlere concrete

Fiecare handler verifică dacă poate procesa. Dacă nu, pasează mai departe.

```java
public class HandlerMic extends AHandler {
    @Override
    public void proceseaza(Cerere cerere) {
        if (cerere.getValoare() <= 100) {
            System.out.println("HandlerMic a rezolvat cererea: " + cerere.getValoare());
        } else {
            System.out.println("HandlerMic pasează mai departe...");
            pasezaMailDeparte(cerere);   // <-- delegă la următor
        }
    }
}

public class HandlerMare extends AHandler {
    @Override
    public void proceseaza(Cerere cerere) {
        if (cerere.getValoare() <= 1000) {
            System.out.println("HandlerMare a rezolvat cererea: " + cerere.getValoare());
        } else {
            System.out.println("HandlerMare pasează mai departe...");
            pasezaMailDeparte(cerere);
        }
    }
}

public class HandlerDefault extends AHandler {
    @Override
    public void proceseaza(Cerere cerere) {
        // ultimul din lanț — preia tot ce a rămas
        System.out.println("HandlerDefault preia cererea: " + cerere.getValoare());
    }
}
```

---

### Pasul 4 — Construiește lanțul în Main

```java
public class Main {
    public static void main(String[] args) {
        // 1. creează handlere
        AHandler mic = new HandlerMic();
        AHandler mare = new HandlerMare();
        AHandler def = new HandlerDefault();

        // 2. leagă-le în lanț
        mic.setUrmator(mare).setUrmator(def);
        //  mic → mare → def

        // 3. trimite cereri — clientul nu știe cine le rezolvă
        mic.proceseaza(new Cerere("test", 50));    // HandlerMic
        mic.proceseaza(new Cerere("test", 500));   // HandlerMare
        mic.proceseaza(new Cerere("test", 5000));  // HandlerDefault
    }
}
```

---

## Variante comune la examen

### Varianta 1 — returnează boolean (aprobat/respins)

Handler-ul returnează `false` și oprește lanțul dacă condiția nu e îndeplinită.

```java
public abstract class AVerificator {
    private AVerificator urmator;

    public AVerificator setUrmator(AVerificator urmator) {
        this.urmator = urmator;
        return urmator;
    }

    protected boolean pasezaMailDeparte(Object cerere) {
        if (urmator != null)
            return urmator.verifica(cerere);
        return true;  // dacă am ajuns la capăt fără rejected → aprobat
    }

    public abstract boolean verifica(Object cerere);
}

// handler concret
public class VerificatorA extends AVerificator {
    @Override
    public boolean verifica(Object cerere) {
        if (/* condiție NU e îndeplinită */) {
            System.out.println("Respins de VerificatorA");
            return false;             // oprește lanțul
        }
        return pasezaMailDeparte(cerere);  // continuă
    }
}
```

### Varianta 2 — modifică o valoare și o pasează (suma maximă)

Fiecare handler poate reduce valoarea. Poate arunca excepție dacă nu e eligibil.

```java
public abstract class ALimitator {
    private ALimitator urmator;

    public ALimitator setUrmator(ALimitator urmator) {
        this.urmator = urmator;
        return urmator;
    }

    protected double pasezaMailDeparte(Object date, double valoareCurenta) throws Exception {
        if (urmator != null)
            return urmator.calculeaza(date, valoareCurenta);
        return valoareCurenta;  // valoarea finală
    }

    public abstract double calculeaza(Object date, double valoareCurenta) throws Exception;
}

public class LimitatorA extends ALimitator {
    @Override
    public double calculeaza(Object date, double valoareCurenta) throws Exception {
        if (/* nu e eligibil deloc */)
            throw new Exception("Refuzat: motiv...");
        double valoareNoua = valoareCurenta * 0.8;  // reduce cu 20%
        return pasezaMailDeparte(date, valoareNoua);
    }
}
```

### Varianta 3 — transformă un String (filtre text)

```java
public abstract class AFiltru {
    private AFiltru urmator;

    public AFiltru setUrmator(AFiltru urmator) {
        this.urmator = urmator;
        return urmator;
    }

    protected String pasezaMailDeparte(String text) {
        if (urmator != null)
            return urmator.aplica(text);
        return text;  // textul final procesat
    }

    public abstract String aplica(String text);
}

public class LowerCaseFilter extends AFiltru {
    @Override
    public String aplica(String text) {
        return pasezaMailDeparte(text.toLowerCase());
    }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „mai mulți verificatori/responsabili"
- „fiecare verifică un criteriu"
- „dacă nu trece → respinge / pasează mai departe"
- „pipeline", „filtre succesive"
- „sistem de aprobare în trepte"

**Structura răspunsului la examen:**
1. Clasă abstractă `AHandler` cu `private AHandler urmator` + `setUrmator()` + `pasezaMailDeparte()`
2. Câte o clasă concretă per criteriu, care `extends AHandler`
3. `Main` care leagă handlere și trimite cereri la primul
