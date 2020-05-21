
/**
 *
 * @author Isaac Murisa
 */
import java.util.*;

public class GraphTester {
    public static void main(String[] args){
        
        //arrays to hold the verticies and edges
        ArrayList<Vertex> vert = new ArrayList<Vertex>();
        ArrayList<Edge> edg = new ArrayList<Edge>();
        
        //declaring the vertices
        Vertex a = new Vertex("A");
        Vertex b = new Vertex("B");
        Vertex c = new Vertex("C");
        Vertex d = new Vertex("D");
        
        //adding the verticies to the array
        vert.add(a); vert.add(b); vert.add(c); vert.add(d);
        
        //declaring the edges
        Edge one = new Edge(a,b);
        Edge two = new Edge(a,c);
        Edge three = new Edge(b,c);
        Edge four = new Edge(c,d);
        Edge fife = new Edge(d,b);
        
        edg.add(one); edg.add(two); edg.add(three); edg.add(four); edg.add(fife);
        
        AdjacencyList g = new AdjacencyList(vert,edg);
        g.printGraph();
        
    }
}
