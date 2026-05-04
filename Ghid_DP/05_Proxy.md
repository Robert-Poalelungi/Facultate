# Proxy — Ghid complet

## Ce este?

Un pattern **structural** care pune un **intermediar** (proxy) în fața obiectului real.
Proxy-ul are aceeași interfață ca obiectul real — clientul nu știe că lucrează cu un proxy.

Proxy-ul poate adăuga: control acces, lazy loading, logging, caching.

---

## Când se folosește?

- **Protection Proxy**: verifică permisiuni înainte de acces
- **Virtual Proxy**: creează obiectul real abia când e nevoie (lazy loading)
- **Logging/Audit Proxy**: înregistrează fiecare apel
- **Cache Proxy**: reutilizează rezultate

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **Subject** (interfață) | interfața comună pentru Real și Proxy |
| **RealSubject** | obiectul real care face munca |
| **Proxy** | intermediarul cu aceeași interfață, adaugă comportament |
| **Client** | lucrează cu Subject — nu știe dacă e Real sau Proxy |

---

## Structura

```
Client → «interface» ISubject
              ↑              ↑
         RealSubject       Proxy ──→ RealSubject
         (face munca)    (intermediar)
```

---

## Implementare pas cu pas

### Pasul 1 — Interfața comună

Atât obiectul real cât și proxy-ul implementează aceeași interfață.

```java
public interface IDocument {
    void afiseaza();
    String getContinut();
}
```

---

### Pasul 2 — Obiectul real

Clasa care face munca efectivă (poate fi costisitor de creat/accesat).

```java
public class Document implements IDocument {
    private String numeFisier;
    private String continut;

    public Document(String numeFisier) {
        this.numeFisier = numeFisier;
        // simulare: citire costisitoare din disc
        System.out.println("Citire fișier din disc: " + numeFisier);
        this.continut = "Conținut din " + numeFisier;
    }

    @Override
    public void afiseaza() {
        System.out.println("Afișez documentul: " + numeFisier);
        System.out.println(continut);
    }

    @Override
    public String getContinut() {
        return continut;
    }
}
```

---

### Pasul 3A — Protection Proxy (control acces)

Verifică permisiunile înainte să delege la obiectul real.

```java
public class ProxyDocumentProtectie implements IDocument {
    private Document documentReal;   // obiectul real
    private String numeFisier;
    private String utilizator;

    public ProxyDocumentProtectie(String numeFisier, String utilizator) {
        this.numeFisier = numeFisier;
        this.utilizator = utilizator;
        // NU creăm documentReal încă — lazy
    }

    private boolean arePermisiune() {
        // logică simplificată: doar "admin" are acces
        return "admin".equals(utilizator);
    }

    @Override
    public void afiseaza() {
        if (!arePermisiune()) {
            System.out.println("Acces refuzat pentru utilizatorul: " + utilizator);
            return;
        }
        // creăm obiectul real abia acum (lazy loading combinat)
        if (documentReal == null)
            documentReal = new Document(numeFisier);
        documentReal.afiseaza();
    }

    @Override
    public String getContinut() {
        if (!arePermisiune()) {
            System.out.println("Acces refuzat pentru: " + utilizator);
            return null;
        }
        if (documentReal == null)
            documentReal = new Document(numeFisier);
        return documentReal.getContinut();
    }
}
```

---

### Pasul 3B — Virtual Proxy (lazy loading)

Creează obiectul real abia la primul acces.

```java
public class ProxyDocumentLazy implements IDocument {
    private Document documentReal;   // null până la primul acces
    private String numeFisier;

    public ProxyDocumentLazy(String numeFisier) {
        this.numeFisier = numeFisier;
        // NU citim fișierul în constructor
        System.out.println("Proxy creat pentru: " + numeFisier + " (fără citire)");
    }

    @Override
    public void afiseaza() {
        if (documentReal == null) {
            System.out.println("Primul acces — se încarcă documentul...");
            documentReal = new Document(numeFisier);   // creat lazy
        }
        documentReal.afiseaza();
    }

    @Override
    public String getContinut() {
        if (documentReal == null)
            documentReal = new Document(numeFisier);
        return documentReal.getContinut();
    }
}
```

---

### Pasul 3C — Logging Proxy

Înregistrează fiecare operație.

```java
public class ProxyDocumentLogging implements IDocument {
    private Document documentReal;

    public ProxyDocumentLogging(String numeFisier) {
        this.documentReal = new Document(numeFisier);
    }

    @Override
    public void afiseaza() {
        System.out.println("[LOG] Apel afiseaza() la " + java.time.LocalTime.now());
        documentReal.afiseaza();
        System.out.println("[LOG] afiseaza() terminat");
    }

    @Override
    public String getContinut() {
        System.out.println("[LOG] Apel getContinut()");
        return documentReal.getContinut();
    }
}
```

---

### Pasul 4 — Client

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Protection Proxy ===");
        IDocument docAdmin = new ProxyDocumentProtectie("secret.pdf", "admin");
        IDocument docUser = new ProxyDocumentProtectie("secret.pdf", "user");

        docAdmin.afiseaza();   // → funcționează
        System.out.println();
        docUser.afiseaza();    // → acces refuzat

        System.out.println("\n=== Virtual Proxy (Lazy) ===");
        IDocument docLazy = new ProxyDocumentLazy("mare.pdf");
        System.out.println("Proxy creat, fișierul nu e citit încă");
        docLazy.afiseaza();    // abia acum se citește
        docLazy.afiseaza();    // a doua oară nu mai citește
    }
}
```

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „control acces", „verificare permisiuni"
- „încărcare lazy", „nu se creează până nu e nevoie"
- „logging", „audit"
- „intermediar", „înlocuitor"

**Structura răspunsului la examen:**
1. Interfață comună `ISubject` cu metodele
2. Clasa reală `RealSubject implements ISubject` — face munca
3. Clasa `Proxy implements ISubject` — ține `private RealSubject real`, adaugă logică înainte/după
4. `Main` creează Proxy (nu Real) și lucrează cu interfața

> Proxy seamănă cu Decorator, dar scopul e diferit:
> - **Decorator** adaugă funcționalitate (preț + topping)
> - **Proxy** controlează accesul la obiect (permisiuni, lazy loading)
