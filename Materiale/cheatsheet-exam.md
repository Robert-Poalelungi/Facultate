# Cheatsheet PAW Exam — Windows Forms MDI

---

## 1. Model (clasa de date)

```csharp
public enum StatusFactura { Emisa, Platita }

public class Factura
{
    public string Serie { get; set; }
    public int Numar { get; set; }
    public string DenumireClient { get; set; }
    public DateTime DataEmitere { get; set; }
    public DateTime DataScadenta { get; set; }
    public decimal SumaDePlata { get; set; }
    public StatusFactura Status { get; set; }

    // Proprietate calculata automat (nu are setter)
    public bool EsteExpirata => DateTime.Now > DataScadenta;
}
```

**Reguli:**
- `public class`, nu `internal`
- Proprietati cu `{ get; set; }`, nu campuri
- Proprietate calculata: `public bool X => expresie;`
- Enum: valorile incep de la 0 (Emisa=0, Platita=1)

---

## 2. MainForm — lista statica + MDI

```csharp
public partial class MainForm : Form
{
    // Lista globala accesibila din orice form
    public static List<Factura> Facturi = new List<Factura>();

    // Deschide form MDI (nu blocat)
    private void btnListaFacturi_Click(object sender, EventArgs e)
    {
        var form = new FacturiForm();
        form.MdiParent = this;
        form.Show();
    }

    // Calcul LINQ + MessageBox
    private void btnTotalSume_Click(object sender, EventArgs e)
    {
        decimal total = Facturi
            .Where(f => f.EsteExpirata && (f.Serie.StartsWith("F") || f.Serie.StartsWith("K")))
            .Sum(f => f.SumaDePlata);

        MessageBox.Show("Suma totala: " + total.ToString("N2") + " RON",
            "Informatii", MessageBoxButtons.OK, MessageBoxIcon.Information);
    }

    // Deschide dialog modal (blocat) — using asigura ca form-ul e distrus dupa
    private void btnAdauga_Click(object sender, EventArgs e)
    {
        using (var form = new AdaugaFacturaForm())
        {
            if (form.ShowDialog() == DialogResult.OK)
                RefreshFacturi();
        }
    }

    // Sterge cu confirmare
    private void btnSterge_Click(object sender, EventArgs e)
    {
        if (dgvFacturi.SelectedRows.Count == 0) return;
        var factura = dgvFacturi.SelectedRows[0].Tag as Factura;

        if (MessageBox.Show("Esti sigur ca vrei sa stergi factura " + factura.Serie + "?",
            "Confirmare stergere", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
        {
            MainForm.Facturi.Remove(factura);
            RefreshFacturi();
        }
    }

    private void RefreshFacturi()
    {
        // reincarca dgv / lv
        IncarcaDate();
    }
}
```

**In Designer.cs al MainForm:**
```csharp
this.IsMdiContainer = true;
```

---

## 3. FacturiForm — DataGridView vs ListView

Coloanele se adauga din **Designer** (click dreapta pe control → Edit Columns).
Ordinea coloanelor din Designer trebuie sa corespunda cu ordinea valorilor din cod.

**Setari Designer:**
- DataGridView: `ReadOnly = true`, `AutoSizeColumnsMode = Fill`, `SelectionMode = FullRowSelect`
- ListView: `View = Details`, `FullRowSelect = true`, `GridLines = true`

### DataGridView

```csharp
private void IncarcaDate()
{
    dgvFacturi.Rows.Clear();

    var facturi = MainForm.Facturi
        .OrderBy(f => f.DataScadenta)
        .ToList();

    foreach (var f in facturi)
    {
        int i = dgvFacturi.Rows.Add(
            f.Serie,
            f.Numar,
            f.DenumireClient,
            f.DataEmitere.ToString("dd.MM.yyyy"),
            f.DataScadenta.ToString("dd.MM.yyyy"),
            f.SumaDePlata.ToString("N2"),
            f.Status,
            f.EsteExpirata ? "Da" : "Nu"
        );
        dgvFacturi.Rows[i].Tag = f;  // stocheaza obiectul in rand!
    }
}

// Recuperare obiect selectat:
var factura = dgvFacturi.SelectedRows[0].Tag as Factura;
```

### ListView

