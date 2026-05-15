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

## 3. FacturiForm — DataGridView cu date

```csharp
public partial class FacturiForm : Form
{
    public FacturiForm()
    {
        InitializeComponent();
        IncarcaDate();
    }

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
}
```

**Coloane DataGridView** (adaugate in Designer via Edit Columns sau cod):
- Ordinea din `Rows.Add(...)` trebuie sa corespunda cu ordinea coloanelor
- `dgvFacturi.ReadOnly = true;`
- `dgvFacturi.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;`

### Recuperare obiect din randul selectat (pattern seminar)
```csharp
// In SelectionChanged sau la click pe buton:
if (dgvFacturi.SelectedRows.Count == 0) return;
var factura = dgvFacturi.SelectedRows[0].Tag as Factura;
```

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

## 5. ListView — pattern complet

### Designer (setari obligatorii)
```
View = Details
FullRowSelect = true
GridLines = true
```

### Adaugare coloane (in Designer sau cod)
```csharp
lvFacturi.Columns.Add("Serie", 80, HorizontalAlignment.Left);
lvFacturi.Columns.Add("Numar", 60, HorizontalAlignment.Right);
lvFacturi.Columns.Add("Client", 150, HorizontalAlignment.Left);
lvFacturi.Columns.Add("Data Emitere", 100, HorizontalAlignment.Center);
lvFacturi.Columns.Add("Suma", 100, HorizontalAlignment.Right);
lvFacturi.Columns.Add("Status", 80, HorizontalAlignment.Left);
lvFacturi.Columns.Add("Expirata", 70, HorizontalAlignment.Center);
```

### Incarcare date
```csharp
private void IncarcaDate()
{
    lvFacturi.Items.Clear();

    var facturi = MainForm.Facturi
        .OrderBy(f => f.DataScadenta)
        .ToList();

    foreach (var f in facturi)
    {
        var item = new ListViewItem(f.Serie);                    // prima coloana
        item.SubItems.Add(f.Numar.ToString());                   // coloana 2
        item.SubItems.Add(f.DenumireClient);                     // coloana 3
        item.SubItems.Add(f.DataEmitere.ToString("dd.MM.yyyy")); // coloana 4
        item.SubItems.Add(f.SumaDePlata.ToString("N2"));         // coloana 5
        item.SubItems.Add(f.Status.ToString());                  // coloana 6
        item.SubItems.Add(f.EsteExpirata ? "Da" : "Nu");         // coloana 7

        // Optional: coloreaza rand dupa conditie
        if (f.EsteExpirata)
            item.BackColor = Color.LightCoral;

        lvFacturi.Items.Add(item);
    }
}
```

### Obtine elementul selectat (cu Tag — pattern seminar)
```csharp
// La incarcare, stocheaza obiectul in Tag:
item.Tag = f;
lvFacturi.Items.Add(item);

// La buton sterge / editeaza:
private void btnSterge_Click(object sender, EventArgs e)
{
    if (lvFacturi.SelectedItems.Count == 0)
    {
        MessageBox.Show("Selectati o factura!", "Atentie",
            MessageBoxButtons.OK, MessageBoxIcon.Warning);
        return;
    }

    var factura = lvFacturi.SelectedItems[0].Tag as Factura;  // recuperezi obiectul
    MainForm.Facturi.Remove(factura);
    IncarcaDate();
}
```

### Diferenta fata de DataGridView

| | DataGridView | ListView |
|---|---|---|
| Adaugare rand | `int i = Rows.Add(v1, v2)` | `new ListViewItem(v1)` + `SubItems.Add(v2)` |
| Stocheaza obiect | `Rows[i].Tag = f` | `item.Tag = f` |
| Recupereaza obiect | `SelectedRows[0].Tag as Factura` | `SelectedItems[0].Tag as Factura` |
| Curatare | `Rows.Clear()` | `Items.Clear()` |
| Culoare rand | `Rows[i].DefaultCellStyle.BackColor` | `item.BackColor` |

### Colorare conditionata
```csharp
if (f.EsteExpirata)
    item.BackColor = Color.LightCoral;
else if (f.Status == StatusFactura.Platita)
    item.BackColor = Color.LightGreen;
```

---

## 6. LINQ — operatii frecvente la examen

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

## 11. Structura tipica subiect examen

```
1. Model (clasa + enum + proprietate calculata)
2. MainForm:
   - Lista statica
   - Buton deschide FacturiForm (MDI)
   - Buton calcul LINQ + MessageBox
   - Buton deschide AdaugaFacturaForm (dialog)
3. FacturiForm / ListaForm:
   - DataGridView SAU ListView cu coloane
   - Incarcare date din lista statica, sortate
4. AdaugaForm:
   - Campuri + DateTimePicker + ComboBox
   - ValidateForm() cu ErrorProvider
   - Salvare in lista statica + DialogResult.OK
```
