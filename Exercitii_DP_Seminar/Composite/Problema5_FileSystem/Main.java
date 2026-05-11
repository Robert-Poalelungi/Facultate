public class Main {
    public static void main(String[] args) {
        Fisier f1 = new Fisier("Main.java", 12.5);
        Fisier f2 = new Fisier("Utils.java", 8.3);
        Fisier f3 = new Fisier("README.md", 2.1);
        Fisier f4 = new Fisier("Test.java", 5.7);
        Fisier f5 = new Fisier("config.json", 1.2);

        Folder src = new Folder("src");
        src.adauga(f1);
        src.adauga(f2);

        Folder test = new Folder("test");
        test.adauga(f4);

        Folder proiect = new Folder("proiect");
        proiect.adauga(f3);
        proiect.adauga(f5);
        proiect.adauga(src);
        proiect.adauga(test);

        System.out.println("=== Structura proiect ===");
        proiect.afiseaza("");
        System.out.printf("%nDimensiune totala: %.1f KB%n", proiect.getDimensiune());

        System.out.println("\n=== Cautare ===");
        AElementSistem gasit = proiect.cauta("Utils.java");
        System.out.println("Cautare 'Utils.java': " + (gasit != null ? "gasit (" + gasit.getDimensiune() + " KB)" : "negasit"));
        System.out.println("Cautare 'absent.txt': " + (proiect.cauta("absent.txt") != null ? "gasit" : "negasit"));

        System.out.println("\n=== Stergere README.md ===");
        proiect.sterge(f3);
        System.out.printf("Dimensiune dupa stergere: %.1f KB%n", proiect.getDimensiune());
    }
}
