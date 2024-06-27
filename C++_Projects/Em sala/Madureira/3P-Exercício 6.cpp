/*
	Name: Insolucionável
	Author: GUilherme Bezerra
	Date: 10/09/23 13:35
	Description: Não funciona -_-
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	char nome_presidente[7][26] = {"José Sarney", "Fernando Collor de Mello", "Itamar Franco",\
		 "Fernando Henrique", "Luiz Inácio Lula da Silva", "Dilma Rousseff"},
		 ano_posse[7][5] = {"1985", "1990", "1992", "1995", "2003", "2011"},
		 matriz[3] = {nome_presidente[7], ano_posse[7]},
		 //[Error] invalid conversion from 'char*' to 'char' [-fpermissive]
		 ano_atual;
	
//	printf("%s", matriz[0]);
	scanf("%s", &ano_atual);
	
getchar();	
return 0;
	
}
