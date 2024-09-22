/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 2830482311024
 */
public class Cadastro {
    public static void main(String []args){
        Pessoas a, b, c;
        a = new Pessoas("Gui", 20, 1.75f, 80);
        b = new Pessoas("Deocleciana", 99, 1.20f, 100.6f);
        
        a.exibirDadosPessoa();
        b.exibirDadosPessoa();
        a.calcularIMC();
    }
}
