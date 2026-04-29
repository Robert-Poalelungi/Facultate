# 02 — Delegates, Acțiuni, Events (Seminar 3)

**Sursa:** `Seminar3/` din github.com/lucianvilcea26/PAW
**Concepte:** delegate, `Action`/`Func`, events, `EventHandler<T>`, `EventArgs` custom.

---

## Concept central

**Delegate = pointer la o funcție.** Stochezi o funcție într-o variabilă, o pasezi ca parametru, o apelezi.

**Event = wrapper peste delegate** care permite notificări (pattern observer):
- Cineva *subscribe-uie* la event (`+=`)
- Când se întâmplă ceva, **emiți** event-ul (`Invoke`) și toți subscriber-ii sunt apelați.

---

## 1. Delegate-uri predefinite — `Action` și `Func`

```csharp
// Action<T> — functie care primeste T si returneaza void
Action<string> tipareste = msg => Console.WriteLine(msg);
tipareste("Salut");

// Action cu mai multi parametri
Action<string, int> log = (mesaj, nivel) => Console.WriteLine($"[{nivel}] {mesaj}");
log("Eroare", 1);

// Func<T1, T2, ..., TResult> — functie care returneaza ceva
Func<int, int, int> suma = (a, b) => a + b;
int rez = suma(2, 3);    // 5

// Func cu un parametru
Func<int, bool> esteParea = n => n % 2 == 0;
```

---

## 2. Delegate custom (alternativ la Action/Func)

```csharp
// Definire (la nivel de namespace)
public delegate void NotificareClient(string numarComanda, string mesaj);

// Folosire
NotificareClient notificator = NotificareService.NotificaPrinSms;
notificator("CMD-001", "Comanda inregistrata");
//          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ apel ca o functie normala
```

În S3, `NotificareClient` e folosit ca parametru opțional:
```csharp
public void InregistreazaComanda(Comanda comanda, NotificareClient notificator = null)
{
    _comenzi.Add(comanda);
    notificator?.Invoke(comanda.NumarComanda, "Comanda inregistrata");
    //         ^^^^^^^^ null-conditional invoke (nu crapa daca e null)
}
```

**`?.Invoke(...)`** = apelează doar dacă delegate-ul nu e null. Echivalent cu `if (notificator != null) notificator(...)`.

---

## 3. Events

```csharp
public class Depozit
{
    // 1. Declarare event
    public event EventHandler<ComandaSchimbatStareEventArgs> ComandaSchimbatStare;
    public event EventHandler<ComandaLivrataEventArgs> ComandaLivrata;

    // 2. Metoda care emite event-ul (convenție: nume cu prefix "On")
    protected virtual void OnComandaSchimbatStare(ComandaSchimbatStareEventArgs e)
    {
        ComandaSchimbatStare?.Invoke(this, e);    // notifica toti subscriberii
    }

    public void AvanseazaComanda(string numar)
    {
        // ... logica ...
        var e = new ComandaSchimbatStareEventArgs() { Comanda = c, StareVeche = ..., StareNoua = ... };
        OnComandaSchimbatStare(e);    // emit event
    }
}
```

### Pas cu pas

**Bloc 1 — declarare:**
```csharp
public event EventHandler<TArgs> NumeEvent;
```
- `event` = keyword.
- `EventHandler<T>` = tip predefinit pentru events. Are signatura `(object sender, T eventArgs)`.
- `<TArgs>` = tipul argumentelor specifice event-ului.

**Bloc 2 — invoke:**
```csharp
ComandaSchimbatStare?.Invoke(this, e);
```
- `this` = sursa event-ului (cine a emis).
- `e` = datele event-ului.
- `?.Invoke` = invocă doar dacă există subscriber-i.

**Bloc 3 — protected virtual `On...` (convenție):**
```csharp
protected virtual void OnComandaSchimbatStare(...) { ... }
```
- `protected` — sub-clasele pot suprascrie.
- `virtual` — pot face `override`.
- Convenție: clasele moștenitoare pot adăuga logică custom înainte/după emisie.

