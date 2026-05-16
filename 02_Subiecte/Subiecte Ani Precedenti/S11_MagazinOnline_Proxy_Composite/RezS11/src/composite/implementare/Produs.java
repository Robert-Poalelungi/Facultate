package composite.implementare;

public class Produs implements IProdus{
    private String denumire;
    private int numarBucati;

    public Produs(String denumire, int numarBucati) {
        this.denumire = denumire;
        this.numarBucati = numarBucati;
    }

    @Override
    public String getDenumireProdus() {
        return denumire;
    }

    @Override
    public int getTotalProduse() {
        return numarBucati;
    }

    @Override
    public void afisare() {
        System.out.println("Produsul: " + denumire + "\nNumar bucati: " + getTotalProduse());
    }

    @Override
    public void addProdus(IProdus produs) {
        throw new RuntimeException("Produsul nu are copii!!!");
    }

    @Override
    public void removeProdus(IProdus produs) {
        throw new RuntimeException("Produsul nu are copii!!!");

    }

    @Override
    public IProdus getProdus(int index) {
        throw new RuntimeException("Produsul nu are copii!!!");
    }
}
