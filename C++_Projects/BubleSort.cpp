/*
	Name: BubleSort.cpp
	Author: GUilherme Bezerra
	Date: 14/05/24 18:46
	Description: Ordena valores utilizando BubleSort
*/

// Libraries
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <locale.h>

// Vari�veis Globais
// seria o mais certo, mas...

// Main Function
int main()
{
	setlocale(LC_ALL, "Portuguese");
	int quantidade, aux;
	int comparacoes, trocas;
	comparacoes = trocas = 0;
	
	printf("Quantidade de n�meros a serem gerados randomicamente: ");
	scanf(" %i", &quantidade);
	int numeros[quantidade];
	int tamanho = sizeof(numeros) / sizeof(int);
	
	// deixa de fato, aleat�rio
	srand(time(NULL));
	puts("\nLista original:");
	
	for (int i=0; i<quantidade; i++)
	{
		// gera n�meros de 0-100 e separa com "|" at� chegar no �ltimo n�mero
		numeros[i] = rand()%100;
		printf("%i%s", numeros[i], (i==quantidade-1)?"":"|"); // #if tern�rio
	}
	
	while (tamanho != 1)
	{
		for (int i=0; i<tamanho; i++)
		{
			comparacoes++;
			if (i == tamanho-1)
				tamanho--;

			else if (numeros[i+1] > numeros[i])
			{
				aux = numeros[i];
				numeros[i] = numeros[i+1];
				numeros[i+1] = aux;
				trocas++;
			}	
		}
	}
	
	puts("\n\nLista ordenada:");
	for (int i=0; i<quantidade; i++)
		printf("%i%s", numeros[i], (i==quantidade-1)?"":"|"); // #if tern�rio
	printf("\n\nCompara��es: %i \nTrocas: %i", comparacoes, trocas);
}
