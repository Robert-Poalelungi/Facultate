package adapter.implementare;

public class AdapterCvExtern implements AbstractCandidatPlatforma{
    private CvExtern cvExtern;

    public AdapterCvExtern(CvExtern cvExtern) {
        this.cvExtern = cvExtern;
    }

    @Override
    public String obtineNume() {
        return cvExtern.getNume();
    }

    @Override
    public int obtineAniExperienta() {
        return cvExtern.getAniExperienta();
    }

    @Override
    public String[] obtineCompetente() {
        return cvExtern.getCompetente().split(",");
    }

    @Override
    public String toString() {
        return "AdapterCvExtern{" +
                "cvExtern=" + cvExtern +
                '}';
    }
}
