package composite.implementare;

import java.util.ArrayList;
import java.util.List;

public class Categorie implements IProdus{
    private String denumire;
    private List<IProdus> produse;

    public Categorie(String denumire) {
        this.denumire = denumire;
        this.produse = new ArrayList<>();
    }

    @Override
    public String getDenumireProdus() {
        return denumire;
    }

    @Override
    public int getTotalProduse() {
        int totalProduse = 0;
        for (IProdus produs:produse){
            totalProduse += produs.getTotalProduse();
        }
        return totalProduse;
    }

    @Override
    public void afisare() {
        System.out.println("Categoria: " + denumire + "\nTotal produse: " + getTotalProduse());
        for (IProdus produs : produse){
            produs.afisare();
        }
    }

    @Override
    public void addProdus(IProdus produs) {
        produse.add(produs);
    }

    @Override
    public void removeProdus(IProdus produs) {
        produse.remove(produs);
    }

    @Override
    public IProdus getProdus(int index) {
        return produse.get(index);
    }
}
