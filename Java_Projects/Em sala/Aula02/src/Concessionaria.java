/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 2830482311024
 */
public class Concessionaria {
    public static void main(String[] args) {
        Carro carro = new Carro("Chevrolet", "Opala", 1977, (float)45000.9, 4.1f, 450, 5);
        //carro.exibirDadosVeiculo();
        //carro.exibirDadosCarro();
        
        Teste aux = new Teste("Chevrolet", "Opala", 1977, (float)45000.9, 4.1f, 450, 5, "Teste OK");
        System.out.println(aux.var);
    }
    
} //Fim da classe

//se tiver 3 classes, como que faz pra mostrar dados da primeira e da segunda a partir da terceira?
//preciso parametrizar tudo de outras classes pai no construtor da classe atual ou somente da última classe pai?