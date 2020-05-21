
/**
 *
 * @author Isaac Murisa 201534328
 */
import java.util.*;

public class LinearProbing {
    
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
    MapEntry[] table;
    
    public LinearProbing(){
        table = new MapEntry[5];
    }
    
    public Student BucketGet(int h,int k){
        //get the element at the position h
        MapEntry answer = table[h];
        
        Student ans = null;
        int numb = answer.getKey();
        if (numb == k){
            ans = (Student) answer.getStudent();
        }
        return ans;
    }
    
    public void bucketPut(int h, int k, Student v){
        boolean entered = false;
        //The MapEntry temp 
        MapEntry temp = new MapEntry(k,v);
        
        //if the bucket is empty then just add
        if (table[h] == null){
            table[h] = temp;
        }
        else {
            //when the bucket is not empty then look for a bucket next to it
            while (!entered){
                
                //set h to the next value
                h = (h + 1) % 5;
                if (table[h] == null){
                    //add the element at the position h
                    table[h] = temp;
                    entered = true;
                }
            }
        }
    }
    
    public Student bucketRemove(int h, int k){
        //get the entry at position k
        MapEntry temp = table[h];
        
        //get the key
        int num = temp.getKey();
        
        //check if the student number is the same as the one to be removed
        if (num == k){
            table[h] = null;
        }
        Student ans = (Student) temp.getStudent();
        return ans;
    }
    
    public void printTable(){
        
        for (int i = 0; i < 5; i++){
            
            if (table[i] != null){
                int c = i;
                MapEntry temp = table[i];
                Student stu = (Student) temp.getStudent();
                System.out.println("Student name:  " + stu.getName() + "    Student id:   " + temp.getKey() + "      Student cumulative grade:  " + stu.getCumGrade() + "      Table position:    " + c);
            }
        }
    }
    
    public int size(){
        return size;
    }
}
