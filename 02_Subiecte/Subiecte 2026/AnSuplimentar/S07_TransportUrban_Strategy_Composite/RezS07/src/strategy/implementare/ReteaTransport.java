package strategy.implementare;

import java.util.ArrayList;
import java.util.List;

public class ReteaTransport {
    private List<Ruta> rute;

    public ReteaTransport() {
        this.rute = new ArrayList<>();
    }

    public void adaugaRuta(Ruta ruta){
        rute.add(ruta);
    }

    public void stergeRuta(Ruta ruta){
        rute.remove(ruta);
    }

    public List<Ruta> getRuta(){
        return rute;
    }
}
