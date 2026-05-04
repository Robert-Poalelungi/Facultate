import java.util.ArrayList;
import java.util.List;

public class Departament extends AComponenta {
    private String nume;
    private List<AComponenta> subordonati = new ArrayList<>();

    public Departament(String nume) {
        this.nume = nume;
    }

    @Override
    public void adauga(AComponenta c) { subordonati.add(c); }

    @Override
    public void elimina(AComponenta c) { subordonati.remove(c); }

    @Override
    public String getNume() { return nume; }

    @Override
    public double getSalariuTotal() {
        double total = 0;
        for (AComponenta c : subordonati)
            total += c.getSalariuTotal();
        return total;
    }

    @Override
    public int getNrAngajati() {
        int total = 0;
        for (AComponenta c : subordonati)
            total += c.getNrAngajati();
        return total;
    }

    @Override
    public void afiseaza(String indent) {
        System.out.println(indent + "[" + nume + "]");
        for (AComponenta c : subordonati)
            c.afiseaza(indent + "  ");
    }
}
