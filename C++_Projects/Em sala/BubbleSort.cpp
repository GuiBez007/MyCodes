/*
	Name: BubbleSort.cpp
	Author: GUilherme Bezerra
	Date: 24/04/24 09:47
	Description: Implementação do método de ordenação Bubble Sort
*/

// Libraries 
#include <stdio.h>
#include <conio.h>

// Prototipation
void Print();

// Variáveis Globais
int vet[] = {17, 24, -5, 8, 15, 10, 1, 19, 12, 3};
int trocas, comparacoes;

//Main Function
main()
{
	int tam = sizeof(vet) / sizeof(int);
	int i, j, aux;
	
	
	printf("Vetor DESORDENADO:");
	Print();
	printf("\n\nVetor ORDENADO:");
	
	
	// Ordenação dos dados em Bubble Sort
	j=0;
	while (j<tam)
	{
		for (i=0; i< tam-1; i++)
		{
			comparacoes++;
			if (vet[i] < vet[i+1]) //T
			{
				aux = vet[i+1];
				vet[i+1] = vet[i];
				vet[i] = aux;
				trocas++;
			}
		}
		tam--;
	}
	Print(); //Printa
}


void Print()
{
	int tam = 10;
	puts("");
	for (int i=0; i<tam; i++)
	{
		printf("%d|", vet[i]);
	}
	
	printf("\nComparacoes: %d \nTrocas: %d", comparacoes, trocas);
}
