# 01 — OOP în C# (Seminar 2)

**Sursa:** `Seminar2/` din github.com/lucianvilcea26/PAW
**Concepte:** clase, proprietăți, moștenire, interfețe, enumerări, polimorfism, generice.

---

## Concept central

OOP în C# = exact ca Java/C++, cu sintaxă proprie:
- **Clase** definite cu `class`
- **Properties** cu `get`/`set` (zahăr peste getter/setter)
- **Moștenire** cu `:` (un singur părinte) + interfețe multiple
- **Polimorfism** cu `virtual` (părinte) + `override` (copil)
- **Interfețe** cu `interface`, fără implementare
- **Enumerări** cu `enum`

---

## 1. Clasa de bază — `Bilet`

```csharp
public class Bilet : IPretCalculabil, IValidabil
{
    // === Properties auto (fara validare) ===
    public string NumeFilm { get; set; }
    public int NumarSala { get; set; }
    public TipFilm TipFilm { get; set; }
    public DateTime ExpiraLa { get; set; }
    public Client Client { get; set; }

    // === Property cu backing field si validare ===
    private int _numarLoc;
    public int NumarLoc
    {
        get { return _numarLoc; }
        set
        {
            if (value < 1 || value > 200)
                throw new ArgumentException("Numarul locului este invalid");
            _numarLoc = value;
        }
    }

    private double _pretBaza;
    public double PretBaza
    {
        get { return _pretBaza; }
        set
        {
            if (value <= 0)
                throw new ArgumentException("Pretul de baza este invalid");
            _pretBaza = value;
        }
    }

    // === Constructor ===
    public Bilet(string numeFilm, int numarSala, TipFilm tipFilm,
                 DateTime expiraLa, Client client, int numarLoc, double pretBaza)
    {
        NumeFilm = numeFilm;
        NumarSala = numarSala;
        TipFilm = tipFilm;
        ExpiraLa = expiraLa;
        Client = client;
        NumarLoc = numarLoc;       // trece prin setter -> validare
        PretBaza = pretBaza;       // trece prin setter -> validare
    }

    // === Metode virtuale (pot fi override) ===
    public virtual double CalculeazaPretFinal()
    {
        return PretBaza - GetReducere();
    }

    public virtual double GetReducere()
    {
        return 0;
    }

    public virtual bool EsteValid()
    {
        return ExpiraLa > DateTime.Now;
    }

    // === Override din object ===
    public override string ToString()
    {
        return $"[{GetType().Name}] {NumeFilm} | Sala {NumarSala} | Loc {NumarLoc}";
    }
}
```

### Pas cu pas

**Bloc 1 — declarare clasă:**
```csharp
public class Bilet : IPretCalculabil, IValidabil
```
- `public` — vizibilitate (alt assembly poate folosi).
- `Bilet` — numele clasei.
- `:` urmat de **0 sau 1 clasă bază + N interfețe** (aici doar interfețe — clasa moștenește implicit `object`).

**Bloc 2 — auto-properties:**
```csharp
public string NumeFilm { get; set; }
```
Compilator-ul generează automat un câmp privat și getter/setter trivial. **Folosești când nu ai validare.**

**Bloc 3 — property cu backing field:**
```csharp
private int _numarLoc;
public int NumarLoc
{
    get { return _numarLoc; }
    set
    {
        if (value < 1 || value > 200)
            throw new ArgumentException(...);
        _numarLoc = value;
    }
}
```
- `private int _numarLoc;` — câmpul real (convenție: underscore prefix).
- `get { ... }` — ce returnezi când cineva citește `obj.NumarLoc`.
- `set { ... }` — ce se întâmplă când cineva scrie `obj.NumarLoc = 5;`. `value` e valoarea primită.
- **Folosești când vrei validare.**

**Bloc 4 — `virtual`:**
```csharp
public virtual double CalculeazaPretFinal()
```
Marchezi metoda ca **suprascriibilă** de către subclase. Fără `virtual`, o subclasă nu poate face `override`.

---

## 2. Moștenire — `BiletSenior : Bilet`

```csharp
public class BiletSenior : Bilet
{
    private const double _procentReducere = 0.3;

    private int _varstaClient;
    public int VarstaClient
    {
        get { return _varstaClient; }
        set
        {
            if (value < 60)
                throw new ArgumentException("Clientul nu este eligibil pentru bilet senior");
            _varstaClient = value;
        }
    }

    public BiletSenior(string numeFilm, int numarSala, TipFilm tipFilm,
                       DateTime expiraLa, Client client, int numarLoc,
                       double pretBaza, int varstaClient)
        : base(numeFilm, numarSala, tipFilm, expiraLa, client, numarLoc, pretBaza)
    {
        VarstaClient = varstaClient;
    }

    public override double GetReducere()
    {
        return PretBaza * _procentReducere;
    }
}
```

