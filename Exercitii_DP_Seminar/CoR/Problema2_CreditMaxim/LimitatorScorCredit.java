public class LimitatorScorCredit extends ALimitator {
    // scor intre 500 (min) si 850 (max)
    private static final int SCOR_MIN = 500;
    private static final int SCOR_MAX = 850;

    @Override
    public double calculeaza(Persoana p, int luni, double sumaMaxima) throws CreditRefuzatException {
        double multiplicator = (double)(p.getSCorCredit() - SCOR_MIN) / (SCOR_MAX - SCOR_MIN);
        multiplicator = Math.max(0.5, Math.min(1.0, multiplicator));
        double sumaAjustata = sumaMaxima * multiplicator;
        System.out.printf("LimitatorScorCredit: suma ajustata la %.2f (scor %d)%n", sumaAjustata, p.getSCorCredit());
        return pasezaMailDeparte(p, luni, sumaAjustata);
    }
}
