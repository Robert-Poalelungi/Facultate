public abstract class AComponenta {
    public abstract String getNume();
    public abstract double getSalariuTotal();
    public abstract int getNrAngajati();
    public abstract void afiseaza(String indent);

    public void adauga(AComponenta c) { throw new UnsupportedOperationException(); }
    public void elimina(AComponenta c) { throw new UnsupportedOperationException(); }
}