### Pas cu pas

**Bloc 1 — moștenire:**
```csharp
public class BiletSenior : Bilet
```
`BiletSenior` extinde `Bilet`. Are toate properties + metodele lui Bilet, plus ce adaugă el.

**Bloc 2 — constant:**
```csharp
private const double _procentReducere = 0.3;
```
`const` = compile-time, nu se poate schimba. Folosit pentru valori magice cu nume.

**Bloc 3 — apelarea constructorului părinte:**
```csharp
public BiletSenior(...) : base(numeFilm, numarSala, ...)
```
- `: base(...)` — apelează **constructorul clasei părinte**.
- Trebuie să furnizezi argumentele.
- Apoi în `{ }`, faci ce e specific clasei tale.

**Bloc 4 — `override`:**
```csharp
public override double GetReducere()
{
    return PretBaza * _procentReducere;
}
```
- `override` = suprascrii metoda `virtual` din părinte.
- Compilator-ul verifică: dacă părintele NU avea `virtual`, primești eroare.
- Acum, când ai `Bilet b = new BiletSenior(...)`, `b.GetReducere()` apelează versiunea lui Senior (polimorfism dinamic).

---

## 3. Subclase cu comportament diferit — `BiletStudent`, `BiletVip`

```csharp
public class BiletStudent : Bilet
{
    public string NumarLegitimatie { get; set; }
    public string Facultate { get; set; }

    // ... constructor cu :base(...)

    public override double GetReducere()
    {
        return PretBaza * 0.2;     // 20% reducere
    }

    public override bool EsteValid()
    {
        return base.EsteValid() && !string.IsNullOrWhiteSpace(NumarLegitimatie);
        //     ^^^^^^^^^^^^^^^^ apel la versiunea părinte
    }
}

public class BiletVip : Bilet
{
    public bool IncludePopcorn { get; set; }
    public bool IncludeBautura { get; set; }

    // ... constructor

    public override double CalculeazaPretFinal()
    {
        return PretBaza + GetExtras();    // VIP nu are reducere, are extras
    }

    public double GetExtras()
    {
        return (IncludePopcorn ? 15 : 0) + (IncludeBautura ? 10 : 0);
    }
}
```

**Lecții:**
- `base.EsteValid()` — apelezi **explicit** versiunea părinte (utile când vrei să extinzi, nu să înlocuiești).
- Operatorul `?:` ternar: `condiție ? dacă-true : dacă-false`.
- Fiecare subclasă suprascrie ce are nevoie. `BiletVip` suprascrie `CalculeazaPretFinal` în loc de `GetReducere`.

---

## 4. Interfețe

```csharp
public interface IPretCalculabil
{
    double CalculeazaPretFinal();
    double GetReducere();
}

public interface IValidabil
{
    bool EsteValid();
}
```

**Reguli:**
- `interface` = doar SEMNĂTURI (fără cod).
- Numele interfețelor încep cu `I` (convenție).
- O clasă **poate implementa N interfețe** (separate prin virgulă).
- Toate metodele din interfață trebuie implementate (sau clasa devine `abstract`).

**Folosire (polimorfism cu interfețe):**
```csharp
List<IPretCalculabil> bilete = new List<IPretCalculabil> { b1, b2, b3 };
foreach (var b in bilete) {
    Console.WriteLine(b.CalculeazaPretFinal());     // apel pe interfață
}
```

---

## 5. Enumerări

```csharp
public enum TipFilm
{
    Comedie,
    Actiune,
    Drama,
    Istoric
}
```

**Folosire:**
```csharp
TipFilm tip = TipFilm.Actiune;
if (tip == TipFilm.Comedie) { ... }
```

**Conversie cu int:**
```csharp
int v = (int)TipFilm.Actiune;        // 1 (indexat de la 0)
TipFilm t = (TipFilm)2;              // Drama
```

---

## 6. Compoziție — `CasaBilete` conține `List<Bilet>`

```csharp
public class CasaBilete
{
    public List<Bilet> Bilete { get; set; }

    public CasaBilete()
    {
        Bilete = new List<Bilet>();
    }

    public void AdaugaBilet(Bilet bilet)
    {
        Bilete.Add(bilet);
    }

    public double GetIncasariTotale()
    {
        return Bilete.Sum(bilet => bilet.CalculeazaPretFinal());
    }

    public double GetReduceriAcordate()
    {
        return Bilete.Sum(bilet => bilet.GetReducere());
    }
}
```

### LINQ basics (vezi 08_LINQ.md pentru mai mult)

