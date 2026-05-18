import Command.implementare.*;

void main() {
    Comanda comanda1 = new Comanda("Robert", "Paste");
    Comanda comanda2 = new Comanda("Viorel", "Pizza");

    ManagerComenzi manager = new ManagerComenzi();

    manager.adaugaActiune(new ActiuneAnuleaza(comanda2));
    manager.adaugaActiune(new ActiuneSalveaza(comanda1));
    manager.adaugaActiune(new ActiuneTrimite(comanda1));
    manager.adaugaActiune(new ActiuneRepeta(comanda1));

    manager.executaActiuni();
}