---

## 4. Custom EventArgs

```csharp
public class ComandaSchimbatStareEventArgs : EventArgs
{
    public Comanda Comanda { get; set; }
    public StareComanda StareVeche { get; set; }
    public StareComanda StareNoua { get; set; }
}

public class ComandaLivrataEventArgs : EventArgs
{
    public Comanda Comanda { get; set; }
    public DateTime DataLivrare { get; set; }
}
```

**Reguli:**
- Moștenește `EventArgs` (clasa de bază pentru toate event args).
- Auto-properties pentru fiecare câmp relevant.
- Numele se termină cu `EventArgs` (convenție).

---

## 5. Subscribe / Unsubscribe la events

```csharp
var depozit = new Depozit("D1");

// Subscribe
depozit.ComandaSchimbatStare += (s, e) =>
{
    Console.WriteLine($"Comanda {e.Comanda.NumarComanda}: {e.StareVeche} -> {e.StareNoua}");
};

depozit.ComandaLivrata += (s, e) =>
{
    Console.WriteLine($"Comanda {e.Comanda.NumarComanda} livrata la {e.DataLivrare}");
};

// Subscribe cu metoda numita
depozit.ComandaLivrata += DepozitOnComandaLivrata;

// Unsubscribe
depozit.ComandaLivrata -= DepozitOnComandaLivrata;

// Definire metoda
private void DepozitOnComandaLivrata(object sender, ComandaLivrataEventArgs e)
{
    Console.WriteLine($"Livrare: {e.Comanda.NumarComanda}");
}
```

**Reguli:**
- `+=` adaugă un handler.
- `-=` îl scoate.
- Mai multe handlers pot fi adăugate la acelaşi event (toate sunt apelate la emisie).

---

## 6. WinForms events — pattern obișnuit

În WinForms (Seminar 4+), event-urile sunt deja peste tot:

```csharp
private void btnSalveaza_Click(object sender, EventArgs e)
{
    // codul tău
}

// Subscribe se face în Designer (Properties → Events tab)
// Sau manual în InitializeComponent:
// this.btnSalveaza.Click += new EventHandler(btnSalveaza_Click);
```

**Toate au signatura `(object sender, EventArgs e)`** — primul parametru e cel ce a emis (butonul), al doilea sunt detalii (poate fi `EventArgs.Empty` pentru click simplu).

---

## Cheatsheet

```csharp
// 1. Action — fara return
Action<string> a = s => Console.WriteLine(s);

// 2. Func — cu return
Func<int, int> f = n => n * 2;

// 3. Event declarare
public event EventHandler<MyArgs> NumeEvent;

// 4. Event emisie
NumeEvent?.Invoke(this, new MyArgs() { ... });

// 5. Event subscribe
obj.NumeEvent += (s, e) => { /* handler */ };

// 6. Custom EventArgs
public class MyArgs : EventArgs { public int Camp { get; set; } }

// 7. Null-conditional invoke
delegate?.Invoke(args);    // sigur (nu crapa daca e null)
```

---

## Capcane

| Capcană | Antidot |
|---------|---------|
| Invoke fara `?.` și delegate e null | `NullReferenceException`. Mereu `delegate?.Invoke(...)`. |
| Subscribe în loop fără unsubscribe | Memory leak. Unsubscribe înainte de a recrea obiectul. |
| Modifici delegate-ul direct (=) în loc de `+=` | Înlocuiești toți subscriber-ii anteriori. Folosește `+=`. |
| `EventArgs` în loc de tip generic `EventArgs<T>` | `EventArgs` n-are date. `EventHandler<MyArgs>` ai nevoie pentru parametri custom. |

---

## Maparea cu testul

Pentru subiectul 2025 nu e nevoie de events custom — testul e simplu (CRUD pe facturi). Dar dacă subiectul tău cere notificări (ex. „afișează un mesaj când o factură expiră"), patternul de aici e exact cel pe care îl folosești.
