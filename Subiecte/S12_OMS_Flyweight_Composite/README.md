# S12 — OMS | Flyweight + Composite

## Pattern 1: Flyweight — 5p

**Indicatori în cerință:**
- *„stochează la un nivel centralizat toate virusurile unice identificate de-a lungul timpului"* — obiect unic partajat
- *„regăsirea pe baza unei amprente a virusului"* — identificator unic pentru obiectul partajat
- „unice" = un singur obiect per tip de virus, refolosit

**Regula:** „stocare centralizată a obiectelor unice", „număr limitat de obiecte reutilizate de multe ori", „optimizare memorie" → **Flyweight**

---

## Pattern 2: Composite — 9p

**Indicatori în cerință:**
- *„gestionarea și prezentarea arborescentă a tulpinilor de virusuri existente în fiecare țară din fiecare continent"* — ierarhie continente → țări → tulpini
- *„afișarea numărului total de cazuri identificate în toate țările"* — operație agregată recursiv
- *„interfața Virus"* — interfață comună pentru toate nivelurile

**Regula:** „structură ierarhică pe niveluri", „agregare recursivă de rezultate" → **Composite**
