package proxy.implementare;

public class Magazin implements IMagazin{
    private String denumire;

    public Magazin(String denumire) {
        this.denumire = denumire;
    }

    @Override
    public double calculeazaTotal(String client, double totalCos, String adresa) {
       double transport;
        if (adresa.equalsIgnoreCase("Galati")){
            transport = 0;
        }else{
            transport = 25;
        }
        double total = totalCos + transport;
        System.out.println(
                client
                + "\nTotal cos: "
                + totalCos + "\ntransport: "
                + transport + "\nTotal cu transport:"
                + total + "\n------------------------------------");

        return total;
    }

}
