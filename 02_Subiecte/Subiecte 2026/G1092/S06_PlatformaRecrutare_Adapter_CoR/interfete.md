```java
public interface AbstractCandidatPlatforma {
    String obtineNume();
    int obtineAniExperienta();
    String[] obtineCompetente();
}
```

```java
public abstract class AbstractFiltruCandidat {
    protected AbstractFiltruCandidat urmator;

    public void seteazaUrmator(AbstractFiltruCandidat urmator) {
        this.urmator = urmator;
    }

    public abstract boolean proceseaza(Candidat candidat);
}
```
