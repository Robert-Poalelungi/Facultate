package proxy.implementare;

import java.util.Map;

public class SpitalProxy implements ISpital{
    private boolean areTrimitere;
    private boolean areHaineDeProtectie;
    private Map<String, String> vizitatoriPacienti;
    @Override
    public void accesSpital(String vizitator, String pacient) {
        if (areTrimitere){
            if (vizitatoriPacienti.size()>=5){
                if (areHaineDeProtectie){
                    vizitatoriPacienti.put(vizitator, pacient);
                    System.out.println("Se permite accesul " + vizitator + " la " +
                            "pacientul " + pacient);
                }else {
                    System.out.println("Nu se permite accesul vizitatorilor fara haine de protectie!!!");
                }
            }else{
                vizitatoriPacienti.put(vizitator, pacient);
                System.out.println("Se permite accesul " + vizitator + " la pacientul " + pacient);
            }
        }else {
            System.out.println("Nu se permite accesul vizitatorilor fra trimitere!!!");
        }
    }
}
