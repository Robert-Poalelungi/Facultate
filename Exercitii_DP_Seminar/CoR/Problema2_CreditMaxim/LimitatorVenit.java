public class LimitatorVenit extends ALimitator {
    private static final double GRAD_MAX = 0.40;

    @Override
    public double calculeaza(Persoana p, int luni, double sumaMaxima) throws CreditRefuzatException {
        double rataMaxima = p.getVenitLunar() * GRAD_MAX;
        double sumaMaxDinVenit = rataMaxima * luni;
        double sumaAjustata = Math.min(sumaMaxima, sumaMaxDinVenit);
        System.out.printf("LimitatorVenit: suma redusa la %.2f (rata max %.2f/luna)%n", sumaAjustata, rataMaxima);
        return pasezaMailDeparte(p, luni, sumaAjustata);
    }
}
