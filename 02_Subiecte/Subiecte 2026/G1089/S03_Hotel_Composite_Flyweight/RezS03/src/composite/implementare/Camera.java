package composite.implementare;

public class Camera implements Hotel {
    private int numar;
    private String tip;
    private double tarif;

    public Camera(int numar, String tip, double tarif) {
        this.numar = numar;
        this.tip = tip;
        this.tarif = tarif;
    }

    @Override
    public void addNod(Hotel nod) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void removeNod(Hotel nod) {
        throw new UnsupportedOperationException();

    }

    @Override
    public Hotel getNod(int index) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void afiseazaDescriere() {
        System.out.println("Camera cu numarul " + numar + " de tipul " + tip + " are un tarif de " + tarif);
    }

    @Override
    public double calculeazaTarif() {
        return tarif;
    }
}
