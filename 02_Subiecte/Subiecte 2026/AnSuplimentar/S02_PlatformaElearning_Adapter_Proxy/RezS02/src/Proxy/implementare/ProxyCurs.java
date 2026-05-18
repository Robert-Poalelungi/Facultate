package Proxy.implementare;

public class ProxyCurs implements AbstractCurs{
    private AbstractCurs curs;
    private String nivelAccesNecesar;

    public ProxyCurs(AbstractCurs curs, String nivelAccesNecesar) {
        this.curs = curs;
        this.nivelAccesNecesar = nivelAccesNecesar;
    }

    private boolean areAcces(String tipUtilizator){
        if (tipUtilizator.equals("profesor")){
            return true;
        } else if (tipUtilizator.equals("student_premium")) {
            return !nivelAccesNecesar.equals("profesor");
        }else if(tipUtilizator.equals("student")){
            return nivelAccesNecesar.equals("student");
        }else{
            return false;
        }
    }

    @Override
    public void afiseazaContinut(String tipUtilizator) {
        if (areAcces(tipUtilizator)){
            curs.afiseazaContinut(tipUtilizator);
        }else{
            System.out.println("Nu are acces la cursuri!!!");
        }
    }
}
