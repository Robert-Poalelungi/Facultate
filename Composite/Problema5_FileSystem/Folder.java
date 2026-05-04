import java.util.ArrayList;
import java.util.List;

public class Folder extends AElementSistem {
    private String nume;
    private List<AElementSistem> elemente = new ArrayList<>();

    public Folder(String nume) {
        this.nume = nume;
    }

    @Override
    public void adauga(AElementSistem e) { elemente.add(e); }

    @Override
    public void sterge(AElementSistem e) { elemente.remove(e); }

    @Override
    public String getNume() { return nume; }

    @Override
    public double getDimensiune() {
        double total = 0;
        for (AElementSistem e : elemente)
            total += e.getDimensiune();
        return total;
    }

    @Override
    public void afiseaza(String indent) {
        System.out.println(indent + "[" + nume + "]");
        for (AElementSistem e : elemente)
            e.afiseaza(indent + "  ");
    }

    @Override
    public AElementSistem cauta(String numeCautat) {
        if (this.nume.equals(numeCautat)) return this;
        for (AElementSistem e : elemente) {
            AElementSistem gasit = e.cauta(numeCautat);
            if (gasit != null) return gasit;
        }
        return null;
    }
}
