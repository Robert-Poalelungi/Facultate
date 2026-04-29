# 04 — DataGridView + Aplicații Multi-fereastră (Seminar 5)

**Sursa:** `Seminar5/` din github.com/lucianvilcea26/PAW
**Concepte:** `DataGridView`, `BindingList<T>`, `ShowDialog`, `DialogResult`, `ErrorProvider`, `MessageBox`, comunicare între forme.

---

## Concept central

Pattern-ul **PRINCIPAL** la testul tău (folosit în S5 și în subiectul 2025):
1. **Form principal** cu un `DataGridView` care afișează lista
2. **Buton „Adaugă" / „Editează"** care deschide un al doilea form (modal cu `ShowDialog`)
3. **Al doilea form** are inputuri + buton Salvează
4. La salvare: validare cu `ErrorProvider`, dacă OK → return cu `DialogResult.OK`
5. Form-ul principal preia rezultatul prin un property pe form-ul secundar

---

## 1. Modelul — `Angajat`

```csharp
public class Angajat
{
    public string Nume { get; set; }
    public string Prenume { get; set; }
    public string Departament { get; set; }
    public decimal Salariu { get; set; }              // decimal pentru bani
    public DateTime DataAngajarii { get; set; }
    public bool EstePermanent { get; set; }

    public override string ToString()
    {
        return $"{Prenume} {Nume}";
    }
}
```

Auto-properties (vezi 01_OOP.md). `decimal` în loc de `double` pentru bani.

---

## 2. Form principal — `Form1.cs`

```csharp
public partial class Form1 : Form
{
    private BindingList<Angajat> _angajati = new BindingList<Angajat>()
    {
        new Angajat()
        {
            Nume = "Popescu",
            Prenume = "Ion",
            Departament = "Vanzari",
            Salariu = 5700m,
            DataAngajarii = new DateTime(2021, 11, 20),
            EstePermanent = true
        }
    };

    public Form1()
    {
        InitializeComponent();              // generat de Designer
        dgvAngajati.DataSource = _angajati;
    }
    // ...
}
```

### Pas cu pas

**Bloc 1 — `partial`:**
```csharp
public partial class Form1 : Form
```
- `partial` = clasa e împărțită în mai multe fișiere. Aici: `Form1.cs` (cod scris de tine) + `Form1.Designer.cs` (cod generat de Designer).
- Compilatorul le combină în memorie ca o singură clasă.

**Bloc 2 — `BindingList<T>`:**
```csharp
private BindingList<Angajat> _angajati = new BindingList<Angajat>() { ... };
```
- `BindingList<T>` e ca `List<T>` dar **notifică automat** când se schimbă conținutul.
- Când o legi de un `DataGridView`, modificările apar automat în UI.
- Inițializare cu **collection initializer**: `{ new Angajat() { ... }, new Angajat() { ... } }`.
- `5700m` — sufixul `m` indică `decimal` (pentru bani).

**Bloc 3 — Constructorul:**
```csharp
public Form1()
{
    InitializeComponent();              // genereaza UI
    dgvAngajati.DataSource = _angajati; // bind list la grid
}
```
- `InitializeComponent()` e generată de Designer; creează butoanele, dgv-ul etc.
- `dgvAngajati.DataSource = _angajati;` → leagă lista de grid. Coloanele apar automat (după properties).

---

## 3. Adăugare — `btnAdauga_Click`

```csharp
private void btnAdauga_Click(object sender, EventArgs e)
{
    using (var formAngajat = new FormAngajat())
    {
        if (formAngajat.ShowDialog() == DialogResult.OK)
        {
            _angajati.Add(formAngajat.AngajatModificat);
        }
    }
}
```

### Pas cu pas

**Bloc 1 — `using` cu `IDisposable`:**
```csharp
using (var formAngajat = new FormAngajat()) { ... }
```
- `using (...) { }` se asigură că `Dispose()` e apelat la sfârșit (chiar dacă apare excepție).
- `Form` implementează `IDisposable` (eliberează resurse UI).
- **Nu confunda cu `using System.Windows.Forms;`** (alt înțeles — directivă de namespace).

