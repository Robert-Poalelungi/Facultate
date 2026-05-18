package composite.implementare;

import java.util.ArrayList;
import java.util.List;

public class Etaj implements Hotel {
    private int nrEtaj;
    private List<Hotel> apartamente = new ArrayList<>();

    public Etaj(int nrEtaj) {
        this.nrEtaj = nrEtaj;
    }

    @Override
    public void addNod(Hotel nod) {
        apartamente.add(nod);
    }

    @Override
    public void removeNod(Hotel nod) {
        apartamente.remove(nod);
    }

    @Override
    public Hotel getNod(int index) {
        return apartamente.get(index);
    }

    @Override
    public void afiseazaDescriere() {
        System.out.println("Etajul cu numarul " + nrEtaj + " are un numar de cemere: " + apartamente.size());
        for (Hotel apartament : apartamente){
            apartament.afiseazaDescriere();
        }
    }

    @Override
    public double calculeazaTarif() {
        double tarifTotal = 0;
        for (Hotel apartament : apartamente){
            tarifTotal += apartament.calculeazaTarif();
        }
        return tarifTotal;
    }
}
