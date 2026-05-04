public abstract class AFiltru {
    private AFiltru urmator;

    public AFiltru setUrmator(AFiltru urmator) {
        this.urmator = urmator;
        return urmator;
    }

    protected String pasezaMailDeparte(String text) {
        if (urmator != null)
            return urmator.aplica(text);
        return text;
    }

    public abstract String aplica(String text);
}
