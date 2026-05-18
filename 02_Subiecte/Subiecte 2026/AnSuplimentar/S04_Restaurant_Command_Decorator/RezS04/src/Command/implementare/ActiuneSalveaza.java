package Command.implementare;

public class ActiuneSalveaza implements AbstractActiuneComanda{
    private Comanda comanda;

    public ActiuneSalveaza(Comanda comanda) {
        this.comanda = comanda;
    }

    @Override
    public void executa() {
        comanda.salvataPentruProcesare();
    }
}
