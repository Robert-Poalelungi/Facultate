public class Fisier extends AElementSistem {
    private String nume;
    private double dimensiune;

    public Fisier(String nume, double dimensiune) {
        this.nume = nume;
        this.dimensiune = dimensiune;
    }

    @Override
    public String getNume() { return nume; }

    @Override
    public double getDimensiune() { return dimensiune; }

    @Override
    public void afiseaza(String indent) {
        System.out.printf("%s- %s (%.1f KB)%n", indent, nume, dimensiune);
    }

    @Override
    public AElementSistem cauta(String numeCautat) {
        return this.nume.equals(numeCautat) ? this : null;
    }
}
