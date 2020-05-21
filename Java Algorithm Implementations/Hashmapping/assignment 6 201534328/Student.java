
/**
 *
 * @author Isaac Murisa 20534328
 */
public class Student {
    
    //instance variables for the student class
    private String name;            //hold name for a student
    private int cumGrade;           //hold the cumulative grade of a student
    private int id;
    
    //constructor
    public Student(String a, int b, int i){
        name = a;
        cumGrade = b;
        id =i;
    }
    
    //setters for the class variables
    public void setName(String a){
        name = a;
    }
    public void setCumGrade(int b){
        cumGrade = b;
    }
    public void setID(int c){
        id = c;
    }
    
    //getters for the instance variables
    public String getName(){
        return name;
    }
    public int getCumGrade(){
        return cumGrade;
    }
    public int getID(){
        return id;
    }
}
