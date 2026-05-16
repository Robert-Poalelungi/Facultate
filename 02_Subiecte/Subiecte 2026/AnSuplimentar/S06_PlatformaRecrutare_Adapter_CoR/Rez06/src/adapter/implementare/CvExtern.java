package adapter.implementare;

import java.util.ArrayList;
import java.util.List;

public class CvExtern{
    private String name;
    private int workExperience;
    private String skills;

    public CvExtern(String name, int workExperience, String skills) {
        this.name = name;
        this.workExperience = workExperience;
        this.skills = skills;
    }

    public String getNume() {
        return name;
    }

    public int getAniExperienta() {
        return workExperience;
    }

    public String getCompetente() {
        return skills;
    }

    @Override
    public String toString() {
        return "CvExtern{" +
                "name='" + name + '\'' +
                ", workExperience=" + workExperience +
                ", skills='" + skills + '\'' +
                '}';
    }
}
