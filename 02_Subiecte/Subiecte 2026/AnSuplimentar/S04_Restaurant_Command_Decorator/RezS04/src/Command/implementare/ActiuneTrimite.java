package Command.implementare;

public class ActiuneTrimite implements AbstractActiuneComanda{
    private Comanda comanda;

    public ActiuneTrimite(Comanda comanda) {
        this.comanda = comanda;
    }

    @Override
    public void executa() {
        comanda.trimite();
    }
}
