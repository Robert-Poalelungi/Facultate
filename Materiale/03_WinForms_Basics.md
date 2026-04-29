# 03 — Windows Forms Basics (Seminar 4)

**Sursa:** `Seminar4/` din github.com/lucianvilcea26/PAW
**Concepte:** Form, Designer, controale (TextBox, Button, ListBox, CheckBox), event handlers, validare simplă.

---

## Concept central

WinForms = framework UI pentru Windows. Bazat pe:
- **Form** = fereastră (clasa moștenește `System.Windows.Forms.Form`).
- **Designer** = unealtă vizuală în Visual Studio. Drag & drop controale pe form. Generează automat cod în `*.Designer.cs`.
- **Code-behind** = fișierul `*.cs` (scris de tine) — handler-e pentru events.
- **Resources** = fișierul `*.resx` (resurse: imagini, traduceri etc.).

---

## 1. Structura unui form (3 fișiere)

```
Form1.cs            <- codul tau (event handlers)
Form1.Designer.cs   <- generat de Designer (NU edita manual)
Form1.resx          <- resurse (auto-generat)
```

```csharp
// Form1.cs
public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();    // metoda din Designer.cs
    }

    private void btnSalveaza_Click(object sender, EventArgs e)
    {
        // codul tău
    }
}
```

`partial` permite ca clasa să fie împărțită în 2 fișiere — Designer-ul gestionează unul, tu pe celălalt.

---

## 2. Controale comune

### TextBox
```csharp
txtNume.Text             // citește/scrie textul
txtNume.Text = string.Empty;     // golește
txtNume.Focus();         // pune focusul
txtNume.Enabled = false; // dezactivează
txtNume.ReadOnly = true; // doar citire (vs Enabled care schimbă culoarea)
```

### Button
```csharp
btnSalveaza.Enabled = false;
btnSalveaza.Text = "Salvează";
// Eveniment Click (in Designer)
private void btnSalveaza_Click(object sender, EventArgs e) { ... }
```

### CheckBox
```csharp
chkActive.Checked       // bool
chkActive.Checked = true;
chkActive.Text = "Activ";
```

### Label
```csharp
lblStatus.Text = "Total: 5";
```

### ComboBox
```csharp
cmbDept.Items.Add("Vanzari");                    // adăugare
cmbDept.SelectedItem                             // itemul ales (object)
cmbDept.SelectedItem.ToString()                  // ca string
cmbDept.SelectedIndex                            // index (-1 = nimic)
cmbDept.DataSource = lista;                       // bind la listă
cmbDept.DropDownStyle = ComboBoxStyle.DropDownList;  // nu permite text custom
```

### ListBox
```csharp
lstContacte.Items.Add(contact);
lstContacte.Items.Clear();
lstContacte.SelectedIndex                        // -1 dacă nimic
lstContacte.SelectedItem
```

### DateTimePicker
```csharp
dtpData.Value             // DateTime
dtpData.Value = DateTime.Now;
dtpData.Format = DateTimePickerFormat.Short;     // DD.MM.YYYY
```

### NumericUpDown
```csharp
nudCantitate.Value        // decimal
nudCantitate.Value = 5;
nudCantitate.Minimum = 0;
nudCantitate.Maximum = 100;
```

---

## 3. Form complet din S4 — `Contact`

```csharp
public partial class Form1 : Form
{
    private List<Contact> _contacte = new List<Contact>();

    public Form1()
    {
        InitializeComponent();
    }

    private void btnSalveaza_Click(object sender, EventArgs e)
    {
        // Validare
        if (string.IsNullOrEmpty(txtNume.Text))
        {
            MessageBox.Show("Numele este obligatoriu", "Eroare",
                MessageBoxButtons.OK, MessageBoxIcon.Error);
            return;
        }
        // ... mai multe verificări

        // Construire obiect
        var contact = new Contact()
        {
            Nume = txtNume.Text.Trim(),
            Prenume = txtPrenume.Text.Trim(),
            Telefon = txtTelefon.Text.Trim(),
            Email = txtEmail.Text.Trim(),
            NotificariActive = chkNotificariActive.Checked
        };
        _contacte.Add(contact);

        RefreshListaContacte(_contacte);

        // Curățare formular
        txtNume.Text = string.Empty;
        txtPrenume.Text = string.Empty;
        txtTelefon.Text = string.Empty;
        txtEmail.Text = string.Empty;
        chkNotificariActive.Checked = false;
        txtNume.Focus();

        lblStatus.Text = $"Total: {_contacte.Count} contacte";
    }

    private void RefreshListaContacte(List<Contact> contacte)
    {
        lstContacte.Items.Clear();
        foreach (Contact contact in contacte)
        {
            lstContacte.Items.Add(contact);    // foloseste contact.ToString()
        }
    }

    private void txtCautare_TextChanged(object sender, EventArgs e)
    {
        var termen = txtCautare.Text.Trim().ToLower();
        var filtrate = _contacte.Where(c =>
            c.ToString().ToLower().Contains(termen)).ToList();
        RefreshListaContacte(filtrate);
    }
}
```

