# S02 — Platformă E-Learning | Adapter + Proxy

## Pattern 1: Adapter — 3p

**Indicatori în cerință:**
- *„materiale provenite din surse externe... au o structură diferită"* — interfață incompatibilă
- *„fără modificarea claselor externe"* — clasa adaptată rămâne intactă
- *„să poată fi utilizate ca și cum ar respecta formatul intern"* — obiect extern tratat ca intern

**Regula:** ori de câte ori cerința spune „integrare fără modificarea clasei externe", „format diferit de la parteneri/sisteme externe", „același tip de referință pentru obiecte incompatibile" → **Adapter**

---

## Pattern 2: Proxy — 3p

**Indicatori în cerință:**
- *„obiect intermediar care verifică permisiunile înainte de accesarea cursului real"* — cuvântul „intermediar" = Proxy
- *„acces controlat în funcție de tipul utilizatorului"* — Proxy de protecție
- Cursul real nu se modifică — Proxy-ul acționează în fața lui

**Regula:** ori de câte ori cerința spune „obiect intermediar", „control acces", „verificare înainte de delegare către obiectul real" → **Proxy**
