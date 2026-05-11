# Composite

Pattern **structural** — tratează uniform frunzele și nodurile container printr-o interfață comună. Operațiile se propagă recursiv în arbore.

---

## Participanți (din seminar)

| Rol | Clasă |
|-----|-------|
| Interfață comună | `INod` |
| Nod container | `NodStructura` — ține `List<INod> listaFii`, propagă recursiv |
| Frunză | `Virus` — returnează valori proprii, aruncă excepție la metodele inaplicabile |
| Client | `Main` |

---

## Explicație pas cu pas

**Ideea în o propoziție:** ai un arbore (Europa → România → Virus), și vrei să chemi `getTotalCazuri()` pe rădăcină să obții totalul din tot arborele — fără să știi câte niveluri sunt.

**Rețeta:**
1. Interfață comună (`INod`) cu toate metodele
2. Nod container (`NodStructura`) — ține `List<INod>`, propagă recursiv
3. Frunză (`Virus`) — returnează valoarea proprie, aruncă excepție la metodele de container
4. Main — construiește arborele cu `addNod()`, apelează pe rădăcină

**Pasul 1 — Interfața comună**

Toți participanții (noduri și frunze) implementează aceeași interfață. Include metode pentru ambele roluri.

```java
public interface INod {
    int getTotalCazuri();
    float getRataMortalitate();     // doar Virus
    boolean esteSiguraDeVizitat(); // doar NodStructura
    void addNod(INod nod);
    void removeNode(INod nod);
    INod getNode(int index);
}
```

**Pasul 2 — Nodul container (NodStructura)**

Ține o listă de copii și propagă recursiv. `getTotalCazuri()` iterează prin copii și adună rezultatele. Metodele inaplicabile frunzelor (ca `getRataMortalitate()`) aruncă excepție.

```java
public class NodStructura implements INod {
    private String label;
    private List<INod> listaFii = new ArrayList<>();

    @Override
    public int getTotalCazuri() {
        int total = 0;
        for (INod nod : listaFii) total += nod.getTotalCazuri(); // recursiv
        return total;
    }

    @Override
    public boolean esteSiguraDeVizitat() { return getTotalCazuri() <= 1000; }

    @Override
    public float getRataMortalitate() {
        throw new UnsupportedOperationException("Nu tine de nod structura");
    }

    @Override public void addNod(INod nod) { listaFii.add(nod); }
    @Override public void removeNode(INod nod) { listaFii.remove(nod); }
    @Override public INod getNode(int i) { return listaFii.get(i); }
}
```

**Pasul 3 — Frunza (Virus)**

Nu are copii. Returnează valorile proprii la metodele relevante, aruncă `UnsupportedOperationException` la metodele de container (`addNod`, `removeNode`, `getNode`, `esteSiguraDeVizitat`).

```java
public class Virus implements INod {
    private String tulpina;
    private int nrCazuri;
    private float rataMortalitate;

    @Override public int getTotalCazuri() { return nrCazuri; }
    @Override public float getRataMortalitate() { return rataMortalitate; }

    @Override public boolean esteSiguraDeVizitat() {
        throw new UnsupportedOperationException("Nu este pentru o frunza");
    }
    @Override public void addNod(INod nod) { throw new UnsupportedOperationException(); }
    @Override public void removeNode(INod nod) { throw new UnsupportedOperationException(); }
    @Override public INod getNode(int i) { throw new UnsupportedOperationException(); }
}
```

**Pasul 4 — Construiești arborele în Main**

Creezi rădăcina, adaugi noduri copil, adaugi frunze la copii.

```java
INod nodEuropa = new NodStructura("Europa");
nodEuropa.addNod(new NodStructura("Romania")); // index 0
nodEuropa.addNod(new NodStructura("Italia"));  // index 1
nodEuropa.getNode(0).addNod(new Virus("Covid", 50, 0.01f));
nodEuropa.getNode(1).addNod(new Virus("Covid", 150, 0.01f));
nodEuropa.getNode(1).addNod(new Virus("Gripa", 150, 0.01f));
```

**Pasul 5 — Apelezi pe rădăcină**

`getTotalCazuri()` pe Europa propagă recursiv: Europa → România (50) + Italia (150+150) = 350.

```java
System.out.println("Total cazuri Europa: " + nodEuropa.getTotalCazuri());      // 350
System.out.println("Este sigura Europa?: " + nodEuropa.esteSiguraDeVizitat()); // true
```

**Ce să ții minte:** frunzele și nodurile au ACEEAȘI interfață; nodul container iterează lista de copii recursiv; frunza aruncă excepție la metodele de container.

---

## Cod seminar

```java
public interface INod {
    int getTotalCazuri();
    float getRataMortalitate();     // doar Virus (frunză)
    boolean esteSiguraDeVizitat(); // doar NodStructura
    void addNod(INod nod);
    void removeNode(INod nod);
    INod getNode(int index);
}

public class NodStructura implements INod {
    private String label;
    private List<INod> listaFii = new ArrayList<>();

    @Override
    public int getTotalCazuri() {
        int total = 0;
        for (INod nod : listaFii) total += nod.getTotalCazuri(); // recursiv
        return total;
    }

    @Override
    public boolean esteSiguraDeVizitat() { return getTotalCazuri() <= 1000; }

    @Override
    public float getRataMortalitate() {
        throw new UnsupportedOperationException("Nu tine de nod structura");
    }

    @Override public void addNod(INod nod) { listaFii.add(nod); }
    @Override public void removeNode(INod nod) { listaFii.remove(nod); }
    @Override public INod getNode(int i) { return listaFii.get(i); }
}

public class Virus implements INod {
    private String tulpina;
    private int nrCazuri;
    private float rataMortalitate;

    @Override public int getTotalCazuri() { return nrCazuri; }
    @Override public float getRataMortalitate() { return rataMortalitate; }

    @Override public boolean esteSiguraDeVizitat() {
        throw new UnsupportedOperationException("Nu este pentru o frunza");
    }
    @Override public void addNod(INod nod) { throw new UnsupportedOperationException(); }
    @Override public void removeNode(INod nod) { throw new UnsupportedOperationException(); }
    @Override public INod getNode(int i) { throw new UnsupportedOperationException(); }
}

// Main
INod nodEuropa = new NodStructura("Europa");
nodEuropa.addNod(new NodStructura("Romania")); // index 0
nodEuropa.addNod(new NodStructura("Italia"));  // index 1
nodEuropa.getNode(0).addNod(new Virus("Covid", 50, 0.01f));
nodEuropa.getNode(1).addNod(new Virus("Covid", 150, 0.01f));
nodEuropa.getNode(1).addNod(new Virus("Gripa", 150, 0.01f));

System.out.println("Total cazuri Europa: " + nodEuropa.getTotalCazuri());      // 350
System.out.println("Este sigura Europa?: " + nodEuropa.esteSiguraDeVizitat()); // true
```

---

## Structura la examen

1. **Interfață** cu metode comune + `addNod/removeNode/getNode`
2. **NodStructura** — `List<INod>`, `for` recursiv în metodele de agregare
3. **Virus (frunză)** — returnează valoarea proprie, `UnsupportedOperationException` la rest
4. **Main** — construiește arborele cu `addNod()`, apelează pe rădăcină

---

## Cum recunoști

- „structură arborescentă", „mai multe niveluri" (continente → țări → tulpini)
- „numărul total de cazuri / produse / voturi" — propagare recursivă
- Interfață dată în subiect (`AbstractRezultat`, `IProdus`, `INod`)
