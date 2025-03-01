package com.example.allinclassapplications;

public class CalculoIMC {
    public float peso;
    public float altura;
    public String resultado;


    // Método construtor
    public CalculoIMC(String peso, String altura) {
        try {
            this.peso = Float.parseFloat(peso);
            this.altura = Float.parseFloat(altura);
            resultado = "Seu IMC é de " + calcularResultado();
        } catch(Exception e) {
            resultado = "Algum dado está errado!";
        }
    }


    private String calcularResultado() {
        return String.valueOf(Math.round(peso/(altura*altura)));
    }


    // Método estático
    public static String calculaIMC(String pesoStr, String alturaStr) {
        try {
            float peso = Float.parseFloat(pesoStr);
            float altura = Float.parseFloat(alturaStr);
            return "Seu IMC é de " +  String.valueOf(Math.round(peso/(altura*altura)));
        } catch (Exception e) {
            return "Algum dado está errado!";
        }
    }
}
