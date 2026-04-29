# 05 — MDI (Multiple Document Interface)

**De ce e aici:** subiectul de anul trecut (2025) cere explicit aplicație **MDI**. Seminariile NU acoperă MDI explicit, dar e parte din curriculum WinForms.

---

## Concept central

**MDI = un form părinte (container) care „adăpostește" alte forme (children) în interiorul lui.**

```
┌─────────── Form principal (MDI parent) ──────────┐
│ Meniu: [Facturi] [Adaugare] [Iesire]            │
│                                                  │
│  ┌──────── ListaFacturi (MDI child) ────────┐   │
│  │ [DataGridView cu facturi]                │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
│  ┌──── AdaugareFactura (MDI child) ─────┐       │
│  │ [Formular]                            │       │
│  └───────────────────────────────────────┘       │
└──────────────────────────────────────────────────┘
```

**vs aplicație multi-fereastră obișnuită:** ferestrele sunt independente (oricare poate fi mutată oriunde pe ecran). MDI le **fixează** în interiorul container-ului.

---

## 1. Setup-ul în Designer (Visual Studio)

**Pași:**
1. Pornești proiectul ca Windows Forms App.
2. **Form1 (containerul):**
   - Click pe Form1 în Designer
   - În Properties: **`IsMdiContainer = True`** ← cheia
   - Background-ul devine gri închis (semn vizual că e container).
3. **Adaugi un MenuStrip** (Toolbox → Menus & Toolbars → MenuStrip).
   - Drag pe Form1.
   - Adaugi item-uri: „Facturi", „Adaugare factura", "Iesire".
4. **Adaugi forme child** (`Add → New Item → Windows Form`):
   - `FormListaFacturi.cs`
   - `FormAdaugareFactura.cs`
   - Acestea sunt forme normale — devin MDI child la rulare prin cod.

---

## 2. Setup-ul în cod — Form1 (MDI parent)

```csharp
public partial class Form1 : Form
{
    private List<Factura> _facturi = new List<Factura>();    // datele aplicatiei

    public Form1()
    {
        InitializeComponent();

        // Optional — daca nu setezi IsMdiContainer din Designer:
        // IsMdiContainer = true;

        // Date de test
        _facturi.Add(new Factura { ... });
        _facturi.Add(new Factura { ... });
    }

    private void facturiToolStripMenuItem_Click(object sender, EventArgs e)
    {
        // Deschide forma de lista in interiorul MDI
        var formLista = new FormListaFacturi(_facturi);
        formLista.MdiParent = this;      // ← cheia! face form-ul MDI child
        formLista.Show();                 // NU ShowDialog (modal nu se face MDI)
    }

    private void adaugareToolStripMenuItem_Click(object sender, EventArgs e)
    {
        var formAdauga = new FormAdaugareFactura();
        formAdauga.MdiParent = this;
        formAdauga.Show();
    }

    private void iesireToolStripMenuItem_Click(object sender, EventArgs e)
    {
        Application.Exit();
    }
}
```

### Pas cu pas

**Bloc 1 — Setarea container-ului:**
```csharp
IsMdiContainer = true;
```
Setat din Designer (Properties) sau din cod în constructor. **Fără asta, MDI nu funcționează.**

**Bloc 2 — Definirea modelului în Form1:**
```csharp
private List<Factura> _facturi = new List<Factura>();
```
Lista facturilor trăiește pe Form1 (container). Form-urile child vor primi acest `_facturi` ca parametru.

**Bloc 3 — Deschiderea unui MDI child:**
```csharp
var formLista = new FormListaFacturi(_facturi);
formLista.MdiParent = this;     // OBLIGATORIU
formLista.Show();                // NU ShowDialog!
```

**3 reguli:**
1. **`MdiParent = this`** — leagă form-ul de container.
2. **`.Show()`** (non-modal), NU `.ShowDialog()` — un MDI child nu poate fi modal.
3. **NU folosi `using`** — form-ul rămâne deschis după ce ieși din metoda click.

---

## 3. Form-ul child — `FormListaFacturi`

```csharp
public partial class FormListaFacturi : Form
{
    private List<Factura> _facturi;

    public FormListaFacturi(List<Factura> facturi)
    {
        InitializeComponent();
        _facturi = facturi;

        // Sortare după data scadenței (cresc.) și bind la dgv
        var sortate = _facturi.OrderBy(f => f.DataScadenta).ToList();
        dgvFacturi.DataSource = sortate;
    }
}
```

