# 06 — Repository Pattern + FakeDatabase (Seminar 6)

**Sursa:** `Seminar6/` din github.com/lucianvilcea26/PAW
**Concepte:** separation of concerns, repository pattern, in-memory data store, `Guid`, CRUD generic.

---

## Concept central

**Repository pattern** = strat intermediar între UI și sursa de date (DB, fișier, in-memory).

```
[Form (UI)] → [CarteRepository] → [FakeDatabase / SQL]
```

**De ce?** Form-ul nu trebuie să știe DACĂ datele vin din SQL, fișier sau in-memory. Schimbi sursa fără să modifici UI-ul (S6 → S7 doar schimbă repository-ul).

---

## 1. Modelul + enum

```csharp
public class Carte
{
    public Guid Id { get; set; }            // identificator unic
    public string Titlu { get; set; }
    public string Autor { get; set; }
    public int AnAparitie { get; set; }
    public GenCarte Gen { get; set; }
}

public enum GenCarte
{
    Roman, Stiinta, Fictiune, Biografie, Tehnic, Altele
}
```

**`Guid`** = Globally Unique IDentifier. Garantat unic la nivel mondial. Generat cu:
```csharp
var id = Guid.NewGuid();   // ex: "550e8400-e29b-41d4-a716-446655440000"
```
Folosit ca `Id` în loc de int (no race conditions, no collision).

---

## 2. FakeDatabase — store static în memorie

```csharp
public static class FakeDatabase
{
    public static List<Carte> Carti = new List<Carte>()
    {
        new Carte() {
            Id = Guid.NewGuid(),
            Titlu = "Mândrie și prejudecată",
            Autor = "Jane Austen",
            AnAparitie = 1813,
            Gen = GenCarte.Roman
        },
        new Carte() {
            Id = Guid.NewGuid(),
            Titlu = "Război și pace",
            Autor = "Lev Tolstoi",
            AnAparitie = 1869,
            Gen = GenCarte.Roman
        },
        // ... mai multe
    };
}
```

### Ce e `static`?

- **`static class`** = nu poți crea instanțe (`new FakeDatabase()` → eroare).
- **`static List<Carte> Carti`** = lista trăiește pe durata programului. Toate locurile care accesează `FakeDatabase.Carti` văd ACEEAȘI listă.

**Folosire:**
```csharp
var toate = FakeDatabase.Carti;             // direct, fara new
FakeDatabase.Carti.Add(carte);
```

**Util pentru testare** când nu vrei DB real. Datele se pierd la închiderea programului (nu sunt persistente).

---

## 3. Repository-ul — CRUD complet

```csharp
public class CarteRepository
{
    public List<Carte> GetAll()
    {
        return new List<Carte>(FakeDatabase.Carti);    // copie (safety)
    }

    public Carte GetById(Guid id)
    {
        return FakeDatabase.Carti.SingleOrDefault(c => c.Id == id);
    }

    public void Add(Carte carte)
    {
        FakeDatabase.Carti.Add(carte);
    }

    public void Update(Carte carte)
    {
        int index = FakeDatabase.Carti.FindIndex(x => x.Id == carte.Id);
        if (index >= 0)
            FakeDatabase.Carti[index] = carte;
    }

    public void Delete(Guid id)
    {
        FakeDatabase.Carti.RemoveAll(c => c.Id == id);
    }
}
```

### Pas cu pas

**`GetAll`** — returnează o **copie** a listei. De ce?
- Dacă returnezi referința directă, UI-ul ar putea modifica lista internă (bug).
- `new List<Carte>(...)` clonează (shallow — itemii sunt aceiași, dar lista e nouă).

**`GetById`** — `SingleOrDefault` returnează:
- Itemul dacă există unic.
- `null` dacă nu există.
- **Aruncă** dacă există MAI MULT decât unul.

**`Add`** — banal, doar adăugare.

**`Update`** — `FindIndex` găsește indexul, apoi înlocuiește elementul.

**`Delete`** — `RemoveAll(predicat)` șterge toate matchurile (aici 0 sau 1, dat fiind că `Id` e unic).

