
/**
 *
 * @author Isaac Murisa 201534328
 */
import java.util.*;

public class AdjacencyList{
    
    //arrays to hold the 
    private ArrayList<Vertex> vertexes;
    private ArrayList<Edge> edges;
    
    public AdjacencyList(ArrayList<Vertex> v, ArrayList<Edge> e){
        vertexes = v;
        edges = e;
    }
    
    //method to add a vertex
    public void insertVertex(Vertex v){
        vertexes.add(v);
    }
    
    //method to insert the 
    public void insertEdge(Vertex a, Vertex b){
        Edge e = new Edge(a,b);
        edges.add(e);
    }
    
    //method to remove a vertex
    public void removeVertex(Vertex v){
        for (int i = 0; i < vertexes.size(); i++){
            if (vertexes.get(i) == v){      //if the current vertex is equal to the one to be deleted
                vertexes.remove(i);         //delete vertex
            }
        }
        
        //removes all the incident edges
        for (int j = 0; j < edges.size(); j++){
            Edge m = edges.get(j);
            /* check if the vertex is associated with any of the edges
            * if its associated then the edge is removed
            */
            if ((m.getStart() == v) || (m.getEnd() == v)){
                edges.remove(j);        
            }
        }
    }
    
    //method to remove add a vertex
    public void removeEdge(Vertex a, Vertex b){
        for (int i = 0; i < edges.size(); i++){
            Edge temp = edges.get(i);
            
            /*checks if for the edge to be deleted
            * looks for the edge with the same start and end vertex
            */
            if ((temp.getStart() == a) && (temp.getEnd() == b)){
                edges.remove(i);            //removes the edge
            }
        }
    }
    
    /*
    method to get the number of vertex in the graph
    */
    public int numVertices(){
        return vertexes.size();
    }
    
    /*
    method to return the  number of edges in the graph
    */
    public int numEdges(){
        return edges.size();
    }
    
    //method to print the graph
    public void printGraph(){
        //print the vertex 
        for (int i = 0; i < vertexes.size(); i++){
            System.out.print(vertexes.get(i).getVertex() + "  -->  ");
            //print the corresponding vertex
            for (int j = 0; j < edges.size(); j++){
                /*
                Get the edge, if the current vertex is available in the edge as the start or the end 
                get the other vertex and print.
                */
                Edge n = edges.get(j);
                if (n.getStart() == vertexes.get(i)){
                    System.out.print(n.getEnd().getVertex() + ", ");
                }
                if (n.getEnd() == vertexes.get(i)){
                    System.out.print(n.getStart().getVertex() + ", ");
                }
            }
            System.out.println();
        }
    }
}
