# Facade — Ghid complet

## Ce este?

Un pattern **structural** care oferă o **interfață simplificată** peste un subsistem complex.

Clientul nu mai interacționează direct cu zeci de clase — apelează o singură clasă Facade
care se ocupă de tot.

---

## Când se folosește?

- Sistem complex cu multe clase interdependente
- Vrei să simplifici utilizarea pentru client
- Vrei să ascunzi implementarea internă
- Exemple: pornire calculator (BIOS, RAM, CPU — ascunse de un buton), comandă la restaurant

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **Facade** | interfața simplificată, orchestrează subsistemul |
| **Subsystem classes** | clasele complexe, nu știu de Facade |
| **Client** | apelează doar Facade |

---

## Structura

```
Client → Facade → SubsistemA
                → SubsistemB
                → SubsistemC
```

Clientul nu știe de A, B, C — Facade le orchestrează.

---

## Implementare pas cu pas

### Pasul 1 — Creează clasele subsistemului

Acestea sunt clasele complexe existente. Facade le va orchestra.

```java
public class VerificareStoc {
    public boolean verificaDisponibilitate(String produs, int cantitate) {
        System.out.println("Verificare stoc pentru: " + produs + " x" + cantitate);
        return true;  // simplificat
    }
}

public class ProcesorPlata {
    public boolean proceseazaPlata(String card, double suma) {
        System.out.println("Procesare plată " + suma + " RON cu cardul " + card);
        return true;  // simplificat
    }
}

public class ServiciuLivrare {
    public String creeazaComandaLivrare(String produs, String adresa) {
        String idComanda = "CMD-" + (int)(Math.random() * 10000);
        System.out.println("Livrare creată: " + idComanda + " → " + adresa);
        return idComanda;
    }
}

public class ServiciuNotificari {
    public void trimiteConfirmare(String email, String idComanda) {
        System.out.println("Email trimis la " + email + " pentru comanda " + idComanda);
    }
}
```

---

### Pasul 2 — Creează Facade

Instanțiază intern subsistemele și expune metode simple.

```java
public class MagazinOnlineFacade {
    // subsistemele — clientul nu le vede
    private VerificareStoc verificareStoc;
    private ProcesorPlata procesorPlata;
    private ServiciuLivrare serviciuLivrare;
    private ServiciuNotificari serviciuNotificari;

    public MagazinOnlineFacade() {
        this.verificareStoc = new VerificareStoc();
        this.procesorPlata = new ProcesorPlata();
        this.serviciuLivrare = new ServiciuLivrare();
        this.serviciuNotificari = new ServiciuNotificari();
    }

    // O singură metodă simplă pentru client — ascunde complexitatea
    public boolean plaseazaComanda(String produs, int cantitate,
                                   String card, double suma,
                                   String adresa, String email) {
        System.out.println("=== Plasare comandă ===");

        // 1. verifică stoc
        if (!verificareStoc.verificaDisponibilitate(produs, cantitate)) {
            System.out.println("Eroare: produs indisponibil");
            return false;
        }

        // 2. procesează plata
        if (!procesorPlata.proceseazaPlata(card, suma)) {
            System.out.println("Eroare: plată refuzată");
            return false;
        }

        // 3. creează livrare
        String idComanda = serviciuLivrare.creeazaComandaLivrare(produs, adresa);

        // 4. trimite notificare
        serviciuNotificari.trimiteConfirmare(email, idComanda);

        System.out.println("Comandă plasată cu succes!");
        return true;
    }
}
```

---

### Pasul 3 — Client simplu

```java
public class Main {
    public static void main(String[] args) {
        // clientul interacționează DOAR cu Facade
        MagazinOnlineFacade magazin = new MagazinOnlineFacade();

        magazin.plaseazaComanda(
            "Laptop Dell",
            1,
            "4111-1111-1111-1111",
            2999.99,
            "Str. Exemplu 1, București",
            "client@email.com"
        );
    }
}
```

**Output:**
```
=== Plasare comandă ===
Verificare stoc pentru: Laptop Dell x1
Procesare plată 2999.99 RON cu cardul 4111-1111-1111-1111
Livrare creată: CMD-7423 → Str. Exemplu 1, București
Email trimis la client@email.com pentru comanda CMD-7423
Comandă plasată cu succes!
```

---

## Exemplu din repo (restaurant)

```java
// Subsisteme
public class Bucatar {
    public void preparaMancare(String preparat) {
        System.out.println("Bucatarul prepară: " + preparat);
    }
}

public class Barman {
    public void preparaBautura(String bautura) {
        System.out.println("Barmanul prepară: " + bautura);
    }
}

public class Casier {
    public double calculeazaTotal(double pretMancare, double pretBautura) {
        return pretMancare + pretBautura;
    }
}

// Facade
public class RestaurantFacade {
    private Bucatar bucatar = new Bucatar();
    private Barman barman = new Barman();
    private Casier casier = new Casier();

    public void serveste(String mancare, String bautura, double pretM, double pretB) {
        bucatar.preparaMancare(mancare);
        barman.preparaBautura(bautura);
        double total = casier.calculeazaTotal(pretM, pretB);
        System.out.printf("Total de plată: %.2f RON%n", total);
    }
}

// Client
public class Main {
    public static void main(String[] args) {
        RestaurantFacade restaurant = new RestaurantFacade();
        restaurant.serveste("Paste", "Suc de portocale", 35.0, 12.0);
    }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „sistem complex cu mai multe subsisteme"
- „simplifică interacțiunea clientului"
- „ascunde detaliile de implementare"
- „punct de intrare unic"

**Structura răspunsului la examen:**
1. Câteva clase simple de subsistem (fiecare face un lucru specific)
2. Clasa `Facade` care le instanțiază intern și expune 1-2 metode simple
3. `Main` care creează Facade și apelează metodele simple

> Facade e simplu — nu are pattern complicat intern. Toată complexitatea e în orchestrare.
