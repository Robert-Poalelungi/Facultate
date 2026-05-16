package composite.implementare;

public interface IProdus {
    String getDenumireProdus();
    int getTotalProduse();
    void afisare();

    void addProdus(IProdus produs);
    void removeProdus(IProdus produs);
    IProdus getProdus(int index);
}