---

## 4. Folosire în form

```csharp
public partial class Form1 : Form
{
    private CarteRepository _repo = new CarteRepository();

    public Form1()
    {
        InitializeComponent();
        Refresh();
    }

    private void Refresh()
    {
        dgvCarti.DataSource = _repo.GetAll();
    }

    private void btnAdauga_Click(object sender, EventArgs e)
    {
        using (var formCarte = new FormCarte())
        {
            if (formCarte.ShowDialog() == DialogResult.OK)
            {
                _repo.Add(formCarte.CarteModificata);
                Refresh();
            }
        }
    }

    private void btnEditeaza_Click(object sender, EventArgs e)
    {
        var idx = dgvCarti.SelectedRows[0].Index;
        var carte = _repo.GetAll()[idx];

        using (var formCarte = new FormCarte(carte))
        {
            if (formCarte.ShowDialog() == DialogResult.OK)
            {
                _repo.Update(formCarte.CarteModificata);
                Refresh();
            }
        }
    }

    private void btnSterge_Click(object sender, EventArgs e)
    {
        var idx = dgvCarti.SelectedRows[0].Index;
        var carte = _repo.GetAll()[idx];

        if (MessageBox.Show($"Sterge {carte.Titlu}?", "Confirmare",
            MessageBoxButtons.YesNo) == DialogResult.Yes)
        {
            _repo.Delete(carte.Id);
            Refresh();
        }
    }
}
```

**Observaţie:** form-ul NU mai cunoaște `FakeDatabase`. Vorbește doar cu `_repo`. **Asta e ideea pattern-ului** — schimbi repo-ul (S7 cu SQL), form-ul rămâne neatins.

---

## 5. Avantajele pattern-ului

| Avantaj | Detalii |
|---------|---------|
| Separation of concerns | UI ≠ Logic ≠ Date. Fiecare strat își vede de treaba lui. |
| Schimbare ușoară a sursei | `FakeDatabase` → `SQL` → fără să modifici Form-ul. |
| Testare ușoară | Poți testa logica fără DB real. |
| Reutilizare | Acelaşi repo poate fi folosit din mai multe forme. |

---

## Cheatsheet

```csharp
// 1. Static class (date globale)
public static class StoreData {
    public static List<T> Items = new List<T>();
}

// 2. Repository CRUD
public class TRepository {
    public List<T> GetAll() => new List<T>(StoreData.Items);
    public T GetById(Guid id) => StoreData.Items.SingleOrDefault(x => x.Id == id);
    public void Add(T item) => StoreData.Items.Add(item);
    public void Update(T item) {
        int i = StoreData.Items.FindIndex(x => x.Id == item.Id);
        if (i >= 0) StoreData.Items[i] = item;
    }
    public void Delete(Guid id) => StoreData.Items.RemoveAll(x => x.Id == id);
}

// 3. Folosire in form
private TRepository _repo = new TRepository();
dgv.DataSource = _repo.GetAll();
_repo.Add(item);
```

---

## Capcane

| Capcană | Antidot |
|---------|---------|
| Form-ul accesează direct `FakeDatabase` | Defeat scopul pattern-ului. Folosește `_repo` peste tot. |
| Nu copiezi lista la `GetAll` | UI poate modifica intern. Returnează `new List<T>(...)`. |
| `Single` în loc de `SingleOrDefault` | Crash dacă nu găsește. Folosește versiunea `OrDefault`. |
| Uiți `FindIndex` ≥ 0 înainte de update | Crash la `lista[-1]`. Verifică. |
| `RemoveAll` cu predicat care nu match-uieşte | OK — nu face nimic. Nu e bug. |
| Multiple repository-uri pe aceeași date | OK — lucrează cu lista statică, indiferent câți. |

---

## Pentru testul tău

Pentru subiectul 2025 NU trebuie repository explicit (testul nu cere asta). Dar **pattern-ul e bun de știut** pentru organizarea codului:
- Lista facturilor = în Form1 (sau într-un repo).
- Form-urile child cer/trimit prin repo (sau prin referință directă la listă).
- Codul devine mai curat.
