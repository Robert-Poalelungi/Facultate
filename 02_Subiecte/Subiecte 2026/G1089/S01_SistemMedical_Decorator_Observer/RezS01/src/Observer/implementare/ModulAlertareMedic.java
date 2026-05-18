package Observer.implementare;

public class ModulAlertareMedic implements AbstractModulNotificare{
    @Override
    public void actualizeaza(String mesaj) {
        System.out.println("Alertare medic " + mesaj);
    }
}
