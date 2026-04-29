# 08 — LINQ (Language Integrated Query)

**Folosit la:** filtrare, sortare, agregări pe colecții. **Esential** pentru cerința 5 din testul 2025 (sumă cu filtru).

---

## Concept central

LINQ permite query-uri pe colecții direct în C# — ca un SQL pentru obiecte:

```csharp
var rezultat = lista
    .Where(x => x.Conditie)        // filtrare
    .OrderBy(x => x.CampOrdonare)   // sortare
    .Sum(x => x.CampSuma);          // agregare
```

**Aceeași logică ca SQL:**
```sql
SELECT SUM(camp_suma) FROM tabela
WHERE conditie
ORDER BY camp_ordonare
```

---

## 1. `Where(...)` — filtrare

```csharp
// Toate facturile expirate
var expirate = _facturi.Where(f => f.EsteExpirata);

// Conditii multiple — AND
var f1 = _facturi.Where(f => f.EsteExpirata && f.Serie == "F");

// Conditii multiple — OR
var f2 = _facturi.Where(f => f.Serie == "F" || f.Serie == "K");

// Cu StartsWith
var f3 = _facturi.Where(f => f.Serie.StartsWith("F") || f.Serie.StartsWith("K"));

// Inlantuire (echivalent cu AND)
var f4 = _facturi
    .Where(f => f.EsteExpirata)
    .Where(f => f.Serie.StartsWith("F"));
```

**Note:**
- `Where` returnează un **`IEnumerable<T>`** (lazy — nu execută până nu cere cineva).
- Pentru forțare la `List<T>`: `.ToList()` la final.

---

## 2. `OrderBy(...)` / `OrderByDescending(...)` — sortare

```csharp
// Sortare crescatoare
var sortate = _facturi.OrderBy(f => f.DataScadenta);

// Sortare descrescatoare
var sortate2 = _facturi.OrderByDescending(f => f.SumaDePlata);

// Sortare multipla (apoi după)
var sortate3 = _facturi
    .OrderBy(f => f.Serie)
    .ThenBy(f => f.Numar);
```

