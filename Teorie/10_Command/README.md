# Command

Pattern **comportamental** — acțiunea este împachetată într-un obiect. Comenzile pot fi puse în coadă, executate amânat sau anulate (undo).

---

## Participanți

| Rol | Descriere |
|-----|-----------|
| `IComanda` | interfața cu metoda `executa()` |
| `Receiver` | clasa care face munca efectivă |
| Comenzi concrete | implementează `IComanda`, țin referința la Receiver |
| `Invoker` | ține `List<IComanda>`, execută comenzile |
| Client | `Main` — creează comenzile și le trimite la Invoker |

---

## Structură generală

```java
public interface IComanda {
    void executa();
}

// Receiver — face munca efectivă
public class Lumina {
    public void aprinde() { System.out.println("Lumina aprinsa"); }
    public void stinge()  { System.out.println("Lumina stinsa"); }
}

// Comenzi concrete — împachetează acțiunea
public class ComandaAprinde implements IComanda {
    private Lumina lumina;

    public ComandaAprinde(Lumina lumina) { this.lumina = lumina; }

    @Override
    public void executa() { lumina.aprinde(); }
}

public class ComandaStinge implements IComanda {
    private Lumina lumina;

    public ComandaStinge(Lumina lumina) { this.lumina = lumina; }

    @Override
    public void executa() { lumina.stinge(); }
}

// Invoker — ține și execută comenzile
public class Telecomanda {
    private List<IComanda> comenzi = new ArrayList<>();

    public void adaugaComanda(IComanda comanda) { comenzi.add(comanda); }

    public void executaToate() {
        for (IComanda c : comenzi) c.executa();
        comenzi.clear();
    }
}

// Main
Lumina lumina = new Lumina();
Telecomanda telecomanda = new Telecomanda();

telecomanda.adaugaComanda(new ComandaAprinde(lumina));
telecomanda.adaugaComanda(new ComandaStinge(lumina));
telecomanda.executaToate();
```

---

## Structura la examen

1. **Interfață** `IComanda` cu `executa()` (și opțional `undo()`)
2. **Receiver** — clasa care face munca reală
3. **Comenzi concrete** — fiecare ține `private Receiver receiver`, implementează `executa()` apelând receiver-ul
4. **Invoker** — `List<IComanda>`, metodă `executaToate()`
5. **Main** — creează receiver, creează comenzi cu receiver-ul, le adaugă la invoker

---

## Cum recunoști

- „coadă de comenzi", „execuție amânată"
- „undo / redo"
- „acțiunile sunt obiecte care pot fi stocate"
