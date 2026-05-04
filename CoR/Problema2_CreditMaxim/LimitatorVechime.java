public class LimitatorVechime extends ALimitator {
    // vechime max considerata: 120 luni (10 ani) = multiplicator 1.0
    private static final int VECHIME_MAX = 120;

    @Override
    public double calculeaza(Persoana p, int luni, double sumaMaxima) throws CreditRefuzatException {
        double multiplicator = Math.min(1.0, (double) p.getVechimeLuni() / VECHIME_MAX);
        double sumaAjustata = sumaMaxima * multiplicator;
        System.out.printf("LimitatorVechime: suma redusa la %.2f (vechime %d luni)%n", sumaAjustata, p.getVechimeLuni());
        return pasezaMailDeparte(p, luni, sumaAjustata);
    }
}
