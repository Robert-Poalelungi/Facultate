import composite.implementare.Apartament;
import composite.implementare.Camera;
import composite.implementare.Etaj;
import composite.implementare.Hotel;

void main() {

    Hotel etaj1 = new Etaj(1);
    Hotel apartament101 = new Apartament("Apartamentul 101");
    apartament101.addNod(new Camera(1, "dubla", 250));
    apartament101.addNod(new Camera(2, "simpla", 150));

    etaj1.addNod(apartament101);
    etaj1.addNod(new Apartament("Apartamentul 102"));
    etaj1.addNod(new Apartament("Apartamentul 103"));

    etaj1.afiseazaDescriere();
    System.out.println("Tarif total etaj: " + etaj1.calculeazaTarif());
}
