/*
	Name: Formas de Pagamento
	Author: GUilherme Bezerra
	Date: 04/09/23 18:44
	Description: Calcula o pre�o final de uma compra
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	float preco, total;
	int codigo;
	
	//Soma o pre�o de todos os produtos informados
	puts("Digite abaixo o pre�o dos produtos:\nUse 0 para parar ");
	while (true){
		scanf("%f", &preco);
		total = total + preco;
		if (preco == 0)
			break;
		fflush(stdin);
		//Pesquisei na internet e esse fflush resolveu o problema. N�o sei pra que serve direito mas t� valendo
	}
	preco = total;
	
	//Parte visual(formas de pagamento)
	puts("\nC�DIGO            FORMA DE PAGAMENTO                  DESCONTO OU ACR�SCIMO	   \
		\n  1               Dinheiro (� vista)                     Desconto de 15%	 	   \
		\n  2               Cart�o de D�bito                       Desconto de 10%	 	   \
		\n  3            Cart�o de Cr�dito (� vista)  	         Desconto de 5%	 	       \
		\n  4           Cart�o de Cr�dito (em at� 3x)	    Sem desconto ou acr�scimo      \
		\n  5         Cart�o de Cr�dito (em mais de 3x)            Acr�scimo de 5%	       ");
	printf("\nDigite o c�digo referente a forma de pagamento: ");
	scanf("%i", &codigo);
	
	//C�lculo e sa�da final
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
