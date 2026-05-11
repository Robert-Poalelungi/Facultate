# S05 — Bancomat | CoR + Strategy

## Pattern 1: Chain of Responsibility — 5p

**Indicatori în cerință:**
- *„bancnote de 50, 20 și 10 lei"* — fiecare tip de bancnotă = un handler
- *„să permită adăugarea de noi tipuri de bancnote cu minim de modificare de cod"* — lanț extensibil
- *„posibilitatea de a schimba ordinea de preluare a bancnotelor"* — ordinea handlerilor se poate schimba
- Dacă handlerul curent nu poate satisface cererea, pasează mai departe

**Regula:** procesare secvențială prin tipuri ordonate, ordine schimbabilă, extensibil → **Chain of Responsibility**

---

## Pattern 2: Strategy — 5p

**Indicatori în cerință:**
- *„clientul are posibilitatea de a alege tipul de bancnote dorite sau toate tipurile"* — comportament ales la runtime
- Două variante: alegere personalizată (citită de la tastatură) vs. toate tipurile

**Regula:** „clientul alege modul de funcționare" → **Strategy**
