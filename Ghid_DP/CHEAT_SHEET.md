# CHEAT SHEET — Test 2 CTS
> Folosești DiagrameDesignPatterns.pdf pentru UML. Foaia asta îți dă CODUL pentru fiecare pattern.
> Fiecare pattern are: denumirile din diagrama cursului + linia cheie (galbenă în PDF) + scheletul complet.

---

## STRUCTURAL

---

### DECORATOR
**Linia cheie (galben în PDF):**
```java
public void operatie() {
    produsDecorat.operatie();   // delegă la obiectul decorat
}
```

**Schelet complet:**
```java
// 1. Componentul abstract
public abstract class ProdusAbstract {
    public abstract void operatie();
}

// 2. Produsul concret (baza)
public class ProdusCoct extends ProdusAbstract {
    @Override
    public void operatie() {
        System.out.println("Produs de baza");
    }
}

// 3. Decorator abstract — extinde ProdusAbstract, ține referința la el
public abstract class Decorator extends ProdusAbstract {
    protected ProdusAbstract produsDecorat;   // ← referința cheie

    public Decorator(ProdusAbstract produsDecorat) {
        this.produsDecorat = produsDecorat;
    }

    @Override
    public void operatie() {
        produsDecorat.operatie();   // ← LINIA GALBENĂ
    }
}

// 4. Decorator concret — suprascrie și adaugă
public class DecoratorConcretA extends Decorator {
    public DecoratorConcretA(ProdusAbstract p) { super(p); }

    @Override
    public void operatie() {
        super.operatie();           // ce era deja
        System.out.println("+ extra A");
    }

    public void metodaNoua() { System.out.println("metoda noua A"); }
}

// Main
ProdusAbstract p = new DecoratorConcretA(new ProdusCoct());
p.operatie();
```

---

### COMPOSITE
**Clase din diagrama cursului:** `ComponentaAbstracta`, `NodFrunza`, `Composite`

```java
// 1. Componenta abstracta
public abstract class ComponentaAbstracta {
    public abstract void metodaSpecifica();
    public void adaugaNod(ComponentaAbstracta c) { throw new UnsupportedOperationException(); }
    public void stergeNod(ComponentaAbstracta c) { throw new UnsupportedOperationException(); }
    public ComponentaAbstracta getNodCopil(int i) { throw new UnsupportedOperationException(); }
}

// 2. NodFrunza (leaf)
public class NodFrunza extends ComponentaAbstracta {
    private String nume;
    public NodFrunza(String nume) { this.nume = nume; }

    @Override
    public void metodaSpecifica() {
        System.out.println("Frunza: " + nume);
    }
}

// 3. Composite — ține lista, iterează recursiv
public class Composite extends ComponentaAbstracta {
    private String nume;
    private List<ComponentaAbstracta> copii = new ArrayList<>();

    public Composite(String nume) { this.nume = nume; }

    @Override
    public void adaugaNod(ComponentaAbstracta c) { copii.add(c); }
    @Override
    public void stergeNod(ComponentaAbstracta c) { copii.remove(c); }
    @Override
    public ComponentaAbstracta getNodCopil(int i) { return copii.get(i); }

    @Override
    public void metodaSpecifica() {
        System.out.println("[" + nume + "]");
        for (ComponentaAbstracta c : copii)
            c.metodaSpecifica();   // ← RECURSIE
    }
}

// Main
Composite radacina = new Composite("root");
radacina.adaugaNod(new NodFrunza("A"));
Composite sub = new Composite("sub");
sub.adaugaNod(new NodFrunza("B"));
radacina.adaugaNod(sub);
radacina.metodaSpecifica();
```

---

### PROXY
**Linia cheie (galben în PDF):**
```java
public void operatie() {
    entitate.operatie();   // delegă la obiectul real
}
```

```java
// 1. Interfata
public interface InterfataEntitate {
    void operatie();
}

// 2. Entitate reală
public class Entitate implements InterfataEntitate {
    @Override
    public void operatie() { System.out.println("Operatie reala"); }
}

// 3. Proxy — aceeași interfață, adaugă logică
public class Proxy implements InterfataEntitate {
    private Entitate entitate;   // referința la real

    public Proxy() {
        this.entitate = new Entitate();   // sau lazy
    }

    @Override
    public void operatie() {
        System.out.println("Proxy: verificare acces...");
        entitate.operatie();   // ← LINIA GALBENĂ
    }
}

// Main
InterfataEntitate p = new Proxy();
p.operatie();
```

---

