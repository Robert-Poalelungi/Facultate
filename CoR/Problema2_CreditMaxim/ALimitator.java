public abstract class ALimitator {
    private ALimitator urmator;

    public ALimitator setUrmator(ALimitator urmator) {
        this.urmator = urmator;
        return urmator;
    }

    protected double pasezaMailDeparte(Persoana p, int luni, double sumaMaxima) throws CreditRefuzatException {
        if (urmator != null)
            return urmator.calculeaza(p, luni, sumaMaxima);
        return sumaMaxima;
    }

    public abstract double calculeaza(Persoana p, int luni, double sumaMaxima) throws CreditRefuzatException;
}
