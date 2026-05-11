# S08 — Spital | Template Method + Flyweight

## Pattern 1: Template Method — 5p

**Indicatori în cerință:**
- *„protocol general valabil format dintr-un număr fix de pași"* — algoritm fix cu pași definiți
- *„Acest protocol este folosit și de spitalele private, însă în acest caz... echipă externă"* — același algoritm, un pas diferit
- Spital stat vs. privat: pași comuni (verificare semne vitale, loc internare) + pas diferit (echipă internă vs. externă)

**Regula:** „număr fix de pași", „unii pași sunt identici, alții diferă între variante" → **Template Method**

---

## Pattern 2: Flyweight — 9p

**Indicatori în cerință:**
- *„există un număr limitat de seturi de recomandări generale în comparație cu numărul mare de rețete"* — obiect partajat între mulți
- *„modul ce optimizează spațiul de memorie ocupat"* — Flyweight = optimizare memorie prin partajare
- Recomandările sunt aceleași pentru multe rețete → se partajează, nu se duplică

**Regula:** „număr mic de obiecte reutilizate de un număr mare de instanțe", „optimizare memorie", „stare intrinsecă partajată" → **Flyweight**