```csharp
// Sumă peste toate biletele
Bilete.Sum(b => b.CalculeazaPretFinal())

// Filtrare
Bilete.Where(b => b.PretBaza > 30)

// Sortare
Bilete.OrderBy(b => b.NumeFilm)
Bilete.OrderByDescending(b => b.PretBaza)

// Primul match
Bilete.FirstOrDefault(b => b.NumarSala == 1)

// Numărare condiționată
Bilete.Count(b => b is BiletVip)
```

---

## 7. Metode generice — `GetNumarBiletePerTip<T>()`

```csharp
public int GetNumarBiletePerTip<T>() where T : Bilet
{
    return Bilete.Count(bilet => bilet.GetType() == typeof(T));
}
```

**Folosire:**
```csharp
casa.GetNumarBiletePerTip<BiletStudent>();  // câți Studenți
casa.GetNumarBiletePerTip<BiletVip>();      // câți VIP
```

**Pas cu pas:**
- `<T>` declară parametrul de tip generic.
- `where T : Bilet` constrânge `T` să fie `Bilet` sau derivat (compilare type-safe).
- `typeof(T)` întoarce tipul exact (vs `obj.GetType()` care întoarce tipul instanței).

**Diferenta `OfType<T>()` vs `GetType() == typeof(T)`:**
```csharp
Bilete.OfType<Bilet>().Count();              // numără ȘI subclase (BiletSenior etc)
Bilete.Count(b => b.GetType() == typeof(Bilet));  // numără DOAR Bilet exact
```

---

## 8. Verificare tip cu `is`

```csharp
if (b is BiletStudent bs)
    Console.WriteLine($"STUDENT: {bs.Facultate}");
else if (b is BiletSenior s)
    Console.WriteLine($"SENIOR: {s.VarstaClient} ani");
else if (b is BiletVip v)
    Console.WriteLine($"VIP: {v.GetExtras()} RON extras");
```

`if (obj is Type variabila)` — testează tipul ȘI face cast în aceeași expresie. Mai elegant decât:
```csharp
if (b is BiletStudent) {
    BiletStudent bs = (BiletStudent)b;       // cast manual
    ...
}
```

---

## Patternuri de memorat

```csharp
// 1. Auto-property
public string Nume { get; set; }

// 2. Property cu validare
private int _x;
public int X { get { return _x; } set { /* validare */ _x = value; } }

// 3. Property auto-calculată (read-only)
public bool EsteExpirat => DateTime.Now > DataScadenta;
//                ^^^^^^^^^ expression-bodied property (sintaxa scurtă)

// 4. Constructor cu : base(...)
public Subclasa(int x) : base(x) { ... }

// 5. virtual + override
public virtual void Metoda() { ... }   // în părinte
public override void Metoda() { ... }   // în copil

// 6. Apel la părinte din override
public override bool Validare() { return base.Validare() && conditie; }

// 7. Compoziție
public List<Bilet> Bilete { get; set; } = new List<Bilet>();

// 8. LINQ pentru agregări
collection.Sum(x => x.Pret)
collection.Where(x => conditie).ToList()
collection.OrderBy(x => x.Camp).FirstOrDefault()
```

---

## Capcane

| Capcană | Antidot |
|---------|---------|
| Folosești `=` în loc de `:` la moștenire | `class Sub : Parent` (nu `=`) |
| Uiți `virtual` în părinte | Compilator: "metoda nu poate fi override-uită". Adaugă `virtual`. |
| Faci `override` fără `virtual` | Eroare de compilare. |
| `new` în loc de `override` | `new` ascunde metoda părinte (NU polimorfism). Fii atent — diferenţă subtilă. |
| Câmp `_x` public | Nu — câmpurile cu `_` sunt PRIVATE prin convenţie. Public expune doar `X` (property). |
| Validare în setter dar NU în constructor | Constructor-ul TREBUIE să folosească setter-ul (`X = x;`), nu câmpul (`_x = x;`). |
| `==` cu DateTime și milisecunde | `DateTime.Now == DateTime.Now` poate fi `false` (ms diferite). Folosește `.Date` sau diferenţă. |

---

## Exercitiu pentru testul 2025 (cerinţa 1+2)

Pentru clasa `Factura` din testul de anul trecut:

```csharp
public class Factura
{
    // Auto-properties simple
    public DateTime DataEmitere { get; set; }
    public DateTime DataScadenta { get; set; }
    public string Serie { get; set; }
    public int Numar { get; set; }
    public string DenumireClient { get; set; }
    public decimal SumaDePlata { get; set; }
    public StatusFactura Status { get; set; }   // enum: Emis, Platit

    // Property auto-calculată (cerinţa 2: 1p)
    public bool EsteExpirata => DateTime.Now > DataScadenta;
    //                  ^^^^^^^ get-only, fără setter
}

public enum StatusFactura
{
    Emis,
    Platit
}
```

**Cheia:** `=>` la property = sintaxă scurtă pentru `get { return ...; }` fără setter. Calculezi pe baza altor properties.
