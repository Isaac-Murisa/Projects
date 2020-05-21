
/**
 *
 * @author Isaac Murisa
 */
import java.util.*;
import java.lang.Comparable;

public abstract class AbstractPriorityQueue<K,V> implements PriorityQueue<K,V> {
    
    //nested PQEnrty class
    protected static class PQEntry<K,V> implements Entry<K,V> {
        private K k;    //key 
        private V v;    //value
        public PQEntry(K key, V value){
            k = key;
            v = value;
        }
        
        //methods to Entry interface
        public K getKey() {return k;}
        public V getValue(){return v;}
        
        //properties not exposed to the Entry interface
        protected void setKey(K key) { k = key; }
        protected void setValue(V value) { v = value; }
    }
    
    //the comparator defining the the ordering of keys
    private Comparator<K> comp;
    
    //creates an empty priority queue using the given comparator to order keys
    protected AbstractPriorityQueue(Comparator<K> c){ comp =c; }
    
    //method for comparing two objects according to the key
    protected int compare(Entry<K,V> a, Entry<K,V> b){
        return comp.compare(a.getKey( ), b.getKey( ));
    }
    
    //determines if a key is valid
    protected boolean checkKey(K key) throws IllegalArgumentException {
        try { 
            return (comp.compare(key,key) == 0); // see if key can be compared to itself
        } 
        catch (ClassCastException e) { 
            throw new IllegalArgumentException("Incompatible key");
        }
    }
    
    //test if the priority queue is empty
    public boolean isEmpty() {
        return size() == 0;
    }
}
