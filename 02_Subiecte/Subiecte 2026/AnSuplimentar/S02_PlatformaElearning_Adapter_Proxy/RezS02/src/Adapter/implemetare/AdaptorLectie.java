package Adapter.implemetare;

public class AdaptorLectie implements AbstractLectiePlatforma{
    private LectieExterna lectieExterna;

    public AdaptorLectie(LectieExterna lectieExterna) {
        this.lectieExterna = lectieExterna;
    }

    @Override
    public String obtineTitlu() {
        return lectieExterna.getTitlu();
    }

    @Override
    public String obtineContinutStandardizat() {
        return lectieExterna.getContinutStandardizat();
    }
}
