package strategy.implementare;

public class StrategyContext{
    private AbstractAlgoritmRuta algoritmRuta;

    public StrategyContext setAlgoritmRuta(AbstractAlgoritmRuta algoritmRuta) {
        this.algoritmRuta = algoritmRuta;
        return this;
    }

    public Ruta calculeazaRuta(ReteaTransport retea, String statieStart, String statieFinal) {
        return algoritmRuta.calculeazaRuta(retea, statieStart, statieFinal);
    }
}
