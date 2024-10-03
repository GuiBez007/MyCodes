/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe que herda da classe pai Animal
 * @author 2830482311024
 */
public class Mamifero extends Animal {
    boolean pelo;
    int quantidadePatas;
    int tetos;
    
    
    public Mamifero(String raça, int idade, String cor, boolean pelo, int quantidadePatas, int tetos) {
        super(raça, idade, cor);
        this.pelo = pelo;
        this.quantidadePatas = quantidadePatas;
        this.tetos = tetos;
    }
    
    
    @Override
    public void exibirDadosAnimal() {
        System.out.println("O mamifero "+raça+" tem "+quantidadePatas+" patas.");
    }
    
    
    @Override
    public void alimentarAnimal() {
        System.out.println("O animal se alimenta de leite");
        System.out.println("Depois ele pode se tornar carnivoro ou não");
    }
    
    
    public void alimentarAnimal(String gyd) {
        System.out.println("Sobrecarga");
    }
    
}
