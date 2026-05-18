package Decorator.implementare;

public abstract class DecoratorAbstract implements AbstractFisaMedicala{
    private AbstractFisaMedicala fisaMedicala;

    public DecoratorAbstract(AbstractFisaMedicala fisaMedicala) {
        this.fisaMedicala = fisaMedicala;
    }

    @Override
    public String genereazaDescriere() {
        return fisaMedicala.genereazaDescriere();
    }

    @Override
    public double calculeazaCostProcesare() {
        return fisaMedicala.calculeazaCostProcesare();
    }
}
