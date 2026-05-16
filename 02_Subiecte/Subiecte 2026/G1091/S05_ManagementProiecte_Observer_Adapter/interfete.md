```java
public interface AbstractSarcinaMonitorizata {
    void adaugaListener(AbstractModulProiect modul);
    void eliminaListener(AbstractModulProiect modul);
    void notificaModule();
}
```

```java
public interface AbstractModulProiect {
    void actualizeaza(String stareNoua);
}
```

```java
public interface AbstractSarcinaInterna {
    String obtineTitlu();
    int obtinePrioritate();
    LocalDate obtineTermenLimita();
}
```
