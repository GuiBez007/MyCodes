/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 2830482311024
 */
public class Pessoa {
    public static void main(String [] args){
        float div;
        String num1, num2; 
        
        num1 = JOptionPane.showInputDialog("Digite o valor do número> ");
        num2 = JOptionPane.showInputDialog("Digite o valor do número> ");
        div = (float)num1/num2;
        
        JOptionPane.showMessageDialog(null, "Divisão -> "+div);
    }
}
