public class RemovePunctuationFilter extends AFiltru {
    @Override
    public String aplica(String text) {
        return pasezaMailDeparte(text.replaceAll("[.,!?;:\"'()\\-]", ""));
    }
}
