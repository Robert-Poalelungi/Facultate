package Decorator.implementare;

public class DecoratorNutritie extends DecoratorAbstract{
    private String recomandariNutritionale;
    private double costAnalizaNutritionala;

    public DecoratorNutritie(AbstractFisaMedicala fisaMedicala, String recomandariNutritionale, double costAnalizaNutritionala) {
        super(fisaMedicala);
        this.recomandariNutritionale = recomandariNutritionale;
        this.costAnalizaNutritionala = costAnalizaNutritionala;
    }

    @Override
    public String genereazaDescriere() {
        return super.genereazaDescriere() + recomandariNutritionale;
    }

    @Override
    public double calculeazaCostProcesare() {
        return super.calculeazaCostProcesare() + costAnalizaNutritionala;
    }
}
