
 /**
 *
 * @author Isaac Murisa 201534328
 */

//gets objects from the Dispenser Input class
public class SnackDispenser {
    private String snack;
    private double price;
    private double coin;
    
    //Current coins in the dispenser.
    private static double totalCoins = 5.00;
    
    //Constructor for the Snack Dispenser class
    public SnackDispenser(String a, double b, int c){
        snack = a;
        price = b;
        coin = this.getCoinValue(c);
    }
    
    /**
     * This method gets the snack the customer chose.
     * @return returns a print statement to print the chosen product.
     */
    public String getSnack() {
        
        //gets the change amount to determine if there is any change. If its zero the output statement differs
        double chn = this.getChange(); String printStatement;
        
        if (chn == 0){
            printStatement = "You can get your snack: " + snack +  "\nYou don't have any change";
        }
        else { printStatement = "You can get your snack: " + snack + "\nAnd your change: $";}
        return printStatement ;
    }
    
    /**
     * This method calculates the change 
     * @return return the change amount if the money is not enough it returns -1
     */
    public double getChange() {
        double change =0;
        if (price <= coin) {
            change = coin - price;
        }
        else {change = -1; }
        return change;
    }
    
    /**
     * Computes the total coins 
     */
    public double TotalCoins() {
        totalCoins = totalCoins + coin;
        return totalCoins;
    }
    
    /**
     * Empties the coins
     */
    public void removeCoins() {
        totalCoins = 0;
    }
    
    /**
     * This method sets the monetary value of the coin
     * @param m the number corresponding to the coin selected
     * @return the actual coin value of the coin selected
     */
    public double getCoinValue(int m) {
        double coinValue = 0;
        if (m == 1) { coinValue = 2.0;}
        if (m == 2) { coinValue = 1.0;}
        if (m == 3) { coinValue = 0.5;}
        if (m == 4) { coinValue = 0.25;}
        if (m == 5) { coinValue = 0.10;}
        if (m == 6) { coinValue = 0.05;}
        if (m == 7) { coinValue = 0.01;}
        return coinValue;
    }
}
