package com.example.allinclassapplications;

import android.app.Activity;
import android.view.View;

public class CalculoDeBases {
    public static String mudarBase(int aux) {
        if (aux == 0)
            return "Binário";
        else if (aux == 1)
            return "Hexadecimal";
        else if (aux == 2)
            return "Octal";
        else//if (aux == 3)
            return "Decimal";
    }

    public String calcular(ConversaoActivity mAct) {
        String numero = mAct.txtNumeroOriginal.getText().toString();
        String base = mAct.txtBase.getText().toString();
        int aux1 = mAct.aux1;
        int aux2 = mAct.aux2;

        try {
            if (aux2 == 0) {
                mAct.txtNovaBase.setText("Binário");
                return calcular(numero, base, "0");
            } else if (aux2 == 1) {
                mAct.txtNovaBase.setText("Hexadecimal");
                return calcular(numero, base, 0f);
            } else if (aux2 == 2) {
                mAct.txtNovaBase.setText("Octal");
                return calcular(numero, base, '0');
            } else{//if (aux2 == 3) {
                mAct.txtNovaBase.setText("Decimal");
                return calcular(numero, base, false);
            }
        } catch (Exception e) {
            mAct.txtNovaBase.setText("");
            return "Campo vazio ou \nvalor inválido!";
        }
    }


    // Método para calcular Decimal
    private String calcular(String numero, String base, boolean x) {
        if (base.equals("Binário"))
            return String.valueOf(Integer.parseInt(numero, 2));
        else if (base.equals("Hexadecimal"))
            return String.valueOf(Integer.parseInt(numero, 16));
        else if (base.equals("Octal"))
            return String.valueOf(Integer.parseInt(numero, 8));
        return numero;
    }


    // Método para calcular Binário (transforma em decimal e depois outra)
    private String calcular(String numero, String base, String x) {
        if (base.equals("Decimal"))
            return Integer.toBinaryString(Integer.parseInt(numero));
        else if (base.equals("Hexadecimal"))
            return Integer.toBinaryString(Integer.parseInt(numero, 16));
        else if (base.equals("Octal"))
            return Integer.toBinaryString(Integer.parseInt(numero, 8));
        return numero;
    }


    // Método para calcular Hexadecimal (transforma em decimal e depois outra)
    private String calcular(String numero, String base, float x) {
        if (base.equals("Decimal"))
            return Integer.toHexString(Integer.parseInt(numero));
        else if (base.equals("Binário"))
            return Integer.toHexString(Integer.parseInt(numero, 2));
        else if (base.equals("Octal"))
            return Integer.toHexString(Integer.parseInt(numero, 8));
        return numero;
    }


    // Método para calcular Octal (transforma em decimal e depois outra)
    private String calcular(String numero, String base, char x) {
        if (base.equals("Decimal"))
            return Integer.toOctalString(Integer.parseInt(numero));
        else if (base.equals("Binário"))
            return Integer.toOctalString(Integer.parseInt(numero, 2));
        else if (base.equals("Hexadecimal"))
            return Integer.toOctalString(Integer.parseInt(numero, 16));
        return numero;
    }

}
