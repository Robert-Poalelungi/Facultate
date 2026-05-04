# Composite — Ghid complet

## Ce este?

Un pattern **structural** care permite tratarea unui obiect simplu și a unui grup de obiecte
în mod **uniform** — prin aceeași interfață.

Construiești un arbore: frunzele sunt obiecte simple, nodurile interne conțin colecții de frunze
sau alte noduri. Operațiile se propagă recursiv în arbore.

---

## Când se folosește?

- Ierarhii arbore: companie → departamente → angajați
- Sisteme de fișiere: foldere → fișiere / subfoldere
- Meniuri cu subMeniuri
- Orice structură „parte-întreg" recursivă

---

## Participanți

| Rol | Clasă | Responsabilitate |
|-----|-------|-----------------|
| **Component** | clasă abstractă | interfața comună pentru leaf și composite |
| **Leaf** | clasă simplă | implementează operațiile pe element simplu |
| **Composite** | clasă cu listă de componente | agregă recursiv din copii |
| **Client** | `Main` | lucrează doar cu tipul `Component` |

---

## Structura

```
         AComponenta (abstract)
        /           \
    Leaf           Composite
  (Angajat)       (Departament)
                  - List<AComponenta> copii
                  + adauga()
                  + elimina()
                  + getSalariuTotal() → sumă recursivă
```

---

## Implementare pas cu pas

### Pasul 1 — Creează clasa abstractă (Component)

Declară toate operațiile comune. Operațiile specifice doar Composite (`adauga`, `elimina`)
aruncă `UnsupportedOperationException` implicit — frunzele le moștenesc fără să le suprascrie.

```java
public abstract class AComponenta {
    // operații comune — implementate diferit în Leaf vs Composite
    public abstract String getNume();
    public abstract double getSalariuTotal();
    public abstract int getNrAngajati();
    public abstract void afiseaza(String indent);

    // operații doar pentru Composite — aruncă excepție în Leaf
    public void adauga(AComponenta c) {
        throw new UnsupportedOperationException("Leaf nu suportă adauga()");
    }
    public void elimina(AComponenta c) {
        throw new UnsupportedOperationException("Leaf nu suportă elimina()");
    }
}
```

> **De ce `UnsupportedOperationException` și nu abstract?**
> Dacă ar fi abstract, Leaf ar trebui să le implementeze (cu corp gol), ceea ce e confuz.
> Excepția semnalează clar că operația nu are sens pe un Leaf.

---

### Pasul 2 — Creează Leaf-ul

Element simplu, fără copii. Returnează valorile proprii.

```java
public class Angajat extends AComponenta {
    private String nume;
    private double salariu;

    public Angajat(String nume, double salariu) {
        this.nume = nume;
        this.salariu = salariu;
    }

    @Override
    public String getNume() { return nume; }

    @Override
    public double getSalariuTotal() {
        return salariu;       // un singur angajat → salariul lui
    }

    @Override
    public int getNrAngajati() {
        return 1;             // el însuși
    }

    @Override
    public void afiseaza(String indent) {
        // indent = spații pentru nivel de adâncime în arbore
        System.out.printf("%s- %s (%.0f RON)%n", indent, nume, salariu);
    }

    // adauga() și elimina() → moștenite din AComponenta → aruncă UnsupportedOperationException
}
```

---

### Pasul 3 — Creează Composite-ul

Conține o listă de `AComponenta` (poate fi Leaf sau alt Composite). Toate operațiile
iterează lista și agregă recursiv.

```java
import java.util.ArrayList;
import java.util.List;

public class Departament extends AComponenta {
    private String nume;
    private List<AComponenta> subordonati = new ArrayList<>();  // copiii

    public Departament(String nume) {
        this.nume = nume;
    }

    // gestionare copii
    @Override
    public void adauga(AComponenta c) { subordonati.add(c); }

    @Override
    public void elimina(AComponenta c) { subordonati.remove(c); }

    @Override
    public String getNume() { return nume; }

    // RECURSIE: sumă din toți copiii (care pot fi și ei Composite → recursie continuă)
    @Override
    public double getSalariuTotal() {
        double total = 0;
        for (AComponenta c : subordonati)
            total += c.getSalariuTotal();   // polimorfism: Angajat.getSalariuTotal() sau Departament.getSalariuTotal()
        return total;
    }

    @Override
    public int getNrAngajati() {
        int total = 0;
        for (AComponenta c : subordonati)
            total += c.getNrAngajati();
        return total;
    }

    // RECURSIE: afișare cu indentare crescătoare
    @Override
    public void afiseaza(String indent) {
        System.out.println(indent + "[" + nume + "]");
        for (AComponenta c : subordonati)
            c.afiseaza(indent + "  ");   // fiecare nivel adaugă 2 spații
    }
}
```

