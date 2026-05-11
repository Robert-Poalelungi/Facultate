public class Main {
    public static void main(String[] args) {
        AVerificator birouCredit = new VerificatorBirouCredit();
        AVerificator vechime = new VerificatorVechime();
        AVerificator gradIndatorare = new VerificatorGradIndatorare();

        birouCredit.setUrmator(vechime).setUrmator(gradIndatorare);

        Persoana p1 = new Persoana("Ion Popescu", 5000, 24, 720);
        System.out.println("=== " + p1.getNume() + " ===");
        System.out.println("Credit aprobat: " + birouCredit.verifica(p1, 50000, 120));

        System.out.println();

        Persoana p2 = new Persoana("Maria Ionescu", 3000, 6, 800);
        System.out.println("=== " + p2.getNume() + " ===");
        System.out.println("Credit aprobat: " + birouCredit.verifica(p2, 20000, 60));

        System.out.println();

        Persoana p3 = new Persoana("Radu Marin", 2000, 18, 550);
        System.out.println("=== " + p3.getNume() + " ===");
        System.out.println("Credit aprobat: " + birouCredit.verifica(p3, 10000, 24));
    }
}
