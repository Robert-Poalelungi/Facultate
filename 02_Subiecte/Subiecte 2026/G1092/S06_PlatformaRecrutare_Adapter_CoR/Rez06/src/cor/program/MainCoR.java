import cor.implementare.*;

void main() {
    AbstractFiltruCandidat competente = new FiltrareCandidatCompetente();
    AbstractFiltruCandidat experienta = new FiltrareCandidatExperienta(2);
    AbstractFiltruCandidat disponibilitate = new FiltruCandidatDisponibilitateInterviu();
    AbstractFiltruCandidat salariu = new FiltruCandidatSalariu(8000);

    Candidat candidat1 = new Candidat("Robert", 2, true, true, 7000);
    Candidat candidat2 = new Candidat("Viorel", 1, true, true, 7000);
    Candidat candidat3 = new Candidat("Andrei", 4, false, true, 7000);
    Candidat candidat4 = new Candidat("Ion", 10, true, true, 9000);

    competente.seteazaUrmator(experienta);
    experienta.seteazaUrmator(disponibilitate);
    disponibilitate.seteazaUrmator(salariu);


    competente.proceseaza(candidat1);
    competente.proceseaza(candidat2);
    competente.proceseaza(candidat3);
    competente.proceseaza(candidat4);

    salariu.seteazaUrmator(experienta);
}