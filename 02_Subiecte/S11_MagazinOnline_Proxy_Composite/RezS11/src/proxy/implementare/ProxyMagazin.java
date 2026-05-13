package proxy.implementare;

import java.util.ArrayList;
import java.util.List;

public class ProxyMagazin implements IMagazin{
   private IMagazin magazin;
   List<String> clienti;


    public ProxyMagazin(IMagazin magazin) {
        this.magazin = magazin;
        this.clienti = new ArrayList<>();
    }

    @Override
    public double calculeazaTotal(String client, double totalCos, String adresa) {
        if (clienti.contains(client)){
            System.out.println("Reducerea a fost deja aplicata!!!");
        }else {
            clienti.add(client);
            totalCos = totalCos - totalCos * 0.10;
            System.out.println("Discount aplicat!!!");
        }
        return magazin.calculeazaTotal(client, totalCos, adresa);
    }
}
