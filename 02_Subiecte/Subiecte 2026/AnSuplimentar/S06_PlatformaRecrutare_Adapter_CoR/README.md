# S06 — Platformă de Recrutare | Adapter + Chain of Responsibility

## Pattern 1: Adapter — 3p

**Indicatori în cerință:**
- *„CV-uri în formate diferite de la mai mulți furnizori externi"* — structuri incompatibile
- *„fără modificarea clasei externe și fără schimbarea codului care procesează candidații interni"* — Adapter clasic
- *„același evaluator pentru ambele cazuri"* — interfață unificată

**Regula:** ori de câte ori cerința spune „integrare fără modificarea clasei externe", „format diferit de la parteneri/sisteme externe", „același tip de referință pentru obiecte incompatibile" → **Adapter**

---

## Pattern 2: Chain of Responsibility — 3p

**Indicatori în cerință:**
- *„filtreze succesiv candidații după mai multe criterii"* — fiecare handler procesează și pasează mai departe
- *„fiecare filtru decide dacă un candidat este respins sau transmis către următorul"* — definiția CoR
- *„ordinea filtrelor trebuie să poată fi schimbată ușor"* — lanțul e reconfigurabil

**Regula:** ori de câte ori cerința spune „procesare succesivă prin filtre/handlere", „fiecare handler decide dacă oprește sau pasează", „ordine reconfigurabilă" → **Chain of Responsibility**
