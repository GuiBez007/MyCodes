/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe para demonstrar o principio de Herança em uma modelagem
 * @author 2830482311024
 */
public class Veiculo {
    String marca;
    String modelo;
    int ano;
    float preço;
    
    //Construtor da classe

    public Veiculo(String marca, String modelo, int ano, float preço) {
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.preço = preço;
    }
    
    
    public void exibirDadosVeiculo() {
            System.out.println("Marca do veículo: " + marca);
            System.out.println("Modelo do veículo: " + modelo);
            System.out.println("Ano do veículo: " + ano);
            System.out.println("Preço do veículo: " + preço);
    }
    
} //Fim da classe
