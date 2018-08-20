
/**
 *
 * @author Isaac Murisa 201534328
 */
public class Vertex<E> {
    private E vertex;
    
    //constructor for the vertex object
    public Vertex(E v){
        vertex = v;
    }
    
    //setters and getters of the vertex object class
    public void setVertex(E v){
        vertex = v;
    }
    public E getVertex(){
        return vertex;
    }
}
