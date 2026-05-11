# Proxy

Pattern **structural** — un intermediar cu aceeași interfață ca obiectul real. Clientul nu știe că lucrează cu proxy-ul.

---

## Participanți (din seminar)

| Rol | Clasă |
|-----|-------|
| Interfață comună | `ISpital` |
| Obiect real | `Spital` — face munca efectivă |
| Proxy | `ProxySpital` — ține `ISpital spital`, adaugă logică (restricție vizite) |
| Client | `Main` — lucrează doar cu `ISpital` |

---

## Explicație pas cu pas

**Ideea în o propoziție:** vrei să controlezi accesul la un obiect (Spital) fără să-l modifici — pui un intermediar (ProxySpital) care are aceeași interfață și adaugă logică înainte de a delega.

**Rețeta:**
1. Interfața comună (`ISpital`)
2. Clasa reală (`Spital`) — face munca fără logică extra
3. Proxy (`ProxySpital`) — ține referința la real, adaugă logică, delegă
4. Main — creează `new ProxySpital(new Spital(...))`, lucrează cu `ISpital`

**Pasul 1 — Interfața comună**

Definești interfața cu metodele pe care le vrea clientul. Atât obiectul real cât și proxy-ul o implementează.

```java
public interface ISpital {
    void accesSpital(String vizitator, String pacient);
}
```

**Pasul 2 — Clasa reală**

Face munca efectivă, fără niciun control sau logică extra. Simplu și curat.

```java
public class Spital implements ISpital {
    private String denumire;

    @Override
    public void accesSpital(String vizitator, String pacient) {
        System.out.println(vizitator + " a vizitat pe " + pacient);
    }
}
```

**Pasul 3 — Proxy-ul**

Ține `private ISpital spital` (referința la real) și adaugă logica proprie înaintea delegării. Cheia: **întotdeauna delegă** la obiectul real când trece de verificare.

```java
public class ProxySpital implements ISpital {
    private ISpital spital;                   // referința obiectului controlat
    private Map<String, String> vizite;       // key=pacient, value=vizitator

    public ProxySpital(ISpital spital) {
        this.spital = spital;
        this.vizite = new HashMap<>();
    }

    @Override
    public void accesSpital(String vizitator, String pacient) {
        if (vizite.containsKey(pacient)) {
            System.out.println("Nu se poate.");
            System.out.println("A mai fost vizitat de " + vizite.get(pacient));
        } else {
            vizite.put(pacient, vizitator);
            this.spital.accesSpital(vizitator, pacient); // obligatoriu — delegă la real
        }
    }

    public void resetZi() { vizite.clear(); }
}
```

**Pasul 4 — Main**

Clientul primește `ISpital` și nu știe că e proxy. Construcția: `new ProxySpital(new Spital(...))`.

```java
ISpital spital = new ProxySpital(new Spital("Spitalul nr 1"));

spital.accesSpital("Gigel", "Pacient 1");   // OK — prima vizită
spital.accesSpital("Costel", "Pacient 1");  // Refuzat — deja vizitat de Gigel
spital.accesSpital("Gigel", "Pacient 2");   // OK — alt pacient

((ProxySpital) spital).resetZi();
spital.accesSpital("Marcel", "Pacient 1"); // OK după reset
```

**Ce să ții minte:** proxy-ul are aceeași interfață ca obiectul real; ține `private IReal obiect`; adaugă logică ÎNAINTE de delegare; delegarea (`this.spital.metoda(...)`) este obligatorie când trece verificarea.

---

## Cod seminar

```java
public interface ISpital {
    void accesSpital(String vizitator, String pacient);
}

public class Spital implements ISpital {
    private String denumire;

    @Override
    public void accesSpital(String vizitator, String pacient) {
        System.out.println(vizitator + " a vizitat pe " + pacient);
    }
}

public class ProxySpital implements ISpital {
    private ISpital spital;                   // referința obiectului controlat
    private Map<String, String> vizite;       // key=pacient, value=vizitator

    public ProxySpital(ISpital spital) {
        this.spital = spital;
        this.vizite = new HashMap<>();
    }

    @Override
    public void accesSpital(String vizitator, String pacient) {
        if (vizite.containsKey(pacient)) {
            System.out.println("Nu se poate.");
            System.out.println("A mai fost vizitat de " + vizite.get(pacient));
        } else {
            vizite.put(pacient, vizitator);
            this.spital.accesSpital(vizitator, pacient); // obligatoriu — delegă la real
        }
    }

    public void resetZi() { vizite.clear(); }
}

// Main — clientul primește ISpital, nu știe că e Proxy
ISpital spital = new ProxySpital(new Spital("Spitalul nr 1"));

spital.accesSpital("Gigel", "Pacient 1");   // OK
spital.accesSpital("Costel", "Pacient 1");  // Refuzat — deja vizitat de Gigel
spital.accesSpital("Gigel", "Pacient 2");   // OK

((ProxySpital) spital).resetZi();
spital.accesSpital("Marcel", "Pacient 1"); // OK după reset
```

---

## Structura la examen

1. **Interfață** `ISpital` cu metodele obiectului real
2. **Clasa reală** `Spital implements ISpital` — face munca fără logică extra
3. **Proxy** `ProxySpital implements ISpital` — ține `private ISpital spital`, adaugă logica înaintea delegării
4. **Main** — creează `new ProxySpital(new Spital(...))`, lucrează cu `ISpital`

---

## Cum recunoști

- „modul intermediar", „fără modificarea clasei existente"
- „control acces", „restricție", „blocare după N încercări"
- Interfață dată în subiect (`ISpital`, `IAutentificare`, `IMagazin`)
