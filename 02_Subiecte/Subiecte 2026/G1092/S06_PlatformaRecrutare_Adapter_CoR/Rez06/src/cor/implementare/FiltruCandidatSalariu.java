package cor.implementare;

public class FiltruCandidatSalariu extends AbstractFiltruCandidat{
    private double salariuMaxim;

    public FiltruCandidatSalariu(double salariuMaxim) {
        this.salariuMaxim = salariuMaxim;
    }

    @Override
    public boolean proceseaza(Candidat candidat) {
        if (salariuMaxim < candidat.getSalariu()){
            System.out.println(candidat.getNume() + " Vrea un salariu mai mare decat putem oferi");
            return false;
        }else{
            System.out.println(candidat.getNume() + " Este compatibil salarial");
        }
        if (urmator != null){
            return urmator.proceseaza(candidat);
        }
        return true;
    }
}