### Pattern-uri utile din S4

**1. Validare cu return early:**
```csharp
if (string.IsNullOrEmpty(txt.Text)) {
    MessageBox.Show("Eroare", ...);
    return;        // iese din metoda — nu mai continua
}
```

**2. `.Trim()` pentru curățare input:**
```csharp
var x = txtNume.Text.Trim();    // scoate spatii la inceput/sfarsit
```

**3. `.ToLower()` pentru comparare case-insensitive:**
```csharp
if (text.ToLower().Contains(termen.ToLower())) { ... }
```

**4. Live search cu `TextChanged`:**
```csharp
private void txtCautare_TextChanged(object sender, EventArgs e)
{
    // se apeleaza la fiecare caracter scris
    Filtreaza(txtCautare.Text);
}
```

**5. `_contacte` ca state al form-ului:**
```csharp
private List<Contact> _contacte = new List<Contact>();
```
Lista trăiește atâta cât există form-ul. La închidere → garbage collected.

---

## 4. Cum adaugi un control + handler din Designer

**În Visual Studio:**
1. Open `Form1.cs [Design]`.
2. Toolbox (View → Toolbox) → drag controlul pe form (ex. Button).
3. Properties (F4):
   - `(Name)` → schimbi numele (ex. `btnSalveaza`).
   - `Text` → ce scrie pe control.
4. Pentru handler de event: dublu-click pe control → generează automat `btnSalveaza_Click` în `Form1.cs`.

**Sau:**
1. Properties → tab fulger ⚡ (Events).
2. Vezi toate event-urile (Click, MouseEnter, etc.).
3. Dublu-click pe event → handler generat.

---

## 5. Layout — ancorare

În Designer, fiecare control are property-ul `Anchor`:
- `Top, Left` (default) — fixed în colțul stânga sus.
- `Top, Bottom, Left, Right` — se redimensionează cu form-ul.

Pentru DataGridView, de obicei: `Top, Bottom, Left, Right` (umple spațiul disponibil).

---

## Cheatsheet

```csharp
// 1. Citire input
string s = txtNume.Text.Trim();
bool b = chkOK.Checked;
DateTime d = dtpData.Value;

// 2. Validare + return
if (string.IsNullOrEmpty(s)) {
    MessageBox.Show("Eroare");
    return;
}

// 3. Parse defensiv
if (!decimal.TryParse(txtSuma.Text, out decimal suma)) {
    MessageBox.Show("Suma invalidă");
    return;
}

// 4. Curățare formular
txtNume.Text = string.Empty;
txtNume.Focus();

// 5. ListBox refresh
lst.Items.Clear();
foreach (var x in lista) lst.Items.Add(x);

// 6. Confirmare
if (MessageBox.Show("Sigur?", "Confirmare",
    MessageBoxButtons.YesNo) == DialogResult.Yes) { ... }
```

---

## Capcane

| Capcană | Antidot |
|---------|---------|
| Modifici `Form1.Designer.cs` manual | Designer-ul îl rescrie. Schimbă din Designer (Properties). |
| Uiți `using System.Windows.Forms;` | Add usings: Ctrl+. |
| `txt.Text == ""` în loc de `string.IsNullOrEmpty(txt.Text)` | Nu prinde whitespace. Folosește `IsNullOrWhiteSpace`. |
| Asociezi handler-ul de 2 ori (în Designer + în cod) | Handler-ul se apelează de 2 ori. Verifică Designer.cs. |
| `Items.Add(obj)` și aștepți să vezi proprietățile | ListBox afișează `ToString()`. Override `ToString()` în clasa ta. |
| `.Trim()` modifică string-ul | NU. String-urile sunt imutabile. `.Trim()` returnează un string nou. |

---

## Pentru testul tău

S4 e baza pe care construiești S5 (multi-form). Cheia pentru testul 2025:
- Folosește `MessageBox` pentru afișări.
- Validează ÎNAINTE de a salva (return early).
- Curăță formularul după salvare (gata pentru următoarea intrare).

Detalii de UI mai avansate (DataGridView, ErrorProvider, ShowDialog) → vezi **04_MultiForm.md**.
