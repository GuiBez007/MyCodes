
import javax.swing.JOptionPane;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe para demonstrar o princípio do Encapsulamento
 * @author GUilherme Bezerra
 * @since 17/10/2024
 */
public class Conta {
    private String cliente;
    private float saldo;
    private int senha;
    private boolean bloqueado;
    private int tentativas;
    
    
    // Construtor da classe
    public Conta(String cliente, float saldo, int senha) {
        this.cliente = cliente;
        this.saldo = saldo;
        this.senha = senha;
        this.bloqueado = false;
        this.tentativas = 0;
    }
    

    //Exibi dados
    public void exibirDadosConta() {
        System.out.println("Nome do cliente> " + cliente);
        System.out.println("Saldo> " + saldo);
        System.out.println("Conta bloqueada? " + (isBloqueado() == true?"Sim":"Não"));
    }
    
    
    public void realizarSaque() {
        int pwd = 0;
        pwd = Integer.valueOf(JOptionPane.showInputDialog("Informe a senha:"));
        
        if (!verificarSenha(pwd)) {
            JOptionPane.showMessageDialog(null, "Senha inválida!");
            if(!isBloqueado())
                realizarSaque();
        }
        else {
            float vlrSaque = 0;
            vlrSaque = Float.valueOf(JOptionPane.showInputDialog("informe o valor do saque:"));
            if(getSaldo() < vlrSaque)
                JOptionPane.showMessageDialog(null, "Saldo insulficiente!");
            else
                setSaldo(getSaldo()-vlrSaque);    
        }
    }
    
    
    //Método para verificar senha
    private boolean verificarSenha(int pwd) {
        if(pwd == getSenha())
            return true;
        else {
            if(tentativas > 1) {
                JOptionPane.showMessageDialog(null, "Conta bloqueada!");
                setBloqueado(true);
            }
            else
                tentativas++;
            return false;
        }
    }
    
    
    // Métodos assessores
    private void setCliente(String cliente) {
        this.cliente = cliente;
    }    
    
    private String getCliente() {
        return this.cliente;
    }     
    
    private void setSaldo(float saldo) {
        this.saldo = saldo;
    }    
    
    private float getSaldo() {
        return this.saldo;
    }     
    
    private void setSenha(int senha) {
        this.senha = senha;
    }    
    
    private int getSenha() {
        return this.senha;
    }

    private boolean isBloqueado() {
        return bloqueado;
    }

    private void setBloqueado(boolean bloqueado) {
        this.bloqueado = bloqueado;
    }
    
} //fim da classe