```csharp
private void IncarcaDate()
{
    lvFacturi.Items.Clear();

    var facturi = MainForm.Facturi
        .OrderBy(f => f.DataScadenta)
        .ToList();

    foreach (var f in facturi)
    {
        var item = new ListViewItem(f.Serie);                     // prima coloana
        item.SubItems.Add(f.Numar.ToString());                    // coloana 2
        item.SubItems.Add(f.DenumireClient);                      // coloana 3
        item.SubItems.Add(f.DataEmitere.ToString("dd.MM.yyyy"));  // coloana 4
        item.SubItems.Add(f.DataScadenta.ToString("dd.MM.yyyy")); // coloana 5
        item.SubItems.Add(f.SumaDePlata.ToString("N2"));          // coloana 6
        item.SubItems.Add(f.Status.ToString());                   // coloana 7
        item.SubItems.Add(f.EsteExpirata ? "Da" : "Nu");          // coloana 8
        item.Tag = f;  // stocheaza obiectul!
        lvFacturi.Items.Add(item);
    }
}

// Recuperare obiect selectat:
var factura = lvFacturi.SelectedItems[0].Tag as Factura;
```

### Colorare conditionata (ambele)
```csharp
// DataGridView
dgvFacturi.Rows[i].DefaultCellStyle.BackColor = Color.LightCoral;

// ListView
item.BackColor = Color.LightCoral;
```

### Comparatie rapida

| | DataGridView | ListView |
|---|---|---|
| Adaugare rand | `int i = Rows.Add(v1, v2, ...)` | `new ListViewItem(v1)` + `SubItems.Add(v2)` |
| Stocheaza obiect | `Rows[i].Tag = f` | `item.Tag = f` |
| Recupereaza obiect | `SelectedRows[0].Tag as Factura` | `SelectedItems[0].Tag as Factura` |
| Curatare | `Rows.Clear()` | `Items.Clear()` |
| Verifica selectie | `SelectedRows.Count == 0` | `SelectedItems.Count == 0` |

---

## 4. AdaugaFacturaForm — validare + salvare

```csharp
public partial class AdaugaFacturaForm : Form
{
    private bool ValidateForm()
    {
        epFactura.Clear();
        bool esteValid = true;

        if (string.IsNullOrWhiteSpace(txtSerie.Text))
        {
            epFactura.SetError(txtSerie, "Seria este obligatorie!");
            esteValid = false;
        }

        if (string.IsNullOrWhiteSpace(txtDenumireClient.Text))
        {
            epFactura.SetError(txtDenumireClient, "Clientul este obligatoriu!");
            esteValid = false;
        }

        if (!decimal.TryParse(txtSumaDePlata.Text, out _))
        {
            epFactura.SetError(txtSumaDePlata, "Suma trebuie sa fie un numar!");
            esteValid = false;
        }

        // Validare data: scadenta >= emitere + 7 zile
        if (dtpDataScadenta.Value.Date < dtpDataEmitere.Value.Date.AddDays(7))
        {
            epFactura.SetError(dtpDataScadenta, "Scadenta trebuie sa fie cu cel putin 7 zile dupa emitere!");
            esteValid = false;
        }

        return esteValid;
    }

    private void btnSalveaza_Click(object sender, EventArgs e)
    {
        if (!ValidateForm()) return;

        var factura = new Factura
        {
            Serie = txtSerie.Text.Trim(),
            Numar = int.Parse(txtNumar.Text),
            DenumireClient = txtDenumireClient.Text.Trim(),
            DataEmitere = dtpDataEmitere.Value.Date,
            DataScadenta = dtpDataScadenta.Value.Date,
            SumaDePlata = decimal.Parse(txtSumaDePlata.Text),
            Status = (StatusFactura)cboStatus.SelectedIndex
        };

        MainForm.Facturi.Add(factura);
        DialogResult = DialogResult.OK;
    }
}
```

---

## 5. LINQ — operatii frecvente la examen

LINQ functioneaza pe liste. Toate operatiile se scriu ca un lant si la final obtii un rezultat.
`f` e numele pe care il dai tu fiecarui element — putea fi orice: `x`, `factura`, `item`.

### Where — filtrare

Pastreaza doar elementele care respecta o conditie.

