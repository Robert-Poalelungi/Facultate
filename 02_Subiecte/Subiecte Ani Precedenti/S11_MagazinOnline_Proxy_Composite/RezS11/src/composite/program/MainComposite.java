import composite.implementare.Categorie;
import composite.implementare.IProdus;
import composite.implementare.Produs;

void main() {
    IProdus magazin = new Categorie("Magazin Online");

    IProdus electronice = new Categorie("Electronice");
    IProdus haine = new Categorie("Haine");

    IProdus telefoane = new Categorie("Telefoane");
    telefoane.addProdus(new Produs("iPhone 16 pro", 12));
    telefoane.addProdus(new Produs("iPhone 13 pro", 2));

    electronice.addProdus(telefoane);
    electronice.addProdus(new Produs("Laptop Lenovo", 4));

    haine.addProdus(new Produs("Tricou", 20));
    haine.addProdus(new Produs("Pantaloni", 15));

    magazin.addProdus(electronice);
    magazin.addProdus(haine);

    magazin.afisare();
}