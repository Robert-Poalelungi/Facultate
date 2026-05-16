# S01 — Mall | Builder

## Pattern: Builder — 7p

**Indicatori în cerință:**
- *„customizabil prin posibilitatea de parametrizare a componentelor obiectului complex magazin"* — obiect complex cu câmpuri obligatorii și opționale
- *„fiecare magazin are obligatoriu o denumire, suprafață și număr de intrări"* — parametri obligatorii = câmpuri fără default în Builder
- *„dacă nu se dorește adăugarea unui tip de podea specială... dacă nu se parametrizează numărul de intrări"* — parametri opționali cu valori default = metodele opționale din Builder
- *„implementarea nu trebuie să permită modificări pe magazinele create"* — obiect imutabil = Builder (nu setter-e pe clasa finală)

**Regula:** ori de câte ori cerința spune „parametrizare flexibilă a unui obiect complex", „câmpuri obligatorii și opționale", „obiect imutabil după creare", „nu permite modificări" → **Builder**

**Structura minimă:**
```
Magazin (clasa finală, imutabilă — doar getteri, fără setteri)
  └── Magazin.Builder (clasă internă statică)
        ├── Builder(String denumire, double suprafata, int nrIntrari)  // obligatorii
        ├── withPodea(Podea podea)       // opțional
        ├── withDecorațiuni(List<...>)   // opțional
        └── build()                      // validare restricții + construire
```
