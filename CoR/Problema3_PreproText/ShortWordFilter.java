public class ShortWordFilter extends AFiltru {
    private final int lungimeMinima;

    public ShortWordFilter(int lungimeMinima) {
        this.lungimeMinima = lungimeMinima;
    }

    @Override
    public String aplica(String text) {
        String[] cuvinte = text.split(" ");
        StringBuilder rezultat = new StringBuilder();
        for (String cuv : cuvinte) {
            if (cuv.length() >= lungimeMinima) {
                if (rezultat.length() > 0) rezultat.append(" ");
                rezultat.append(cuv);
            }
        }
        return pasezaMailDeparte(rezultat.toString());
    }
}