**Pas cu pas:**
- Constructor primește lista (referință) de la Form1.
- Sortezi cu LINQ `OrderBy(...)`.
- Bind la DataGridView.

**Atentie la referință vs copie:**
- `List<Factura>` e referință → ce primesti aici e ACEEASI lista din Form1.
- Dacă form-ul child modifică `_facturi.Add(...)`, modificările apar și la nivel de Form1.

---

## 4. Form-ul child — `FormAdaugareFactura`

```csharp
public partial class FormAdaugareFactura : Form
{
    public Factura FacturaAdaugata { get; private set; }

    public FormAdaugareFactura()
    {
        InitializeComponent();
        // Implicit: data emiterii = azi, data scadenței = azi + 30 zile
        dtpDataEmitere.Value = DateTime.Now;
        dtpDataScadenta.Value = DateTime.Now.AddDays(30);
    }

    private void btnSalveaza_Click(object sender, EventArgs e)
    {
        epFactura.Clear();
        bool valid = true;

        // Toate câmpurile obligatorii
        if (string.IsNullOrEmpty(txtSerie.Text)) {
            epFactura.SetError(txtSerie, "Seria este obligatorie");
            valid = false;
        }
        if (!int.TryParse(txtNumar.Text, out int numar)) {
            epFactura.SetError(txtNumar, "Numar invalid");
            valid = false;
        }
        if (string.IsNullOrEmpty(txtClient.Text)) {
            epFactura.SetError(txtClient, "Clientul e obligatoriu");
            valid = false;
        }
        if (!decimal.TryParse(txtSuma.Text, out decimal suma)) {
            epFactura.SetError(txtSuma, "Suma invalida");
            valid = false;
        }

        // Verificare cheie: data scadenta - data emitere >= 7 zile (cerinta 4)
        TimeSpan diff = dtpDataScadenta.Value - dtpDataEmitere.Value;
        if (diff.TotalDays < 7) {
            epFactura.SetError(dtpDataScadenta, "Scadenta trebuie sa fie cu cel putin 7 zile dupa emitere");
            valid = false;
        }

        if (!valid) return;

        FacturaAdaugata = new Factura {
            DataEmitere = dtpDataEmitere.Value,
            DataScadenta = dtpDataScadenta.Value,
            Serie = txtSerie.Text,
            Numar = numar,
            DenumireClient = txtClient.Text,
            SumaDePlata = suma,
            Status = StatusFactura.Emis
        };

        // În MDI, NU închidem prin DialogResult.OK (form-ul nu e modal)
        // Notificăm Form1 că s-a adăugat — vezi sectiunea „Comunicare in MDI"
        Close();
    }
}
```

---

## 5. Comunicarea între MDI parent și child

În MDI obișnuit nu poți folosi `ShowDialog` + `DialogResult` (forme child sunt non-modale). 3 abordări:

### A. Pasezi referința la lista în constructor (cea mai simplă)

```csharp
// Form1
var f = new FormAdaugareFactura(_facturi);   // pasezi referinta
f.MdiParent = this;
f.Show();

// FormAdaugareFactura
private List<Factura> _facturi;
public FormAdaugareFactura(List<Factura> facturi) {
    InitializeComponent();
    _facturi = facturi;
}
// La salvare:
_facturi.Add(noulNou);    // adauga in lista — Form1 vede modificarea
```

**Avantaj:** simplu.
**Dezavantaj:** Form1 nu știe ÎN MOD ACTIV că s-a adăugat ceva (trebuie să refacă `dgv.DataSource` manual când redeschide form-ul de listă).

### B. Cu `BindingList<T>` (auto-update)

```csharp
// Form1
private BindingList<Factura> _facturi = new BindingList<Factura>();

// FormAdaugareFactura primeste si tot adauga in lista
_facturi.Add(noulNou);
// DataGridView legat de BindingList se actualizeaza automat pe toate formele!
```

**Avantaj:** se actualizează totul automat.

### C. Cu event custom (avansat — vezi 02_Events.md)

```csharp
// FormAdaugareFactura
public event EventHandler<FacturaAdaugataEventArgs> FacturaAdaugata;

// La salvare, raise event:
FacturaAdaugata?.Invoke(this, new FacturaAdaugataEventArgs(noulNou));

// Form1 (la deschidere)
var f = new FormAdaugareFactura();
f.FacturaAdaugata += (s, e) => _facturi.Add(e.Factura);
f.MdiParent = this;
f.Show();
```

---

## 6. MessageBox info — cerinta 5 din test

