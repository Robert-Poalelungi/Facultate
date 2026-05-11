# S01 — Spital | Proxy + Memento

## Pattern 1: Proxy — 5p

**Indicatori în cerință:**
- *„s-a restricționat numărul de vizitatori"* — se adaugă un strat intermediar care controlează accesul
- *„modul intermediar ce gestionează noile restricții"* — cuvântul „intermediar" = Proxy
- Accesul real (intrarea în salon) nu se modifică — Proxy-ul acționează în fața obiectului real

**Regula:** ori de câte ori cerința spune „modul intermediar", „fără a modifica clasa existentă", „control acces" → **Proxy**

---

## Pattern 2: Memento — 9p

**Indicatori în cerință:**
- *„revenirea într-o singură stare anterioară... pe care utilizatorul o poate alege în orice moment"*
- *„utilizatorul poate stoca o versiune anterioară"*
- Se salvează starea unui obiect și se poate restaura ulterior

**Regula:** ori de câte ori cerința spune „revenire la stare anterioară", „salvare stare", „undo" → **Memento**
