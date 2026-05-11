public class Main {
    public static void main(String[] args) {
        ALimitator verificator = new VerificatorEligibilitateMinima();
        ALimitator limitVechime = new LimitatorVechime();
        ALimitator limitVenit = new LimitatorVenit();
        ALimitator limitScor = new LimitatorScorCredit();

        verificator.setUrmator(limitVechime).setUrmator(limitVenit).setUrmator(limitScor);

        double plafonGeneral = 100000;

        Persoana p1 = new Persoana("Ion Popescu", 5000, 36, 720);
        System.out.println("=== " + p1.getNume() + " ===");
        try {
            double sumaMax = verificator.calculeaza(p1, 120, plafonGeneral);
            System.out.printf("Suma maxima eligibila: %.2f RON%n", sumaMax);
        } catch (CreditRefuzatException e) {
            System.out.println(e.getMessage());
        }

        System.out.println();

        Persoana p2 = new Persoana("Maria Ionescu", 2000, 3, 800);
        System.out.println("=== " + p2.getNume() + " ===");
        try {
            double sumaMax = verificator.calculeaza(p2, 60, plafonGeneral);
            System.out.printf("Suma maxima eligibila: %.2f RON%n", sumaMax);
        } catch (CreditRefuzatException e) {
            System.out.println(e.getMessage());
        }

        System.out.println();

        Persoana p3 = new Persoana("Radu Marin", 4000, 24, 400);
        System.out.println("=== " + p3.getNume() + " ===");
        try {
            double sumaMax = verificator.calculeaza(p3, 60, plafonGeneral);
            System.out.printf("Suma maxima eligibila: %.2f RON%n", sumaMax);
        } catch (CreditRefuzatException e) {
            System.out.println(e.getMessage());
        }
    }
}
