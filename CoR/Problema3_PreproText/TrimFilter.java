public class TrimFilter extends AFiltru {
    @Override
    public String aplica(String text) {
        return pasezaMailDeparte(text.trim());
    }
}
