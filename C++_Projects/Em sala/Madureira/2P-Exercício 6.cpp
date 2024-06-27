/*
	Name: Perímetro de Polígono
	Author: GUilherme Bezerra
	Date: 04/09/23 18:28
	Description: Calcula o perímetro de polígonos
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int quantidade_lados;
	float tamanho[15], soma_total;
	soma_total = 0.0;
	
	//Inicializa todo o vetor
	for (int i=0; i<15; i++)
		tamanho[i] = 0;
	puts("Quantos lados têm seu polígono?");
	scanf("%i", &quantidade_lados);
	
	//Pega o tamanho de cada lado do polígono
	puts("\nInforme abaixo a medida de cada lado:");
	for (int i=0; i<quantidade_lados; i++){
		scanf("%f", &tamanho[i]);
		soma_total = soma_total + tamanho[i];
	}
	printf("\nO perímetro desse polígono é de %f", soma_total);
	
getchar();
return 0;	
	
}
