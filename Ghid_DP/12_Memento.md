# Memento — Ghid complet

## Ce este?

Un pattern **comportamental** care permite salvarea și restaurarea stării anterioare a unui obiect
**fără a expune detaliile implementării** (encapsulare păstrată).

Practic: implementează **undo**.

---

## Când se folosește?

- Undo/redo (editor text, joc)
- Salvare stare (checkpoint într-un joc)
- Rollback la stare anterioară

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **Originator** | obiectul a cărui stare o salvăm; creează și restaurează Memento |
| **Memento** | „fotografia" stării — obiect simplu cu câmpuri |
| **Caretaker** | ține lista de Memento-uri (stiva undo); nu inspectează conținutul |

---

## Structura

```
Client → Caretaker (stiva de Memento-uri)
              ↕ salveaza/restaureaza
         Originator ──→ Memento
         (are stare)   (fotografia starii)
```

---

## Implementare pas cu pas

### Pasul 1 — Memento

Un obiect simplu, imutabil — stochează starea la un moment dat.
**Nu** expune logică — doar ține datele.

```java
public class Memento {
    // câmpurile stării — pot fi final (imutabil)
    private final String text;
    private final int pozitieCursor;

    public Memento(String text, int pozitie) {
        this.text = text;
        this.pozitieCursor = pozitie;
    }

    // getteri — Originator le va folosi la restaurare
    public String getText() { return text; }
    public int getPozitie() { return pozitie; }
}
```

---

### Pasul 2 — Originator

Obiectul cu stare. Știe să creeze Memento (salvare) și să restaureze din Memento.

```java
public class EditorText {
    private String text;
    private int pozitia;

    public EditorText() {
        this.text = "";
        this.pozitia = 0;
    }

    // operații normale
    public void scrieText(String fragment) {
        text += fragment;
        pozitia = text.length();
        System.out.println("Scris: '" + text + "'  cursor: " + pozitia);
    }

    public void stergeUltimeleN(int n) {
        if (n <= text.length()) {
            text = text.substring(0, text.length() - n);
            pozitia = text.length();
            System.out.println("Șters. Text curent: '" + text + "'");
        }
    }

    // SALVARE — creează un Memento cu starea curentă
    public Memento salveazaStare() {
        System.out.println("  [Checkpoint salvat]");
        return new Memento(text, pozitia);
    }

    // RESTAURARE — readuce starea din Memento
    public void restaureazaStare(Memento memento) {
        this.text = memento.getText();
        this.pozitia = memento.getPozitie();
        System.out.println("  [Restaurat] Text: '" + text + "'  cursor: " + pozitia);
    }

    public String getText() { return text; }
}
```

---

### Pasul 3 — Caretaker

Ține stiva de Memento-uri. **Nu inspectează** conținutul lor — joacă rol de gestionar.

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class Caretaker {
    // Deque ca stivă — push/pop pentru undo
    private Deque<Memento> istoricUndo = new ArrayDeque<>();

    // salvează starea curentă în stivă
    public void salveaza(Memento memento) {
        istoricUndo.push(memento);
    }

    // returnează ultimul Memento pentru undo (și îl scoate din stivă)
    public Memento undo() {
        if (istoricUndo.isEmpty()) {
            System.out.println("Nu există stare anterioară.");
            return null;
        }
        return istoricUndo.pop();
    }

    public int nrCheckpointuri() {
        return istoricUndo.size();
    }
}
```

---

### Pasul 4 — Main

```java
public class Main {
    public static void main(String[] args) {
        EditorText editor = new EditorText();
        Caretaker caretaker = new Caretaker();

        // scriem text și salvăm checkpoint-uri
        caretaker.salveaza(editor.salveazaStare());   // checkpoint 1: ""
        editor.scrieText("Salut ");

        caretaker.salveaza(editor.salveazaStare());   // checkpoint 2: "Salut "
        editor.scrieText("lume!");

        caretaker.salveaza(editor.salveazaStare());   // checkpoint 3: "Salut lume!"
        editor.scrieText(" Cum ești?");

        System.out.println("\nText curent: '" + editor.getText() + "'");
        System.out.println("Checkpointuri disponibile: " + caretaker.nrCheckpointuri());

        // UNDO - revine la checkpoint anterior
        System.out.println("\n--- Undo ---");
        editor.restaureazaStare(caretaker.undo());   // revine la "Salut lume!"

        System.out.println("\n--- Undo din nou ---");
        editor.restaureazaStare(caretaker.undo());   // revine la "Salut "

        System.out.println("\n--- Undo din nou ---");
        editor.restaureazaStare(caretaker.undo());   // revine la ""
    }
}
```

**Output:**
```
  [Checkpoint salvat]
Scris: 'Salut '  cursor: 6
  [Checkpoint salvat]
Scris: 'Salut lume!'  cursor: 11
  [Checkpoint salvat]
Scris: 'Salut lume! Cum ești?'  cursor: 22

Text curent: 'Salut lume! Cum ești?'
Checkpointuri disponibile: 3

--- Undo ---
  [Restaurat] Text: 'Salut lume!'  cursor: 11

--- Undo din nou ---
  [Restaurat] Text: 'Salut '  cursor: 6

--- Undo din nou ---
  [Restaurat] Text: ''  cursor: 0
```

---

## Variantă simplă (fără Deque, cu listă)

```java
import java.util.ArrayList;
import java.util.List;

public class CaretakerSimple {
    private List<Memento> istoric = new ArrayList<>();

    public void salveaza(Memento m) { istoric.add(m); }

    public Memento undo() {
        if (istoric.isEmpty()) return null;
        Memento m = istoric.get(istoric.size() - 1);
        istoric.remove(istoric.size() - 1);
        return m;
    }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „undo", „rollback", „revenire la stare anterioară"
- „salvare stare", „checkpoint"
- „istoric operații"

**Structura răspunsului la examen:**
1. Clasa `Memento` cu câmpurile stării (final, imutabil) + getteri
2. Clasa `Originator` (EditorText) cu `salveazaStare() → Memento` și `restaureazaStare(Memento)`
3. Clasa `Caretaker` cu `Deque<Memento>` (sau `List`) + `salveaza()` + `undo()`
4. `Main`: salveaza înainte de operație → operație → undo dacă e nevoie
