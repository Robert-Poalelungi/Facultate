# S10 — OMS | Proxy + Composite

## Pattern 1: Proxy — 5p

**Indicatori în cerință:**
- *„modul intermediar ce permite accesul în saloane conform noilor restricții"* — „intermediar" = Proxy
- *„implementarea trebuie să țină cont de interfața ISpital primită"* — Proxy implementează aceeași interfață
- Accesul real (intrarea în salon) nu se modifică — Proxy-ul adaugă verificări înainte

**Regula:** „modul intermediar", „fără modificarea clasei existente", „adăugare verificări/restricții înainte de acces" → **Proxy**

---

## Pattern 2: Composite — 9p

**Indicatori în cerință:**
- *„gestionarea și prezentarea arborescentă a tulpinilor de virusuri"* — structură arborescentă
- *„continente → țări → tulpini"* — ierarhie pe niveluri cu același tip de operație
- *„afișarea numărului total de cazuri din cadrul arborescenței"* — operație propagată recursiv

**Regula:** „structură ierarhică cu niveluri", „operație aplicată uniform pe tot arborele" → **Composite**
