# S05 — Management de Proiecte | Observer + Adapter

## Pattern 1: Observer — 3p

**Indicatori în cerință:**
- *„mai multe componente trebuie notificate atunci când starea unei sarcini se schimbă"* — notificare automată la schimbare
- *„modulele pot fi adăugate sau eliminate dinamic"* — abonare/dezabonare
- *„fără modificarea clasei care gestionează sarcina"* — subiectul delegă notificarea, nu o hardcodează

**Regula:** ori de câte ori cerința spune „notificare automată la schimbare de stare", „componente care ascultă", „adăugare/eliminare dinamică de ascultători" → **Observer**

---

## Pattern 2: Adapter — 3p

**Indicatori în cerință:**
- *„importarea sarcinilor dintr-o aplicație externă de tip task manager"* — sistem extern incompatibil
- *„folosește descriere, nivel textual de urgență și dată în alt format"* — structură diferită față de intern
- *„integrarea sarcinilor externe în fluxul intern de planificare fără modificarea clasei externe"* — Adapter

**Regula:** ori de câte ori cerința spune „integrare fără modificarea clasei externe", „format diferit de la sistem extern", „același planificator pentru sarcini interne și externe" → **Adapter**