**Pentru testul 2025 cerința 3** („sortare crescătoare după dată"):
```csharp
var sortate = _facturi.OrderBy(f => f.DataScadenta).ToList();
dgv.DataSource = sortate;
```

---

## 3. Agregări — `Sum`, `Count`, `Average`, `Min`, `Max`

```csharp
// Suma totala
decimal total = _facturi.Sum(f => f.SumaDePlata);

// Numar de facturi expirate
int n = _facturi.Count(f => f.EsteExpirata);

// Numar TOTAL (fara filtru)
int total2 = _facturi.Count();

// Media
decimal medie = _facturi.Average(f => f.SumaDePlata);

// Min/Max
decimal cea_mai_mare = _facturi.Max(f => f.SumaDePlata);
decimal cea_mai_mica = _facturi.Min(f => f.SumaDePlata);

// Cea mai mare ca obiect (nu doar valoarea)
Factura cea_mai_scumpa = _facturi.OrderByDescending(f => f.SumaDePlata).First();
```

**Pentru testul 2025 cerința 5** (sumă cu filtru complex):
```csharp
decimal total = _facturi
    .Where(f => f.EsteExpirata)                                          // expirate
    .Where(f => f.Serie.StartsWith("F") || f.Serie.StartsWith("K"))     // serie F sau K
    .Sum(f => f.SumaDePlata);                                            // suma sumelor

MessageBox.Show($"Total: {total:C}", "Informații",
                MessageBoxButtons.OK, MessageBoxIcon.Information);
```

---

## 4. Selecție — `Select` (proiecție)

```csharp
// Doar numele filmelor
var nume = bilete.Select(b => b.NumeFilm);

// Obiecte anonime (cu mai multe campuri)
var rezumat = bilete.Select(b => new {
    Film = b.NumeFilm,
    Loc = b.NumarLoc,
    Pret = b.CalculeazaPretFinal()
});
```

`new { ... }` = obiect anonim — tip generat de compilator. Util pentru DataGridView când nu vrei să afișezi toate properties.

---

## 5. `First` / `FirstOrDefault` / `Single`

```csharp
var prima = lista.First(f => f.Serie == "F");           // arunca exceptie daca nu gaseste
var prima2 = lista.FirstOrDefault(f => f.Serie == "F"); // returneaza null daca nu gaseste

var unic = lista.Single(f => f.Numar == 100);           // exact 1 — exceptie altfel
var unic2 = lista.SingleOrDefault(f => f.Numar == 100); // exact 1 sau null
```

**Recomandare:** `FirstOrDefault` în 90% din cazuri — sigur (no exception).

---

## 6. `Any` / `All` — verificări de existență

```csharp
// Exista cel putin una?
bool exista = _facturi.Any(f => f.EsteExpirata);

// Toate indeplinesc?
bool toate = _facturi.All(f => f.SumaDePlata > 0);
```

---

## 7. `GroupBy` — grupare

```csharp
// Group by serie
var pe_serie = _facturi.GroupBy(f => f.Serie);

foreach (var grup in pe_serie)
{
    Console.WriteLine($"Serie {grup.Key}: {grup.Count()} facturi, total {grup.Sum(f => f.SumaDePlata)}");
}
```

`grup.Key` = valoarea după care s-a grupat. Iterezi peste `grup` pentru elemente.

---

## 8. `Distinct` — valori unice

```csharp
var serii = _facturi.Select(f => f.Serie).Distinct();
```

---

## 9. Conversii — `ToList`, `ToArray`, `ToDictionary`

```csharp
List<Factura> lista = _facturi.Where(...).ToList();
Factura[] vector = _facturi.Where(...).ToArray();
Dictionary<string, Factura> dict = _facturi.ToDictionary(f => f.Serie + f.Numar);
```

---

## 10. Sintaxa de query (alternativă, mai puțin folosită)

LINQ are 2 sintaxe — fluent (cu `.Method()`) și query (cu `from ... where ... select ...`):

```csharp
// Fluent (recomandat)
var rez1 = _facturi
    .Where(f => f.EsteExpirata)
    .OrderBy(f => f.DataScadenta)
    .Select(f => f.Serie);

// Query (echivalent — cum e SQL)
var rez2 = from f in _facturi
           where f.EsteExpirata
           orderby f.DataScadenta
           select f.Serie;
```

**Folosește fluent** — e mai modern și mai ușor de înlănțuit.

---

## Cheatsheet patternuri

```csharp
// 1. Filtru + count
int n = lista.Count(x => conditie);

// 2. Filtru + sum
var total = lista.Where(x => cond).Sum(x => x.Camp);

// 3. Sortare crescatoare
var sortat = lista.OrderBy(x => x.Camp).ToList();

// 4. Sortare descendenta
var sortat2 = lista.OrderByDescending(x => x.Camp).ToList();

// 5. Top N
var top3 = lista.OrderByDescending(x => x.Camp).Take(3).ToList();

// 6. Cautare
var x = lista.FirstOrDefault(x => x.Id == 5);

// 7. Verificare existenta
if (lista.Any(x => cond)) { ... }

// 8. Filtru complex (AND si OR)
var f = lista.Where(x => x.A == 1 && (x.B == 2 || x.B == 3));

// 9. Filtru pe data (intre doua date)
var inIntervalul = lista.Where(x => x.Data >= start && x.Data <= end);

// 10. Filtru pe string
var startsF = lista.Where(x => x.Serie.StartsWith("F"));
var endsX = lista.Where(x => x.Serie.EndsWith("X"));
var contains = lista.Where(x => x.Nume.Contains("Pop"));
```

---

## Capcane

| Capcană | Antidot |
|---------|---------|
| Iteri peste IEnumerable de 2 ori (lazy) | Forțează cu `.ToList()` o singură dată dacă o folosești de mai multe ori. |
| `Select` în loc de `Where` | `Select` transformă fiecare element. `Where` filtrează. Diferite! |
| `First` pe colecție goală | Crash. Folosește `FirstOrDefault` și verifică `null`. |
| `Sum` pe `null` items | Aruncă excepție. Pre-filtrează cu `.Where(x => x != null)` sau folosește `?.` |
| LINQ cu lambda complicat | Splitează în pași: `var pas1 = lista.Where(...); var pas2 = pas1.OrderBy(...);` |
| `==` între string-uri în lambda | OK în C# (compară conținut). |
| Crezi că LINQ modifică sursa | NU — toate metodele returnează **noi** colecții. Sursa e neatinsă. |

---

## Performanță (pentru când contează)

- **Lazy evaluation** — `Where`, `Select`, etc. nu execută până nu cere cineva (`foreach`, `ToList`).
- **`ToList()`** evaluează imediat și salvează rezultatul în memorie.
- Pentru colecții mari, evită `OrderBy` urmat de `Where` — mai bine `Where` întâi (mai puțin de sortat).

```csharp
// MAI BINE
var rez = lista.Where(...).OrderBy(...).ToList();

// Mai prost (sortează totul, apoi filtrează)
var rez2 = lista.OrderBy(...).Where(...).ToList();
```

---

## Maparea cu testul 2025

| Cerință | LINQ |
|---------|------|
| 3. Lista sortată după data scadenței | `_facturi.OrderBy(f => f.DataScadenta).ToList()` |
| 5. Sumă filtrată (expirate + serie F/K) | `_facturi.Where(f => f.EsteExpirata).Where(f => f.Serie.StartsWith("F") \|\| f.Serie.StartsWith("K")).Sum(f => f.SumaDePlata)` |
