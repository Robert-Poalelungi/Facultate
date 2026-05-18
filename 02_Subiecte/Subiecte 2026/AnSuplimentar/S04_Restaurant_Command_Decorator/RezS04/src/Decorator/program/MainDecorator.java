import Decorator.implementare.*;

void main() {
    AbstractProdusRestaurant produsRestaurant = new Produs("Pizza", 30);

    produsRestaurant = new DecoratorAmbalaj(produsRestaurant, 5);
    produsRestaurant = new DecoratorLivrare(produsRestaurant, 15);
    produsRestaurant = new DecoratorBranza(produsRestaurant, 7);

    System.out.println(produsRestaurant.obtineDescriere());
    System.out.println(produsRestaurant.calculeazaPret());
}