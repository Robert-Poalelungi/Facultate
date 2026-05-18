package Decorator.implementare;

public class FisaMedicala implements AbstractFisaMedicala{
    private String diagnostic;
    private String tratament;
    private String recomandari;
    private double costProcesare;

    public FisaMedicala(String diagnostic, String tratament, String recomandari, double costProcesare) {
        this.diagnostic = diagnostic;
        this.tratament = tratament;
        this.recomandari = recomandari;
        this.costProcesare = costProcesare;
    }

    @Override
    public String genereazaDescriere() {
        return "Fisa medicala indica diagnosticul " + diagnostic + " cu tratamentul " + tratament + " si urmatoarele recomandari " + recomandari;
    }

    @Override
    public double calculeazaCostProcesare() {
        return costProcesare;
    }
}
