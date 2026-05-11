# CHEAT SHEET — Test 2 CTS

Cod bazat pe implementările de la seminar (G1093). Denumirile sunt exact cele din cod.

---

## STRUCTURAL

---

### 01. COMPOSITE
**Seminar:** INod (interfață) + NodStructura (container) + Virus (frunză)

```java
public interface INod {
    int getTotalCazuri();
    float getRataMortalitate();     // doar Virus
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
        for (INod nod : listaFii) total += nod.getTotalCazuri(); // RECURSIV
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
INod europa = new NodStructura("Europa");
europa.addNod(new NodStructura("Romania")); // index 0
europa.addNod(new NodStructura("Italia"));  // index 1
europa.getNode(0).addNod(new Virus("Covid", 50, 0.01f));
europa.getNode(1).addNod(new Virus("Covid", 150, 0.01f));
System.out.println(europa.getTotalCazuri());      // 200
System.out.println(europa.esteSiguraDeVizitat()); // true
```

---

### 02. PROXY
**Seminar:** ISpital (interfață) + Spital (real) + ProxySpital (intermediar cu Map vizite)

```java
public interface ISpital {
    void accesSpital(String vizitator, String pacient);
}

public class Spital implements ISpital {
    @Override
    public void accesSpital(String vizitator, String pacient) {
        System.out.println(vizitator + " a vizitat pe " + pacient);
    }
}

public class ProxySpital implements ISpital {
    private ISpital spital;
    private Map<String, String> vizite = new HashMap<>(); // key=pacient, value=vizitator

    public ProxySpital(ISpital spital) { this.spital = spital; }

    @Override
    public void accesSpital(String vizitator, String pacient) {
        if (vizite.containsKey(pacient)) {
            System.out.println("Nu se poate. A mai fost vizitat de " + vizite.get(pacient));
        } else {
            vizite.put(pacient, vizitator);
            this.spital.accesSpital(vizitator, pacient); // obligatoriu — delegă la real
        }
    }

    public void resetZi() { vizite.clear(); }
}

// Main
ISpital spital = new ProxySpital(new Spital("Spitalul nr 1"));
spital.accesSpital("Gigel", "Pacient 1");  // OK
spital.accesSpital("Costel", "Pacient 1"); // Refuzat
((ProxySpital) spital).resetZi();
spital.accesSpital("Marcel", "Pacient 1"); // OK după reset
```

---

### 05. FLYWEIGHT
**Seminar:** IRecomandare + Recomandare (intrinsec) + FabricaDeRecomandari (HashMap) + Reteta (extrinsec)

```java
public interface IRecomandare {
    void printare(Reteta reteta); // Reteta = stare extrinsecă
}

public class Recomandare implements IRecomandare {
    private String textRecomandare; // stare intrinsecă — partajată

    public Recomandare(String text) { this.textRecomandare = text; }

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
        if (!colectieRecomandari.containsKey(cheie))
            throw new RuntimeException("Nu exista aceasta recomandare " + cheie);
        return colectieRecomandari.get(cheie); // ACELAȘI obiect pentru aceeași cheie
    }
}

// Main
for (int i = 0; i < 10; i++) {
    Reteta reteta = new Reteta(1 + i, "otita", List.of("paracetamol"));
    FabricaDeRecomandari.getRecomandare("Somn").printare(reteta);
}
```

---

### 06. DECORATOR
**Seminar:** IComanda + Comanda (baza) + DecoratorAbstract + DecoratorMartie

```java
public interface IComanda {
    void inchideComanda();
    void addProdus(float pret);
    void printeazaBon();
    double getTotal();
}

public class Comanda implements IComanda {
    private int id;
    private List<Float> listaProduse = new ArrayList<>();
    private boolean esteInchisa = false;

    @Override public void addProdus(float pret) { listaProduse.add(pret); }

    @Override public void inchideComanda() {
        if (!esteInchisa) { esteInchisa = true; System.out.println("Comanda s-a inchis"); }
    }

    @Override public void printeazaBon() {
        if (esteInchisa) System.out.println("Comanda " + id + " | Total: " + getTotal());
    }

    @Override public double getTotal() {
        float s = 0; for (Float f : listaProduse) s += f; return s;
    }
}

public abstract class DecoratorAbstract implements IComanda {
    private IComanda comanda; // obiectul decorat

    public DecoratorAbstract(IComanda comanda) { this.comanda = comanda; }

    @Override public void inchideComanda() { this.comanda.inchideComanda(); }
    @Override public void addProdus(float pret) { this.comanda.addProdus(pret); }
    @Override public void printeazaBon() { this.comanda.printeazaBon(); }
    @Override public double getTotal() { return this.comanda.getTotal(); }
}

public class DecoratorMartie extends DecoratorAbstract {
    private boolean esteFemeie;

    public DecoratorMartie(IComanda comanda, boolean esteFemeie) {
        super(comanda);
        this.esteFemeie = esteFemeie;
    }

    @Override public void printeazaBon() {
        if (esteFemeie) System.out.println("** La multi ani! **");
        super.printeazaBon();
    }

    @Override public double getTotal() {
        return esteFemeie ? 0.9 * super.getTotal() : super.getTotal();
    }
}

// Main
IComanda comanda = new DecoratorMartie(new Comanda(1), true);
comanda.addProdus(1); comanda.addProdus(2); comanda.addProdus(4);
comanda.inchideComanda();
comanda.printeazaBon();                          // "** La multi ani! **" + bon
System.out.println("Total: " + comanda.getTotal()); // 6.3
```

