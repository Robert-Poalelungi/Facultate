package Decorator.implementare;

public class DecoratorAmbalaj extends DecoratorAbstract{
    private double pretAmbalaj;

    public DecoratorAmbalaj(AbstractProdusRestaurant produs, double pretAmbalaj) {
        super(produs);
        this.pretAmbalaj = pretAmbalaj;
    }

    @Override
    public String obtineDescriere() {
        return super.obtineDescriere() + " Ambalaj ";
    }

    @Override
    public double calculeazaPret() {
        return super.calculeazaPret() + pretAmbalaj;
    }
}
