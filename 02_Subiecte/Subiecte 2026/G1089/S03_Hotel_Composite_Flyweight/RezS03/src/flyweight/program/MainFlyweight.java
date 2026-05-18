import flyweight.implementare.AbstractPictogramaFacilitate;
import flyweight.implementare.PictogramaFacilitate;
import flyweight.implementare.PictogramaFactory;

void main() {
    AbstractPictogramaFacilitate wifi1 = PictogramaFactory.getPictograma("wifi");
    AbstractPictogramaFacilitate wifi2 = PictogramaFactory.getPictograma("wifi");
    AbstractPictogramaFacilitate wifi3 = PictogramaFactory.getPictograma("wifi");
    AbstractPictogramaFacilitate parcare = PictogramaFactory.getPictograma("parcare");
    AbstractPictogramaFacilitate piscina = PictogramaFactory.getPictograma("piscina");

    wifi1.afiseaza(10, 23, "Wifi Gratuit");
    wifi2.afiseaza(50, 30, "WiFi camera 101");
    wifi3.afiseaza(80, 40, "WiFi lobby");
    parcare.afiseaza(15, 60, "Parcare subterana");
    piscina.afiseaza(25, 70, "Piscina etaj 2");

    System.out.println("wifi1 == wifi2 " + (wifi1 == wifi2));
    System.out.println("wifi1 == wifi3 " + (wifi1 == wifi3));

    System.out.println("Instante create cu Flyweight: " + PictogramaFactory.getNrInstante()); // 3

}



