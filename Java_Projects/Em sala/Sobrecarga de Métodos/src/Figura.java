/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import javax.swing.JOptionPane;

/**
 *
 * @author 2830482311024
 */
public class Figura {
    private Integer a, b, c, d;
    
    
    //Construtor para um Ponto
    public Figura(int a) {
        this.a = a;
    }
    
    
    //Construtor para uma Linha
    public Figura(int a, int b) {
        this.a = a;
        this.b = b;
    }
    
    
    //Construtor para uma Triangulo
    public Figura(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    
    
    //Construtor para uma Retangulo
    public Figura(int a, int b, int c, int d) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }
    
    //Método comum que identifique o tipo de objeto
    public void exibirFigura() {
        
        if (a != null && b == null && c == null && d == null)
            exibirFigura(1);
        else if (a != null && b != null && c == null && d == null)
            exibirFigura(1.0f);
        else if (a != null && b != null && c != null && d == null)
            exibirFigura(true);
        else if (a != null && b != null && c != null && d != null)
            exibirFigura("1");
    }
    
    //Método para exibir os dados de um ponto
    private void exibirFigura(int x) {
        System.out.println("É um ponto de valor: " + a);
    }
    
    
    //Método para exibir os dados de uma linha
    private void exibirFigura(float x) {
        System.out.println("É uma linha de coordenadas: " + a + b);
    }   
    
    
    //Método para exibir os dados de um triangulo
    private void exibirFigura(boolean x) {
        System.out.println("É um triangulo de medidas: " + a + b + c);
    }
    
    
    //Método para exibir os dados de um retangulo
    private void exibirFigura(String x) {
        System.out.println("É um retangulo de medidas: " + a + b + c + d);
        
    }
}