```csharp
// O conditie simpla
var expirate = MainForm.Facturi.Where(f => f.EsteExpirata);

// Conditii multiple cu && (si)
var expirateNePlatite = MainForm.Facturi
    .Where(f => f.EsteExpirata && f.Status == StatusFactura.Emisa);

// Conditii multiple cu || (sau)
var serieFK = MainForm.Facturi
    .Where(f => f.Serie.StartsWith("F") || f.Serie.StartsWith("K"));
```

### OrderBy / OrderByDescending — sortare

```csharp
// Crescator dupa data scadenta (cel mai vechi primul)
var sortate = MainForm.Facturi.OrderBy(f => f.DataScadenta);

// Descrescator dupa suma (cel mai mare primul)
var sortate = MainForm.Facturi.OrderByDescending(f => f.SumaDePlata);

// Alfabetic dupa nume
var sortate = MainForm.Facturi.OrderBy(f => f.DenumireClient);
```

### Sum — suma

```csharp
// Suma tuturor facturilor
decimal total = MainForm.Facturi.Sum(f => f.SumaDePlata);

// Suma doar a celor expirate (Where + Sum inlantuite)
decimal totalExpirate = MainForm.Facturi
    .Where(f => f.EsteExpirata)
    .Sum(f => f.SumaDePlata);
```

### Count — numarare

```csharp
// Cate facturi sunt in total
int total = MainForm.Facturi.Count();

// Cate facturi sunt platite
int platite = MainForm.Facturi.Count(f => f.Status == StatusFactura.Platita);
```

### Max / Min — maxim si minim

```csharp
decimal maxSuma = MainForm.Facturi.Max(f => f.SumaDePlata);
decimal minSuma = MainForm.Facturi.Min(f => f.SumaDePlata);
DateTime primaData = MainForm.Facturi.Min(f => f.DataEmitere);
```

### StartsWith / Contains / EndsWith — filtrare pe text

```csharp
.Where(f => f.Serie.StartsWith("F"))        // incepe cu F
.Where(f => f.Serie.EndsWith("X"))          // se termina cu X
.Where(f => f.DenumireClient.Contains("SRL")) // contine SRL oriunde
```

**Atentie:** toate sunt case-sensitive — `"F"` nu e acelasi cu `"f"`.

### Cum se inlantuiesc

```csharp
decimal rezultat = MainForm.Facturi
    .Where(f => f.EsteExpirata)            // 1. filtreaza
    .Where(f => f.Serie.StartsWith("F"))   // 2. filtreaza din nou
    .OrderBy(f => f.SumaDePlata)           // 3. sorteaza
    .Sum(f => f.SumaDePlata);              // 4. calculeaza suma
```

Ordinea conteaza: `Where` mereu inainte de `Sum`/`Count`/`Max`/`Min`.

### ToList() — cand il folosesti

Obligatoriu inainte de `foreach`:

```csharp
var facturi = MainForm.Facturi
    .Where(f => f.EsteExpirata)
    .OrderBy(f => f.DataScadenta)
    .ToList();  // <-- obligatoriu inainte de foreach

foreach (var f in facturi)
{
    dgvFacturi.Rows.Add(...);
}
```

---

## 7. Formate frecvente

```csharp
data.ToString("dd.MM.yyyy")   // 14.05.2026
suma.ToString("N2")           // 1.234,56
suma.ToString("C")            // 1.234,56 RON (depinde de cultura)
suma.ToString("F2")           // 1234,56
```

---

## 8. MessageBox

```csharp
// Informatii simple
MessageBox.Show("Mesaj", "Titlu", MessageBoxButtons.OK, MessageBoxIcon.Information);

// Confirmare
var raspuns = MessageBox.Show("Esti sigur?", "Confirmare",
    MessageBoxButtons.YesNo, MessageBoxIcon.Question);
if (raspuns == DialogResult.Yes) { /* sterge */ }

// Eroare
MessageBox.Show("A aparut o eroare!", "Eroare",
    MessageBoxButtons.OK, MessageBoxIcon.Error);
```

---

## 9. Pattern MDI vs Dialog

| Situatie | Cod |
|---|---|
| Form secundar (lista, raport) | `form.MdiParent = this; form.Show();` |
| Form de adaugare/editare | `using (var form = new XForm()) { if (form.ShowDialog() == DialogResult.OK) ... }` |
| Inchide cu succes | `DialogResult = DialogResult.OK;` |
| Inchide cu anulare | `DialogResult = DialogResult.Cancel;` sau buton cu `DialogResult = Cancel` |

