# S07 — Sistem de Transport Urban | Strategy + Composite

## Pattern 1: Strategy — 3p

**Indicatori în cerință:**
- *„utilizatorul poate alege criteriul de optimizare: timp minim, număr minim de stații, cost minim, schimbări minime"* — algoritmi interschimbabili
- *„algoritmul utilizat trebuie să poată fi schimbat la rulare"* — definiția Strategy
- Aceeași rețea de transport, algoritm diferit → rezultate diferite

**Regula:** ori de câte ori cerința spune „algoritm schimbabil la rulare", „mai multe variante de calcul/comportament pentru același input", „alegerea strategiei de către utilizator" → **Strategy**

---

## Pattern 2: Composite — 3p

**Indicatori în cerință:**
- *„o stație simplă... un nod de transport poate conține stații simple, peroane sau alte noduri"* — structură arborescentă
- *„calcularea recursivă a numărului total de pasageri"* — calcul recursiv pe arbore
- *„stații și grupuri de stații reprezentate uniform"* — interfață unică pentru frunze și noduri compuse

**Regula:** ori de câte ori cerința spune „element simplu și element compus tratate uniform", „calcul recursiv pe o structură ierarhică", „nod care poate conține alte noduri de același tip" → **Composite**
