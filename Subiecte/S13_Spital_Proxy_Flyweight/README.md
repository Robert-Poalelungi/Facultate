# S13 — Spital | Proxy + Flyweight

## Pattern 1: Proxy — 5p

**Indicatori în cerință:**
- *„managementul spitalului a restricționat accesul... doar vizitatorilor care dețin certificat verde"* — control acces
- *„modul intermediar ce gestionează noile restricții"* — „intermediar" = Proxy
- Accesul real în spital nu se modifică — Proxy-ul verifică certificatul înainte

**Regula:** „modul intermediar", „restricție de acces adăugată fără modificarea clasei existente" → **Proxy**

---

## Pattern 2: Flyweight — 9p

**Indicatori în cerință:**
- *„există un număr limitat de diagnostice în comparație cu numărul mare de rețete ce se tipăresc"* — obiect partajat între mulți
- *„modul ce optimizează spațiul de memorie ocupat privind listarea recomandărilor"* — Flyweight = optimizare memorie
- Seturile de recomandări sunt puține și se reutilizează la multe rețete

**Regula:** „număr limitat de obiecte reutilizate de un număr mare de instanțe", „optimizare memorie" → **Flyweight**
