import java.util.Arrays;
import java.util.LinkedHashSet;

public class DuplicateWordRemover extends AFiltru {
    @Override
    public String aplica(String text) {
        String[] cuvinte = text.split(" ");
        LinkedHashSet<String> unice = new LinkedHashSet<>(Arrays.asList(cuvinte));
        return pasezaMailDeparte(String.join(" ", unice));
    }
}
