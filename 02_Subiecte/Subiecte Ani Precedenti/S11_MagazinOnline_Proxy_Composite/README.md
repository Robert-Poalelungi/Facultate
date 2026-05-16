# S11 — Magazin Online | Proxy + Composite

## Pattern 1: Proxy — 5p

**Indicatori în cerință:**
- *„modul intermediar care să gestioneze noul context"* — „intermediar" = Proxy
- *„această opțiune nu trebuie să implice modificări în codul existent"* — Proxy adaugă comportament fără modificare
- *„discount de 10% aplicat doar o singură dată la prima comandă"* — logică adăugată transparent în fața clasei Magazin

**Regula:** „nu trebuie să implice modificări în codul existent", „modul intermediar" → **Proxy**

---

## Pattern 2: Composite — 5p

**Indicatori în cerință:**
- *„vizualizarea produselor într-o manieră arborescentă"* — structură arborescentă
- *„minim două niveluri de agregare: categorii, subcategorii"* — ierarhie parte-întreg
- *„la nivel de categorie: denumire + număr total produse; la nivel de produs: denumire + stoc"* — interfață comună, comportament diferit

**Regula:** „structură ierarhică de produse/categorii", „operație aplicată uniform pe noduri și frunze" → **Composite**
