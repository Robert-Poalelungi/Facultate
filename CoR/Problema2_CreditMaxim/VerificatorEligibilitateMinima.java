public class VerificatorEligibilitateMinima extends ALimitator {
    private static final int SCOR_MINIM = 500;
    private static final int VECHIME_MINIMA_LUNI = 6;

    @Override
    public double calculeaza(Persoana p, int luni, double sumaMaxima) throws CreditRefuzatException {
        if (p.getSCorCredit() < SCOR_MINIM)
            throw new CreditRefuzatException("scor credit prea mic: " + p.getSCorCredit());
        if (p.getVechimeLuni() < VECHIME_MINIMA_LUNI)
            throw new CreditRefuzatException("vechime insuficienta: " + p.getVechimeLuni() + " luni");
        System.out.println("EligibilitateMinima: OK");
        return pasezaMailDeparte(p, luni, sumaMaxima);
    }
}
