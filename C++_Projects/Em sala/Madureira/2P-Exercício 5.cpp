/*
	Name: Operações "Infinitas"
	Author: GUilherme Bezerra
	Date: 04/09/23 17:43
	Description: Realiza operações com números armazenados em um vetor
*/

//Libraries
#include <stdio.h>
#include <locale.h>
#include <math.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int numero[150];
	float quadrado, cubo, raiz;
	
	//Inicializa(com -1) todo o vetor
	for (int i=0; i<150; i++)
		numero[i] = -1;
	puts("Digite os números que deseja operar:");
	
	//Armazena os números em um vetor
	for (int i=0; i<150; i++){
		scanf("%i", &numero[i]);
		if (numero[i] <= 0)
			break;
	} //Caso menor que 0, quebra
	
	//Executa cálculos até onde o vetor foi preenchido e mostra na tela
	puts("\nNúmero           Quadrado             Cubo        Raíz");
	for (int i=0; i<150; i++){
		if (numero[i] <= 0)
			break;
		quadrado = numero[i] *numero[i];
		cubo = numero[i] *numero[i] *numero[i];
		raiz = sqrt(numero[i]);
		printf("%6.i           %.0f                %7.0f           %.4f\n", numero[i], quadrado, cubo, raiz);
	}
	
getchar();
return 0;
	
}
