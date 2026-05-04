# Decorator — Ghid complet

## Ce este?

Un pattern **structural** care adaugă funcționalitate unui obiect **dinamic**, fără să modifice clasa lui
și fără moștenire.

Decoratorul „împachetează" obiectul original și adaugă comportament înainte sau după apelul original.
Poți stivui mai mulți decoratori: `D2(D1(obiectOriginal))`.

---

## Când se folosește?

- Vrei să adaugi funcționalitate fără să modifici clasa existentă
- Vrei combinații flexibile (ex: pizza cu N toppinguri diferite)
- Moștenirea ar produce explozie de subclase (PizzaCuJambon, PizzaCuJambonSiCiuperci, etc.)

---

## Participanți

| Rol | Responsabilitate |
|-----|-----------------|
| **Component** (interfață/abstract) | interfața comună |
| **ConcreteComponent** | obiectul de bază care se decorează |
| **Decorator abstract** | implementează Component, ține referința la Component |
| **ConcreteDecorator** | adaugă funcționalitatea specifică |

---

## Structura

```
«interface»
 IComponent
    ↑
    │  implements
    │
APizza ←────────────── ADecoratorPizza
(abstract)              (abstract, ține referința la APizza)
    ↑                        ↑
PizzaVegetariana       DecoratorJambon
                       DecoratorCiuperci
```

---

## Implementare pas cu pas

### Pasul 1 — Componentul abstract (sau interfață)

Definește contractul comun. Toate clasele (de bază și decoratori) îl respectă.

```java
public abstract class APizza {
    public abstract String getDenumire();
    public abstract double getPret();

    // metodă concretă care folosește cele abstracte
    public String getInfo() {
        return getDenumire() + " - " + getPret() + " RON";
    }
}
```

---

### Pasul 2 — Componentul concret (obiectul de bază)

Pizza simplă, fără decoratori.

```java
public class PizzaVegetariana extends APizza {
    @Override
    public String getDenumire() {
        return "Pizza Vegetariana";
    }

    @Override
    public double getPret() {
        return 20.0;
    }
}
```

---

### Pasul 3 — Decoratorul abstract

**Cheia pattern-ului**: extinde `APizza` (e tot o pizza) și ține o referință la altă `APizza`
(obiectul pe care îl decorează).

```java
public abstract class ADecoratorPizza extends APizza {
    // referința la obiectul decorat (poate fi PizzaVegetariana sau alt decorator)
    private APizza pizzaDecorata;

    public ADecoratorPizza(APizza pizzaDecorata) {
        this.pizzaDecorata = pizzaDecorata;
    }

    // delegă la obiectul decorat — subclasele pot suprascrie și adăuga
    @Override
    public String getDenumire() {
        return pizzaDecorata.getDenumire();
    }

    @Override
    public double getPret() {
        return pizzaDecorata.getPret();
    }
}
```

> **De ce extinde APizza?**
> Ca decoratorul să fie interschimbabil cu obiectul decorat — poți
> decora un decorator cu alt decorator: `D2(D1(pizza))`.

---

### Pasul 4 — Decoratori concreți

Fiecare adaugă propria funcționalitate și apelează `super` pentru rest.

```java
public class DecoratorJambon extends ADecoratorPizza {
    public DecoratorJambon(APizza pizza) {
        super(pizza);
    }

    @Override
    public String getDenumire() {
        return super.getDenumire() + ", Jambon";   // adaugă la ce era deja
    }

    @Override
    public double getPret() {
        return super.getPret() + 5.0;              // adaugă la prețul existent
    }
}

public class DecoratorCiuperci extends ADecoratorPizza {
    public DecoratorCiuperci(APizza pizza) {
        super(pizza);
    }

    @Override
    public String getDenumire() {
        return super.getDenumire() + ", Ciuperci";
    }

    @Override
    public double getPret() {
        return super.getPret() + 3.0;
    }
}

public class DecoratorPicant extends ADecoratorPizza {
    public DecoratorPicant(APizza pizza) {
        super(pizza);
    }

    @Override
    public String getDenumire() {
        return super.getDenumire() + ", Sos Picant";
    }

    @Override
    public double getPret() {
        return super.getPret() + 2.0;
    }
}
```

---

### Pasul 5 — Construiește în Main

Decoratorii se stivuiesc: fiecare primește în constructor obiectul anterior.

```java
public class Main {
    public static void main(String[] args) {
        // pizza simplă
        APizza pizza = new PizzaVegetariana();
        System.out.println(pizza.getInfo());
        // → Pizza Vegetariana - 20.0 RON

        // adaugă jambon
        pizza = new DecoratorJambon(pizza);
        System.out.println(pizza.getInfo());
        // → Pizza Vegetariana, Jambon - 25.0 RON

        // adaugă ciuperci peste
        pizza = new DecoratorCiuperci(pizza);
        System.out.println(pizza.getInfo());
        // → Pizza Vegetariana, Jambon, Ciuperci - 28.0 RON

        // adaugă sos picant
        pizza = new DecoratorPicant(pizza);
        System.out.println(pizza.getInfo());
        // → Pizza Vegetariana, Jambon, Ciuperci, Sos Picant - 30.0 RON

        // sau totul dintr-un apel
        APizza alta = new DecoratorPicant(new DecoratorJambon(new PizzaVegetariana()));
        System.out.println(alta.getInfo());
        // → Pizza Vegetariana, Jambon, Sos Picant - 27.0 RON
    }
}
```

---

## Cum funcționează apelul `getPret()`?

Urmărește cascada de apeluri:

```
pizza.getPret()                      // DecoratorPicant
  → super.getPret() + 2             // = DecoratorCiuperci.getPret() + 2
  → super.getPret() + 3             // = DecoratorJambon.getPret() + 3
  → super.getPret() + 5             // = PizzaVegetariana.getPret() + 5
  → 20.0 + 5 + 3 + 2 = 30.0
```

Fiecare decorator adaugă la valoarea precedentă — asta e recursivitatea implicită.

---

## Cum recunoști problema la examen

Cuvinte cheie în enunț:
- „toppinguri", „opțiuni suplimentare", „extras"
- „prețul crește cu fiecare adăugire"
- „combinații flexibile"
- „fără să modifici clasa de bază"

**Structura răspunsului la examen:**
1. Clasă abstractă `AComponenta` cu metodele comune
2. Clasă concretă de bază (`PizzaVegetariana`) extinde `AComponenta`
3. Decorator abstract `ADecorator` extinde `AComponenta` și ține `private AComponenta decorat`
4. Decoratori concreți extind `ADecorator`, suprascriau metodele cu `super.metoda() + adaos`
5. `Main` stivuiește decoratori: `new D2(new D1(new Base()))`
