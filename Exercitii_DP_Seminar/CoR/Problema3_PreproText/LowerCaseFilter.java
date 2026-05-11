public class LowerCaseFilter extends AFiltru {
    @Override
    public String aplica(String text) {
        return pasezaMailDeparte(text.toLowerCase());
    }
}
