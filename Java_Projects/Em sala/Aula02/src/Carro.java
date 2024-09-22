/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe herdeira de Veiculo
 * @author 2830482311024
 */
public class Carro extends Veiculo{
    float potencia;
    int volumePM;
    int numPass;
    
    
    public Carro(String marca, String modelo, int ano, float valor, float potencia, int volumePM, int numPass) {
        super(marca, modelo, ano, valor);
        this.potencia = potencia;
        this.volumePM = volumePM;
        this.numPass = numPass;
    }
    
    
    //Método comum para exibir os dados do carro
    public void exibirDadosCarro() {
            System.out.println("Potência: " + potencia);
            System.out.println("Volume do porta-malas: " + volumePM);
            System.out.println("Número de passageiros: " + numPass);
    }
    
}//Fim da classe