package Observer.implementare;

public class ModulProgramari implements AbstractModulNotificare{
    @Override
    public void actualizeaza(String mesaj) {
        System.out.println("Programari " + mesaj);
    }
}
