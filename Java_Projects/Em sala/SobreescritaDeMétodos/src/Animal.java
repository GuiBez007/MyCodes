/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import javax.swing.JOptionPane;
/**
 *
 * @author 2830482311024
 */
public class Animal {
    String raça;
    int idade;
    String cor;

    public Animal(String raça, int idade, String cor) {
        this.raça = raça;
        this.idade = idade;
        this.cor = cor;
    }
    
    
    public Animal() {
        this.raça = jOptionPane.showInputDialog("Informe a raça: ");
        this.idade = jOptionPane.showInputDialog("Informe a raça: ");
        this.cor = jOptionPane.showInputDialog("Informe a raça: ");
    }
    
    
    public void exibirDadosAnimal() {
        System.out.println("");
    }
    
    
    public void alimentarAnimal() {
        System.out.println("");
    }
        
}
