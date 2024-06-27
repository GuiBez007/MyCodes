/*
	Name: ShellSort.cpp 
	Author: GUilherme Bezerra
	Date: 15/05/24 10:22
	Description: Implementação do método de ordenação ShellSort
*/

// Libraries
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <locale.h>

// Prototipation
void shellSort(int *, int);

// Global vars
int comparacoes, trocas;

// Main function
main()
{
	// {17, 24, -5, 8, 15, 10, 1, 19, 12, 3}
	setlocale(LC_ALL, "Portuguese");
	int quantidade, i;
	
	printf("Quantidade de números a serem gerados: ");
	scanf(" %i", &quantidade);
	
	int numeros[quantidade];
	int tam = sizeof(numeros) / sizeof(int);
	
	for (int i=0; i<tam; i++)
	{
		numeros[i] = rand()%100;
	} 
	
	puts("\nVetor ORIGINAL:");
	for (i=0; i<tam; i++)
		printf("%i%s", numeros[i], (i==tam-1?"":"|"));
		
	shellSort(numeros, tam); // chamada da função
	
	puts("\n\nVetor ORDENADO:");
	for (i=0; i<tam; i++)
		printf("%i%s", numeros[i], (i==tam-1?"":"|"));
		
	printf("\n\nComparações: %i \nTrocas: %i", comparacoes, trocas);
} // Fim do main


void shellSort(int vet[], int tam)
{
	int i, j, chave;
	int h = 1;
	comparacoes = trocas = 0;
	
	while (h < tam)
	{
		h = 3*h+1;
	}
	
	while (h > 0)
	{
		for (i=h; i<tam; i++)
		{
			comparacoes++; //
			chave = vet[i];
			j = i;
			
			while (j > h-1 && chave <= vet[j-h])
			{
				trocas++; //
				vet[j] = vet[j-h];
				j = j-h;
			}
			vet[j] = chave;
		}
		h = h/2;
	}
}
