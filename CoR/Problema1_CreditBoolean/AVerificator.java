public abstract class AVerificator {
    private AVerificator urmator;

    public AVerificator setUrmator(AVerificator urmator) {
        this.urmator = urmator;
        return urmator;
    }

    protected boolean pasezaMailDeparte(Persoana p, double suma, int luni) {
        if (urmator != null)
            return urmator.verifica(p, suma, luni);
        return true;
    }

    public abstract boolean verifica(Persoana p, double suma, int luni);
}
