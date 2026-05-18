package Adapter.implemetare;

public class LectieExterna {
    private String title;
    private String content;

    public LectieExterna(String title, String content) {
        this.title = title;
        this.content = content;
    }

    public String getTitlu() {
        return title;
    }

    public String getContinutStandardizat() {
        return content;
    }
}
