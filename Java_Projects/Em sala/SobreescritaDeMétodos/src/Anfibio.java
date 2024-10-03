/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 2830482311024
 */
public class Anfibio extends Animal {
    boolean pular;
    boolean venenoso;
    int temperatura;

    public Anfibio(String raça, int idade, String cor, boolean pular, boolean venenoso, int temperatura) {
        super(raça, idade, cor);
        this.pular = pular;
        this.venenoso = venenoso;
        this.temperatura = temperatura;
    }
    
    
    @Override
    public void exibirDadosAnimal() {
        System.out.println("O mamifero "+raça+" tem veneno: "+venenoso);
    }

    
    
    
    
    
    
}
