# S05 — Magazin | Singleton

## Pattern: Singleton — 4p + 2p

**Indicatori în cerință:**
- *„restricționată deținerea în același timp a mai multor comenzi în desfășurare"* — o singură instanță activă
- *„unica comandă în curs de desfășurare"* — cuvântul „unică" = Singleton
- *„se dorește extinderea... prin posibilitatea de a permite existența a două case de marcat"* — pool limitat de instanțe = Multiton (Singleton generalizat)
- Thread safety necesară: „simularea procesului... folosind două fire de execuție diferite"

**Regula:** ori de câte ori cerința spune „o singură instanță", „unic în aplicație", „acces global controlat" → **Singleton**. Dacă numărul de instanțe e limitat dar > 1 → **Multiton** (variație a Singleton cu pool)

**Structura minimă:**
```
// Singleton clasic (1 instanță):
CasaMarcat implements AbstractCasaMarcat {
    private static CasaMarcat instanta;
    private CasaMarcat() {}
    public static synchronized CasaMarcat getInstanta() {
        if (instanta == null) instanta = new CasaMarcat();
        return instanta;
    }
}

// Multiton (2 instanțe):
CasaMarcat {
    private static final int MAX = 2;
    private static Map<Integer, CasaMarcat> pool = new HashMap<>();
    public static synchronized CasaMarcat getInstanta(int id) {
        if (id < 1 || id > MAX) throw new RuntimeException(...);
        pool.putIfAbsent(id, new CasaMarcat());
        return pool.get(id);
    }
}
```