---

### 09. ADAPTER
**Seminar:** IPrizaAmerica (target) + PrizaEuropa (existing) + AdapterEuropaToAmerica (class adapter)

```java
public interface IPrizaAmerica { void incarcaLa110V(); } // target — ce vrea clientul
public interface IPrizaEuropa  { void incarcaLa230V(); } // existing

public class PrizaEuropa implements IPrizaEuropa {
    @Override public void incarcaLa230V() { System.out.println("Priza ofera flux 230V...."); }
}

// Class adapter — extends ce avem, implements ce vrea clientul
public class AdapterEuropaToAmerica extends PrizaEuropa implements IPrizaAmerica {
    @Override public void incarcaLa110V() {
        this.incarcaLa230V(); // folosește ce există
        System.out.println("Adaptor care face conversie de la 230V la 110V.");
    }
}

public class Laptop {
    public void incarca(IPrizaAmerica priza) { priza.incarcaLa110V(); }
}

// Main
Laptop laptop = new Laptop("Dell", 60);
laptop.incarca(new AdapterEuropaToAmerica()); // adaptorul face trecerea
```

**Object adapter (alternativă cu compoziție — exemplul USB din seminar):**
```java
public class Adaptor implements IUSBcIncarcator {
    private IMicroUSBIncarcator incarcatorVechi; // compoziție în loc de moștenire

    public Adaptor(IMicroUSBIncarcator inc) { this.incarcatorVechi = inc; }

    @Override public void incarcaUSBc() { incarcatorVechi.incarcaMicroUSB(); }
}

// Main
Telefon telefon = new Telefon("Huawei p20", 60);
telefon.chargeUSBc(new Adaptor(new MicroUSB()));
```

---

### 08. FACADE
```java
public class SubsistemA { public void operatieA() { System.out.println("A"); } }
public class SubsistemB { public void operatieB() { System.out.println("B"); } }
public class SubsistemC { public void operatieC() { System.out.println("C"); } }

public class Facade {
    private SubsistemA a = new SubsistemA();
    private SubsistemB b = new SubsistemB();
    private SubsistemC c = new SubsistemC();

    public void operatieComplexaSimplificata() { a.operatieA(); b.operatieB(); c.operatieC(); }
}

// Main
new Facade().operatieComplexaSimplificata();
```

---

## COMPORTAMENTAL

---

### 03. STRATEGY
**Seminar:** IStrategy + PlataCard/PlataCash + Bon (context)

```java
public interface IStrategy { void plata(int suma); }

public class PlataCard implements IStrategy {
    @Override public void plata(int suma) { System.out.println("Plata card " + suma); }
}

public class PlataCash implements IStrategy {
    @Override public void plata(int suma) { System.out.println("Plata cash " + suma); }
}

public class Bon { // Context
    private IStrategy strategie;
    private float total;

    public Bon(float total) { this.total = total; }
    public void setStrategie(IStrategy s) { this.strategie = s; }
    public void inchideBon() { if (strategie != null) strategie.plata((int) total); }
}

// Main
Bon bon = new Bon(100f);
bon.setStrategie(new PlataCash()); bon.inchideBon(); // "Plata cash 100"
bon.setStrategie(new PlataCard()); bon.inchideBon(); // "Plata card 100"
```

---

### 04. CHAIN OF RESPONSIBILITY
**Seminar:** IHandler + AbstractHandler + FiltrarePret/FiltrareRecenzii/FiltrareProcentReducere

```java
public interface IHandler {
    ColectieProduse filtrareProduse(ColectieProduse colectie, Client client);
    void setNextHandler(IHandler next);
    IHandler getNextHandler();
}

public abstract class AbstractHandler implements IHandler {
    private IHandler nextHandler;

    @Override public void setNextHandler(IHandler next) { this.nextHandler = next; }
    @Override public IHandler getNextHandler() { return nextHandler; }
}

public class FiltrarePret extends AbstractHandler {
    @Override
    public ColectieProduse filtrareProduse(ColectieProduse colectie, Client client) {
        for (var produs : colectie.getListaProduse()) {
            if (produs.getPret() > client.getBuget()) colectie.removeProdus(produs);
        }
        System.out.println("S-a filtrat dupa pret");
        if (getNextHandler() != null) return getNextHandler().filtrareProduse(colectie, client);
        return colectie;
    }
}
// FiltrareRecenzii, FiltrareProcentReducere — aceeași structură

// Main
IHandler f1 = new FiltrarePret();
IHandler f2 = new FiltrareRecenzii();
IHandler f3 = new FiltrareProcentReducere();

f1.setNextHandler(f2); f2.setNextHandler(f3);

Client client = new Client("Gigel", 175, true, false);
ColectieProduse rezultat = f1.filtrareProduse(colectie, client);
```

