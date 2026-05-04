public class ReplaceDiacriticsFilter extends AFiltru {
    @Override
    public String aplica(String text) {
        return pasezaMailDeparte(text
            .replace("ă", "a").replace("â", "a").replace("î", "i")
            .replace("ș", "s").replace("ț", "t")
            .replace("Ă", "A").replace("Â", "A").replace("Î", "I")
            .replace("Ș", "S").replace("Ț", "T"));
    }
}
