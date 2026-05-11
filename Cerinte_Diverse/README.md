# Cerinte DP Diverse

Cerințe practice date de profesoară — nu sunt subiecte de examen anterioare, ci exerciții suplimentare.

---

## 1. Command — Telecomandă universală (locuință inteligentă)

**Pattern:** Command  
**Domeniu:** Smart home

**Ce se cere:** telecomandă cu 3 butoane configurabile. Fiecare buton execută o acțiune (aprinde lumina, pornește TV, deschide jaluzele). Acțiunile pot fi schimbate dinamic fără modificarea telecomenzii.

**Participanți:**
| Rol | Clasă |
|-----|-------|
| Interfață comandă | `IComanda` cu `executa()` |
| Receiver | `Lumina`, `Televizor`, `Jaluzele` |
| Comenzi concrete | `ComandaAprindeLumina`, `ComandaPornesteTv`, `ComandaDeschideJaluzele` etc. |
| Invoker | `Telecomanda` — array de 3 `IComanda[]` |
| Client | `Main` |

**Cheie:** `Telecomanda` ține `IComanda[] butoane = new IComanda[3]`, `setBuon(int index, IComanda c)`, `apasaBuon(int index)`.

> Cod de referință: `Teorie_DP/10_Command/cod_curs/`

---

## 2. Command — Sistem tranzacționare bursă

**Pattern:** Command  
**Domeniu:** Bursă / finanțe

**Ce se cere:** ordine de cumpărare și vânzare pentru acțiuni executate uniform. Obiectul care declanșează tranzacția nu depinde de implementarea concretă.

**Participanți:**
| Rol | Clasă |
|-----|-------|
| Interfață comandă | `IOrdin` cu `executa()` |
| Receiver | `Broker` (sau `Portofoliu`) — face cumpărarea/vânzarea efectivă |
| Comenzi concrete | `OrdinCumparare`, `OrdinVanzare` — țin receiver + simbol + cantitate |
| Invoker | `BursaClient` — `List<IOrdin>`, `executaOrdine()` |
| Client | `Main` |

---

## 3. Adapter — Telefon USB-C / încărcător MicroUSB

**Pattern:** Adapter (object adapter)  
**Domeniu:** Hardware

**Ce se cere:** telefonul acceptă `chargeUSBc()`, utilizatorul are `chargeMicroUsb()` → adaptor.

**Participanți:**
| Rol | Clasă |
|-----|-------|
| Interfață cerută | `IUSBcIncarcator` cu `incarcaUSBc()` |
| Clasa existentă | `MicroUSB implements IMicroUSBIncarcator` |
| Adapter | `Adaptor implements IUSBcIncarcator` + `private IMicroUSBIncarcator inc` |
| Client | `Telefon` — acceptă `IUSBcIncarcator` |

> Cod de referință: `Teorie_DP/08_Adapter/cod_seminar/` (exemplul 2 — USB)

---

## 4. Composite — Referendum (secții → județe → național)

**Pattern:** Composite  
**Domeniu:** Vot / civic

**Ce se cere:** voturi înregistrate la nivel de secție de votare; secțiile sunt grupate în județe. Fiecare entitate (secție, județ, național) trebuie să poată răspunde dacă referendumul a fost aprobat prin majoritate.

**Participanți:**
| Rol | Clasă |
|-----|-------|
| Interfață comună | `IEntitateVot` cu `getNrVoturiPentru()`, `getNrVoturiImpotriva()`, `esteAprobat()` |
| Nod container | `Judet` — `List<IEntitateVot>`, agregă recursiv |
| Frunză | `SectieVotare` — returnează valorile proprii |
| Client | `Main` |

**Logică `esteAprobat()`:** `getNrVoturiPentru() > getNrVoturiImpotriva()`

> Similar cu S07_Referendum — dar acolo era și TemplateMethod. Aici e doar Composite.

---

## 5. Strategy — Companie design interior (vizualizare planuri)

**Pattern:** Strategy  
**Domeniu:** Design interior / software

**Ce se cere:** clientul poate alege modalitatea de vizualizare a planurilor (2D, 3D, Detalii produse) dacă are opțiunea în pachetul achiziționat. Poate schimba oricând vizualizarea.

**Participanți:**
| Rol | Clasă |
|-----|-------|
| Interfață strategie | `IVizualizare` cu `vizualizeaza(Plan plan)` |
| Strategii concrete | `Vizualizare2D`, `Vizualizare3D`, `VizualizareDetaliiProduse` |
| Context | `ClientDesign` — ține `IVizualizare strategie` + `List<String> pachet` |
| Client | `Main` |

**Cheie:** `setVizualizare(IVizualizare v)` verifică dacă opțiunea e în pachet înainte de setare.

---

## 6. Flyweight — Randări AI camere (bucătărie, baie, living, dining)

**Pattern:** Flyweight  
**Domeniu:** Design interior / AI

**Ce se cere:** modele AI pentru fiecare tip de cameră sunt costisitoare de generat → se reutilizează. Starea variabilă (dimensiunile camerei: lungime, lățime) se pasează ca parametru.

**Participanți:**
| Rol | Clasă |
|-----|-------|
| Interfață flyweight | `IModelCamera` cu `randeaza(double lungime, double latime)` |
| Flyweight concret | `ModelCamera` — ține `String tipCamera` (intrinsecă) |
| Factory | `FabricaModeleAI` — `static Map<String, IModelCamera>`, `static {}` |
| Stare extrinsecă | `lungime`, `latime` — pasate la `randeaza()` |

**Tipuri de cameră (chei în map):** `"bucatarie"`, `"baie"`, `"living"`, `"dining"`

> Aceeași structură ca `Teorie_DP/05_Flyweight/` — doar domeniul diferă.
