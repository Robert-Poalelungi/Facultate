public class VerificatorGradIndatorare extends AVerificator {
    private static final double GRAD_MAX = 0.40;

    @Override
    public boolean verifica(Persoana p, double suma, int luni) {
        double rataLunara = suma / luni;
        double gradIndatorare = rataLunara / p.getVenitLunar();
        if (gradIndatorare > GRAD_MAX) {
            System.out.printf("Respins GradIndatorare: %.1f%% > %.0f%%%n", gradIndatorare * 100, GRAD_MAX * 100);
            return false;
        }
        System.out.printf("GradIndatorare: OK (%.1f%%)%n", gradIndatorare * 100);
        return pasezaMailDeparte(p, suma, luni);
    }
}
