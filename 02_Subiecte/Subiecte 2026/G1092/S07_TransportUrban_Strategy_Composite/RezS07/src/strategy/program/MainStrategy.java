import strategy.implementare.*;

void main() {
    Ruta r1 = new Ruta("Galati", "Bucuresti", 4, 120,4);
    Ruta r3 = new Ruta("Galati", "Bucuresti", 2, 140,3);
    Ruta r4 = new Ruta("Galati", "Bucuresti", 2, 110,2);
    Ruta r2 = new Ruta("Galati", "Braila", 1, 12,1);

    ReteaTransport reteaTransport = new ReteaTransport();
    reteaTransport.adaugaRuta(r1);
    reteaTransport.adaugaRuta(r2);
    reteaTransport.adaugaRuta(r3);
    reteaTransport.adaugaRuta(r4);

    StrategyContext context = new StrategyContext();
    context.setAlgoritmRuta(new AlgoritmTimpMinim());
    context.calculeazaRuta(reteaTransport,"Galati", "Bucuresti");
}
