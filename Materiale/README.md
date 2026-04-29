# Programarea Aplicațiilor Windows (PAW) — Materiale

**Profesor:** Lucian Vilcea
**Tehnologie:** C# + .NET + Windows Forms
**Sursa codului:** [github.com/lucianvilcea26/PAW](https://github.com/lucianvilcea26/PAW)
**Site:** [ase.lucianvilcea.ro/programarea-aplicatiilor-windows](https://ase.lucianvilcea.ro/programarea-aplicatiilor-windows)
**Test:** **18 mai 2026**

---

## Structura cursului

| Seminar | Subiect | Fișier sumar |
|---------|---------|--------------|
| 1 | Introducere C# și .NET | (concepte, fără cod) |
| 2 | OOP — clase, moștenire, interfețe | [01_OOP.md](01_OOP.md) |
| 3 | Delegates, Acțiuni, Events | [02_Events.md](02_Events.md) |
| 4 | Windows Forms basics | [03_WinForms_Basics.md](03_WinForms_Basics.md) |
| 5 | DataGridView + Multi-fereastră | [04_MultiForm.md](04_MultiForm.md) |
| 5+ | **MDI** (Multiple Document Interface) | [05_MDI.md](05_MDI.md) |
| 6 | Repository + FakeDatabase | [06_Repository.md](06_Repository.md) |
| 7 | ADO.NET + LocalDB | [07_ADO_NET.md](07_ADO_NET.md) |
| 8 | LINQ + extra | [08_LINQ.md](08_LINQ.md) |

---

## Subiectul de anul trecut (2025) — analizat

În folderul `../Subiecte/` ai poza cu testul. Pe scurt:

> **Aplicație Windows Forms MDI** pentru gestiune facturi (data emitere, scadență, serie, număr, client, sumă, status).
>
> 1. (2p) Implementează aplicația MDI cu clasa `Factura`
> 2. (1p) Property auto-calculată: e expirată data scadenței?
> 3. (2p) Form separat cu lista facturilor sortate după dată, deschis în MDI
> 4. (2p) Form pentru adăugare factură nouă cu validări (data scadență ≥ 7 zile după emitere)
> 5. (2p) Metodă care afișează (în MessageBox) suma totală a facturilor expirate cu serie F sau K

**Mapping cerințe → materiale:**
- Cerința 1 → [01_OOP.md](01_OOP.md) (clase + properties) + [05_MDI.md](05_MDI.md) (container MDI)
- Cerința 2 → [01_OOP.md](01_OOP.md) (proprietăți auto-calculate cu `get`)
- Cerința 3 → [04_MultiForm.md](04_MultiForm.md) (DataGridView + sortare LINQ) + [05_MDI.md](05_MDI.md) (MdiParent)
- Cerința 4 → [04_MultiForm.md](04_MultiForm.md) (ShowDialog + ErrorProvider)
- Cerința 5 → [08_LINQ.md](08_LINQ.md) (LINQ filter + sum) + [04_MultiForm.md](04_MultiForm.md) (MessageBox)

---

## Plan de drill (3 săptămâni până la test)

### Săpt 1 (29 apr - 5 mai) — Bazele
- 01_OOP.md (clase, properties, moștenire, interfețe)
- 02_Events.md (delegates + events)
- 03_WinForms_Basics.md (primul form, Designer)

### Săpt 2 (6-12 mai) — Aplicații complete
- 04_MultiForm.md (S5 — pattern principal de test)
- 05_MDI.md (specific pentru test 2025)
- 06_Repository.md (pattern repository)

### Săpt 3 (13-17 mai) — Date + revizie
- 07_ADO_NET.md (database real)
- 08_LINQ.md (filtrare, sortare, sumă)
- **Drill final:** rezolvi subiectul 2025 de la 0, fără să te uiți. Cronometrat.

### 18 mai — testul
- Dimineață: revizie scurtă (15 min) pe README + cheatsheet
- La examen: respiri, citești subiectul, scrii pe ordinea: clasa → DGV → form add → MDI → metoda extra

---

## Compilare + rulare

**Visual Studio (recomandat):**
- File → New → Project → Windows Forms App (.NET Framework SAU .NET 6+)
- Ai automat Form1.Designer.cs și Form1.cs

**Linie de comandă (mai rar pe Windows Forms):**
```bash
dotnet new winforms -n MyApp
cd MyApp
dotnet run
```

---

## Reguli de aur pentru drill

1. **Activ, nu pasiv** — Visual Studio deschis, scrii cod, rulezi, vezi. Nu doar citești.
2. **Setează break-points** — F9 pe linie, apoi F5 pentru debug. Vezi efectiv ce se întâmplă.
3. **Compilează des** — F5 sau Ctrl+F5 după fiecare schimbare semnificativă.
4. **Designer-ul nu e magic** — vezi ce generează în `Form1.Designer.cs` (e cod, nu black-box).
5. **MessageBox.Show e prietenul tău** — pentru debug rapid.

---

## Capcane comune (la toate seminariile)

| Capcană | Antidot |
|---------|---------|
| Modifici `Form1.Designer.cs` manual | Nu — folosește Designer-ul (Visual Studio). Designer-ul rescrie fișierul. |
| Uiți `using System.Windows.Forms;` | Add usings cu Ctrl+. (Visual Studio sugerează automat) |
| `decimal` vs `double` la valori monetare | Mereu `decimal` pentru bani (mai exact). `double` doar pentru științific. |
| `BindingList<T>` vs `List<T>` | `BindingList` actualizează automat DataGridView când adaugi/scoți. `List` nu. |
| Strings comparate cu `==` | În C# `==` pentru string compară conținut. OK. (Diferit de Java/C++.) |
| `EventHandler` vs custom delegate | Pentru events folosește `EventHandler<T>`. Custom doar dacă ai nevoie. |
