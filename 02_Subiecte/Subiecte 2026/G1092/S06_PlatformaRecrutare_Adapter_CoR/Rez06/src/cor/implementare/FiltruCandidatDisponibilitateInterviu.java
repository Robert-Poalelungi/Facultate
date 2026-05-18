package cor.implementare;

public class FiltruCandidatDisponibilitateInterviu extends AbstractFiltruCandidat{
    @Override
    public boolean proceseaza(Candidat candidat) {
        if (!candidat.isEsteDisponibilInterviu()){
            System.out.println(candidat.getNume() + " nu este disponibil pentru interviu");
            return false;
        }else{
            System.out.println(candidat.getNume() + " are dsiponibilitate pentru interviu");
        }

        if (urmator!= null){
            return urmator.proceseaza(candidat);
        }
        return true;
    }
}
