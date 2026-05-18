package cor.implementare;

import java.util.ArrayList;
import java.util.List;

public class Candidat {
    private String nume;
    private int experiena;
    private boolean areCompetente;
    private boolean esteDisponibilInterviu;
    private double salariu;

    public Candidat(String nume, int experiena, boolean areCompetente, boolean esteDisponibilInterviu, double salariu) {
        this.nume = nume;
        this.experiena = experiena;
        this.areCompetente = areCompetente;
        this.esteDisponibilInterviu = esteDisponibilInterviu;
        this.salariu = salariu;
    }

    public String getNume() {
        return nume;
    }

    public int getExperiena() {
        return experiena;
    }

    public boolean isAreCompetente() {
        return areCompetente;
    }

    public boolean isEsteDisponibilInterviu() {
        return esteDisponibilInterviu;
    }

    public double getSalariu() {
        return salariu;
    }
}
