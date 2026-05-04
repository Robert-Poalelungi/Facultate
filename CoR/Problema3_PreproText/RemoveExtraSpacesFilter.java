public class RemoveExtraSpacesFilter extends AFiltru {
    @Override
    public String aplica(String text) {
        return pasezaMailDeparte(text.replaceAll("\\s+", " "));
    }
}
