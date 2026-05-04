# Strategy — Ghid complet

## Ce este?

Un pattern **comportamental** care definește o familie de algoritmi, îi încapsulează separat
și îi face interschimbabili **la runtime**.

Contextul nu știe cum lucrează algoritmul — delegă totul Strategiei.

---

## Când se folosește?

- Ai mai mulți algoritmi pentru aceeași problemă (sortare, plată, discount)
- Vrei să schimbi algoritmul fără să modifici contextul
- Vrei să elimini if-else / switch cu tipuri de algoritmi
- Exemple: strategii de sortare, strategii de plată, strategii de alegere meniu

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **IStrategie** | interfața comună pentru toți algoritmii |
| **Strategie concretă** | implementează algoritmul specific |
| **Context** | ține referința la strategie, delegă execuția |
| **Client** | setează strategia în context |

---

## Structura

```
Client → Context
           - IStrategie strategie
           + setStrategie()
           + executa()  ──→ strategie.aplica()
                               ↑         ↑
                         StrategieA   StrategieB
```

---

## Implementare pas cu pas

### Pasul 1 — Interfața Strategy

```java
import java.util.List;

public interface IProcesabil {
    // primește datele și returnează rezultatul
    OfertaMeniu alegereMeniu(List<OfertaMeniu> listaMeniuri);
}
```

---

### Pasul 2 — Modelul de date

```java
public class OfertaMeniu {
    private String denumire;
    private int calorii;
    private int carbohidrati;
    private double pret;

    public OfertaMeniu(String denumire, int calorii, int carbohidrati, double pret) {
        this.denumire = denumire;
        this.calorii = calorii;
        this.carbohidrati = carbohidrati;
        this.pret = pret;
    }

    public String getDenumire() { return denumire; }
    public int getCalorii() { return calorii; }
    public int getCarbohidrati() { return carbohidrati; }
    public double getPret() { return pret; }

    @Override
    public String toString() {
        return denumire + " (" + calorii + " cal, " + pret + " RON)";
    }
}
```

---

### Pasul 3 — Strategii concrete

Fiecare implementează un algoritm diferit de alegere.

```java
// Strategia 1: alege meniul cu cele mai puține calorii
public class StrategieCaloriiMinim implements IProcesabil {
    @Override
    public OfertaMeniu alegereMeniu(List<OfertaMeniu> listaMeniuri) {
        OfertaMeniu minim = listaMeniuri.get(0);
        for (OfertaMeniu oferta : listaMeniuri) {
            if (oferta.getCalorii() < minim.getCalorii())
                minim = oferta;
        }
        return minim;
    }
}

// Strategia 2: alege meniul cel mai ieftin
public class StrategiePretMinim implements IProcesabil {
    @Override
    public OfertaMeniu alegereMeniu(List<OfertaMeniu> listaMeniuri) {
        OfertaMeniu minim = listaMeniuri.get(0);
        for (OfertaMeniu oferta : listaMeniuri) {
            if (oferta.getPret() < minim.getPret())
                minim = oferta;
        }
        return minim;
    }
}

// Strategia 3: alege meniul cu cei mai puțini carbohidrați
public class StrategieCarbohidratiMinim implements IProcesabil {
    @Override
    public OfertaMeniu alegereMeniu(List<OfertaMeniu> listaMeniuri) {
        OfertaMeniu minim = listaMeniuri.get(0);
        for (OfertaMeniu oferta : listaMeniuri) {
            if (oferta.getCarbohidrati() < minim.getCarbohidrati())
                minim = oferta;
        }
        return minim;
    }
}
```

---

### Pasul 4 — Context

Ține referința la strategie și delegă execuția. Strategia poate fi schimbată oricând.

```java
import java.util.ArrayList;
import java.util.List;

public class MeniuRestaurant {
    private List<OfertaMeniu> listaMeniuri = new ArrayList<>();
    private IProcesabil strategie;   // referința la strategie curentă

    public void addOferta(OfertaMeniu oferta) {
        listaMeniuri.add(oferta);
    }

    // setează strategia — poate fi apelat oricând pentru schimbare
    public void setStrategie(IProcesabil strategie) {
        this.strategie = strategie;
    }

    // execută algoritmul prin delegare la strategie
    public OfertaMeniu alegeMeniu() {
        if (strategie == null)
            throw new UnsupportedOperationException("Nicio strategie setată");
        return strategie.alegereMeniu(listaMeniuri);
    }
}
```

---

### Pasul 5 — Main

```java
public class Main {
    public static void main(String[] args) {
        // construiește contextul
        MeniuRestaurant restaurant = new MeniuRestaurant();
        restaurant.addOferta(new OfertaMeniu("Salată", 150, 10, 25.0));
        restaurant.addOferta(new OfertaMeniu("Paste", 600, 80, 35.0));
        restaurant.addOferta(new OfertaMeniu("Grătar", 400, 5, 55.0));
        restaurant.addOferta(new OfertaMeniu("Supă", 200, 20, 20.0));

        // setează strategia 1
        restaurant.setStrategie(new StrategieCaloriiMinim());
        System.out.println("Recomandat (calorii minime): " + restaurant.alegeMeniu());

        // schimbă strategia la runtime
        restaurant.setStrategie(new StrategiePretMinim());
        System.out.println("Recomandat (cel mai ieftin): " + restaurant.alegeMeniu());

        // altă strategie
        restaurant.setStrategie(new StrategieCarbohidratiMinim());
        System.out.println("Recomandat (carbohidrați minimi): " + restaurant.alegeMeniu());
    }
}
```

**Output:**
```
Recomandat (calorii minime): Salată (150 cal, 25.0 RON)
Recomandat (cel mai ieftin): Supă (200 cal, 20.0 RON)
Recomandat (carbohidrați minimi): Grătar (400 cal, 55.0 RON)
```

---

## Variantă: strategii de plată

```java
// interfața
public interface IStrategieDecontare {
    void plateste(double suma);
}

// strategii
public class PlataCuCard implements IStrategieDecontare {
    private String numarCard;
    public PlataCuCard(String numarCard) { this.numarCard = numarCard; }

    @Override
    public void plateste(double suma) {
        System.out.println("Plată " + suma + " RON cu cardul " + numarCard);
    }
}

public class PlataCuCash implements IStrategieDecontare {
    @Override
    public void plateste(double suma) {
        System.out.println("Plată " + suma + " RON cash");
    }
}

public class PlataCuVoucher implements IStrategieDecontare {
    private String cod;
    public PlataCuVoucher(String cod) { this.cod = cod; }

    @Override
    public void plateste(double suma) {
        System.out.println("Plată " + suma + " RON cu voucherul " + cod);
    }
}

// context
public class Cos {
    private double total;
    private IStrategieDecontare strategie;

    public Cos(double total) { this.total = total; }
    public void setStrategie(IStrategieDecontare s) { this.strategie = s; }
    public void finalizeaza() { strategie.plateste(total); }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „mai mulți algoritmi pentru aceeași problemă"
- „selectare", „alegere", „criteriu de..."
- „schimbă comportamentul la runtime"
- „sortare după X sau Y", „plată cu card sau cash"

**Structura răspunsului la examen:**
1. Interfață `IStrategie` cu o metodă (algoritmul)
2. Câte o clasă per algoritm concret, implementează `IStrategie`
3. Clasa Context cu `private IStrategie strategie` + `setStrategie()` + metodă care delegă
4. `Main` creează contextul, setează strategii diferite, execută

> **Diferența față de State:**
> - **Strategy**: algoritmul e schimbat de CLIENT din exterior
> - **State**: starea se schimbă de OBIECT în interior, în funcție de condiții
