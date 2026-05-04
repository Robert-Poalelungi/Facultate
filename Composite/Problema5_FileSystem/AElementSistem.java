public abstract class AElementSistem {
    public abstract String getNume();
    public abstract double getDimensiune();
    public abstract void afiseaza(String indent);
    public abstract AElementSistem cauta(String numeCautat);

    public void adauga(AElementSistem e) { throw new UnsupportedOperationException(); }
    public void sterge(AElementSistem e) { throw new UnsupportedOperationException(); }
}
