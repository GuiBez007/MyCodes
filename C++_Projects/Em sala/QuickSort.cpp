/*
	Name: QuickSort.cpp 
	Author: GUilherme Bezerra
	Date: 29/05/24 09:46
	Description: Implementação do método de ordenação QuickSort
*/

// Libraries
#include <stdio.h>
#include <conio.h>

// Prototipation
void quickSort(int*, int, int);
int particionar(int*, int, int);

// Global vars
int vet[] = {17,24,-5,8,15,10,1,19,12,3};
int tam;
int comparacoes, trocas;

main()
{
	int i;
	tam = sizeof(vet) / sizeof(int);
	comparacoes = trocas = 0;
	
	puts("Vetor DESORDENADO:");
	for (int i=0; i<tam; i++)
		printf("%i|", vet[i]);
		
	quickSort(vet, 0, tam-1);
	
	puts("\n\nVetor ORDENADO:");
	for (int i=0; i<tam; i++)
		printf("%i|", vet[i]);
	printf("\nTrocas: %i", trocas);
	printf("\nComparações: %i", comparacoes);
	
} // fim do main


void quickSort(int *V, int inicio, int fim)
{
	int pivot;
	if(fim > inicio)
	{
		pivot = particionar(V, inicio, fim);
		quickSort(V, inicio, pivot-1);
		quickSort(V, pivot+1, fim);
	}
	
} // fim do quickSort


int particionar(int *V, int inicio, int fim)
{
	int dir, esq, pivo, aux;
	esq = inicio;
	dir = fim;
	pivo = V[inicio];
	
	while (esq < dir)
	{
		while (V[esq] <= pivo)
		{
			esq++;
			comparacoes++;
		}
		while (V[dir] > pivo)
		{
			dir--;
			comparacoes++;
		}
			
		if (esq < dir)
		{
			trocas++; //
			aux = V[esq];
			V[esq] = V[dir];
			V[dir] = aux;
		}
		
//		puts("\n");
//		for (int i=0; i<tam; i++)
//			printf("%i|", vet[i]);
//		getch();
		
	} // fim do while
	
	V[inicio] = V[dir];
	V[dir] = pivo;
	
	trocas++; //
	return dir;
	
} // fim de particionar