```csharp
private void afisareTotalToolStripMenuItem_Click(object sender, EventArgs e)
{
    // Filter: facturi expirate + serie F sau K
    var total = _facturi
        .Where(f => f.EsteExpirata)
        .Where(f => f.Serie.StartsWith("F") || f.Serie.StartsWith("K"))
        .Sum(f => f.SumaDePlata);

    MessageBox.Show(
        $"Suma totala a facturilor expirate cu seria F sau K: {total:C}",
        "Informații",
        MessageBoxButtons.OK,
        MessageBoxIcon.Information
    );
}
```

**Format-uri utile pentru `:` în interpolare:**
- `{total:C}` — currency („1.234,56 lei")
- `{total:F2}` — fixed 2 zecimale („1234.56")
- `{total:N2}` — număr cu separator („1,234.56")
- `{data:dd.MM.yyyy}` — dată
- `{data:HH:mm}` — oră

---

## 7. Layout MDI — afișare child-uri

Form1 poate aranja automat formele child:

```csharp
LayoutMdi(MdiLayout.Cascade);          // în cascadă
LayoutMdi(MdiLayout.TileHorizontal);   // tiled orizontal
LayoutMdi(MdiLayout.TileVertical);     // tiled vertical
LayoutMdi(MdiLayout.ArrangeIcons);     // aranjare iconițe
```

Util la cerința „afișare în MDI".

---

## Capcane MDI

| Capcană | Antidot |
|---------|---------|
| Uiți `IsMdiContainer = true` pe Form1 | Form-urile copil apar peste Form1 (independente). Setează property-ul. |
| Folosești `ShowDialog` pentru child | Crash sau comportament neașteptat. Foloseste `.Show()`. |
| Setezi `MdiParent = this` ÎNAINTE de `Show()` | OK — ordinea corectă. Dacă inversezi: `Show()` apoi `MdiParent = this` — uneori funcționează, dar e fragil. |
| `using (var f = ...)` la MDI child | Form-ul se închide imediat (Dispose). Nu folosi `using` pentru MDI children. |
| Crezi că `DialogResult.OK` închide formul | NU în MDI. Folosește `Close()`. |
| Mai multe instanțe ale aceleiași forme child | Posibil — fiecare click pe meniu deschide nou. Dacă vrei doar UNA, ține o referință. |

---

## Pattern complet pentru testul 2025

```csharp
// === Form1 (MDI container) ===
public partial class Form1 : Form
{
    private BindingList<Factura> _facturi = new BindingList<Factura>();

    public Form1()
    {
        InitializeComponent();
        IsMdiContainer = true;            // si in Designer

        // date de test (cerinta: aplicatia trebuie sa contina date de verificare)
        _facturi.Add(new Factura { Serie = "F", Numar = 100,
                                   DataEmitere = DateTime.Now.AddDays(-30),
                                   DataScadenta = DateTime.Now.AddDays(-7),
                                   DenumireClient = "ASE", SumaDePlata = 1000m,
                                   Status = StatusFactura.Emis });
        // ... mai multe
    }

    private void listaToolStripMenuItem_Click(object s, EventArgs e)
    {
        var f = new FormListaFacturi(_facturi);
        f.MdiParent = this;
        f.Show();
    }

    private void adaugareToolStripMenuItem_Click(object s, EventArgs e)
    {
        var f = new FormAdaugareFactura(_facturi);
        f.MdiParent = this;
        f.Show();
    }

    private void totalToolStripMenuItem_Click(object s, EventArgs e)
    {
        var total = _facturi
            .Where(f => f.EsteExpirata)
            .Where(f => f.Serie.StartsWith("F") || f.Serie.StartsWith("K"))
            .Sum(f => f.SumaDePlata);

        MessageBox.Show(
            $"Total: {total:C}",
            "Informații",
            MessageBoxButtons.OK,
            MessageBoxIcon.Information);
    }
}

// === Factura.cs ===
public class Factura
{
    public DateTime DataEmitere { get; set; }
    public DateTime DataScadenta { get; set; }
    public string Serie { get; set; }
    public int Numar { get; set; }
    public string DenumireClient { get; set; }
    public decimal SumaDePlata { get; set; }
    public StatusFactura Status { get; set; }

    public bool EsteExpirata => DateTime.Now > DataScadenta;    // auto-prop
}

public enum StatusFactura { Emis, Platit }
```

Vezi și **04_MultiForm.md** (DataGridView, ErrorProvider) și **08_LINQ.md** (filtrare, sortare, sumă).
