package Observer.implementare;

public class ModulIstoric implements AbstractModulNotificare{
    @Override
    public void actualizeaza(String mesaj) {
        System.out.println("Istoric" + mesaj);
    }
}
