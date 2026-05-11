# Facade

Pattern **structural** — o singură clasă simplifică accesul la un subsistem complex cu mai multe clase. Clientul interacționează doar cu Facade-ul.

---

## Participanți

| Rol | Descriere |
|-----|-----------|
| Clase subsistem | clase cu logică complexă, independente între ele |
| `Facade` | orchestrează subsistemul, expune metode simple |
| Client | apelează doar Facade, nu știe de subsistem |

---

## Structură generală

```java
// Clase subsistem (complexe, independente)
public class SubsistemA {
    public void operatieA() { System.out.println("Subsistem A"); }
}

public class SubsistemB {
    public void operatieB() { System.out.println("Subsistem B"); }
}

public class SubsistemC {
    public void operatieC() { System.out.println("Subsistem C"); }
}

// Facade — orchestrează subsistemul
public class Facade {
    private SubsistemA a = new SubsistemA();
    private SubsistemB b = new SubsistemB();
    private SubsistemC c = new SubsistemC();

    public void operatieComplexaSimplificata() {
        a.operatieA();
        b.operatieB();
        c.operatieC();
    }
}

// Main — clientul apelează doar Facade
Facade facade = new Facade();
facade.operatieComplexaSimplificata();
```

---

## Structura la examen

1. **Clase subsistem** — fiecare face un lucru specific (ex. `CheckInventar`, `ProcessarePlata`, `TrimitereFact`)
2. **Facade** — câmpuri private pentru fiecare subsistem, metodă publică simplificată care le orchestrează
3. **Main** — `new Facade().metodaSimplificata()`

---

## Cum recunoști

- „un singur punct de intrare", „simplifică accesul la mai multe module"
- „clientul nu trebuie să cunoască detaliile interne"
- Mai multe subsisteme care trebuie coordonate împreună

---

## Diferența față de Adapter

- **Facade**: simplifică mai multe clase existente
- **Adapter**: face o clasă incompatibilă să respecte o interfață cerută
