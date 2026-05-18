package composite.implementare;

public interface Hotel extends AbstractUnitateCazare{
    void addNod(Hotel nod);
    void removeNod(Hotel nod);
    Hotel getNod(int index);
}
