```java
public interface AbstractAngajat {
    String getNume();
}
```

```java
public interface AbstractCasaMarcat {
    void deschideComanda(AbstractAngajat angajat);
    void inchideComanda(AbstractAngajat angajat);
    void adaugaProdus(String denumireProdus);
    void showInfoComanda();
}
```
