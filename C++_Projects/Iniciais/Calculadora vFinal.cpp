/*	
	Name: Calculadora
	Author: GUilherme Bezerra
	Date: 15/04/2023 14:55
	Description: Executa as seguintes opera��es: ("/*+-"). 	
*/
//char sinal[5]; scanf ("%*f"); elimina
//sinal[1] = ' '; sinal[2] = ' '; sinal[3] = ' '; sinal[4] = ' '; sinal[5] = ' ';

//Se��o de Importa��o de Bibliotecas
#include <stdio.h>
#include <locale.h>

main(){
	setlocale (LC_ALL, "Portuguese");
	int i;
	float resultado_n1, n2;
	char sinal[2];
	resultado_n1 = 0.0;
	
	puts ("CALCULADORA DE ADD, SUB, MULT, DIV (+-*/)");
	puts ("Para encerrar atividade, digite 'P'!");
	puts ("===========================================");
	scanf ("%f", &resultado_n1);
	
	i = 0;
		while (i < 1500){
			sinal[1] = ' '; sinal[2] = ' '; n2 = 0.0; //zera para evitar erros
			scanf (" %c", &sinal[1]); //recebe o sinal
			
			if (sinal[1] == 'p' || sinal[1] == 'P'){ //digitar 'p' para encerrar
				printf ("C�LCULO FINALIZADO!");
				i = 1500;}
			else if (sinal[1] == '+' ){ //realiza a Adi��o
				scanf ("%f", &n2);
				resultado_n1 = resultado_n1 + n2;
				printf ("%.2f         > ", resultado_n1);}
			else if (sinal[1] == '-' ){ //realiza a Subtra��o
				scanf ("%f", &n2);
				resultado_n1 = resultado_n1 - n2;
				printf ("%.2f         > ", resultado_n1);}
			else if (sinal[1] == '*' ){ //realiza a Multiplica��o
				scanf ("%f", &n2);
				resultado_n1 = resultado_n1 * n2;
				printf ("%.2f         > ", resultado_n1);}
			else if (sinal[1] == '/' ){ //realiza a Divis�o
				scanf ("%f", &n2);
				resultado_n1 = resultado_n1 / n2;
				printf ("%.2f         > ", resultado_n1);}
			else if (sinal[1] != '+' && sinal[1] != '-' && sinal[1] != '*' && sinal[1] != '/' ){
				printf ("\nOpera��o/sinal Inv�lido(a)!\n�ltimo resultado:\n%.2f         > ", resultado_n1);
				printf ("");}
			i = i + 1;}
}
