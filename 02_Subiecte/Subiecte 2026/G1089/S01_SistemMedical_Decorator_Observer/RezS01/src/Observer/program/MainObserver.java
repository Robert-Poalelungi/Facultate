import Observer.implementare.*;

void main() {
    Pacient pacient = new Pacient("Robert", "Buna");

    AbstractModulNotificare istoric = new ModulIstoric();
    AbstractModulNotificare alertareMedic = new ModulAlertareMedic();
    AbstractModulNotificare notificarePacient = new ModulNotificariPacient();
    AbstractModulNotificare programari = new ModulProgramari();

    pacient.adaugaModul(istoric);
    pacient.adaugaModul(alertareMedic);
    pacient.adaugaModul(notificarePacient);
    pacient.adaugaModul(programari);


    pacient.setStare(" critica");
    System.out.println("--------------------------------------");


    pacient.eliminaModul(istoric);
    pacient.setStare("Stabila");
}