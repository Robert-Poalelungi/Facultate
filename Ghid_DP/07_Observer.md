# Observer — Ghid complet

## Ce este?

Un pattern **comportamental** care definește o dependență **one-to-many**: când un obiect
(Subject/Publisher) își schimbă starea, toți dependenții (Observers/Subscribers) sunt notificați automat.

---

## Când se folosește?

- Eveniment care trebuie propagat la mai mulți interesați
- Sistem de notificări / subscripții
- Interfață grafică: model schimbă → view se actualizează
- Exemple: stoc produs, notificări email/SMS, feed social media

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **IObserver** | interfața observatorilor — metoda de notificare |
| **ISubiect** | interfața subiectului — add/remove/notify |
| **Subject concret** | ține lista de observatori, notifică la schimbare |
| **Observer concret** | reacționează la notificare |

---

## Structura

```
ISubiect                    IObserver
+ addObserver()    ←──── (lista de)  + getMesaj()
+ removeObserver()                        ↑
+ notifyAll()               Client     Observer1
      ↑                                Observer2
  Restaurant
  (Subject concret)
```

---

## Implementare pas cu pas

### Pasul 1 — Interfața Observer

O singură metodă — va fi apelată când subiectul se schimbă.

```java
public interface IObserver {
    void getMesaj(String mesaj);
}
```

---

### Pasul 2 — Interfața Subject

```java
public interface ISubiect {
    void addObserver(IObserver observer);
    void removeObserver(IObserver observer);
    void notifyObservers(String mesaj);
}
```

---

### Pasul 3 — Subject concret

Ține lista de observatori și îi notifică la fiecare schimbare relevantă.

```java
import java.util.ArrayList;
import java.util.List;

public class Restaurant implements ISubiect {
    private String numeRestaurant;
    private List<IObserver> listaObservatori = new ArrayList<>();

    public Restaurant(String numeRestaurant) {
        this.numeRestaurant = numeRestaurant;
    }

    @Override
    public void addObserver(IObserver observer) {
        listaObservatori.add(observer);
    }

    @Override
    public void removeObserver(IObserver observer) {
        listaObservatori.remove(observer);
    }

    // notifică TOȚI observatorii înregistrați
    @Override
    public void notifyObservers(String mesaj) {
        for (IObserver observer : listaObservatori)
            observer.getMesaj(mesaj);
    }

    // metodă de business care declanșează notificarea
    public void adaugaMeniu(String numeMeniu) {
        System.out.println("[Restaurant] Meniu nou adăugat: " + numeMeniu);
        notifyObservers("Meniu nou disponibil la " + numeRestaurant + ": " + numeMeniu);
    }

    public void schimbaOrar(String orarNou) {
        System.out.println("[Restaurant] Orar actualizat: " + orarNou);
        notifyObservers("Noul orar pentru " + numeRestaurant + ": " + orarNou);
    }
}
```

---

### Pasul 4 — Observatori concreți

Fiecare reacționează diferit la aceeași notificare.

```java
public class Client implements IObserver {
    private String nume;

    public Client(String nume) {
        this.nume = nume;
    }

    @Override
    public void getMesaj(String mesaj) {
        System.out.println("Client [" + nume + "] a primit: " + mesaj);
    }
}

public class ServiciuEmail implements IObserver {
    private String emailAdmin;

    public ServiciuEmail(String emailAdmin) {
        this.emailAdmin = emailAdmin;
    }

    @Override
    public void getMesaj(String mesaj) {
        System.out.println("Email trimis la [" + emailAdmin + "]: " + mesaj);
    }
}

public class ServiciuSMS implements IObserver {
    private String nrTelefon;

    public ServiciuSMS(String nrTelefon) {
        this.nrTelefon = nrTelefon;
    }

    @Override
    public void getMesaj(String mesaj) {
        System.out.println("SMS trimis la [" + nrTelefon + "]: " + mesaj);
    }
}
```

---

### Pasul 5 — Main

```java
public class Main {
    public static void main(String[] args) {
        // subiectul
        Restaurant restaurant = new Restaurant("La Mama");

        // observatori
        Client client1 = new Client("Ion");
        Client client2 = new Client("Maria");
        ServiciuEmail email = new ServiciuEmail("admin@lamama.ro");
        ServiciuSMS sms = new ServiciuSMS("+40700000000");

        // subscripții
        restaurant.addObserver(client1);
        restaurant.addObserver(client2);
        restaurant.addObserver(email);
        restaurant.addObserver(sms);

        // eveniment → toți sunt notificați
        restaurant.adaugaMeniu("Meniu Paste");
        System.out.println();

        // Ion se dezabonează
        restaurant.removeObserver(client1);

        // al doilea eveniment — Ion nu mai primește
        restaurant.schimbaOrar("Lu-Vi: 10:00-22:00");
    }
}
```

**Output:**
```
[Restaurant] Meniu nou adăugat: Meniu Paste
Client [Ion] a primit: Meniu nou disponibil la La Mama: Meniu Paste
Client [Maria] a primit: Meniu nou disponibil la La Mama: Meniu Paste
Email trimis la [admin@lamama.ro]: Meniu nou disponibil la La Mama: Meniu Paste
SMS trimis la [+40700000000]: Meniu nou disponibil la La Mama: Meniu Paste

[Restaurant] Orar actualizat: Lu-Vi: 10:00-22:00
Client [Maria] a primit: Noul orar pentru La Mama: Lu-Vi: 10:00-22:00
Email trimis la [admin@lamama.ro]: Noul orar pentru La Mama: Lu-Vi: 10:00-22:00
SMS trimis la [+40700000000]: Noul orar pentru La Mama: Lu-Vi: 10:00-22:00
```

---

## Variantă: cu date concrete în notificare (nu doar String)

Poți transmite un obiect cu date în loc de `String`:

```java
public interface IObserverStoc {
    void onSchimbareStoc(String produs, int cantitateNoua);
}

public class MagazinStoc implements ISubiect {
    private List<IObserverStoc> observatori = new ArrayList<>();
    private Map<String, Integer> stoc = new HashMap<>();

    public void adaugaObserver(IObserverStoc o) { observatori.add(o); }

    public void actualizeazaStoc(String produs, int cantitate) {
        stoc.put(produs, cantitate);
        for (IObserverStoc o : observatori)
            o.onSchimbareStoc(produs, cantitate);
    }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „notificare", „abonare", „subscripție"
- „când X se schimbă, Y și Z trebuie să știe"
- „mai mulți clienți interesați de același eveniment"
- „publish-subscribe"

**Structura răspunsului la examen:**
1. Interfața `IObserver` cu `getMesaj()` (sau `update()`)
2. Interfața `ISubiect` cu `addObserver()`, `removeObserver()`, `notifyObservers()`
3. Clasa subiect (`Restaurant`) implementează `ISubiect`, ține `List<IObserver>`, apelează `notifyObservers()` în metodele de business
4. Clase observator (`Client`, `ServiciuEmail`) implementează `IObserver`
5. `Main`: creează subiectul, adaugă observatori, declanșează evenimente
