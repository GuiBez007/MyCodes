/*
	Name: Formas de Pagamento
	Author: GUilherme Bezerra
	Date: 04/09/23 18:44
	Description: Calcula o preço final de uma compra
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	float preco, total;
	int codigo;
	
	//Soma o preço de todos os produtos informados
	puts("Digite abaixo o preço dos produtos:\nUse 0 para parar ");
	while (true){
		scanf("%f", &preco);
		total = total + preco;
		if (preco == 0)
			break;
		fflush(stdin);
		//Pesquisei na internet e esse fflush resolveu o problema. Não sei pra que serve direito mas tá valendo
	}
	preco = total;
	
	//Parte visual(formas de pagamento)
	puts("\nCÓDIGO            FORMA DE PAGAMENTO                  DESCONTO OU ACRÉSCIMO	   \
		\n  1               Dinheiro (à vista)                     Desconto de 15%	 	   \
		\n  2               Cartão de Débito                       Desconto de 10%	 	   \
		\n  3            Cartão de Crédito (à vista)  	         Desconto de 5%	 	       \
		\n  4           Cartão de Crédito (em até 3x)	    Sem desconto ou acréscimo      \
		\n  5         Cartão de Crédito (em mais de 3x)            Acréscimo de 5%	       ");
	printf("\nDigite o código referente a forma de pagamento: ");
	scanf("%i", &codigo);
	
	//Cálculo e saída final
	switch (codigo){
		case 1:
			total = preco - (preco/100)*15;
			break;
		case 2:
			total = preco - (preco/100)*10;
			break;
		case 3:
			total = preco - (preco/100)*5;
			break;
		case 4:
			total = preco - (preco/100)*0;
			break;
		case 5:
			total = preco + (preco/100)*5;
			break;
	}
	printf("Valor total: R$%.2f\nValor total com a forma de pagamento: R$%.2f",preco, total);
	
getchar();
return 0;
	
}
