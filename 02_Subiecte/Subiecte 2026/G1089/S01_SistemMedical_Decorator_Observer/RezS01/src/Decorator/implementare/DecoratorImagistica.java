package Decorator.implementare;

public class DecoratorImagistica extends DecoratorAbstract{
    private String observatiiImagistica;
    private double costImagistica;

    public DecoratorImagistica(AbstractFisaMedicala fisaMedicala, String observatiiImagistica, double costImagistica) {
        super(fisaMedicala);
        this.observatiiImagistica = observatiiImagistica;
        this.costImagistica = costImagistica;
    }

    @Override
    public String genereazaDescriere() {
        return super.genereazaDescriere() + observatiiImagistica;
    }

    @Override
    public double calculeazaCostProcesare() {
        return super.calculeazaCostProcesare() + costImagistica;
    }
}