### Enable/Disable butoane la selectie (pattern seminar)
```csharp
public MainForm()
{
    InitializeComponent();
    btnEditeaza.Enabled = false;
    btnSterge.Enabled = false;
}

private void dgvFacturi_SelectionChanged(object sender, EventArgs e)
{
    bool areSelectie = dgvFacturi.SelectedRows.Count > 0;
    btnEditeaza.Enabled = areSelectie;
    btnSterge.Enabled = areSelectie;
}
```

---

## 10. Greseli clasice de evitat

| Greseala | Corect |
|---|---|
| `internal class Factura` | `public class Factura` |
| `public string Serie;` (camp) | `public string Serie { get; set; }` |
| `serie.startsWith("f")` | `serie.StartsWith("F")` (case-sensitive!) |
| `total.ToString()` | `total.ToString("N2")` |
| Uiti `IsMdiContainer = true` | Seteaza in Designer pe MainForm |
| `(int)cboStatus.SelectedIndex` | `(StatusFactura)cboStatus.SelectedIndex` |
| Uiti `epFactura.Clear()` la inceput | Intotdeauna primul rand in ValidateForm |

---

## 11. Mostenire (Inheritance)

```csharp
// Clasa de baza
public class Bilet
{
    public string NumeFilm { get; set; }
    public double PretBaza { get; set; }

    public virtual double CalculeazaPretFinal()
    {
        return PretBaza - GetReducere();
    }

    public virtual double GetReducere()
    {
        return 0;  // clasa de baza nu are reducere
    }
}

// Clasa derivata — mosteneste din Bilet
public class BiletStudent : Bilet
{
    public string NumarLegitimatie { get; set; }

    // override = suprascrie metoda din clasa de baza
    public override double GetReducere()
    {
        return PretBaza * 0.20;  // 20% reducere
    }
}

// Alta clasa derivata
public class BiletSenior : Bilet
{
    public override double GetReducere()
    {
        return PretBaza * 0.15;  // 15% reducere
    }
}
```

**Reguli:**
- `virtual` in clasa de baza = poate fi suprascris
- `override` in clasa derivata = suprascrie metoda
- `base.MetodaParinte()` = apeleaza metoda din clasa parinte
- Clasa derivata mosteneste toate proprietatile si metodele parintelui

```csharp
// Polimorfism — apelezi metoda pe tipul de baza
Bilet b = new BiletStudent { PretBaza = 30, NumarLegitimatie = "123" };
double pret = b.CalculeazaPretFinal();  // apeleaza override-ul din BiletStudent
```

---

## 12. Interfete (Interfaces)

```csharp
// Definire interfata — doar semnaturi, fara implementare
public interface IPretCalculabil
{
    double CalculeazaPretFinal();
    double GetReducere();
}

public interface IValidabil
{
    bool EsteValid();
}

// Clasa care implementeaza interfetele
public class Bilet : IPretCalculabil, IValidabil
{
    public double CalculeazaPretFinal() { return PretBaza; }
    public double GetReducere() { return 0; }
    public bool EsteValid() { return ExpiraLa > DateTime.Now; }
}
```

**Reguli:**
- Interfata defineste CE trebuie sa faca o clasa, nu CUM
- O clasa poate implementa mai multe interfete (spre deosebire de mostenire unde e doar una)
- Toate metodele din interfata TREBUIE implementate in clasa

---

## 13. Proprietati cu validare (backing field)

Cand vrei sa validezi valoarea la setare:

```csharp
public class Bilet
{
    // Backing field — campul privat care stocheaza valoarea
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
}
```

Diferenta fata de proprietatea simpla:
- `public int X { get; set; }` — fara validare
- `private int _x; public int X { get { return _x; } set { /* validare */ _x = value; } }` — cu validare

---

## 14. Date de test (IncarcaDateTest)

Varianta cea mai simpla la examen — lista statica in MainForm + metoda care adauga obiecte hardcodate pentru testare:

