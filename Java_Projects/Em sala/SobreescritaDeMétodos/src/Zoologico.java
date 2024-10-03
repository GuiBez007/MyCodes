/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe para instanciar os diversos tipos de animais
 * @author 2830482311024
 */
public class Zoologico {
    public static void main(String [] args) {
        Mamifero gato = new Mamifero("Siames",3,"bege e preto",true,4,8);
        gato.alimentarAnimal("aux");
        
        Anfibio sapo = new Anfibio("<name>",3,"verde",true,false,22);
        sapo.exibirDadosAnimal();
    }
    
}
