# S04 — Magazin Pantofi Online | CoR + Strategy

## Pattern 1: Chain of Responsibility — 5p

**Indicatori în cerință:**
- *„modul de filtrare a produselor în funcție de criterii de selecție"* — filtrare în lanț
- *„să permită extinderea prin adăugarea de noi criterii"* — lanț extensibil
- *„posibilitatea de rearanjare a ordinii de aplicare a criteriilor"* — ordinea handlerilor se poate schimba
- *„dacă un client nu parametrizează un criteriu, nu se ține cont de acesta"* — handlerul se sare

**Regula:** filtrare în mai mulți pași, ordine schimbabilă, pași opționali → **Chain of Responsibility**

---

## Pattern 2: Strategy — 5p

**Indicatori în cerință:**
- *„clientul poate alege între parametrizare implicită sau setarea proprie a parametrilor"* — comportament ales la runtime
- Două variante de comportament interschimbabile: implicit vs. custom

**Regula:** „clientul alege între mai multe moduri de a face același lucru" → **Strategy**
