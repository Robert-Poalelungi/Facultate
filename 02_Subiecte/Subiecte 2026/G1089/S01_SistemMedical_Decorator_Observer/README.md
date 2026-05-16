# S01 — Sistem Medical Digital | Decorator + Observer

## Pattern 1: Decorator — 3p

**Indicatori în cerință:**
- *„fișa trebuie extinsă cu informații suplimentare"* — se adaugă comportament peste un obiect existent
- *„adăugarea succesivă a mai multor extensii externe"* — învelire strat cu strat, nu arbore
- *„fără modificarea clasei de bază"* — obiectul original rămâne intact, decoratorul îl împachetează

**Regula:** ori de câte ori cerința spune „opțiuni adăugate dinamic", „combinare liberă de extensii", „adăugare succesivă" peste un obiect → **Decorator** (nu Composite — Composite e pentru arbori de obiecte uniforme, nu pentru adăugare de comportament)

---

## Pattern 2: Observer — 3p

**Indicatori în cerință:**
- *„mai multe module care trebuie notificate atunci când se actualizează starea unui pacient"*
- *„modulele pot fi adăugate sau eliminate dinamic"* — abonare/dezabonare
- *„fără modificarea clasei care gestionează pacientul"* — subiectul nu știe concret cine ascultă

**Regula:** ori de câte ori cerința spune „notificare automată la schimbare de stare", „module care ascultă", „adăugare/eliminare dinamică de ascultători" → **Observer**
