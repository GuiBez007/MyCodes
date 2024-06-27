/*
	Name: Sal�rio Fam�lia
	Author: GUilherme Bezerra
	Date: 04/09/23 16:50
	Description: Define se o funcion�rio tem direito ao sal�rio fam�lia ou n�o
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int filhos;
	float salario, aumento;
	
	//Pega o sal�rio do funcion�rio
	
	puts("VEJA AQUI SE TEM DIREITO AO SAL�RIO FAM�LIA");
	printf("Informe seu sal�rio: ");
	scanf("%f", &salario);
	
	//Pega a quantidade de filhos
	printf("Quantidade de filhos: ");
	scanf("%i", &filhos);
	
	//Executa as condi��es
	if (salario <= 808.80)
		aumento = 41.27 *filhos;
	else if (salario < 1212.64)
		aumento = 29.16 *filhos;
		
	//Sa�da final
	if (salario > 1212.64)
		printf("N�o tem direito! Sal�rio acima do permitido!");
	else if (aumento == 0)
		printf("N�o tem direito! O sal�rio fam�lia � destinado somente a quem t�m filhos!");
	else
		printf("Voc� tem direito ao sal�rio fam�lia, no valor de: R$%.2f", aumento);
	
getchar();
return 0;
	
}
