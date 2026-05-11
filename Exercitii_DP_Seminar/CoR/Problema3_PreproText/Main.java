public class Main {
    public static void main(String[] args) {
        AFiltru trim = new TrimFilter();
        AFiltru lower = new LowerCaseFilter();
        AFiltru extraSpaces = new RemoveExtraSpacesFilter();
        AFiltru punctuatie = new RemovePunctuationFilter();
        AFiltru diacritice = new ReplaceDiacriticsFilter();
        AFiltru stopWords = new StopWordsFilter();
        AFiltru shortWords = new ShortWordFilter(3);
        AFiltru duplicates = new DuplicateWordRemover();

        trim.setUrmator(lower)
            .setUrmator(extraSpaces)
            .setUrmator(punctuatie)
            .setUrmator(diacritice)
            .setUrmator(stopWords)
            .setUrmator(shortWords)
            .setUrmator(duplicates);

        String text = "  Ana are  mere, și mere,  și pere! Ana iubește fructele. ";
        System.out.println("Input:  \"" + text + "\"");
        System.out.println("Output: \"" + trim.aplica(text) + "\"");
    }
}