---

### 07. OBSERVER
**Seminar:** IObserver + IServiciuMeteo + ServiciuMeteo + Client

```java
public interface IObserver { void mesaj(float temperatura); }

public interface IServiciuMeteo {
    void adaugaObserver(IObserver o);
    void elimibaObserver(IObserver o);
    void notivicareObservers(float temperatura);
    void setTemperatura(float temperatura);
}

public class ServiciuMeteo implements IServiciuMeteo {
    private List<IObserver> observers = new ArrayList<>();
    private float temperatura;

    public ServiciuMeteo(float temp) { this.temperatura = temp; }

    @Override public void setTemperatura(float temp) {
        if (temp != temperatura) temperatura = temp;
        notivicareObservers(temp); // trigger
    }

    @Override public void adaugaObserver(IObserver o) { observers.add(o); }
    @Override public void elimibaObserver(IObserver o) { observers.remove(o); }

    @Override public void notivicareObservers(float temp) {
        for (IObserver o : observers) o.mesaj(temp); // notifică toți
    }
}

public class Client implements IObserver {
    @Override public void mesaj(float temp) {
        System.out.println("Clientul a fost anuntat. Temperatura noua: " + temp);
    }
}

// Main
IServiciuMeteo serviciu = new ServiciuMeteo(10);
IObserver obs1 = new Client(), obs2 = new Client(), obs3 = new Client();

serviciu.adaugaObserver(obs1); serviciu.adaugaObserver(obs2); serviciu.adaugaObserver(obs3);
serviciu.setTemperatura(30); // notifică obs1, obs2, obs3

serviciu.elimibaObserver(obs3);
serviciu.setTemperatura(25); // notifică obs1, obs2
```

---

### 10. COMMAND

```java
public interface IComanda { void executa(); }

public class Lumina { // Receiver
    public void aprinde() { System.out.println("Lumina aprinsa"); }
    public void stinge()  { System.out.println("Lumina stinsa"); }
}

public class ComandaAprinde implements IComanda {
    private Lumina lumina;
    public ComandaAprinde(Lumina l) { this.lumina = l; }
    @Override public void executa() { lumina.aprinde(); }
}

public class Telecomanda { // Invoker
    private List<IComanda> comenzi = new ArrayList<>();
    public void adaugaComanda(IComanda c) { comenzi.add(c); }
    public void executaToate() { for (IComanda c : comenzi) c.executa(); comenzi.clear(); }
}

// Main
Lumina lumina = new Lumina();
Telecomanda telecomanda = new Telecomanda();
telecomanda.adaugaComanda(new ComandaAprinde(lumina));
telecomanda.executaToate();
```

---

## REZUMAT — LINIA CHEIE DIN FIECARE PATTERN

| Pattern | Linia cheie |
|---------|-------------|
| **Composite** | `for (INod nod : listaFii) total += nod.getTotalCazuri();` |
| **Proxy** | `this.spital.accesSpital(vizitator, pacient);` (după verificare) |
| **Flyweight** | `return colectieRecomandari.get(cheie);` (din factory) |
| **Decorator** | `super.getTotal()` / `super.printeazaBon()` (delegă la decorat) |
| **Adapter** | `this.incarcaLa230V();` (în AdapterEuropaToAmerica) |
| **Strategy** | `this.strategie.plata((int) total);` (în Bon.inchideBon) |
| **CoR** | `getNextHandler().filtrareProduse(colectie, client);` |
| **Observer** | `for (IObserver o : observers) o.mesaj(temp);` |
| **Command** | `lumina.aprinde();` (în ComandaAprinde.executa) |
| **Facade** | `a.operatieA(); b.operatieB(); c.operatieC();` |

---

## CLEAN CODE — OBLIGATORIU

```java
package cts.poalelungi.robert.g1090.proxy;    // un pachet per pattern
package cts.poalelungi.robert.g1090.composite;
package cts.poalelungi.robert.g1090.strategy;
package cts.poalelungi.robert.g1090.main;
```

- Denumiri legate de subiect: `ProxySpital`, `FiltrarePret`, `PlataCard` — **NU** `HandlerA`, `StrategieA`
- Depinde de interfețe: `private ISpital spital` — **NU** `private Spital spital`
- Mesaje contextuale: `System.out.println(vizitator + " a vizitat pe " + pacient)`