**Bloc 2 — `ShowDialog()`:**
```csharp
formAngajat.ShowDialog()
```
- Deschide form-ul **modal** — utilizatorul nu poate interacționa cu Form1 până când nu închide FormAngajat.
- Returnează `DialogResult` (OK, Cancel, etc.).
- **Diferență vs `Show()`:** `Show()` deschide non-modal (poți avea ambele forme deschise simultan).

**Bloc 3 — Verificare rezultat și preluare date:**
```csharp
if (formAngajat.ShowDialog() == DialogResult.OK)
{
    _angajati.Add(formAngajat.AngajatModificat);
}
```
- Dacă utilizatorul a apăsat Salvează (care setează `DialogResult = OK`), preluăm angajatul nou.
- `_angajati.Add(...)` adaugă în lista bound la dgv → grid-ul se actualizează automat.

---

## 4. Editare — `btnEditeaza_Click`

```csharp
private void btnEditeaza_Click(object sender, EventArgs e)
{
    var index = dgvAngajati.SelectedRows[0].Index;
    var angajat = _angajati[index];

    using (var formAngajat = new FormAngajat(angajat))     // pasezi angajatul existent
    {
        if (formAngajat.ShowDialog() == DialogResult.OK)
        {
            _angajati[index] = formAngajat.AngajatModificat;
        }
    }
}
```

**Cheia:** la editare, pasezi angajatul existent în constructorul lui `FormAngajat`. Form-ul îl pre-completează (vezi mai jos).

---

## 5. Ștergere cu confirmare — `btnSterge_Click`

```csharp
private void btnSterge_Click(object sender, EventArgs e)
{
    var index = dgvAngajati.SelectedRows[0].Index;
    var angajat = _angajati[index];

    if (MessageBox.Show(
            $"Sunteti sigur ca vreti sa stergeti angajatul {angajat.Prenume} {angajat.Nume}?",
            "Confirmare",
            MessageBoxButtons.YesNo,
            MessageBoxIcon.Question)
        == DialogResult.Yes)
    {
        _angajati.Remove(angajat);
    }
}
```

### `MessageBox.Show(...)` — toate variantele

```csharp
MessageBox.Show("Mesaj");                                      // doar mesaj
MessageBox.Show("Mesaj", "Titlu");                             // mesaj + titlu
MessageBox.Show("Mesaj", "Titlu", MessageBoxButtons.OK);       // butoane
MessageBox.Show("Mesaj", "Titlu",
                MessageBoxButtons.YesNo,                       // butoane: Yes/No
                MessageBoxIcon.Question);                      // iconita
```

**Iconițe disponibile:** `Information`, `Warning`, `Error`, `Question`, `None`, `Hand`, `Stop`, `Asterisk`.

**Butoane disponibile:** `OK`, `OKCancel`, `YesNo`, `YesNoCancel`, `RetryCancel`, `AbortRetryIgnore`.

**Returnează** `DialogResult.Yes`, `.No`, `.OK`, `.Cancel`, etc.

---

## 6. Filtrare cu LINQ — `cmbFiltruDepartament_SelectedIndexChanged`

```csharp
private void cmbFiltruDepartament_SelectedIndexChanged(object sender, EventArgs e)
{
    if (cmbFiltruDepartament.SelectedItem.ToString() == "Toate")
    {
        dgvAngajati.DataSource = _angajati;
    }
    else
    {
        var departament = cmbFiltruDepartament.SelectedItem.ToString();
        var angajatiFiltrati = _angajati.Where(a => a.Departament == departament).ToList();
        var bindingListFiltrat = new BindingList<Angajat>(angajatiFiltrati);

        dgvAngajati.DataSource = bindingListFiltrat;
    }
}
```

**Pas cu pas:**
1. Citești ce a ales utilizatorul în ComboBox.
2. Dacă „Toate" → afișezi lista completă.
3. Altfel → folosești LINQ `.Where(...)` pentru filtrare, apoi `.ToList()`.
4. Înfăsori în `BindingList` ca să funcționeze cu DataGridView.
5. Setezi `DataSource` la lista filtrată.

---

