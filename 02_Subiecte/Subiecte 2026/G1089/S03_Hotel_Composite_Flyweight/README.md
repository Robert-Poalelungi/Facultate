# S03 — Management Hotelier | Composite + Flyweight

## Pattern 1: Composite — 3p

**Indicatori în cerință:**
- *„o cameră simplă are un număr de paturi, un apartament poate conține mai multe camere simple și apartamente"* — structură arborescentă
- *„gruparea lor în apartamente și etaje"* — nod compus din noduri
- *„calcularea tarifului total pentru o structură complexă"* — calcul recursiv pe arbore

**Regula:** ori de câte ori cerința spune „element simplu și element compus tratate uniform", „calcul recursiv pe o structură ierarhică", „grupare în noduri care conțin alte noduri" → **Composite**

---

## Pattern 2: Flyweight — 3p

**Indicatori în cerință:**
- *„pictogramele apar în multe locuri: pagina camerei, emailuri, panouri"* — același obiect folosit în contexte multiple
- *„resursele grafice sunt mari, se dorește reutilizarea obiectelor comune"* — partajarea stării intrinseci
- *„transmiterea separată a informațiilor variabile: poziție, dimensiune, etichetă"* — stare extrinsecă separată

**Regula:** ori de câte ori cerința spune „obiecte costisitoare reutilizate în mai multe locuri", „stare partajată + informații variabile transmise separat", „reducerea numărului de instanțe create" → **Flyweight**
