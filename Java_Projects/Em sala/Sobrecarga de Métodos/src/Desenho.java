/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author 2830482311024
 */
public class Desenho {
    public static void main(String[] args) {
        Figura fPoint = new Figura(1);
        Figura fLine = new Figura(1, 2);
        Figura fTriangle = new Figura(1, 2, 3);
        Figura fRetangle = new Figura(1, 2, 3, 4);
        
        fPoint.exibirFigura();
        fLine.exibirFigura();
        fTriangle.exibirFigura();
        fRetangle.exibirFigura();
        
//        fPoint.exibirFigura(1);
//        fLine.exibirFigura(1.f);
//        fTriangle.exibirFigura(true);
//        fRetangle.exibirFigura("1");
    }
}
