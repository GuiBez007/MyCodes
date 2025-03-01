package com.example.allinclassapplications;

import android.graphics.Color;

public class CalculoNotaFalta {
    public static String calcular(SituacaoActivity mAct) {
        float p1, p2, p3, media;
        int faltas;

        try {
            p1 = Float.parseFloat(mAct.txtP1.getText().toString());
            p2 = Float.parseFloat(mAct.txtP2.getText().toString());
            p3 = Float.parseFloat(mAct.txtP3.getText().toString());
            faltas = Integer.parseInt(mAct.txtFaltas.getText().toString());

            media = Math.max(p1, Math.max(p2, p3));
            if (p1 == media)
                media += Math.max(p2, p3);
            else if (p2 == media)
                media += Math.max(p1, p3);
            else
                media += Math.max(p1, p2);

            mAct.txtResultado.setTextColor(Color.RED);
            if ((media / 2) < 6 && faltas > 5)
                return "REPROVADO \npor falta e nota!";
            else if ((media / 2) < 6)
                return "REPROVADO \npor nota!";
            else if (faltas > 5)
                return "REPROVADO \npor falta!";
            else {
                mAct.txtResultado.setTextColor(Color.GREEN);
                return "APROVADO!";
            }
        } catch(Exception e) {
            mAct.txtResultado.setTextColor(Color.RED);
            return "Falta de dados para \nefetuar verificação!";
        }
    }
}
