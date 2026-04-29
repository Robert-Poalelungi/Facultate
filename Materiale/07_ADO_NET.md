# 07 — ADO.NET + LocalDB (Seminar 7)

**Sursa:** `Seminar7/` din github.com/lucianvilcea26/PAW
**Concepte:** `SqlConnection`, `SqlCommand`, `SqlDataReader`, parametri SQL, LocalDB.

---

## Concept central

**ADO.NET** = librăria built-in a .NET pentru acces la baze de date SQL.

**LocalDB** = SQL Server simplificat, instalat cu Visual Studio. Baze de date în fișiere `.mdf`.

**Diferența vs S6 (FakeDatabase):**
- S6: `List<T>` în memorie (se pierde la închidere)
- S7: SQL real (persistent, survive restarts)
- **Dar repository-ul are aceeași semnătură!** UI nu observă schimbarea.

---

## 1. Connection string

```csharp
private string _connectionString =
    "Data Source=(LocalDB)\\MSSQLLocalDB;" +
    "AttachDbFilename=|DataDirectory|\\Carti.mdf;" +
    "Integrated Security=True";
```

**Componente:**
- `Data Source` — instanța SQL (LocalDB îl pornește on-demand).
- `AttachDbFilename` — fișierul `.mdf` (baza de date).
- `|DataDirectory|` — placeholder pentru folder-ul aplicației (rezolvat la runtime).
- `Integrated Security=True` — autentificare cu user-ul Windows curent (no password).

---

## 2. Pattern complet — `using` peste `SqlConnection`

```csharp
public List<Carte> GetAll()
{
    var results = new List<Carte>();

    using (var connection = new SqlConnection(_connectionString))
    {
        connection.Open();

        using (var command = new SqlCommand(
            "SELECT Id, Titlu, Autor, AnAparitie, Gen FROM Carti", connection))
        {
            var reader = command.ExecuteReader();
            while (reader.Read())
            {
                var carte = new Carte();
                carte.Id = reader.GetGuid(reader.GetOrdinal("Id"));
                carte.Titlu = reader.GetString(reader.GetOrdinal("Titlu"));
                carte.Autor = reader.GetString(reader.GetOrdinal("Autor"));
                carte.AnAparitie = reader.GetInt32(reader.GetOrdinal("AnAparitie"));
                carte.Gen = (GenCarte)Enum.Parse(typeof(GenCarte),
                                                  reader.GetString(reader.GetOrdinal("Gen")));
                results.Add(carte);
            }
        }
        connection.Close();
    }

    return results;
}
```

### Pas cu pas

**Bloc 1 — `using` pentru connection:**
```csharp
using (var connection = new SqlConnection(_connectionString)) { ... }
```
Garantează că conexiunea se închide chiar dacă apare excepție (`Dispose()` automat).

**Bloc 2 — `using` pentru command:**
```csharp
using (var command = new SqlCommand("SELECT ...", connection)) { ... }
```
Idem pentru command — eliberează resursele după.

**Bloc 3 — `ExecuteReader()`:**
```csharp
var reader = command.ExecuteReader();
while (reader.Read())
{
    // o linie pe iteratie
}
```
- `Read()` avansează la rândul următor; returnează `false` la sfârșit.
- Iterativ — citești rând cu rând, nu tot deodată.

**Bloc 4 — Citire câmpuri:**
```csharp
carte.Id = reader.GetGuid(reader.GetOrdinal("Id"));
carte.Titlu = reader.GetString(reader.GetOrdinal("Titlu"));
```
- `GetOrdinal("Nume")` returnează indexul coloanei (mai sigur decât hardcoded `0, 1, 2`).
- `GetString`, `GetInt32`, `GetGuid`, `GetDateTime`, `GetDecimal` — methode tipizate.

**Bloc 5 — Enum din string:**
```csharp
carte.Gen = (GenCarte)Enum.Parse(typeof(GenCarte), reader.GetString(...));
```
SQL nu are tipuri enum native — sunt stocate ca string. Parsare cu `Enum.Parse`.

---

## 3. INSERT cu parametri

```csharp
public void Add(Carte carte)
{
    using (var connection = new SqlConnection(_connectionString))
    {
        connection.Open();
        using (var command = new SqlCommand(
            "INSERT INTO Carti (Id, Titlu, Autor, AnAparitie, Gen) " +
            "VALUES (@id, @titlu, @autor, @anAparitie, @gen)",
            connection))
        {
            command.Parameters.AddWithValue("id", carte.Id.ToString());
            command.Parameters.AddWithValue("titlu", carte.Titlu);
            command.Parameters.AddWithValue("autor", carte.Autor);
            command.Parameters.AddWithValue("anAparitie", carte.AnAparitie);
            command.Parameters.AddWithValue("gen", carte.Gen.ToString());

            command.ExecuteNonQuery();
        }
        connection.Close();
    }
}
```

### Pas cu pas

**Parametri SQL:**
```csharp
"INSERT INTO Carti (Id, Titlu, ...) VALUES (@id, @titlu, ...)"
//                                          ^^^^^^^ placeholder

command.Parameters.AddWithValue("id", carte.Id.ToString());
//                              ^^^^ numele (fara @)
```

