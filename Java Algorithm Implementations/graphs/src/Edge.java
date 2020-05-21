
/**
 *
 * @author Isaac Murisa 201534328
 */
public class Edge {
    //the start and the end vertexes of the edge
    private Vertex start;
    private Vertex end;
    
    //constructor
    public Edge(Vertex f, Vertex l){
        start = f;
        end = l;
    }
    
    //setters and getters 
    public void setStart(Vertex v){
        start = v;
    }
    public  void setEnd(Vertex v){
        end = v;
    }
    public Vertex getStart(){
        return start;
    }
    public Vertex getEnd(){
        return end;
    }
}
