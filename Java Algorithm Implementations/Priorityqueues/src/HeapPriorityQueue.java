/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Isaac Murisa
 */
public class HeapPriorityQueue<K,V> extends AbstractPriorityQueue<K,V> {
    
    Protected ArrayList<Entry<K,V>> heap = new ArrayList<>();
    
    public HeapPriorityQueue() { super();}
    public HeapPriorityQueue(Comparator<K> comp) { super(comp); }
    
    protected int parent(int j) { (j-1)/ 2 ; }
    protected int left(int j) { return  2*j + 1; }
    protected int right(int j) { 
}
