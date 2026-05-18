package Command.implementare;

public class Comanda {
    private String numeClient;
    private String produs;

    public Comanda(String numeClient, String produs) {
        this.numeClient = numeClient;
        this.produs = produs;
    }

    public void trimite(){
        System.out.println("Comanda lui: " + numeClient + " are urmatorul produs " + produs);
    }

    public void anuleaza(){
        System.out.println("Comanda lui: " + numeClient + " a fost anulata");
    }

    public void repeta(){
        System.out.println("Comanda lui: " + numeClient + " este repetata");
    }

    public void salvataPentruProcesare(){
        System.out.println("Comanda lui: " + numeClient + " a fost salvata pentru procesare");
    }
}
