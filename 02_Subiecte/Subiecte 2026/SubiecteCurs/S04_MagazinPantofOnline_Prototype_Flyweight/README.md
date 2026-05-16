# S04 — Magazin Pantofi Online | Prototype + Flyweight

## Pattern 1: Prototype — 7p (parțial)

**Indicatori în cerință:**
- *„în funcție de fiecare stil de pantof ales, perechea se personalizează cu mesaje text predefinite... set de mesaje diferă de la un stil la altul"* — există template per stil (prototip)
- *„clientul are posibilitatea ulterior să își modifice propria listă"* — copie independentă care poate fi modificată, originalul rămâne intact

**Regula:** ori de câte ori cerința spune „template predefinit per tip/categorie", „copie independentă modificabilă", „fiecare instanță pornește de la un prototip" → **Prototype**

---

## Pattern 2: Flyweight — 7p (parțial)

**Indicatori în cerință:**
- *„lista de mesaje se găsește într-o bază de date și s-a observat că timpul de încărcare a acestei liste pentru fiecare pantof este foarte mare"* — obiect costisitor de creat
- Aceeași listă de mesaje per stil este partajată între toți pantofii de același stil — stare intrinsecă
- Informațiile variabile per pantof (număr, client) = stare extrinsecă

**Regula:** ori de câte ori cerința spune „timp mare de încărcare/creare", „același obiect costisitor reutilizat în mai multe contexte", „stare partajată + informații variabile separate" → **Flyweight**
