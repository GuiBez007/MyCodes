/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 2830482311024
 */
public class Pessoas {
    String nome;
    int idade;
    float altura;
    float peso;
    
    //Construtor da classe
    public Pessoas(String nome, int idade, float altura, float peso){
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;
        this.peso = peso;
    }
    
    
    //Método para exibir os dados do objeto Pessoa
    public void exibirDadosPessoa(){
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
        System.out.println("Altura: " + altura);
        System.out.println("Peso: " + peso); 
    }
    
    
    public void calcularIMC(){
        System.out.println("IMC> " + peso/(altura * altura));
    }
    
}
