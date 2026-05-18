package Observer.implementare;

import java.util.ArrayList;
import java.util.List;

public class Pacient implements AbstractPacientMonitorizat{
    private String numePacient;
    private String stare;
    private List<AbstractModulNotificare> module = new ArrayList<>();

    public Pacient(String numePacient, String stare) {
        this.numePacient = numePacient;
        this.stare = stare;
    }

    public void setStare(String stare) {
        this.stare = stare;
        notificaModule();
    }

    @Override
    public void adaugaModul(AbstractModulNotificare modul) {
        module.add(modul);
    }

    @Override
    public void eliminaModul(AbstractModulNotificare modul) {
        module.remove(modul);
    }

    @Override
    public void notificaModule() {
        for (AbstractModulNotificare modul : module){
            modul.actualizeaza(stare);
        }
    }
}
