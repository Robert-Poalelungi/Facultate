package strategy.implementare;

public class AlgoritmCostMinim implements AbstractAlgoritmRuta{
    @Override
    public Ruta calculeazaRuta(ReteaTransport retea, String statieStart, String statieFinal) {
        Ruta rutaOptima = null;
        for (int i = 0; i < retea.getRuta().size(); i++) {
            Ruta ruta = retea.getRuta().get(i);
            if (ruta.getStatieStart().equals(statieStart) && ruta.getStatieFinal().equals(statieFinal)){
                if (rutaOptima == null || ruta.getCost() < rutaOptima.getCost()){
                    rutaOptima = ruta;
                }
            }
        }

        if (rutaOptima == null){
            System.out.println("Ruta dintre statia de inceputi si final nu exista");
        }else{
            System.out.println("Ruta optima etst: " + rutaOptima);
        }

        return rutaOptima;
    }
}
