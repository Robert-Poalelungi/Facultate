package Command.implementare;

public class ActiuneAnuleaza implements AbstractActiuneComanda{
    private Comanda comanda;

    public ActiuneAnuleaza(Comanda comanda) {
        this.comanda = comanda;
    }

    @Override
    public void executa() {
        comanda.anuleaza();
    }
}
