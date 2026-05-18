import Adapter.implemetare.AbstractLectiePlatforma;
import Adapter.implemetare.AdaptorLectie;
import Adapter.implemetare.LectieExterna;
import Adapter.implemetare.LectieInterna;

void main() {
    LectieExterna lectieExterna = new LectieExterna("Mate", "probleme");
    LectieInterna lectieInterna = new LectieInterna("Romana", "citit");

    AdaptorLectie adaptorLectie = new AdaptorLectie(lectieExterna);

    afiseazaLectie(lectieInterna);
    afiseazaLectie(adaptorLectie);

}

static void afiseazaLectie(AbstractLectiePlatforma lectie) {
    System.out.println("Titlu: " + lectie.obtineTitlu());
    System.out.println("Continut: " + lectie.obtineContinutStandardizat());
    System.out.println("----");
}
