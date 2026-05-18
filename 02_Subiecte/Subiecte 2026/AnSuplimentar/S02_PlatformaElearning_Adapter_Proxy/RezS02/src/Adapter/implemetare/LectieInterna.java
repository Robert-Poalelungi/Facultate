package Adapter.implemetare;

public class LectieInterna implements AbstractLectiePlatforma{
    private String titluLectie;
    private String continut;

    public LectieInterna(String titluLectie, String continut) {
        this.titluLectie = titluLectie;
        this.continut = continut;
    }

    @Override
    public String obtineTitlu() {
        return titluLectie;
    }

    @Override
    public String obtineContinutStandardizat() {
        return continut;
    }
}