### ADAPTER (Adaptor de obiecte)
**Linia cheie (galben în PDF):**
```java
// în Adaptor:
referinta.metoda();
// alte operatii
```

```java
// 1. Clasa existentă (nu o modifici)
public class ClasaExistenta {
    public void metoda() { System.out.println("metoda veche"); }
}

// 2. Interfata nouă cerută de client
public interface ClasaContextNou {
    void metodaSpecifica();
}

// 3. Adaptor — implementează interfata nouă, ține referința la cea veche
public class Adaptor implements ClasaContextNou {
    private ClasaExistenta referinta;   // ← referinta din diagrama

    public Adaptor(ClasaExistenta referinta) {
        this.referinta = referinta;
    }

    @Override
    public void metodaSpecifica() {
        referinta.metoda();   // ← LINIA GALBENĂ — traduce apelul
    }
}

// Main
ClasaContextNou adaptor = new Adaptor(new ClasaExistenta());
adaptor.metodaSpecifica();
```

---

### FACADE
```java
// Subsisteme existente
public class Clasa1 { public void metoda1() { System.out.println("Clasa1"); } }
public class Clasa2 { public void metoda2() { System.out.println("Clasa2"); } }
public class Clasa4 { public void metoda4() { System.out.println("Clasa4"); } }

// Facade — orchestrează subsistemele
public class Facade {
    private Clasa1 c1 = new Clasa1();
    private Clasa2 c2 = new Clasa2();
    private Clasa4 c4 = new Clasa4();

    public void metoda1() { c1.metoda1(); c2.metoda2(); }
    public void metoda2() { c4.metoda4(); }
}

// Main — clientul apelează doar Facade
Facade f = new Facade();
f.metoda1();
```

---

## COMPORTAMENTAL

---

### CHAIN OF RESPONSIBILITY
**Clase din diagrama cursului:** `Handler` (cu `-succesor:Handler`), `HandlerA`, `HandlerB`

```java
// 1. Handler abstract
public abstract class Handler {
    private Handler succesor;   // ← din diagrama: -succesor:Handler

    public Handler setSuccesor(Handler succesor) {
        this.succesor = succesor;
        return succesor;   // permite chaining: h1.setSuccesor(h2).setSuccesor(h3)
    }

    protected void gestioneazaUrmatorul(Object cerere) {
        if (succesor != null)
            succesor.gestioneazaCererea(cerere);
    }

    public abstract void gestioneazaCererea(Object cerere);   // ← din diagrama
}

// 2. Handlere concrete
public class HandlerA extends Handler {
    @Override
    public void gestioneazaCererea(Object cerere) {
        if (/* pot rezolva */) {
            System.out.println("HandlerA rezolvă");
        } else {
            gestioneazaUrmatorul(cerere);   // pasează mai departe
        }
    }
}

// Main
Handler h1 = new HandlerA();
Handler h2 = new HandlerB();
h1.setSuccesor(h2);
h1.gestioneazaCererea(cerere);
```

---

### COMMAND
**Linia cheie (galben în PDF):**
```java
public void executa() {
    executant.actiune();   // ← LINIA GALBENĂ
}
```
**Clase din diagrama cursului:** `ManagerComenzi` (Invoker), `Comanda` (interfață), `ComandaConcreta`, `Executant` (Receiver)

```java
// 1. Interfata Comanda
public interface Comanda {
    void executa();   // ← din diagrama
}

// 2. Executant (Receiver) — cel care face munca
public class Executant {
    public void actiune() { System.out.println("Executant: actiune"); }
}

// 3. ComandaConcreta — ține executantul
public class ComandaConcreta implements Comanda {
    private Executant executant;   // ← din diagrama: -executant:Executant

    public ComandaConcreta(Executant executant) {
        this.executant = executant;
    }

    @Override
    public void executa() {
        executant.actiune();   // ← LINIA GALBENĂ
    }
}

// 4. ManagerComenzi (Invoker)
public class ManagerComenzi {
    private List<Comanda> comenzi = new ArrayList<>();

    public void adaugaComanda(Comanda c) { comenzi.add(c); }

    public void executeazaToate() {
        for (Comanda c : comenzi) c.executa();
        comenzi.clear();
    }
}

// Main
Executant executant = new Executant();
ManagerComenzi manager = new ManagerComenzi();
manager.adaugaComanda(new ComandaConcreta(executant));
manager.executeazaToate();
```

---

