package Decorator.implementare;

public class DecoratorBranza extends DecoratorAbstract{
    private double pretBranza;

    public DecoratorBranza(AbstractProdusRestaurant produs, double pretBranza) {
        super(produs);
        this.pretBranza = pretBranza;
    }

    @Override
    public String obtineDescriere() {
        return super.obtineDescriere() + " Branza ";
    }

    @Override
    public double calculeazaPret() {
        return super.calculeazaPret() + pretBranza;
    }
}
