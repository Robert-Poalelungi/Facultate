public class Angajat extends AComponenta {
    private String nume;
    private double salariu;

    public Angajat(String nume, double salariu) {
        this.nume = nume;
        this.salariu = salariu;
    }

    @Override
    public String getNume() { return nume; }

    @Override
    public double getSalariuTotal() { return salariu; }

    @Override
    public int getNrAngajati() { return 1; }

    @Override
    public void afiseaza(String indent) {
        System.out.printf("%s- %s (%.0f RON)%n", indent, nume, salariu);
    }
}
