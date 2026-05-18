package composite.implementare;

import java.util.ArrayList;
import java.util.List;

public class Apartament implements Hotel {
    private String denumire;
    private List<Hotel> camere = new ArrayList<>();

    public Apartament(String denumire) {
        this.denumire = denumire;
    }

    @Override
    public void addNod(Hotel nod) {
        camere.add(nod);
    }

    @Override
    public void removeNod(Hotel nod) {
        camere.remove(nod);
    }

    @Override
    public Hotel getNod(int index) {
        return camere.get(index);
    }

    @Override
    public void afiseazaDescriere() {
        System.out.println("Apartamentul " + denumire + " are un numar de camere: " + camere.size() + " si are un tarif de " + calculeazaTarif());
        for (Hotel camera : camere){
            camera.afiseazaDescriere();
        }
    }

    @Override
    public double calculeazaTarif() {
        double tarifTotal = 0;
        for (Hotel camera : camere){
            tarifTotal += camera.calculeazaTarif();
        }
        return tarifTotal;
    }
}