### STRATEGY
**Linia cheie (galben în PDF):**
```java
public void request() {
    strategie.algoritm();   // ← LINIA GALBENĂ
}
```
**Clase din diagrama cursului:** `Obiect` (Context), `Strategy` (interfață), `StrategieA`, `StrategieB`

```java
// 1. Interfata Strategy
public interface Strategy {
    void algoritm();   // ← din diagrama
}

// 2. Strategii concrete
public class StrategieA implements Strategy {
    @Override
    public void algoritm() { System.out.println("Algoritmul A"); }
}

public class StrategieB implements Strategy {
    @Override
    public void algoritm() { System.out.println("Algoritmul B"); }
}

// 3. Obiect (Context)
public class Obiect {
    private Strategy strategie;   // ← din diagrama: -strategie:Strategy

    public void setStrategie(Strategy strategie) {
        this.strategie = strategie;
    }

    public void request() {
        strategie.algoritm();   // ← LINIA GALBENĂ
    }
}

// Main
Obiect context = new Obiect();
context.setStrategie(new StrategieA());
context.request();
context.setStrategie(new StrategieB());
context.request();
```

---

### STATE
**Linia cheie (galben în PDF):**
```java
public void request() {
    stare.actiune();   // ← LINIA GALBENĂ
}
```
**Clase din diagrama cursului:** `Context`, `State` (interfață), `StareConcretaA`, `StareConcretaB`

```java
// 1. Interfata State
public interface State {
    void actiune();   // ← din diagrama
}

// 2. Stari concrete — pot face tranzitii prin context.setStare(...)
public class StareConcretaA implements State {
    @Override
    public void actiune() {
        System.out.println("Actiune in starea A");
        // context.setStare(new StareConcretaB(context));  // tranzitie
    }
}

public class StareConcretaB implements State {
    @Override
    public void actiune() { System.out.println("Actiune in starea B"); }
}

// 3. Context — delegă la starea curentă
public class Context {
    private State stare;   // ← din diagrama: -stare:State

    public Context() { this.stare = new StareConcretaA(); }

    public void setStare(State stare) { this.stare = stare; }

    public void request() {
        stare.actiune();   // ← LINIA GALBENĂ
    }
}

// Main
Context ctx = new Context();
ctx.request();                       // StareConcretaA
ctx.setStare(new StareConcretaB());
ctx.request();                       // StareConcretaB
```

---

### OBSERVER
**Clase din diagrama cursului:** `Observabil`, `ObservabilConcret`, `Observer` (interfață), `ObserverA`, `ObserverB`

```java
// 1. Interfata Observer
public interface Observer {
    void notificare();   // ← din diagrama
}

// 2. Observabil (Subject abstract) — sau direct clasa concreta
public class ObservabilConcret {
    private List<Observer> colectieObservatori = new ArrayList<>();   // ← din diagrama
    private String stare;

    public void abonareObservator(Observer o) { colectieObservatori.add(o); }
    public void dezabonareObservator(Observer o) { colectieObservatori.remove(o); }

    public void notificareObservatori() {   // ← din diagrama
        for (Observer o : colectieObservatori)
            o.notificare();
    }

    public void modificareStare(String stareNoua) {   // ← din diagrama
        this.stare = stareNoua;
        generareEveniment();
    }

    public void generareEveniment() {   // ← din diagrama
        System.out.println("Eveniment: stare noua = " + stare);
        notificareObservatori();
    }

    public String getStare() { return stare; }
}

// 3. Observatori concreți
public class ObserverA implements Observer {
    private ObservabilConcret subiect;

    public ObserverA(ObservabilConcret subiect) { this.subiect = subiect; }

    @Override
    public void notificare() {
        System.out.println("ObserverA notificat, stare: " + subiect.getStare());
    }
}

// Main
ObservabilConcret subiect = new ObservabilConcret();
subiect.abonareObservator(new ObserverA(subiect));
subiect.modificareStare("activ");
```

---

### MEMENTO
**Clase din diagrama cursului:** `ManagerStari` (CareTaker), `Memento`, `Originator`

