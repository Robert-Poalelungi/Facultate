package composite.implementare;

public class Statie implements INod{
    private String denumire;
    private int nrPasageri;

    public Statie(int nrPasageri, String denumire) {
        this.nrPasageri = nrPasageri;
        this.denumire = denumire;
    }

    @Override
    public void addNod(INod nod) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void removeNod(INod nod) {
        throw new UnsupportedOperationException();

    }

    @Override
    public INod getNod(int index) {
        throw new UnsupportedOperationException();
    }

    @Override
    public int calculeazaNumarPasageri() {
        return nrPasageri;
    }

    @Override
    public boolean verificaCapacitate(int capacitateMaxima) {
        throw new UnsupportedOperationException();
    }
}
