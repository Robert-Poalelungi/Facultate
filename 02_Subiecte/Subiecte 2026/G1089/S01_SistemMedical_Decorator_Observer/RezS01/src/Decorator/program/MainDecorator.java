import Decorator.implementare.*;

void main() {
    AbstractFisaMedicala fisaMedicala = new FisaMedicala("Amigdalita acuta", "Antibiotic", "Gargara cu apa cu sare", 40);
    fisaMedicala = new DecoratorLaborator(fisaMedicala, " Stafilococ Auriu", 100);
    fisaMedicala = new DecoratorImagistica(fisaMedicala, "Radiografie pulmonara clara", 80);
    fisaMedicala = new DecoratorNutritie(fisaMedicala, "Dieta bogata in vitamina C", 20);

    System.out.println(fisaMedicala.genereazaDescriere());
    System.out.println(fisaMedicala.calculeazaCostProcesare());
}
