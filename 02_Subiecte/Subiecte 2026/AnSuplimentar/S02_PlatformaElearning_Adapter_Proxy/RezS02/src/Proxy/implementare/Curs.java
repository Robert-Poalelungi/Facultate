package Proxy.implementare;

public class Curs implements AbstractCurs{
    private String numeCurs;
    private String continut;

    public Curs(String numeCurs, String continut) {
        this.numeCurs = numeCurs;
        this.continut = continut;
    }

    @Override
    public void afiseazaContinut(String tipUtilizator) {
        System.out.println("Cursul: " + numeCurs + " are continutul " + continut);
    }
}
