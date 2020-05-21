
/**
 *
 * @author Isaac Murisa 201534328
 */

/**
 * This class gets input from the customer
 * 
 */
import java.util.*;

public class DispenserRunner {
    
    public static void main(String[] args) throws IllegalArgumentException {
	Scanner in = new Scanner(System.in);
	
        //Arrays to hold the snacks and the price of each snack
	ArrayList<String> snacks = new ArrayList<String>();
	ArrayList<Double> prices = new ArrayList<Double>();
	
        //These are the products in the snack dispenser currently
	snacks.add("Doritos"); snacks.add("Ruffles"); snacks.add("HumtyDummty"); snacks.add("Chocolates");
	prices.add(2.00); prices.add(2.00);prices.add(1.00); prices.add(0.50);
        
        //this loop passes objects of type PrintSnacks to the PrintSnacks class.
        //so that the PrintSnacks prints the prduct details.
        for (int i = 0; i < snacks.size(); i++){
            PrintSnacks snp = new PrintSnacks(snacks.get(i), prices.get(i), i+1);
            snp.formart(); 
        }
        
        //This section prompts user what s\he wants to do
        System.out.println("\nWhat do you want to do? Enter the letter: \nA: Buy a product \nB: Add a product \nC:  Empty Coins  \nQ: Quit");
        String action;
        
        if (in.hasNext()){
            action = in.next();
        }
        else {
            throw new IllegalArgumentException("You didn't enter a letter corresponding to what you want to do");
        }
        
        /**
        * gets the number corresponding to the coin user wants to input
        * gets the type of snack the user wants
        * which is the number corresponding to the list of products
        */
        int coinAmount = 0; int productChoice = 1;
        if (action.equals("A") || action.equals("a")) {
            coinAmount = getCoins();
            
            //executed if the user wants to quit
            if (coinAmount == 8){
                Quit();
            }
            
            else {productChoice = getInput();}
        }
        
        
        
        /**
        * creates an SnackDispenser object
        */
        SnackDispenser sn = new SnackDispenser(snacks.get(productChoice-1), prices.get(productChoice-1), coinAmount);
        
        
        /**
         * Executed if the user wants to buy a product
         * This section gets the coin from user
         * gets change from the SnackDispenser class
         * gives the snack and change to the customer
         */
        if (action.equals("A") || action.equals("a")){   
            
            double change = sn.getChange();
            
            if (change == 0){
                System.out.println(sn.getSnack());
            }
            if (change == -1){
                System.out.println("Not enough coins. \nYou can get your coin $" + sn.getCoinValue(coinAmount));
            }
            else if (!(change == 0) && !(change == -1)){
                System.out.println(sn.getSnack() + change);
            }
        }
        
        /**
         * this section adds a new product to the snack dispenser
         * 
         */
        else if (action.equals("B") || action.equals("b")) {
            
            System.out.print("Enter the name of the product: ");
            if (in.hasNext()){
                String newProduct = in.next();
                snacks.add(newProduct);
            }
            else { System.out.println("You did not enter the product name."); }
            
            System.out.print("Enter the product price: ");
            if (in.hasNextDouble()){
                double newPrice = in.nextDouble();
                prices.add(newPrice);
            }
            else { System.out.println("You did not enter product price."); }
            System.out.println("Product succefully addded");
        }
        
        /**
         * Executed if the user wants to quit
         */
        else if (action.equals("Q") || action.equals("q")){
            Quit();
        }
        
        /**
         * Executed if the user wants to empty the coins
         */
        else if (action.equals("C") || action.equals("c")) {
           System.out.println("Coins successfully emptied. Total: $" + sn.TotalCoins());
           sn.removeCoins();
        }
        
        //if the user enters the wrong action letter
        else {System.out.println("You entered the wrong letter.");}
        
    }
    
    /**
     * This method gets the input corresponding to the product the product the user wants
     * @return the index corresponding to the product the user wants
     */
    public static int getInput() {
        Scanner in = new Scanner(System.in);
        int product = 0;
        
        System.out.println("\nEnter the number corresponding to the product you want: ");
        if (in.hasNextInt()){
            product = in.nextInt();
        }
        else {
            throw new IllegalArgumentException("You didn't enter the product number.");
        }
        return product;
    }
    
    /**
     * this method simulates a coin being entered into the snack dispenser
     * @return the index corresponding to the coin the user wants to insert
     */
    public static int getCoins(){
        Scanner in = new Scanner(System.in);
        System.out.println("Insert Coin by typing the coin number: \n1:  Two dollar coin \n2:  One dollar coin \n3:  "
                + "50 cent coin \n4:  25 cent coin  \n5:  10 cent coin \n6:  5 cent coin \n7:  1 cent coin \n8:  Quit");
        int coin = in.nextInt();
        return coin; 
    }
    
    /**
     * This method is called when someone quits. And prints out a confirmation.
     */
    public static void Quit() {
        System.out.println("Process stopped");
    }
}
