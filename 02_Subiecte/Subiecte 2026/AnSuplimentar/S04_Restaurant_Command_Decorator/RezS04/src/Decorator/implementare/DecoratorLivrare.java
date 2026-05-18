package Decorator.implementare;

public class DecoratorLivrare extends DecoratorAbstract{
    private double pretLivrare;

    public DecoratorLivrare(AbstractProdusRestaurant produs, double pretLivrare) {
        super(produs);
        this.pretLivrare = pretLivrare;
    }

    @Override
    public String obtineDescriere() {
        return super.obtineDescriere() + " Livrare ";
    }

    @Override
    public double calculeazaPret() {
        return super.calculeazaPret() + pretLivrare;
    }
}
