# S03 — Aplicație Web | Strategy + CoR

## Pattern 1: Strategy — 5p

**Indicatori în cerință:**
- *„utilizatorul are opțiunea de a selecta tehnica de vizualizare"* — comportament interschimbabil ales la runtime
- *„se pot adăuga noi tehnici de vizualizare în timp"* — extensibil fără modificare cod existent
- Variantele: ordine crescătoare preț / descrescătoare / doar cu recenzii — algoritmi interșanjabili

**Regula:** ori de câte ori cerința spune „utilizatorul poate alege între X, Y, Z moduri de a face ceva", „se pot adăuga noi variante în timp" → **Strategy**

---

## Pattern 2: Chain of Responsibility — 9p

**Indicatori în cerință:**
- *„filtrarea este formată din mai multe etape"* — lanț de procesare
- *„etapele pot fi interschimbate"* — ordinea handlerilor se poate schimba
- *„se pot adăuga filtrări suplimentare"* — lanțul e extensibil
- Fiecare etapă procesează și pasează mai departe

**Regula:** ori de câte ori cerința spune „mai multe etape de procesare înlănțuite", „ordinea poate fi schimbată", „se pot adăuga etape noi" → **Chain of Responsibility**
