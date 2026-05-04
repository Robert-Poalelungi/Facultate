# Template Method — Ghid complet

## Ce este?

Un pattern **comportamental** care definește **scheletul unui algoritm** într-o clasă de bază,
lăsând subclasele să completeze pașii specifici — fără să modifice structura algoritmului.

„Algoritmul e fix, detaliile sunt variabile."

---

## Când se folosește?

- Algoritm cu structură fixă dar pași variabili
- Vrei să eviți duplicarea codului comun
- Subclasele diferă doar în anumiți pași
- Exemple: preparare băuturi (cafea/ceai), generare rapoarte, procesare date

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **AbstractClass** | definește `templateMethod()` + pași comuni concreți + pași abstracti |
| **ConcreteClass** | implementează pașii abstracti (variabili) |

---

## Structura

```
AbstractClass
+ templateMethod()    ← final — nu se suprascrie
    ├── pasulComun1() ← implementat în AbstractClass
    ├── pasulVariabil1() ← abstract → implementat în ConcreteClass
    ├── pasulComun2() ← implementat în AbstractClass
    └── pasulVariabil2() ← abstract → implementat în ConcreteClass
           ↑
     ConcreteClassA     ConcreteClassB
     (implementează     (implementează
      pașii variabili)   pașii variabili)
```

---

## Implementare pas cu pas

### Pasul 1 — Clasa abstractă cu template method

`preparare()` e template method-ul — definește ordinea pașilor.
Pașii variabili sunt abstracti, pașii comuni sunt implementați direct.

```java
public abstract class ABautura {
    // TEMPLATE METHOD — scheletul algoritmului (nu se suprascrie în subclase)
    public final void preparare() {
        System.out.println("=== Preparare " + getDenumire() + " ===");
        fierbeApa();               // pas comun — implementat aici
        adaugaIngredientPrincipal(); // pas variabil — abstract
        toarnaInCana();            // pas comun — implementat aici
        adaugaExtras();            // pas variabil — poate fi suprascris (hook)
    }

    // PAS COMUN — același pentru toate băuturile
    private void fierbeApa() {
        System.out.println("1. Se fierbe apa.");
    }

    // PAS COMUN — același pentru toate
    private void toarnaInCana() {
        System.out.println("3. Se toarnă în cană.");
    }

    // PAS VARIABIL — fiecare subclasă implementează diferit
    protected abstract String getDenumire();
    protected abstract void adaugaIngredientPrincipal();

    // HOOK — pas opțional, subclasele pot suprascrie sau nu
    protected void adaugaExtras() {
        // implicit nu face nimic
    }
}
```

> **`final` pe templateMethod()**: Garantează că subclasele nu pot schimba ordinea pașilor.
> Dacă nu pui `final`, e tot template method, dar mai permisiv.

---

### Pasul 2 — Clase concrete

Fiecare implementează DOAR pașii variabili.

```java
public class Cafea extends ABautura {
    @Override
    protected String getDenumire() {
        return "Cafea";
    }

    @Override
    protected void adaugaIngredientPrincipal() {
        System.out.println("2. Se adaugă cafea măcinată.");
    }

    @Override
    protected void adaugaExtras() {
        System.out.println("4. Se adaugă zahăr și lapte.");   // override hook
    }
}

public class Ceai extends ABautura {
    @Override
    protected String getDenumire() {
        return "Ceai";
    }

    @Override
    protected void adaugaIngredientPrincipal() {
        System.out.println("2. Se adaugă pliculețul de ceai.");
    }

    // NU suprascrie adaugaExtras → fără extras (hook implicit)
}

public class Ciocolata extends ABautura {
    @Override
    protected String getDenumire() {
        return "Ciocolată Caldă";
    }

    @Override
    protected void adaugaIngredientPrincipal() {
        System.out.println("2. Se adaugă pudra de cacao și zahăr.");
    }

    @Override
    protected void adaugaExtras() {
        System.out.println("4. Se adaugă frișcă și scorțișoară.");
    }
}
```

---

### Pasul 3 — Main

```java
public class Main {
    public static void main(String[] args) {
        ABautura cafea = new Cafea();
        cafea.preparare();

        System.out.println();

        ABautura ceai = new Ceai();
        ceai.preparare();

        System.out.println();

        ABautura ciocolata = new Ciocolata();
        ciocolata.preparare();
    }
}
```

**Output:**
```
=== Preparare Cafea ===
1. Se fierbe apa.
2. Se adaugă cafea măcinată.
3. Se toarnă în cană.
4. Se adaugă zahăr și lapte.

=== Preparare Ceai ===
1. Se fierbe apa.
2. Se adaugă pliculețul de ceai.
3. Se toarnă în cană.

=== Preparare Ciocolată Caldă ===
1. Se fierbe apa.
2. Se adaugă pudra de cacao și zahăr.
3. Se toarnă în cană.
4. Se adaugă frișcă și scorțișoară.
```

---

## Variantă: generare raport

```java
public abstract class AGeneratorRaport {
    // template method
    public final String genereaza() {
        StringBuilder sb = new StringBuilder();
        sb.append(getHeader()).append("\n");
        sb.append(getContinut()).append("\n");
        sb.append(getFooter()).append("\n");
        return sb.toString();
    }

    // pas comun
    private String getFooter() {
        return "--- Generat automat la " + java.time.LocalDate.now() + " ---";
    }

    // pași variabili
    protected abstract String getHeader();
    protected abstract String getContinut();
}

public class RaportVanzari extends AGeneratorRaport {
    @Override
    protected String getHeader() { return "=== RAPORT VÂNZĂRI ==="; }

    @Override
    protected String getContinut() {
        return "Total vânzări: 15,000 RON\nNumăr tranzacții: 42";
    }
}

public class RaportAngajati extends AGeneratorRaport {
    @Override
    protected String getHeader() { return "=== RAPORT ANGAJAȚI ==="; }

    @Override
    protected String getContinut() {
        return "Total angajați: 15\nSalarii totale: 75,000 RON";
    }
}
```

---

## Hook vs Abstract

| | Abstract | Hook |
|--|----------|------|
| **Obligatoriu de implementat?** | Da | Nu |
| **Comportament implicit** | Nu are | Are (poate fi gol sau cu logică) |
| **Utilizare** | pași esențiali care diferă | pași opționali / extensii |

```java
// Hook cu comportament implicit
protected boolean adaugaLapaite() {
    return true;   // implicit: da, subclasele pot suprascrie
}

// Hook gol
protected void adaugaExtras() {
    // implicit nimic
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „algoritm cu pași comuni și pași diferiți"
- „schelet comun, detalii variabile"
- „subclasele completează anumiți pași"
- „preparare", „procesare", „generare"

**Structura răspunsului la examen:**
1. Clasă abstractă cu `templateMethod()` care apelează pașii în ordine
2. Pași comuni → `private` sau `protected` cu implementare
3. Pași variabili → `protected abstract`
4. Pași opționali → `protected` cu corp gol (hook)
5. Subclase concrete (`Cafea`, `Ceai`) → implementează doar pașii abstracti

> **Diferența față de Strategy:**
> - **Template Method**: algoritmul fix în clasă de bază, pașii sunt în subclase (moștenire)
> - **Strategy**: algoritmul întreg e interschimbabil (compoziție)
