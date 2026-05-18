import adapter.implementare.AbstractCandidatPlatforma;
import adapter.implementare.AdapterCvExtern;
import adapter.implementare.CvExtern;
import adapter.implementare.CvIntern;

void main() {

    AbstractCandidatPlatforma intern = new CvIntern("Robert", 10, new String[]{"Programare", "Citire", "Scriere"});
    CvExtern cvExtern = new CvExtern("Viorel", 1, "consdus, mers, sarit");
    AbstractCandidatPlatforma extern = new AdapterCvExtern(cvExtern);

    evalueazaCandidat(intern);
    evalueazaCandidat(extern);
}
static void evalueazaCandidat(AbstractCandidatPlatforma candidat) {
    System.out.println("Nume: " + candidat.obtineNume());
    System.out.println("Experienta: " + candidat.obtineAniExperienta() + " ani");
    System.out.println("Competente: " + String.join(", ", candidat.obtineCompetente()));
    System.out.println("------------------------------------");
}