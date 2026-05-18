package flyweight.implementare;

public class PictogramaFacilitate implements AbstractPictogramaFacilitate{
    private String tip;

    public PictogramaFacilitate(String tip) {
        this.tip = tip;
    }

    @Override
    public void afiseaza(int x, int y, String eticheta) {
        System.out.println("Pictograma " + tip
                        + " se afla la pozaita x: "
                + x + " si y: " + y + " si are eticheta " + eticheta
        );
    }
}
