public class Main {
    public static void main(String[] args) {
        Angajat ceo = new Angajat("Ion Popescu", 15000);
        Angajat dev1 = new Angajat("Ana Ionescu", 7000);
        Angajat dev2 = new Angajat("Radu Marin", 6500);
        Angajat qa1 = new Angajat("Elena Dumitrescu", 5500);
        Angajat hr1 = new Angajat("Maria Popa", 5000);
        Angajat manager = new Angajat("Gheorghe Stan", 9000);

        Departament dev = new Departament("Development");
        dev.adauga(dev1);
        dev.adauga(dev2);

        Departament qa = new Departament("QA");
        qa.adauga(qa1);

        Departament it = new Departament("IT");
        it.adauga(manager);
        it.adauga(dev);
        it.adauga(qa);

        Departament hr = new Departament("HR");
        hr.adauga(hr1);

        Departament companie = new Departament("Companie SRL");
        companie.adauga(ceo);
        companie.adauga(it);
        companie.adauga(hr);

        companie.afiseaza("");
        System.out.printf("%nSalariu total: %.0f RON%n", companie.getSalariuTotal());
        System.out.println("Total angajati: " + companie.getNrAngajati());

        System.out.println("\n--- Doar departamentul IT ---");
        it.afiseaza("");
        System.out.printf("Salariu IT: %.0f RON, Angajati IT: %d%n",
            it.getSalariuTotal(), it.getNrAngajati());
    }
}
