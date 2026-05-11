# Observer

Pattern **comportamental** — relație one-to-many: un subiect notifică automat toți observatorii înregistrați când starea sa se schimbă.

---

## Participanți (din seminar)

| Rol | Clasă |
|-----|-------|
| Interfață observator | `IObserver` |
| Interfață subiect | `IServiciuMeteo` |
| Subiect concret | `ServiciuMeteo` — ține `List<IObserver>`, notifică la `setTemperatura()` |
| Observator concret | `Client` |
| Client | `Main` |

---

## Explicație pas cu pas

**Ideea în o propoziție:** subiectul (ServiciuMeteo) ține o listă de observatori (clienți abonați) și îi notifică automat pe toți când starea se schimbă (temperatura).

**Rețeta:**
1. Interfața observatorului (`IObserver`) cu metoda de notificare
2. Interfața subiectului (`IServiciuMeteo`) cu metodele de abonare + schimbare stare
3. Subiectul concret (`ServiciuMeteo`) — `List<IObserver>`, notifică în `setTemperatura()`
4. Observatori concreti (`Client`) — implementează `IObserver`
5. Main — creează subiectul, adaugă observatori, schimbă starea

**Pasul 1 — Interfața observatorului**

Definești metoda pe care subiectul o apelează la notificare.

```java
public interface IObserver {
    void mesaj(float temperatura);
}
```

**Pasul 2 — Interfața subiectului**

Metodele de gestionare a abonamentelor + metoda de schimbare stare.

```java
public interface IServiciuMeteo {
    void adaugaObserver(IObserver observer);
    void elimibaObserver(IObserver observer);
    void notivicareObservers(float temperatura);
    void setTemperatura(float temperatura);
}
```

**Pasul 3 — Subiectul concret**

Ține `List<IObserver> observers`. La `setTemperatura()` verifică dacă s-a schimbat și apelează `notivicareObservers()` care iterează lista și apelează `mesaj()` pe fiecare.

```java
public class ServiciuMeteo implements IServiciuMeteo {
    private List<IObserver> observers = new ArrayList<>();
    private float temperatura;

    public ServiciuMeteo(float temperatura) { this.temperatura = temperatura; }

    @Override
    public void setTemperatura(float temperatura) {
        if (temperatura != this.temperatura)
            this.temperatura = temperatura;
        notivicareObservers(temperatura);  // trigger → notifică toți
    }

    @Override
    public void adaugaObserver(IObserver observer) { observers.add(observer); }

    @Override
    public void elimibaObserver(IObserver observer) { observers.remove(observer); }

    @Override
    public void notivicareObservers(float temperatura) {
        for (IObserver observer : observers) {
            observer.mesaj(temperatura);
        }
    }
}
```

**Pasul 4 — Observatorul concret**

Implementează `IObserver`. Primește notificarea și reacționează.

```java
public class Client implements IObserver {
    @Override
    public void mesaj(float temperatura) {
        System.out.println("Clientul a fost anuntat. Temperatura noua: " + temperatura);
    }
}
```

**Pasul 5 — Main**

Creezi subiectul, adaugi observatori cu `adaugaObserver()`, schimbi starea — toți observatorii primesc notificarea automat.

```java
IObserver obs1 = new Client();
IObserver obs2 = new Client();
IObserver obs3 = new Client();

IServiciuMeteo serviciu = new ServiciuMeteo(10);
serviciu.adaugaObserver(obs1);
serviciu.adaugaObserver(obs2);
serviciu.adaugaObserver(obs3);

serviciu.setTemperatura(30);  // notifică obs1, obs2, obs3

serviciu.elimibaObserver(obs3);
serviciu.setTemperatura(25);  // notifică obs1, obs2
```

**Ce să ții minte:** subiectul ține `List<IObserver>`; `adaugaObserver/elimibaObserver` gestionează lista; `notivicareObservers` iterează și apelează metoda de notificare pe fiecare; schimbarea stării (setter) declanșează notificarea.

---

## Cod seminar

```java
public interface IObserver {
    void mesaj(float temperatura);
}

public interface IServiciuMeteo {
    void adaugaObserver(IObserver observer);
    void elimibaObserver(IObserver observer);
    void notivicareObservers(float temperatura);
    void setTemperatura(float temperatura);
}

public class ServiciuMeteo implements IServiciuMeteo {
    private List<IObserver> observers = new ArrayList<>();
    private float temperatura;

    public ServiciuMeteo(float temperatura) { this.temperatura = temperatura; }

    @Override
    public void setTemperatura(float temperatura) {
        if (temperatura != this.temperatura)
            this.temperatura = temperatura;
        notivicareObservers(temperatura);  // trigger → notifică toți
    }

    @Override
    public void adaugaObserver(IObserver observer) { observers.add(observer); }

    @Override
    public void elimibaObserver(IObserver observer) { observers.remove(observer); }

    @Override
    public void notivicareObservers(float temperatura) {
        for (IObserver observer : observers) {
            observer.mesaj(temperatura);
        }
    }
}

public class Client implements IObserver {
    @Override
    public void mesaj(float temperatura) {
        System.out.println("Clientul a fost anuntat. Temperatura noua: " + temperatura);
    }
}

// Main
IObserver obs1 = new Client();
IObserver obs2 = new Client();
IObserver obs3 = new Client();

IServiciuMeteo serviciu = new ServiciuMeteo(10);
serviciu.adaugaObserver(obs1);
serviciu.adaugaObserver(obs2);
serviciu.adaugaObserver(obs3);

serviciu.setTemperatura(30);  // notifică obs1, obs2, obs3

serviciu.elimibaObserver(obs3);
serviciu.setTemperatura(25);  // notifică obs1, obs2
```

---

## Structura la examen

1. **Interfață observator** `IObserver` cu metoda de notificare (ex. `mesaj`, `update`, `notificare`)
2. **Interfață subiect** `IServiciuMeteo` cu `adaugaObserver`, `elimibaObserver`, `notivicareObservers`, metoda de schimbare stare
3. **Subiect concret** `ServiciuMeteo` — `List<IObserver> observers`, `for` în `notivicareObservers`
4. **Observatori concreti** (`Client`) — implementează `IObserver`
5. **Main** — creează subiectul, adaugă observatori, schimbă starea

---

## Cum recunoști

- „notificări la reduceri / schimbări de preț / temperatură"
- „abonare / dezabonare"
- „clienții pot primi prin email și/sau telefon notificări"
