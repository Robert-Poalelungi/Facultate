package composite.implementare;

import java.util.ArrayList;
import java.util.List;

public class NodTransport implements INod{
    private String denumire;
    private List<INod> statii;

    public NodTransport(String denumire) {
        this.denumire = denumire;
        this.statii = new ArrayList<>();
    }

    @Override
    public void addNod(INod nod) {
        statii.add(nod);
    }

    @Override
    public void removeNod(INod nod) {
statii.remove(nod);
    }

    @Override
    public INod getNod(int index) {
        return statii.get(index);
    }

    @Override
    public int calculeazaNumarPasageri() {
        int total = 0;
        for (INod nod : statii) {
            total += nod.calculeazaNumarPasageri();
        }
        return total;
    }

    @Override
    public boolean verificaCapacitate(int capacitateMaxima) {
        return calculeazaNumarPasageri() <= capacitateMaxima;
    }
}
