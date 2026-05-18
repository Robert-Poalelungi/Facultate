package Observer.implementare;

public class ModulNotificariPacient implements AbstractModulNotificare{
    @Override
    public void actualizeaza(String mesaj) {
        System.out.println("Notificari pacient" + mesaj);
    }
}
