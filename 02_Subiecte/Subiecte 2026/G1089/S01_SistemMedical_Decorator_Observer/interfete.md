```java
public interface AbstractFisaMedicala {
    String genereazaDescriere();
    double calculeazaCostProcesare();
}
```

```java
public interface AbstractPacientMonitorizat {
    void adaugaModul(AbstractModulNotificare modul);
    void eliminaModul(AbstractModulNotificare modul);
    void notificaModule();
}
```

```java
public interface AbstractModulNotificare {
    void actualizeaza(String mesaj);
}
```