## 7. Form-ul secundar — `FormAngajat.cs`

```csharp
public partial class FormAngajat : Form
{
    public Angajat AngajatModificat { get; private set; }    // returul

    public FormAngajat(Angajat angajat = null)               // parametru opțional
    {
        InitializeComponent();

        if (angajat != null)
        {
            // Modul editare — pre-completare câmpuri
            Text = $"Editeaza angajatul {angajat.Prenume} {angajat.Nume}";
            txtNume.Text = angajat.Nume;
            txtPrenume.Text = angajat.Prenume;
            cmbDepartament.SelectedItem = angajat.Departament;
            txtSalariu.Text = angajat.Salariu.ToString();
            dtpDataAngajarii.Value = angajat.DataAngajarii;
            chkEstePermanent.Checked = angajat.EstePermanent;
        }
        else
        {
            // Modul adaugare
            Text = "Adauga angajat nou";
        }
    }

    private void btnSalveaza_Click(object sender, EventArgs e)
    {
        epAngajati.Clear();        // ErrorProvider — sterge erorile vechi
        bool esteValid = true;

        // Validări
        if (string.IsNullOrEmpty(txtNume.Text))
        {
            epAngajati.SetError(txtNume, "Numele este obligatoriu");
            esteValid = false;
        }
        if (string.IsNullOrEmpty(txtPrenume.Text))
        {
            epAngajati.SetError(txtPrenume, "Prenumele este obligatoriu");
            esteValid = false;
        }
        if (!decimal.TryParse(txtSalariu.Text, out decimal salariu))
        {
            epAngajati.SetError(txtSalariu, "Salariul este invalid");
            esteValid = false;
        }
        else if (salariu < 0)
        {
            epAngajati.SetError(txtSalariu, "Salariul nu poate fi negativ");
            esteValid = false;
        }

        if (!esteValid)
            return;

        // Construiesc obiectul si setez DialogResult
        AngajatModificat = new Angajat()
        {
            Nume = txtNume.Text,
            Prenume = txtPrenume.Text,
            Departament = cmbDepartament.SelectedItem.ToString(),
            Salariu = salariu,
            DataAngajarii = dtpDataAngajarii.Value,
            EstePermanent = chkEstePermanent.Checked,
        };

        DialogResult = DialogResult.OK;     // închide modal cu OK
    }
}
```

### Pas cu pas

**Bloc 1 — Property pentru rezultat:**
```csharp
public Angajat AngajatModificat { get; private set; }
```
- `private set` — doar codul DIN `FormAngajat` îl poate seta. Form1 doar îl citește.
- E **canalul** prin care Form1 primește datele.

**Bloc 2 — Constructor cu parametru opțional:**
```csharp
public FormAngajat(Angajat angajat = null)
```
- `= null` — parametru opțional. Apelat fără argumente → `null`.
- Permite **două moduri** într-un singur form:
  - `new FormAngajat()` → adăugare
  - `new FormAngajat(angajatExistent)` → editare

**Bloc 3 — Pre-completare la editare:**
```csharp
if (angajat != null) {
    txtNume.Text = angajat.Nume;
    cmbDepartament.SelectedItem = angajat.Departament;
    dtpDataAngajarii.Value = angajat.DataAngajarii;
    chkEstePermanent.Checked = angajat.EstePermanent;
}
```
- `TextBox.Text` — string
- `ComboBox.SelectedItem` — obiect (foloseşte `.ToString()` la citire)
- `DateTimePicker.Value` — DateTime
- `CheckBox.Checked` — bool

**Bloc 4 — Validare cu `ErrorProvider`:**
```csharp
ErrorProvider epAngajati;     // în Designer
epAngajati.Clear();            // resetează erorile
epAngajati.SetError(txtNume, "Mesaj");   // afișează ! lângă control
```
- `ErrorProvider` afișează un `!` roșu lângă controlul cu eroare.
- Hover peste `!` = vezi mesajul.
- `Clear()` la început, apoi `SetError(...)` per câmp invalid.

