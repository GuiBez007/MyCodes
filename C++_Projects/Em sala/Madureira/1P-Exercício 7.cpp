/*
	Name: Salário Família
	Author: GUilherme Bezerra
	Date: 04/09/23 16:50
	Description: Define se o funcionário tem direito ao salário família ou não
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int filhos;
	float salario, aumento;
	
	//Pega o salário do funcionário
	
	puts("VEJA AQUI SE TEM DIREITO AO SALÁRIO FAMÍLIA");
	printf("Informe seu salário: ");
	scanf("%f", &salario);
	
	//Pega a quantidade de filhos
	printf("Quantidade de filhos: ");
	scanf("%i", &filhos);
	
	//Executa as condições
	if (salario <= 808.80)
		aumento = 41.27 *filhos;
	else if (salario < 1212.64)
		aumento = 29.16 *filhos;
		
	//Saída final
	if (salario > 1212.64)
		printf("Não tem direito! Salário acima do permitido!");
	else if (aumento == 0)
		printf("Não tem direito! O salário família é destinado somente a quem têm filhos!");
	else
		printf("Você tem direito ao salário família, no valor de: R$%.2f", aumento);
	
getchar();
return 0;
	
}
