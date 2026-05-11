public class CreditRefuzatException extends Exception {
    public CreditRefuzatException(String motiv) {
        super("Credit refuzat: " + motiv);
    }
}
