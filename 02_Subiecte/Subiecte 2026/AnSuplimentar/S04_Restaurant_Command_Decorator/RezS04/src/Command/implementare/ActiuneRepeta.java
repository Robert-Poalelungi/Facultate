package Command.implementare;

public class ActiuneRepeta implements AbstractActiuneComanda{
    private Comanda comanda;

    public ActiuneRepeta(Comanda comanda) {
        this.comanda = comanda;
    }

    @Override
    public void executa() {
        comanda.repeta();
    }
}