---

### Pasul 4 — Construiește arborele în Main

```java
public class Main {
    public static void main(String[] args) {
        // creează frunze
        Angajat a1 = new Angajat("Ana", 7000);
        Angajat a2 = new Angajat("Radu", 6500);
        Angajat a3 = new Angajat("Maria", 5500);
        Angajat ceo = new Angajat("Ion CEO", 15000);

        // creează noduri interne
        Departament dev = new Departament("Development");
        dev.adauga(a1);
        dev.adauga(a2);

        Departament it = new Departament("IT");
        it.adauga(dev);      // Composite în Composite → recursie
        it.adauga(a3);

        Departament firma = new Departament("Firma SRL");
        firma.adauga(ceo);
        firma.adauga(it);

        // apelezi aceeași metodă pe toată ierarhia
        firma.afiseaza("");
        System.out.println("Total salarii: " + firma.getSalariuTotal());
        System.out.println("Total angajati: " + firma.getNrAngajati());
    }
}
```

**Output:**
```
[Firma SRL]
  - Ion CEO (15000 RON)
  [IT]
    [Development]
      - Ana (7000 RON)
      - Radu (6500 RON)
    - Maria (5500 RON)
Total salarii: 34000.0
Total angajati: 4
```

---

## Variantă: sistem de fișiere (cu căutare + ștergere)

### AElementSistem.java
```java
public abstract class AElementSistem {
    public abstract String getNume();
    public abstract double getDimensiune();
    public abstract void afiseaza(String indent);
    public abstract AElementSistem cauta(String numeCautat);  // recursiv

    public void adauga(AElementSistem e) { throw new UnsupportedOperationException(); }
    public void sterge(AElementSistem e) { throw new UnsupportedOperationException(); }
}
```

### Fisier.java (Leaf)
```java
public class Fisier extends AElementSistem {
    private String nume;
    private double dimensiune;  // KB

    public Fisier(String nume, double dimensiune) {
        this.nume = nume;
        this.dimensiune = dimensiune;
    }

    @Override public String getNume() { return nume; }
    @Override public double getDimensiune() { return dimensiune; }

    @Override
    public void afiseaza(String indent) {
        System.out.printf("%s- %s (%.1f KB)%n", indent, nume, dimensiune);
    }

    @Override
    public AElementSistem cauta(String numeCautat) {
        return this.nume.equals(numeCautat) ? this : null;
    }
}
```

### Folder.java (Composite)
```java
import java.util.*;

public class Folder extends AElementSistem {
    private String nume;
    private List<AElementSistem> elemente = new ArrayList<>();

    public Folder(String nume) { this.nume = nume; }

    @Override public void adauga(AElementSistem e) { elemente.add(e); }
    @Override public void sterge(AElementSistem e) { elemente.remove(e); }
    @Override public String getNume() { return nume; }

    @Override
    public double getDimensiune() {
        double total = 0;
        for (AElementSistem e : elemente) total += e.getDimensiune();
        return total;
    }

    @Override
    public void afiseaza(String indent) {
        System.out.println(indent + "[" + nume + "]");
        for (AElementSistem e : elemente) e.afiseaza(indent + "  ");
    }

    @Override
    public AElementSistem cauta(String numeCautat) {
        if (this.nume.equals(numeCautat)) return this;  // găsit chiar folderul
        for (AElementSistem e : elemente) {
            AElementSistem gasit = e.cauta(numeCautat); // recursiv
            if (gasit != null) return gasit;
        }
        return null;
    }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „ierarhie", „structură arbore"
- „departamente care conțin angajați sau alte departamente"
- „foldere care conțin fișiere sau alte foldere"
- „calcul total propagat"
- „afișare cu indentare"

**Structura răspunsului la examen:**
1. Clasă abstractă `AComponenta` cu metodele comune + `adauga/elimina` cu `UnsupportedOperationException`
2. `Leaf` (ex: `Angajat`) extinde `AComponenta`, returnează valori simple
3. `Composite` (ex: `Departament`) extinde `AComponenta`, are `List<AComponenta>`, iterează recursiv
4. `Main` construiește arborele cu `adauga()` și apelează metodele pe rădăcină