```csharp
public partial class MainForm : Form
{
    public static List<Factura> Facturi = new List<Factura>();

    public MainForm()
    {
        InitializeComponent();
        IncarcaDateTest();
    }

    private void IncarcaDateTest()
    {
        Facturi.Add(new Factura
        {
            DataEmitere = new DateTime(2024, 11, 1),
            DataScadenta = new DateTime(2024, 12, 1),
            Serie = "F",
            Numar = 1001,
            DenumireClient = "SC Alpha SRL",
            SumaDePlata = 1500.00m,
            Status = StatusFactura.Emisa
        });
        Facturi.Add(new Factura
        {
            DataEmitere = new DateTime(2024, 10, 5),
            DataScadenta = new DateTime(2024, 11, 5),
            Serie = "K",
            Numar = 2001,
            DenumireClient = "SC Beta SRL",
            SumaDePlata = 3200.00m,
            Status = StatusFactura.Emisa
        });
        Facturi.Add(new Factura
        {
            DataEmitere = new DateTime(2025, 1, 10),
            DataScadenta = new DateTime(2025, 2, 10),
            Serie = "F",
            Numar = 1002,
            DenumireClient = "SC Omega SRL",
            SumaDePlata = 2000.00m,
            Status = StatusFactura.Platita
        });
    }
}
```

**De ce e bine:** datele apar automat la pornire, poti testa imediat fara sa adaugi manual.

**Regula:** pune date variate — unele expirate, unele nu, serii diferite, statusuri diferite — ca sa poti verifica ca LINQ-ul filtreaza corect.

---

## 14b. Repository + FakeDatabase (varianta seminar)

Pattern din Seminar 6 — date stocate intr-o clasa statica separata, operatii intr-un repository.

```csharp
// FakeDatabase.cs
public static class FakeDatabase
{
    public static List<Carte> Carti = new List<Carte>
    {
        new Carte { Id = Guid.NewGuid(), Titlu = "Ion", Autor = "Rebreanu", AnAparitie = 1920, Gen = GenCarte.Roman },
        new Carte { Id = Guid.NewGuid(), Titlu = "Morometii", Autor = "Preda", AnAparitie = 1955, Gen = GenCarte.Roman },
    };
}

// CarteRepository.cs
public class CarteRepository
{
    public List<Carte> GetAll() => FakeDatabase.Carti;

    public Carte GetById(Guid id) => FakeDatabase.Carti.FirstOrDefault(c => c.Id == id);

    public void Add(Carte carte) => FakeDatabase.Carti.Add(carte);

    public void Update(Carte carte)
    {
        var existent = GetById(carte.Id);
        existent.Titlu = carte.Titlu;
        existent.Autor = carte.Autor;
        existent.AnAparitie = carte.AnAparitie;
        existent.Gen = carte.Gen;
    }

    public void Delete(Guid id) => FakeDatabase.Carti.Remove(GetById(id));
}
```

**Folosire in Form:**
```csharp
private CarteRepository _repo = new CarteRepository();

private void RefreshList()
{
    lvCarti.Items.Clear();
    foreach (var c in _repo.GetAll())
    {
        var item = new ListViewItem(c.Titlu);
        item.SubItems.Add(c.Autor);
        item.Tag = c;
        lvCarti.Items.Add(item);
    }
}
```

---

## 15. Form de editare cu parametru

Pattern din Seminar 5/6 — acelasi form pentru adaugare SI editare.

```csharp
public partial class FormCarte : Form
{
    private Carte _carteEditare;
    private bool _esteAdaugare;

    // Constructorul primeste id-ul null pentru adaugare, sau id-ul cartii pentru editare
    public FormCarte(Guid? id = null)
    {
        InitializeComponent();

        if (id == null)
        {
            Text = "Adauga carte";
            _esteAdaugare = true;
            _carteEditare = new Carte();
        }
        else
        {
            Text = "Editeaza carte";
            _esteAdaugare = false;
            _carteEditare = new CarteRepository().GetById(id.Value);

            // Precompletare campuri
            txtTitlu.Text = _carteEditare.Titlu;
            txtAutor.Text = _carteEditare.Autor;
        }
    }

    private void btnSalveaza_Click(object sender, EventArgs e)
    {
        if (!ValidateForm()) return;

        _carteEditare.Titlu = txtTitlu.Text.Trim();
        _carteEditare.Autor = txtAutor.Text.Trim();

        var repo = new CarteRepository();
        if (_esteAdaugare)
        {
            _carteEditare.Id = Guid.NewGuid();
            repo.Add(_carteEditare);
        }
        else
        {
            repo.Update(_carteEditare);
        }

        DialogResult = DialogResult.OK;
    }
}
```

