package cor.implementare;

public class FiltrareCandidatCompetente extends AbstractFiltruCandidat{

    @Override
    public boolean proceseaza(Candidat candidat) {
        if (!candidat.isAreCompetente()){
            System.out.println(candidat.getNume() + " nu a trecut filtrul de competente");
            return false;
        }else{
            System.out.println(candidat.getNume() + " are competentele minime pentru acest rol!!!");
        }

        if (urmator != null){
            return urmator.proceseaza(candidat);
        }
        return true;
    }
}