```java
// 1. Memento — fotografia starii
public class Memento {
    private String stare;   // ← din diagrama: -stare:Stare

    public Memento(String stare) { this.stare = stare; }
    public String getStare() { return stare; }   // ← +getStare():Stare
    public void setStare(String stare) { this.stare = stare; }   // ← +setStare()
}

// 2. Originator — creează și restaurează Memento
public class Originator {
    private String stare;   // ← din diagrama: -stare:Stare

    public void setStare(String stare) { this.stare = stare; }
    public String getStare() { return stare; }

    public Memento creareMemento() {   // ← din diagrama: +creareMemento():Memento
        return new Memento(stare);
    }

    public void setMemento(Memento m) {   // ← din diagrama: +setMemento
        this.stare = m.getStare();
        System.out.println("Restaurat: " + stare);
    }
}

// 3. ManagerStari (CareTaker) — ține lista de Memento-uri
public class ManagerStari {
    private List<Memento> istoricMemento = new ArrayList<>();   // ← din diagrama: -memento:Memento

    public void adaugaMemento(Memento m) { istoricMemento.add(m); }   // ← din diagrama

    public Memento getMemento(int index) { return istoricMemento.get(index); }   // ← din diagrama
}

// Main
Originator originator = new Originator();
ManagerStari manager = new ManagerStari();

originator.setStare("stare1");
manager.adaugaMemento(originator.creareMemento());   // salvare

originator.setStare("stare2");
manager.adaugaMemento(originator.creareMemento());

originator.setStare("stare3");

// undo
originator.setMemento(manager.getMemento(0));   // revine la stare1
```

---

### TEMPLATE METHOD
**Linia cheie (galben în PDF):**
```java
public final void testeaza() {
    definesteUnitateTestare();
    definesteDateIntrare();
    definesteRezultate();
    ruleazaUnitatea();
    afisareRezultatTest();
}
```
**Clase din diagrama cursului:** `TemplateTESTare` (abstract), `TestareJUnit`, `TestareNUnit`

```java
// 1. Clasa abstracta cu template method
public abstract class TemplateTESTare {
    // TEMPLATE METHOD — final, nu se suprascrie
    public final void testeaza() {   // ← LINIA GALBENĂ
        definesteUnitateTestare();
        definesteDateIntrare();
        definesteRezultate();
        ruleazaUnitatea();
        afisareRezultatTest();
    }

    // pasi abstracți — subclasele îi implementează
    protected abstract void definesteUnitateTestare();
    protected abstract void definesteDateIntrare();
    protected abstract void definesteRezultate();
    protected abstract void ruleazaUnitatea();
    protected abstract void afisareRezultatTest();
}

// 2. Subclase concrete — implementează DOAR pașii variabili
public class TestareJUnit extends TemplateTESTare {
    @Override
    protected void definesteUnitateTestare() { System.out.println("JUnit: unitate"); }
    @Override
    protected void definesteDateIntrare() { System.out.println("JUnit: date"); }
    @Override
    protected void definesteRezultate() { System.out.println("JUnit: rezultate"); }
    @Override
    protected void ruleazaUnitatea() { System.out.println("JUnit: ruleaza"); }
    @Override
    protected void afisareRezultatTest() { System.out.println("JUnit: afisare"); }
}

// Main
TemplateTESTare test = new TestareJUnit();
test.testeaza();   // apelezi template method-ul
```

---

## REZUMAT — LINIA CHEIE DIN FIECARE PATTERN

| Pattern | Linia cheie (galben în PDF) |
|---------|---------------------------|
| **Decorator** | `produsDecorat.operatie();` |
| **Strategy** | `strategie.algoritm();` |
| **State** | `stare.actiune();` |
| **Command** | `executant.actiune();` |
| **Proxy** | `entitate.operatie();` |
| **Adapter** | `referinta.metoda();` |
| **Observer** | `o.notificare();` (în buclă) |
| **Template** | `final void testeaza(){ pas1(); pas2(); ... }` |
| **Chain** | `succesor.gestioneazaCererea(cerere);` |
| **Composite** | `for(c : copii) c.metodaSpecifica();` |
| **Memento** | `originator.creareMemento()` / `originator.setMemento(m)` |

---

## CUM FOLOSEȘTI DIAGRAMELE LA TEST

1. **DiagrameDesignPatterns.pdf** → uită-te la diagrama pattern-ului cerut → identifică clasele și relațiile
2. **Foaia asta** → scrie codul cu denumirile din diagrama cursului (nu din cartea GoF)
3. **designpatternscard.pdf** → dacă nu ești sigur ce tip e un pattern (Structural/Behavioral)

> Denumiri din cursul tău (diferite de GoF):
> - `NodFrunza` = Leaf, `ComponentaAbstracta` = Component
> - `ManagerComenzi` = Invoker, `Executant` = Receiver
> - `Observabil` = Subject, `notificare()` = update()
> - `ManagerStari` = CareTaker, `creareMemento()` = save()
> - `succesor` = next handler, `gestioneazaCererea()` = handleRequest()
