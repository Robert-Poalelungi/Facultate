package Observer.implementare;

public interface AbstractPacientMonitorizat {
    void adaugaModul(AbstractModulNotificare modul);
    void eliminaModul(AbstractModulNotificare modul);
    void notificaModule();
}