**Alternativa din Seminar 5** — form primeste obiectul direct si returneaza rezultatul printr-o proprietate publica:

```csharp
public partial class FormAngajat : Form
{
    public Angajat AngajatModificat { get; private set; }  // rezultatul

    public FormAngajat(Angajat angajat = null)  // null = adaugare, obiect = editare
    {
        InitializeComponent();

        if (angajat != null)
        {
            txtNume.Text = angajat.Nume;
            txtPrenume.Text = angajat.Prenume;
            // ... precompletare
        }
    }

    private void btnSalveaza_Click(object sender, EventArgs e)
    {
        if (!ValidateForm()) return;

        AngajatModificat = new Angajat
        {
            Nume = txtNume.Text.Trim(),
            Prenume = txtPrenume.Text.Trim(),
        };

        DialogResult = DialogResult.OK;
    }
}

// Folosire din MainForm:
var form = new FormAngajat(angajatSelectat);  // editare
if (form.ShowDialog() == DialogResult.OK)
{
    var angajatNou = form.AngajatModificat;  // ia rezultatul
    RefreshList();
}
```

---

## 16. Evenimente (Events)

```csharp
// EventArgs custom — datele trimise cu evenimentul
public class ComandaLivrataEventArgs : EventArgs
{
    public string NumarComanda { get; set; }
    public DateTime DataLivrare { get; set; }
}

// Clasa care declanseaza evenimentul
public class Depozit
{
    // Declarare eveniment
    public event EventHandler<ComandaLivrataEventArgs> ComandaLivrata;

    public void LivreazaComanda(string numar)
    {
        // ... logica livrare

        // Declanseaza evenimentul
        ComandaLivrata?.Invoke(this, new ComandaLivrataEventArgs
        {
            NumarComanda = numar,
            DataLivrare = DateTime.Now
        });
    }
}

// Clasa care asculta evenimentul
public class NotificareClient
{
    public void Aboneaza(Depozit depozit)
    {
        depozit.ComandaLivrata += OnComandaLivrata;
    }

    private void OnComandaLivrata(object sender, ComandaLivrataEventArgs e)
    {
        Console.WriteLine("Comanda " + e.NumarComanda + " livrata la " + e.DataLivrare);
    }
}
```

---

## 17. Controale suplimentare

### NumericUpDown
```csharp
// Valoarea curenta
int an = (int)numAn.Value;
decimal suma = numSuma.Value;

// Setare limite in Designer: Minimum, Maximum, DecimalPlaces
```

### CheckBox
```csharp
bool estePermanent = chkEstePermanent.Checked;  // true / false

// Setare programatic
chkEstePermanent.Checked = true;
```

### ComboBox populat cu enum
```csharp
// In constructor / Form_Load — adauga valorile enumului
cmbGen.Items.AddRange(Enum.GetNames(typeof(GenCarte)));
cmbGen.SelectedIndex = 0;

// La salvare — citire din ComboBox
var gen = (GenCarte)Enum.Parse(typeof(GenCarte), cmbGen.SelectedItem.ToString());

// SAU daca enum-ul incepe de la 0 (mai simplu):
var gen = (GenCarte)cmbGen.SelectedIndex;
```

---

## 18. Structura tipica subiect examen

```
1. Model (clasa + mostenire + enum + proprietate calculata)
2. MainForm:
   - Lista statica SAU Repository + FakeDatabase
   - Buton deschide ListaForm (MDI)
   - Buton calcul LINQ + MessageBox
   - Buton deschide AdaugaForm (dialog)
3. ListaForm:
   - DataGridView SAU ListView cu coloane
   - Incarcare date, sortate
   - Butoane Adauga / Editeaza / Sterge
4. AdaugaForm / EditeazaForm (sau unul singur cu parametru):
   - Campuri + DateTimePicker + ComboBox + NumericUpDown + CheckBox
   - ValidateForm() cu ErrorProvider
   - Salvare + DialogResult.OK
```
