# Command — Ghid complet

## Ce este?

Un pattern **comportamental** care împachetează o cerere ca obiect — cu toate parametrii necesari.
Astfel poți: pune comenzi în coadă, executa mai târziu, face undo, sau loga operații.

---

## Când se folosește?

- Vrei să pui acțiuni în coadă (queue de comenzi)
- Ai nevoie de undo/redo
- Vrei să loghezi operații
- Exemple: comenzi la restaurant, editor text (Ctrl+Z), task queue

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **IComanda** | interfața comenzii — o singură metodă `execute()` |
| **ComandaConcretă** | implementează comanda, ține Receiver + parametri |
| **Receiver** | obiectul care știe să execute acțiunea (Bucătarul) |
| **Invoker** | ține lista de comenzi, le execută la momentul ales |
| **Client** | creează comenzile și le dă Invoker-ului |

---

## Structura

```
Client → Invoker (Ospatarul)
           - List<IComanda> comenzi
           + preiaComanda()
           + transmiteComenzile()
                    ↓ executa()
              IComanda
                  ↑
         ComandaPizza ──→ Bucatar (Receiver)
         ComandaPaste ──→ Bucatar
```

---

## Implementare pas cu pas

### Pasul 1 — Interfața Command

O singură metodă. Toate comenzile o implementează.

```java
public interface IComanda {
    void prelucreaza();   // sau execute()
}
```

---

### Pasul 2 — Receiver (Bucătarul)

Clasa care știe efectiv să execute acțiunile. Comanda îl apelează pe el.

```java
public class Bucatar {
    private String numeBucatar;

    public Bucatar(String numeBucatar) {
        this.numeBucatar = numeBucatar;
    }

    public void preparaPizza(String tip, String blat) {
        System.out.println("Bucatarul [" + numeBucatar + "] pregătește pizza: "
            + tip + " cu blat " + blat);
    }

    public void preparaPaste(String tip) {
        System.out.println("Bucatarul [" + numeBucatar + "] pregătește paste: " + tip);
    }

    public void preparaSalata(String ingrediente) {
        System.out.println("Bucatarul [" + numeBucatar + "] pregătește salată cu: " + ingrediente);
    }
}
```

---

### Pasul 3 — Comenzi concrete

Fiecare comandă ține Receiver-ul și parametrii necesari. `prelucreaza()` apelează metoda potrivită.

```java
public class ComandaPizza implements IComanda {
    private String tipPizza;
    private String tipBlat;
    private Bucatar bucatar;   // receiver

    public ComandaPizza(String tipPizza, String tipBlat, Bucatar bucatar) {
        this.tipPizza = tipPizza;
        this.tipBlat = tipBlat;
        this.bucatar = bucatar;
    }

    @Override
    public void prelucreaza() {
        bucatar.preparaPizza(tipPizza, tipBlat);   // delegă la receiver
    }
}

public class ComandaPaste implements IComanda {
    private String tipPaste;
    private Bucatar bucatar;

    public ComandaPaste(String tipPaste, Bucatar bucatar) {
        this.tipPaste = tipPaste;
        this.bucatar = bucatar;
    }

    @Override
    public void prelucreaza() {
        bucatar.preparaPaste(tipPaste);
    }
}

public class ComandaSalata implements IComanda {
    private String ingrediente;
    private Bucatar bucatar;

    public ComandaSalata(String ingrediente, Bucatar bucatar) {
        this.ingrediente = ingrediente;
        this.bucatar = bucatar;
    }

    @Override
    public void prelucreaza() {
        bucatar.preparaSalata(ingrediente);
    }
}
```

---

### Pasul 4 — Invoker (Ospătarul)

Nu știe ce sunt comenzile sau cum se execută — le pune în coadă și le trimite la momentul ales.

```java
import java.util.ArrayList;
import java.util.List;

public class Ospatar {
    private List<IComanda> listaComenzi = new ArrayList<>();

    // primește comanda de la client și o pune în coadă
    public void preiaComanda(IComanda comanda) {
        listaComenzi.add(comanda);
        System.out.println("Comanda preluată și pusă în coadă.");
    }

    // la momentul ales, trimite toate comenzile la bucătărie
    public void transmiteComenzile() {
        System.out.println("--- Trimitere comenzi la bucătărie ---");
        for (IComanda comanda : listaComenzi)
            comanda.prelucreaza();
        listaComenzi.clear();   // golește coada după execuție
    }

    // anulează ultima comandă din coadă
    public void anuleazaUltimaComanda() {
        if (!listaComenzi.isEmpty()) {
            listaComenzi.remove(listaComenzi.size() - 1);
            System.out.println("Ultima comandă anulată.");
        }
    }
}
```

---

### Pasul 5 — Main

```java
public class Main {
    public static void main(String[] args) {
        // receiver
        Bucatar bucatar = new Bucatar("Gheorghe");

        // invoker
        Ospatar ospatar = new Ospatar();

        // clientul creează comenzi și le dă ospatarului
        ospatar.preiaComanda(new ComandaPizza("Margherita", "subtire", bucatar));
        ospatar.preiaComanda(new ComandaPaste("Carbonara", bucatar));
        ospatar.preiaComanda(new ComandaSalata("rosii, castraveti, ulei", bucatar));

        System.out.println("(clientul a mai schimbat ceva)");
        ospatar.anuleazaUltimaComanda();   // renunță la salată

        // ospatarul transmite comenzile (la momentul ales)
        ospatar.transmiteComenzile();
    }
}
```

**Output:**
```
Comanda preluată și pusă în coadă.
Comanda preluată și pusă în coadă.
Comanda preluată și pusă în coadă.
(clientul a mai schimbat ceva)
Ultima comandă anulată.
--- Trimitere comenzi la bucătărie ---
Bucatarul [Gheorghe] pregătește pizza: Margherita cu blat subtire
Bucatarul [Gheorghe] pregătește paste: Carbonara
```

---

## Variantă cu Undo

Adaugi metodă `undo()` în interfață și ții o stivă de comenzi executate:

```java
public interface IComandaUndo {
    void execute();
    void undo();   // inversează acțiunea
}

public class ComandaAdaugaText implements IComandaUndo {
    private StringBuilder document;
    private String textAdaugat;

    public ComandaAdaugaText(StringBuilder document, String text) {
        this.document = document;
        this.textAdaugat = text;
    }

    @Override
    public void execute() {
        document.append(textAdaugat);
        System.out.println("Adăugat: '" + textAdaugat + "' → document: " + document);
    }

    @Override
    public void undo() {
        int pozitie = document.lastIndexOf(textAdaugat);
        document.delete(pozitie, pozitie + textAdaugat.length());
        System.out.println("Undo → document: " + document);
    }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „coadă de comenzi", „execuție amânată"
- „undo/redo"
- „înregistrare operații"
- „decuplare între cel care cere și cel care execută"

**Structura răspunsului la examen:**
1. Interfață `IComanda` cu `prelucreaza()` (sau `execute()`)
2. Receiver: clasa care face munca (`Bucatar`)
3. Comenzi concrete: fiecare implementează `IComanda`, ține Receiver + parametri
4. Invoker (`Ospatar`): ține `List<IComanda>`, are `preiaComanda()` și `transmiteComenzile()`
5. `Main`: creează Receiver → creează Comenzi cu Receiver → le dă Invoker-ului → Invoker execută

> **Diferența față de Strategy:**
> - **Strategy**: un singur algoritm selectat, executat imediat
> - **Command**: acțiuni împachetate, puse în coadă, executate mai târziu
