/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package prog6;
import java.util.Scanner;

/**
 * @author: GUilherme Bezerra
 * @RA: 2830482311024
 * @date: 26/08/24 09:24h 
 */
public class Prog6 {
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int number;
        int sum = 0;
        
        Scanner input = new Scanner(System.in);
        
        for (int i=0; i<2; i++){
            System.out.printf("%s%d%s", "Informe o ", i+1, "° número: ");
            number = input.nextInt();
            sum = sum + number;
        }
        System.out.printf("%s%d%n", "A soma desses números é> ", sum);
    }
    
}
