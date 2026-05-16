# S04 — Aplicație Restaurant | Command + Decorator

## Pattern 1: Command — 3p

**Indicatori în cerință:**
- *„fiecare acțiune să fie reprezentată printr-un obiect separat"* — definiția Command
- *„acțiunile să poată fi stocate, executate ulterior sau combinate în liste"* — queue de comenzi
- *„salvarea mai multor acțiuni într-o listă și executarea lor succesivă"* — batch execution

**Regula:** ori de câte ori cerința spune „acțiune ca obiect", „stocare și executare ulterioară", „undo/redo", „liste de operații" → **Command**

---

## Pattern 2: Decorator — 3p

**Indicatori în cerință:**
- *„un produs de bază poate primi opțiuni suplimentare"* — adăugare de comportament
- *„fără crearea unei clase separate pentru fiecare combinație posibilă"* — explozie combinatorială evitată prin învelire
- *„combinate liber"* — orice ordine și număr de decoratori

**Regula:** ori de câte ori cerința spune „opțiuni adăugate dinamic peste un obiect de bază", „combinare liberă fără explozie de clase", „același tip de referință înainte și după adăugare" → **Decorator**
