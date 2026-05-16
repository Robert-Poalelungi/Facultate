# S03 — Magazin Pantofi | Builder

## Pattern: Builder — 7p

**Indicatori în cerință:**
- *„creare personalizată de pantofi unicat, clienții își parametrizează pantofii"* — obiect complex cu opțiuni
- *„fiecare cerere trebuie să conțină obligatoriu tipul pantofului, numărul, dimensiunea tocului și tipul de material de bază"* — câmpuri obligatorii
- *„suplimentar... set de materiale secundare... și o listă de mesaje text"* — câmpuri opționale
- *„magazinul nu permite ca cererile odată lansate să poată fi modificabile"* — imutabil după build = Builder

**Regula:** ori de câte ori cerința spune „parametrizare flexibilă a unui obiect complex", „câmpuri obligatorii și opționale", „obiect imutabil după creare" → **Builder**

**Structura minimă:**
```
CerereComandaPantofi (imutabilă — doar getteri)
  └── CerereComandaPantofi.Builder
        ├── Builder(TipPantof tip, int numar, double toc, String materialBaza)  // obligatorii
        ├── withMaterialeSecundare(List<String>)   // opțional
        ├── withMesejeText(List<String>)            // opțional
        └── build()  // validare restricții + construire
```
