# S02 — Club Sportiv | Prototype + Observer

## Pattern 1: Prototype — 7p (parțial)

**Indicatori în cerință:**
- *„procesul de înregistrare a unui nou jucător implică un consum mare de timp"* — creare costisitoare
- *„pentru fiecare sportiv nou, există un set predefinit de antrenamente... și o listă de medicamente interzise"* — există un template/prototip per tip de jucător
- *„fiecare jucător își poate actualiza propria listă de antrenamente"* — copie independentă, nu referință la original

**Regula:** ori de câte ori cerința spune „creare costisitoare", „set predefinit copiat pentru fiecare instanță nouă", „modificare independentă față de original" → **Prototype**

**Structura minimă:**
```
AbstractJucator implements Cloneable
  ├── Portar extends AbstractJucator
  ├── Atacant extends AbstractJucator
  └── Mijlocas extends AbstractJucator

RegistruJucatori — Map<TipJucator, AbstractJucator> prototipuri
  └── inregistreazaJucator(tip) → prototip.clone()
```

---

## Pattern 2: Observer — 7p (parțial)

**Indicatori în cerință:**
- *„dacă un jucător depistează un nou tip de medicament interzis, atunci toți jucătorii trebuie să cunoască această observație nouă"* — notificare automată la toți
- Jucătorii sunt atât subiect (când ei descoperă) cât și observatori (când alții descoperă)

**Regula:** ori de câte ori cerința spune „toți trebuie notificați la o schimbare", „propagare automată a informației" → **Observer**
