import composite.implementare.INod;
import composite.implementare.NodTransport;
import composite.implementare.Statie;

void main() {
    INod retea = new NodTransport("Reteaua de Nord");

    INod zonaCentrala = new NodTransport("Zona Centrala");
    zonaCentrala.addNod(new Statie(500,"Statia Unirii"));
    zonaCentrala.addNod(new Statie(300,"Statia Victoriei"));

    INod zonaVest = new NodTransport("Zona Vest");
    zonaVest.addNod(new Statie(400,"Statia Garii"));
    zonaVest.addNod(new Statie(200,"Statia Drumul Taberei"));

    retea.addNod(zonaCentrala);
    retea.addNod(zonaVest);

    System.out.println("Total pasageri: " + retea.calculeazaNumarPasageri());
    System.out.println("Capacitate ok (2000)? " + retea.verificaCapacitate(2000));
    System.out.println("Capacitate ok (500)? " + retea.verificaCapacitate(500));}