
/**
 *
 * @author Isaac Murisa 201534328
 */
import java.util.*;

public class HashRunner {
    
    public static void main(String[] args){
        
        //student objects
        Student one = new Student("Isaac Murisa", 78, 20152323);
        Student two = new Student("Col Dave", 78, 20146757);
        Student three = new Student("Ice Cud", 78, 20163445);
        Student four = new Student("Dan Tue", 78, 20157600);
        Student fife = new Student("Mira Amina", 78, 20150971);
        
        //list to hold the objects 
        Student[] list = new Student[5];
        
        //add the objects to the list
        list[0] = one;
        list[1] = two;
        list[2] = three;
        list[3] = four;
        list[4] = fife;
        
        //add using the first function
        functionOne(list);
        
        //add using the second function
        functionTwo(list);
    }
    
    /**
     * function to add the hash table using the first function which is (x mod 3) on the last number
     * @param list the list of student objects
     */
    public static void functionOne(Student[] list){
        System.out.println("Function one ");
        //the variable to hold the table pointer, calculated from the hash function
        int h = 0;
        
        //linear probing 
        LinearProbing phash = new LinearProbing();
        //phash.CreateTable();            //create the table
        
        //separate chaining
        SeparateChaining shash = new SeparateChaining();
        //shash.CreateTable();            //create the table
        
        for (int i = 0; i < 5; i++){
            Student temp = list[i];
            
            //get the last number of the student id and calculate the value of h
            int num = temp.getID() % 10000000;
            h = num % 3;
            
            phash.bucketPut(h, temp.getID(), temp);
            
            shash.bucketPut(h, temp.getID(), temp);
            
        }
        
        phash.printTable();
        System.out.println();
            
        shash.printTable();
        System.out.println();
    }
    
    /**
     * function to add the hash table using the first function which is (x mod 4) on the last number
     * @param list the list of student objects
     */
    public static void functionTwo(Student[] list){
        System.out.println("Function two");
        //the variable to hold the table pointer, calculated from the hash function
        int h = 0;
        
        //linear probing
        LinearProbing phash2 = new LinearProbing();
        //phash2.CreateTable();            //create the table
        
        //separate chaining
        SeparateChaining shash2 = new SeparateChaining();
        //shash2.CreateTable();           //create the table
        
        for (int i = 0; i < 5; i++){
            Student temp = list[i];
            
            //get the last number of the student id and calculate the value of h
            int num = temp.getID() % 10000000;
            h = num % 4;
            
            phash2.bucketPut(h, temp.getID(), temp);
            
            shash2.bucketPut(h, temp.getID(), temp);
            
        }
        phash2.printTable();
        System.out.println();
            
        shash2.printTable();
        System.out.println();
    }
}
