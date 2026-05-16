# S06 — Restaurant | Decorator + Composite

## Pattern 1: Decorator — 5p

**Indicatori în cerință:**
- *„i se poate adăuga un topping suplimentar"* — funcționalitate adăugată dinamic
- *„selecția specificului culinar nu conduce la o modificare a prețului de bază"* — obiectul de bază rămâne intact
- *„clienții pot comanda și produsele de bază, fără vreo modificare"* — decoratorul e opțional
- *„să permită adăugarea de noi specificuri culinare din alte regiuni"* — extensibil fără modificare cod

**Regula:** „se adaugă funcționalitate opțională unui obiect existent", „fără modificarea clasei de bază", „extensibil cu noi variante" → **Decorator**

---

## Pattern 2: Composite — 9p

**Indicatori în cerință:**
- *„meniurile zilei care sunt formate din mai multe componente de tip produs"* — container care conține elemente de același tip
- *„arborescența care definește meniul restaurantului"* — structură arborescentă
- *„pentru fiecare produs de tip meniul zilei sau produs, clientul poate afla prețul"* — interfață comună pentru frunze și noduri

**Regula:** „componentă formată din alte componente de același tip", „structură ierarhică", „operație aplicată uniform pe tot arborele" → **Composite**
