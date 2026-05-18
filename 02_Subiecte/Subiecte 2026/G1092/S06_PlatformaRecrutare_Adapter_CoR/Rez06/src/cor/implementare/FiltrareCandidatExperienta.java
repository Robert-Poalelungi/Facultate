package cor.implementare;

public class FiltrareCandidatExperienta extends AbstractFiltruCandidat{
    private int experientaMinima;

    public FiltrareCandidatExperienta(int experientaMinima) {
        this.experientaMinima = experientaMinima;
    }

    @Override
    public boolean proceseaza(Candidat candidat) {
        if (candidat.getExperiena() < experientaMinima){
            System.out.println(candidat.getNume() + " nu are exeprienta destula");
            return false;
        }else{
            System.out.println(candidat.getNume() + " a trecut filtrul de experienta");
        }
        if (urmator != null){
            return urmator.proceseaza(candidat);
        }
        return true;
    }
}
