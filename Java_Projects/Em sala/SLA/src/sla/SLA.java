/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sla;
import java.util.Scanner;
/**
 *
 * @ author GUilherme Bezerra
 * @ data: 26/08/24 11:30h
 */
public class SLA {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int number;
        
        System.out.print("Inform the number to calculate its table> ");
        number = input.nextInt();
        for (int i=0; i<10; i++){
            System.out.printf("%d%s%d%s%d%n", i+1, " * ", number, " = ", (i+1)*number);
        }
        
    }
    
}
