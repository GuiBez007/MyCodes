/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe para instanciar objetos encapsulados da classe Conta
 * @author GUilherme Bezerra
 */
public class Banco {
    public static void main(String [] args) {
        Conta cc = new Conta("Sem Nome", 2000, 1234);
        cc.realizarSaque();
        cc.exibirDadosConta();
    }
    
} //fim da classe

// consultarSaldo() // trocarSenha() // depositarDinheiro() // "Senha inválida, vc tem mais X tentativas!"