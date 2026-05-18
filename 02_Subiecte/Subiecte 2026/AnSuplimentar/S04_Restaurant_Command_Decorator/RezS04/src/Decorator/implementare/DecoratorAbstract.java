package Decorator.implementare;

public abstract class DecoratorAbstract implements AbstractProdusRestaurant{
    private AbstractProdusRestaurant produs;

    public DecoratorAbstract(AbstractProdusRestaurant produs) {
        this.produs = produs;
    }

    @Override
    public String obtineDescriere() {
        return produs.obtineDescriere();
    }

    @Override
    public double calculeazaPret() {
        return produs.calculeazaPret();
    }
}
