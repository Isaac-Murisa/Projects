
/**
 *
 * @author Isaac Murisa
 */

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class stats {
    public static void main(String[] args) throws FileNotFoundException, IOException{
        
        String row;
        ArrayList<String> contained = new ArrayList<>();
        int count = 0;
        ArrayList<String> data = new ArrayList<>();
        ArrayList<String> meetings = new ArrayList<>();
        
        BufferedReader csv = new BufferedReader(new FileReader("D:/Courses/MCE/Week3/meetings.csv"));
        while ((row = csv.readLine()) != null) {
            String[] r = row.split(",");
            meetings.add(r[0]);
        }
        
        BufferedReader emails = new BufferedReader(new FileReader("D:/Courses/MCE/Week3/projects.csv"));
        while ((row = emails.readLine()) != null) {
            String[] r = row.split(",");
            data.add(r[0]);
        }
        
        for (int i = 0; i < meetings.size(); i++){
            
            String student = meetings.get(i);
            if (!(data.contains(student))) {
                contained.add(student);
            }
        }
        
        for (int i = 0; i < contained.size(); i++){
            System.out.println(contained.get(i));
        }
        
    }
}
