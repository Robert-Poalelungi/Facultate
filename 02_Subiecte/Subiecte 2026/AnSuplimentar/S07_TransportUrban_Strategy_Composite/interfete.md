```java
public interface AbstractAlgoritmRuta {
    Ruta calculeazaRuta(ReteaTransport retea, String statieStart, String statieFinal);
}
```

```java
public interface AbstractElementTransport {
    int calculeazaNumarPasageri();
    boolean verificaCapacitate(int capacitateMaxima);
}
```
