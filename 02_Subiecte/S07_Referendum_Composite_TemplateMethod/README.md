# S07 — Referendum | Composite + Template Method

## Pattern 1: Composite — 5p

**Indicatori în cerință:**
- *„voturile sunt înregistrate la nivel de secții de votare, iar secțiile sunt încadrate în județe"* — ierarhie parte-întreg
- *„să se afișeze centralizat rezultatul referendumului"* — operație propagată recursiv în sus
- *„interfața AbstractRezultat"* — interfață comună pentru secții și județe

**Regula:** „structură ierarhică cu agregare de rezultate pe niveluri" → **Composite**

---

## Pattern 2: Template Method — 5p

**Indicatori în cerință:**
- *„procedura este aceeași pentru toate persoanele, însă unele etape pot fi diferite în funcție de secția de votare (străinătate sau în țară)"* — algoritm comun cu pași variabili
- *„interfața AbstractVotare... să se construiască un șablon cu sens în care unii pași sunt aceiași iar alții diferă"* — șablon = Template Method
- Spital de stat vs. privat urmează același protocol dar cu pași diferiți

**Regula:** „pași comuni + pași care diferă între variante", „șablon de algoritm", „Abstract... cu metode suprascrise" → **Template Method**
