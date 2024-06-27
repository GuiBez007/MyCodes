/*
	Name: Vetores
	Author: GUilherme Bezerra
	Date: 28/08/2023 09:00h
	Description: Armazena e utiliza valores de um vetor
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	float vet[2], resultado;
	
	for (int i=0; i<2; i++){
		if (i == 0)
			printf("Digite o valor da base: ");
		else 
			printf("Digite o valor da altura: ");
		scanf("%f", &vet[i]);
	}
	resultado = (vet[0] * vet[1]) /2;
	printf("\nA área de um triângulo-retângulo de %.2f de base e %.2f de altura é:\n           -> %.2f <-", vet[0], vet[1], resultado);

getchar();
return 0;
	
}
