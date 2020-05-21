/**
 * this class prints all the products in the snack dispenser.
 */
/**
 *
 * @author Isaac Murisa 201534328
 */

public class PrintSnacks {
    private String snack;
    private double price;
    private int index;
    
    //constructor for the class
    public PrintSnacks(String a, double b, int c){
        snack = a;
        price = b;
        index = c;
    }
    
    public void formart() {
        System.out.println(index + ": Product: " + snack + ".    Price: " + price);
    }
}
