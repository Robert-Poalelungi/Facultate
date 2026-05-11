# S14 — Magazin Online | Proxy + Memento

## Pattern 1: Proxy — 5p

**Indicatori în cerință:**
- *„modul securizat de autentificare... implementarea securizată nu trebuie să implice modificări la nivelul actualului modul"* — adăugare comportament fără modificare cod existent
- *„modul intermediar"* între client și modulul de autentificare real
- Proxy-ul adaugă logica de blocare (5 parole greșite) transparent

**Regula:** „nu trebuie să implice modificări la nivelul actualului modul", „strat de securitate adăugat transparent" → **Proxy**

---

## Pattern 2: Memento — 5p

**Indicatori în cerință:**
- *„posibilitatea de a reveni într-o stare anterioară a unei comenzi"* — restaurare stare salvată
- *„fiecare client poate stoca o singură versiune de coș de cumpărături"* — salvare stare (snapshot)
- *„reseta coșul curent pe baza coșului anterior salvat"* — restore din snapshot

**Regula:** „revenire la stare anterioară", „salvare snapshot al unui obiect", „undo" → **Memento**
