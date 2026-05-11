# S02 — Restaurant | Composite + Memento

## Pattern 1: Composite — 5p

**Indicatori în cerință:**
- *„pachet format din: interfețe, clase, metode, funcții"* — structură ierarhică parte-întreg
- *„parsare recursivă a codului"* — traversare recursivă = Composite
- *„analiza tuturor elementelor de tip Item"* — interfață comună pentru frunze și noduri

**Regula:** ori de câte ori cerința spune „structură arborescentă", „parsare recursivă", „componentă formată din alte componente de același tip" → **Composite**

---

## Pattern 2: Memento — 5p

**Indicatori în cerință:**
- *„afișarea... pe baza versiunii anterioare de afișare"* — revenire la o stare anterioară
- Se salvează o versiune a afișării și se poate restaura

**Regula:** ori de câte ori cerința spune „versiune anterioară", „revenire la stare salvată", „undo" → **Memento**
