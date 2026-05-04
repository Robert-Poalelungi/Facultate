public class Persoana {
    private String nume;
    private double venitLunar;
    private int vechimeLuni;
    private int scorCredit;

    public Persoana(String nume, double venitLunar, int vechimeLuni, int scorCredit) {
        this.nume = nume;
        this.venitLunar = venitLunar;
        this.vechimeLuni = vechimeLuni;
        this.scorCredit = scorCredit;
    }

    public String getNume() { return nume; }
    public double getVenitLunar() { return venitLunar; }
    public int getVechimeLuni() { return vechimeLuni; }
    public int getSCorCredit() { return scorCredit; }
}