**Bloc 5 — Validări tipice:**
```csharp
// String gol
if (string.IsNullOrEmpty(txtNume.Text)) { ... }

// String gol sau doar spații
if (string.IsNullOrWhiteSpace(txtNume.Text)) { ... }

// Parsare număr
if (!decimal.TryParse(txtSalariu.Text, out decimal salariu)) { ... }

// Range
if (salariu < 0) { ... }

// Lungime string
if (txt.Text.Length < 3) { ... }

// Începe cu litera anume
if (!txt.Text.StartsWith("F")) { ... }
```

**Bloc 6 — Setarea `DialogResult`:**
```csharp
DialogResult = DialogResult.OK;
```
- **Setarea automată închide form-ul** și revine la `ShowDialog()`-ul apelantului.
- Apelantul citește același `DialogResult.OK` și îl interpretează.

---

## Cheatsheet patternuri

```csharp
// 1. Open form modal cu return
using (var f = new FormulX(/* opțional date */))
{
    if (f.ShowDialog() == DialogResult.OK)
    {
        var rezultat = f.PropertyDeIesire;
        // foloseste rezultatul
    }
}

// 2. Bind list la DataGridView
var bindingList = new BindingList<T>(initialList);
dgv.DataSource = bindingList;
// Modifici bindingList -> dgv se actualizeaza automat

// 3. Sortare in dgv (dupa data, descendenta)
var sortat = lista.OrderBy(x => x.Data).ToList();
dgv.DataSource = new BindingList<T>(sortat);

// 4. ErrorProvider — afisare erori la TextBox
ep.Clear();
if (!valid) {
    ep.SetError(txtX, "Eroare");
    return;
}

// 5. MessageBox cu YesNo
if (MessageBox.Show("Esti sigur?", "Confirmare",
    MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
{
    // sterge / executa
}

// 6. Inchide form cu rezultat
DialogResult = DialogResult.OK;       // închide automat

// 7. Selected row index in dgv
var idx = dgv.SelectedRows[0].Index;
var item = lista[idx];

// 8. Parse numeric defensiv
if (!decimal.TryParse(txt.Text, out decimal val)) { /* eroare */ }
if (!DateTime.TryParse(txt.Text, out DateTime data)) { /* eroare */ }
if (!int.TryParse(txt.Text, out int n)) { /* eroare */ }
```

---

## Capcane

| Capcană | Antidot |
|---------|---------|
| Folosești `Show()` în loc de `ShowDialog()` la modal | `Show()` nu blochează apelantul. Pentru rezultat, folosește `ShowDialog()`. |
| Uiți `using` la form | Memory leak (resurse UI nu se eliberează). Mereu `using (var f = ...)`. |
| Modifici `List<T>` și aștepți să se actualizeze dgv | `List<T>` nu notifică. Folosește `BindingList<T>`. |
| `decimal.Parse` în loc de `TryParse` | `Parse` aruncă excepție pe input invalid. `TryParse` returnează bool — mai sigur. |
| Setezi `DialogResult.OK` ÎNAINTE de validare | Form-ul se închide imediat. Validează ÎNTÂI, apoi setezi DialogResult la sfârșit. |
| `SelectedRows[0]` când nu e nimic selectat | Crash. Verifică `dgv.SelectedRows.Count > 0`. |
| Comparare string cu `==` | OK în C# (compară conținut, nu referință). Diferit de Java. |
| Folosești `cmbDepartament.Text` în loc de `.SelectedItem` | `Text` poate fi text editabil; `SelectedItem` e itemul ales. Pentru ComboBox cu DropDownList, foloseste `SelectedItem.ToString()`. |

---

## Maparea cu testul 2025

| Cerință | Pattern de aici |
|---------|----------------|
| 3. Form lista facturi sortate după dată | DataGridView + `BindingList<Factura>` cu `OrderBy(f => f.DataScadenta)` |
| 4. Form adăugare factură | FormFactura cu `ShowDialog()` + `ErrorProvider` + validare „data scadență ≥ data emitere + 7 zile" |
| 5. Sumă în MessageBox | `MessageBox.Show($"Total: {suma}", "Informații", OK, Information)` |

Pentru cerința 5 vezi și 08_LINQ.md (filter + sum).
