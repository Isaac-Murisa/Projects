/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Isaac Murisa
 */
public interface PriorityQueue {
    int size();
    boolean isEmpty();
    Entry<K,V> min();
    Entry<K,V> removeMin();
}
