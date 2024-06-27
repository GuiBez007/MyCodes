/*
	Name: InsertionSort.cpp 
	Author: GUilherme Bezerra
	Date: 15/05/24 09:48
	Description: Implementação do método de ordenação InsertionSort
*/

// Libraries
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <locale.h>

// Prototipation
void insertionSort(int *, int);

// Global vars
int comparacoes, trocas;

// Main function
main()
{
	setlocale(LC_ALL, "Portuguese");
	int numeros[] = {17, 24, -5, 8, 15, 10, 1, 19, 12, 3};
	int i;
	int tam = sizeof(numeros) / sizeof(int);
//	for (int i=0; i<tam; i++)
//	{
//		numeros[i] = rand()%100;
//	} IMPLEMENTAR DEPOIS
	
	puts("Vetor ORIGINAL:");
	for (i=0; i<tam; i++)
		printf("%i%s", numeros[i], (i==tam-1?"":"|"));
		
	insertionSort(numeros, tam);
	
	puts("\n\nVetor ORDENADO:");
	for (i=0; i<tam; i++)
		printf("%i%s", numeros[i], (i==tam-1?"":"|"));
	
	printf("\n\nComparações: %i \nTrocas: %i", comparacoes, trocas);
	
} // Fim do main


void insertionSort(int vet[], int tam)
{
	int i, j, chave;
	for (i=1; i<tam; i++)
	{
		comparacoes++; //
		chave = vet[i];
		j = i-1;
		
		while (j >= 0 && vet[j] > chave)
		{
			comparacoes++; //
			trocas++; //
			vet[j+1] = vet[j];
			j = j-1;
		}
		vet[j+1] = chave;	
	}
}
