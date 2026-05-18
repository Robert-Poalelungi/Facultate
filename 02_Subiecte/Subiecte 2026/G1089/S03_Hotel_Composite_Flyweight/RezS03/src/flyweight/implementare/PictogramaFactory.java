package flyweight.implementare;

import java.util.HashMap;
import java.util.Map;

public class PictogramaFactory {
    private static Map<String, AbstractPictogramaFacilitate> pictograme = new HashMap<>();

    public static AbstractPictogramaFacilitate getPictograma(String cheie){
        if (!pictograme.containsKey(cheie)){
            pictograme.put(cheie, new PictogramaFacilitate(cheie));
        }
        return pictograme.get(cheie);
    }

    public static int getNrInstante(){
        return pictograme.size();
    }


}
