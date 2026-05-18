package Command.implementare;

import java.util.ArrayList;
import java.util.List;

public class ManagerComenzi {
    private List<AbstractActiuneComanda> actiuni = new ArrayList<>();

    public void adaugaActiune(AbstractActiuneComanda actiune){
        actiuni.add(actiune);
    }

    public void stergeActiune(AbstractActiuneComanda actiune){
        actiuni.remove(actiune);
    }

    public void executaActiuni(){
        for (AbstractActiuneComanda actiune : actiuni){
            actiune.executa();
        }
        actiuni.clear();
    }


}
