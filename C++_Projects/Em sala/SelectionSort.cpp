/*
	Name:  SelectionSort.cpp
	Author: GUilherme Bezerra
	Date: 08/05/24 10:10
	Description: Implementação do algoritmo de selection sort
*/

// Libraries
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Global
int vet[] = {17, 24, -5, 8, 15, 10, 1, 19, 12, 3};
int trocas, comparacoes;
int big_vet[100]; //#

main()
{
	srand(time(NULL)); //SEED padr
	
	
	for (int i=0; i<100; i++)
	{
		big_vet[i] = rand()%100;
		printf("%d ", big_vet[i]);
	}
	
	trocas = comparacoes = 0;
	int i, j, aux, menor, tam;
	tam = sizeof(vet) / sizeof(int);
	
	printf("\nVetor original: \n|");
	for (i=0; i<tam; i++)
		printf("%d|", vet[i]);
		
	for (i=0; i<tam; i++)
	{
		menor = i;
		for (j=i+1; j<tam; j++)
		{
			comparacoes++; //
			if (vet[j] < vet[menor])
				menor = j;
		}
		comparacoes++; //
		
		if (menor != j)
		{
			aux = vet[i];
			vet[i] = vet[menor];
			vet[menor] = aux;
			trocas++; //
			//comparacoes++; //
		}
	}
	
	printf("\n\nApós selection sort: \n|");
	for (i=0; i<tam; i++)
		printf("%d|", vet[i]);
	printf("\nTrocas: %d   |   Comparações: %d", trocas, comparacoes);
}
