package Decorator.implementare;

public class Produs implements AbstractProdusRestaurant{
    private String denumireProdus;
    private double pretBaza;

    public Produs(String denumireProdus, double pretBaza) {
        this.denumireProdus = denumireProdus;
        this.pretBaza = pretBaza;
    }

    @Override
    public String obtineDescriere() {
        return denumireProdus;
    }

    @Override
    public double calculeazaPret() {
        return pretBaza;
    }
}
