
/**
 *
 * @author Isaac Murisa 201534328
 */
import java.util.*;

public class SeparateChaining {
    
     //nested mapentry class
    protected static class MapEntry<Int,Student> {
        private int k;        //instance variables of the MapEntry class
        private Student v;
        
        public MapEntry(int a, Student b){
            k = a;
            v = b;
        }
        
        //setters 
        public void setKey(int a) {
            k = a;
        }
        public void setStudent(Student b){
            v = b;
        }
        
        //getters
        public int getKey() {
            return k;
        }
        public Student getStudent(){
            return v;
        }
    }
    //instance variables for the class 
    private static int size;
    ArrayList[] table;            //table for the  function
    
    public SeparateChaining(){
        table = new ArrayList[5];
    }
    
    //method to return the 
    public Student BucketGet(int h,int k){
        
        MapEntry answer = new MapEntry(0,null);
        
        //get the array bucket at position h
        if (table[h] != null) {
            ArrayList<MapEntry> bucket = table[h];
        
            for (int i = 0; i < bucket.size(); i++){
                //get the key for the current student on the bucket
                int key = bucket.get(i).getKey();
            
            if (key == k){      //found the element
                answer = bucket.get(i);
                }
            }
            //return the student object
            
        }
        return (Student) answer.getStudent();
    }
    
    //method to add an element in the table
    public void bucketPut(int h, int k, Student v){
        if (table[h] == null){
            ArrayList<MapEntry> bucket = new ArrayList<>();
            MapEntry ans = new MapEntry(k,v);
            bucket.add(ans);
            table[h] = bucket;
            size++;
        }
        else {
            //get the array bucket at position h
            ArrayList<MapEntry> bucket = table[h];
            
            //create the MapEntry object
            MapEntry ans = new MapEntry(k,v);
            
            //add the elemwnt into the bucket
            table[h].add(ans);
            size++;
        }
            
    }
    
    public Student bucketRemove(int h, int k){
        MapEntry answer = new MapEntry(0,null);
        
        if (table[h] != null){
            //get the array bucket at position h
            ArrayList<MapEntry> bucket = table[h];
            
            for (int i = 0; i < bucket.size(); i++){
                //get the key for the current student on the bucket
                int key = bucket.get(i).getKey();
                
                if (key == k){      //found the element
                    answer = bucket.get(i);
                    //remove the element
                    bucket.remove(i);
                }
            }
        }
        //return the student object
        return (Student) answer.getStudent();
    }
    
    public void printTable(){
        //get the array bucket at position h
        for (int i = 0; i < 5; i++){
            if (table[i] != null){
                ArrayList<MapEntry> bucket = table[i];
                
                for (int j = 0; j < bucket.size(); j++){
                    int c = i;
                    MapEntry temp = bucket.get(j);
                    Student stu = (Student) temp.getStudent();
                    System.out.println("Student name:  " + stu.getName() + "    Student id:   " + temp.getKey() + "Student cumulative grade:  " + stu.getCumGrade() + "Table position:    " + c);
                }
            }
        }
    }
    
    public int size(){
        return size;
    }

}
