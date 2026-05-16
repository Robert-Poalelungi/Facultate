package adapter.implementare;

import java.util.Arrays;

public class CvIntern implements AbstractCandidatPlatforma{
    private String nume;
    private int experienta;
    private String[] competente;

    public CvIntern(String nume, int experienta, String[] competente) {
        this.nume = nume;
        this.experienta = experienta;
        this.competente = competente;
    }

    @Override
    public String obtineNume() {
        return nume;
    }

    @Override
    public int obtineAniExperienta() {
        return experienta;
    }

    @Override
    public String[] obtineCompetente() {
        return competente;
    }

    @Override
    public String toString() {
        return "CvIntern{" +
                "nume='" + nume + '\'' +
                ", experienta=" + experienta +
                ", competente=" + Arrays.toString(competente) +
                '}';
    }
}
