package composite.implementare;

public interface INod extends AbstractElementTransport{
    void addNod (INod nod);
    void removeNod (INod nod);
    INod getNod(int index);
}
