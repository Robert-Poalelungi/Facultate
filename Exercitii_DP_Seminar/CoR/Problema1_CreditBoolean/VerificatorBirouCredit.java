public class VerificatorBirouCredit extends AVerificator {
    private static final int SCOR_MINIM = 600;

    @Override
    public boolean verifica(Persoana p, double suma, int luni) {
        if (p.getSCorCredit() < SCOR_MINIM) {
            System.out.println("Respins BirouCredit: scor " + p.getSCorCredit() + " < " + SCOR_MINIM);
            return false;
        }
        System.out.println("BirouCredit: OK (scor " + p.getSCorCredit() + ")");
        return pasezaMailDeparte(p, suma, luni);
    }
}
