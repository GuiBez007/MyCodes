/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe para herdar atributos e métodos da superclasse Veículos
 * @author 2830482311024
 */
public class Caminhao extends Veiculo {
    String tipoCarroceria;
    int nEixos;
    int qntdPneus;
    boolean refrigerado;


    
    //Método construtor da classe Caminhão
    public Caminhao(String marca, String modelo, int ano, float valor, String tipoCarroceria, int nEixos, int qntdPneus, boolean refrigerado) {
        super(marca, modelo, ano, valor);
        this.tipoCarroceria = tipoCarroceria;
        this.nEixos = nEixos;
        this.qntdPneus = qntdPneus;
        this.refrigerado = refrigerado;
    }
    
    
    //Método comum para exibir dados do caminhão
    public void exibirDadosCaminhao() {
        System.out.println("Tipo de carroceria: " + tipoCarroceria);
        System.out.println("Número de eixos: " + nEixos);
        System.out.println("Quantidade de pneus: " + qntdPneus);
        System.out.println("É refrigerado: " + (refrigerado?"Sim":"Não"));
    }
    
} //Fim da classe
