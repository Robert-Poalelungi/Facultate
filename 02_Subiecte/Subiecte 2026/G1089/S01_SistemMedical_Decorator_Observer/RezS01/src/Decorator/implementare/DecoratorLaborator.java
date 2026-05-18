package Decorator.implementare;

public class DecoratorLaborator extends DecoratorAbstract {
    private String rezultateAnalize;
    private double costAnalize;

    public DecoratorLaborator(AbstractFisaMedicala fisaMedicala, String rezultateAnalize, double costAnalize) {
        super(fisaMedicala);
        this.rezultateAnalize = rezultateAnalize;
        this.costAnalize = costAnalize;
    }

    @Override
    public String genereazaDescriere() {
        return super.genereazaDescriere() + rezultateAnalize;
    }

    @Override
    public double calculeazaCostProcesare() {
        return super.calculeazaCostProcesare() + costAnalize;
    }
}
