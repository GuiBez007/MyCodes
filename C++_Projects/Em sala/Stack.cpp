/*
	Name: Stack.cpp
	Author: GUilherme Bezerra 
	Date: 10/04/24 09:51
	Description: Programa para demonstrar o algoritmo da Pilha - LIFO
*/

// Libraries
#include <stdio.h>
#include <locale.h>

// Prototipation
void push(int);
int pop();
int isFull();
int isEmpty();
void listarPilha();

// Variáveis globais
int pilha[10];
int topo = -1;


main()
{
	int valor = default;
	printf("%d", valor);
}


// Função que mostra o conteúdo da pilha
void listarPilha()
{
	if (isEmpty() == 1)
		puts("Pilha vazia!");
	else
	{
		for (int i = 0; i<=topo; i++)
			printf("%d ", pilha[i]);
	}
}


// Função que adiciona um elemento da pilha
void push(int vlr)
{
	if (isFull() == 1)
		puts("A pilha está cheia - Stack Overflow!");
	else 
	{
		topo++;
		pilha[topo] = vlr;
	}
}


// Função que deleta um elemento da pilha
int pop()
{
	if (isEmpty() == 1)
		puts("A pilha está vazia - Stack is Empty");
	else
	{
		int elemento;
		elemento = pilha[topo];
		topo--;
		return elemento;
	}
}


int isFull()
{
	if (topo == 10)
		return 1;
	else return 0;
}


int isEmpty()
{
	if (topo == -1)
		return 1;
	else return 0;
}
