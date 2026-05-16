import proxy.implementare.IMagazin;
import proxy.implementare.Magazin;
import proxy.implementare.ProxyMagazin;

void main() {
    IMagazin magazin = new ProxyMagazin(new Magazin("Magazin 1"));

    magazin.calculeazaTotal("Robert", 200, "Galati");
    magazin.calculeazaTotal("Viorel", 200, "Bucuresti");
    magazin.calculeazaTotal("Viorel", 100, "Bucuresti");
}
