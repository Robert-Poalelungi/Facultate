package strategy.implementare;

public class Ruta {
    private String statieStart;
    private String statieFinal;
    private int nrStatii;
    private double cost;
    private int durata;

    public Ruta(String statieStart, String statieFinal, int nrStatii, double cost, int durata) {
        this.statieStart = statieStart;
        this.statieFinal = statieFinal;
        this.nrStatii = nrStatii;
        this.cost = cost;
        this.durata = durata;
    }

    public String getStatieStart() {
        return statieStart;
    }

    public String getStatieFinal() {
        return statieFinal;
    }

    public int getNrStatii() {
        return nrStatii;
    }

    public double getCost() {
        return cost;
    }

    public int getDurata() {
        return durata;
    }

    @Override
    public String toString() {
        return "Ruta{" +
                "statieStart='" + statieStart + '\'' +
                ", getStatieFinal='" + statieFinal + '\'' +
                ", nrStatii=" + nrStatii +
                ", cost=" + cost +
                ", durata=" + durata +
                '}';
    }
}