**De ce parametri și NU concatenare?**
```csharp
// PERICULOS — SQL Injection
"INSERT INTO Carti VALUES ('" + carte.Titlu + "', ...)"   // ❌

// SIGUR — parametri
command.Parameters.AddWithValue("titlu", carte.Titlu);     // ✅
```

Dacă `carte.Titlu` conține `'); DROP TABLE Carti; --`, prima variantă DISTRUGE BD-ul. Parametrii escapează automat.

**`ExecuteNonQuery()`** — pentru INSERT/UPDATE/DELETE (nu return data, doar număr de rânduri afectate).

---

## 4. UPDATE și DELETE

```csharp
public void Update(Carte carte)
{
    using (var connection = new SqlConnection(_connectionString))
    {
        connection.Open();
        using (var command = new SqlCommand(
            "UPDATE Carti SET Titlu = @titlu, Autor = @autor, " +
            "AnAparitie = @anAparitie, Gen = @gen WHERE Id = @id",
            connection))
        {
            command.Parameters.AddWithValue("id", carte.Id.ToString());
            command.Parameters.AddWithValue("titlu", carte.Titlu);
            command.Parameters.AddWithValue("autor", carte.Autor);
            command.Parameters.AddWithValue("anAparitie", carte.AnAparitie);
            command.Parameters.AddWithValue("gen", carte.Gen.ToString());

            command.ExecuteNonQuery();
        }
        connection.Close();
    }
}

public void Delete(Guid id)
{
    using (var connection = new SqlConnection(_connectionString))
    {
        connection.Open();
        using (var command = new SqlCommand("DELETE FROM Carti WHERE Id = @id", connection))
        {
            command.Parameters.AddWithValue("id", id.ToString());
            command.ExecuteNonQuery();
        }
        connection.Close();
    }
}
```

**Pattern identic pentru toate** — diferă doar SQL-ul.

---

## 5. Setup LocalDB în Visual Studio

**Pași:**
1. **Add → New Item → Service-based Database** → `Carti.mdf` în folderul proiectului.
2. View → Server Explorer → conectezi la `Carti.mdf`.
3. Right-click pe Tables → Add New Table → definești coloanele.
4. Save (Ctrl+S) și introduci numele tabelei.
5. Right-click tabela → Show Table Data → poți adăuga date manual.

**Sau prin SQL:**
```sql
CREATE TABLE Carti (
    Id NVARCHAR(36) PRIMARY KEY,
    Titlu NVARCHAR(200),
    Autor NVARCHAR(100),
    AnAparitie INT,
    Gen NVARCHAR(50)
);
```

---

## 6. Tipuri de date SQL ↔ C#

| SQL | C# | Method de citire |
|-----|-----|------------------|
| `INT` | `int` | `GetInt32` |
| `NVARCHAR` / `VARCHAR` | `string` | `GetString` |
| `BIT` | `bool` | `GetBoolean` |
| `DATETIME` / `DATETIME2` | `DateTime` | `GetDateTime` |
| `DECIMAL` / `MONEY` | `decimal` | `GetDecimal` |
| `FLOAT` / `REAL` | `double` | `GetDouble` |
| `UNIQUEIDENTIFIER` | `Guid` | `GetGuid` |

---

## Cheatsheet

```csharp
// Pattern complet pentru orice query
using (var conn = new SqlConnection(connStr))
{
    conn.Open();
    using (var cmd = new SqlCommand("SQL aici", conn))
    {
        // pentru parametri:
        cmd.Parameters.AddWithValue("nume", valoare);

        // pentru SELECT:
        var reader = cmd.ExecuteReader();
        while (reader.Read()) { /* citeste */ }

        // pentru INSERT/UPDATE/DELETE:
        cmd.ExecuteNonQuery();

        // pentru SELECT scalar (un singur rezultat):
        var rez = cmd.ExecuteScalar();    // ex: COUNT(*)
    }
}
```

---

## Capcane

| Capcană | Antidot |
|---------|---------|
| Concatenare SQL — SQL injection | **MEREU** parametri (`AddWithValue`). |
| Uiți `connection.Open()` | Toate metodele crapă. Mereu Open înainte de Execute. |
| Uiți `using` la connection/command | Connection rămâne deschisă → leaks. Mereu `using`. |
| `GetString` pe coloană NULL | `InvalidCastException`. Verifică `reader.IsDBNull(idx)` înainte. |
| `GetInt32` pe coloană mismatched | Tip greșit. Verifică schema BD-ului. |
| `ExecuteReader` pe INSERT | `ExecuteNonQuery` e corect pentru INSERT/UPDATE/DELETE. |
| Modifici BD-ul direct fără `command.ExecuteNonQuery()` | Nu se întâmplă nimic. |

---

## Pentru testul tău

Subiectul 2025 NU cere DB. Restul cursului folosește S6 (FakeDatabase) ca alternativă mai simplă. **Dar dacă subiectul tău cere persistență:**

```csharp
// In loc de List<Factura> in memorie
private FacturaRepository _repo = new FacturaRepository();   // SQL inside

// Add factura
_repo.Add(facturaNoua);

// Get all (sortate)
var sortate = _repo.GetAll().OrderBy(f => f.DataScadenta);
dgv.DataSource = sortate.ToList();
```

Repository-ul ascunde SQL-ul. Form-urile rămân la fel ca în S5/S6.
