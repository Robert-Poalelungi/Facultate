# Flyweight

Pattern **structural** — partajează obiecte cu stare comună pentru a reduce consumul de memorie. Un număr mic de flyweight-uri sunt reutilizate de un număr mare de instanțe.

---

## Terminologie

| Termen | Descriere |
|--------|-----------|
| **Stare intrinsecă** | stocată în flyweight, partajată, nu depinde de context (`textRecomandare`) |
| **Stare extrinsecă** | specifică fiecărei utilizări, pasată ca parametru (`Reteta`) |
| **Factory** | `HashMap<String, IRecomandare>` — returnează flyweight-ul existent sau îl creează |

---

## Participanți (din seminar)

| Rol | Clasă |
|-----|-------|
| Interfață flyweight | `IRecomandare` |
| Flyweight concret | `Recomandare` — ține `String textRecomandare` (intrinsecă) |
| Factory | `FabricaDeRecomandari` — `static Map<String, IRecomandare>` |
| Stare extrinsecă | `Reteta` — pasată la `printare()` |

---

## Explicație pas cu pas

**Ideea în o propoziție:** în loc să creezi 1000 de obiecte `Recomandare` identice (una per rețetă), le creezi o dată și le reutilizezi — factory-ul returnează mereu același obiect pentru aceeași cheie.

**Rețeta:**
1. Interfața flyweight — metodă care primește starea extrinsecă ca parametru
2. Flyweight concret — ține starea intrinsecă în câmp
3. Factory — `static Map`, populat în `static {}`, metodă `get(cheie)`
4. Stare extrinsecă — creată nou de fiecare dată, pasată la metodă
5. Main — apelează factory, pasează starea extrinsecă

**Pasul 1 — Interfața flyweight**

Metoda primește starea extrinsecă (ce variază) ca parametru.

```java
public interface IRecomandare {
    void printare(Reteta reteta);  // Reteta = stare extrinsecă
}
```

**Pasul 2 — Flyweight concret**

Ține starea intrinsecă (ce e partajat) ca câmp. Constructorul o inițializează.

```java
public class Recomandare implements IRecomandare {
    private String textRecomandare;  // stare intrinsecă — partajată

    public Recomandare(String textRecomandare) {
        this.textRecomandare = textRecomandare;
    }

    @Override
    public void printare(Reteta reteta) {
        System.out.println("Se printeaza reteta " + reteta);
        System.out.println("!!Se recomanda " + textRecomandare);
    }
}
```

**Pasul 3 — Factory**

Map static populat o singură dată în blocul `static {}`. Metoda `getRecomandare()` returnează mereu același obiect pentru aceeași cheie — NU creează unul nou.

```java
public class FabricaDeRecomandari {
    private static Map<String, IRecomandare> colectieRecomandari;

    static {  // se execută o singură dată la încărcarea clasei
        colectieRecomandari = new HashMap<>();
        colectieRecomandari.put("Sare-Zahar", new Recomandare("Evitarea consumului de zahar si apa"));
        colectieRecomandari.put("2 litri",    new Recomandare("Bea 2 litri de apa pe zi"));
        colectieRecomandari.put("Somn",       new Recomandare("Minim 8 ore de somn"));
    }

    public static IRecomandare getRecomandare(String cheie) {
        if (!colectieRecomandari.containsKey(cheie)) {
            throw new RuntimeException("Nu exista aceasta recomandare " + cheie);
        }
        return colectieRecomandari.get(cheie); // același obiect, de fiecare dată
    }
}
```

**Pasul 4 — Starea extrinsecă (Reteta)**

Creată nou de fiecare dată, pasată ca parametru la `printare()`. NU e stocată în flyweight.

**Pasul 5 — Main**

10 rețete diferite → același obiect `Recomandare("Somn")` reutilizat de 10 ori.

```java
for (int i = 0; i < 10; i++) {
    Reteta reteta = new Reteta(1 + i, "otita", List.of("paracetamol", "picaturi"));
    FabricaDeRecomandari.getRecomandare("Somn").printare(reteta);
}
```

**Ce să ții minte:** `static Map` + `static {}` în factory; `get()` returnează ACELAȘI obiect; starea variabilă (extrinsecă) se pasează ca parametru la metodă, nu se stochează în flyweight.

---

## Cod seminar

```java
public interface IRecomandare {
    void printare(Reteta reteta);  // Reteta = stare extrinsecă
}

public class Recomandare implements IRecomandare {
    private String textRecomandare;  // stare intrinsecă — partajată

    public Recomandare(String textRecomandare) {
        this.textRecomandare = textRecomandare;
    }

    @Override
    public void printare(Reteta reteta) {
        System.out.println("Se printeaza reteta " + reteta);
        System.out.println("!!Se recomanda " + textRecomandare);
    }
}

public class FabricaDeRecomandari {
    private static Map<String, IRecomandare> colectieRecomandari;

    static {
        colectieRecomandari = new HashMap<>();
        colectieRecomandari.put("Sare-Zahar", new Recomandare("Evitarea consumului de zahar si apa"));
        colectieRecomandari.put("2 litri",    new Recomandare("Bea 2 litri de apa pe zi"));
        colectieRecomandari.put("Somn",       new Recomandare("Minim 8 ore de somn"));
    }

    public static IRecomandare getRecomandare(String cheie) {
        if (!colectieRecomandari.containsKey(cheie)) {
            throw new RuntimeException("Nu exista aceasta recomandare " + cheie);
        }
        return colectieRecomandari.get(cheie); // returnează ACELAȘI obiect pentru aceeași cheie
    }
}

// Main — același obiect Recomandare reutilizat pentru 10 rețete diferite
for (int i = 0; i < 10; i++) {
    Reteta reteta = new Reteta(1 + i, "otita", List.of("paracetamol", "picaturi"));
    FabricaDeRecomandari.getRecomandare("Somn").printare(reteta);
}
```

---

## Structura la examen

1. **Interfață** `IRecomandare` cu metoda care primește starea extrinsecă ca parametru
2. **Flyweight concret** `Recomandare` — câmp cu starea intrinsecă în constructor
3. **Factory** `FabricaDeRecomandari` — `static Map<String, IRecomandare>`, populat în `static { }`, metodă `getRecomandare(cheie)`
4. **Stare extrinsecă** `Reteta` — creată nou de fiecare dată, pasată la metodă
5. **Main** — apelează factory, pasează starea extrinsecă

---

## Cum recunoști

- „număr limitat de seturi reutilizate de un număr mare de instanțe"
- „optimizare spațiu de memorie"
- „stocare centralizată", „regăsire pe baza unei chei / amprente"
