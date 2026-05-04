public class VerificatorVechime extends AVerificator {
    private static final int VECHIME_MINIMA_LUNI = 12;

    @Override
    public boolean verifica(Persoana p, double suma, int luni) {
        if (p.getVechimeLuni() < VECHIME_MINIMA_LUNI) {
            System.out.println("Respins Vechime: " + p.getVechimeLuni() + " luni < " + VECHIME_MINIMA_LUNI);
            return false;
        }
        System.out.println("Vechime: OK (" + p.getVechimeLuni() + " luni)");
        return pasezaMailDeparte(p, suma, luni);
    }
}
