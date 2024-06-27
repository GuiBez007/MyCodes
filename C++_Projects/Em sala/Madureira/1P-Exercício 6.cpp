/*
	Name: Salários
	Author: GUilherme Bezerra
	Date: 04/09/23 16:30
	Description: Indica o salário referente ao total de horas trabalhadas
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int codigo; 
	float horas_trabalhadas, total;
	
	//Instrução visual
	printf("CÓDIGO        	  CARGO		  \
			\n  1   	 Administrador de Dados	  \
			\n  2   	 Analista de Suporte	  \
			\n  3   	 Analista Programador 	  \
			\n  4   	 Programador	  \n");
	printf("\nInforme o código correspondente ao seu cargo: ");
	scanf("%i", &codigo);
	printf("Horas trabalhadas no mês: ");
	scanf("%f", &horas_trabalhadas);
	
	//Condições para modificar os valores
	if (codigo == 1)
		total = horas_trabalhadas *45.32;
	else if (codigo == 2)
		total = horas_trabalhadas *32.23;
	else if (codigo == 3)
		total = horas_trabalhadas *47.25;
	else if (codigo == 4)
		total = horas_trabalhadas *33.70;
	
	//Saída final	
	printf("Seu salário é de RS%.2f", total);
	
getchar();
return 0;	
	
}
