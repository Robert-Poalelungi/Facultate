import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class StopWordsFilter extends AFiltru {
    private static final Set<String> STOP_WORDS = new HashSet<>(Arrays.asList(
        "si", "in", "la", "pe", "de", "cu", "un", "o", "cel", "cea", "a", "al"
    ));

    @Override
    public String aplica(String text) {
        String[] cuvinte = text.split(" ");
        StringBuilder rezultat = new StringBuilder();
        for (String cuv : cuvinte) {
            if (!STOP_WORDS.contains(cuv)) {
                if (rezultat.length() > 0) rezultat.append(" ");
                rezultat.append(cuv);
            }
        }
        return pasezaMailDeparte(rezultat.toString());
    }
}
