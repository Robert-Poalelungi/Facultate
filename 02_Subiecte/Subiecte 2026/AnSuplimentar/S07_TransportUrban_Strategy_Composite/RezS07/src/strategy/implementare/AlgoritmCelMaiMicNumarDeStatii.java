package strategy.implementare;

public class AlgoritmCelMaiMicNumarDeStatii implements AbstractAlgoritmRuta{
    @Override
    public Ruta calculeazaRuta(ReteaTransport retea, String statieStart, String statieFinal) {
        Ruta rutaOptima = null;
        for (int i = 0; i < retea.getRuta().size(); i++) {
            Ruta ruta = retea.getRuta().get(i);
            if (ruta.getStatieStart().equals(statieStart) && ruta.getStatieFinal().equals(statieFinal)){
                if (rutaOptima == null || ruta.getNrStatii() < rutaOptima.getNrStatii()){
                    rutaOptima = ruta;
                }
            }
        }

        if (rutaOptima == null){
            System.out.println("Nu exista ruta intre " + statieStart + " si " + statieFinal);
        }else{
            System.out.println("Ruta optima: " + rutaOptima);
        }

        return rutaOptima;
    }
}
