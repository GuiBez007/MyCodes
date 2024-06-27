/*
	Name: Fila.cpp
	Author: GUilherme Bezerra
	Date: 03/04/24 09:48
	Description: Implementação do conceito de pilhas FIFO
*/

// Libraries
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>

// Prototipação
void Inserir(int);
int Retirar();
int isFull();
int isEmpty();
void imprimirFila();

// Variáveis globais
int inicio, fim, total;
int senhas[5];

// Função Main()
int main()
{
	setlocale(LC_ALL, "Portuguese");
	int menu;
	inicio = fim = total = menu = 0;
	
	while(1)
	{
		
		system("cls");
		printf("1 - Inserir na Fila \n2 - Retirar da Fila \n3 - Exibir Fila \n4 - Sair.. \nOpção: ");
		scanf("%d", &menu);
		
		switch (menu)
		{
			case 1: int e;
				printf("Digite um número para adicionar à Fila: ");
				scanf("%d", &e);
				Inserir(e);
				break;
			case 2: 
				Retirar();
				break;
			case 3:
				imprimirFila();
				break;
			case 4:
				exit(0);
			default:
				printf("Opção inválida!\n");
		} // Fim switch case
		//getch();
		system("pause");
	}
	
	return 0;
}



// Função para inserir elemento na fila
void Inserir(int elemento)
{
	if (isFull() == 1)
		puts("\n======> A Fila está cheia!");
	else
	{
		senhas[fim] = elemento;
		fim = (fim + 1) % 5;
		total++;
		puts("Senha criada!\n");
	}
}



// Função para retirar elemento da Fila 
int Retirar()
{
	if(isEmpty() == 1)
		puts("\n\n======> A Fila está vazia!");
	else
	{
		int elem;
		elem = senhas[inicio];
		inicio = (inicio + 1) % 5;
		total--;
		return elem;
	}
}



// Função que verifica se a Fila  está cheia - retorna 1
int isFull()
{
	if (total == 5)
		return 1;
	else
		return 0;
}



// Função que verifica se a Fila está vazia - retorna 1
int isEmpty()
{
	if (total == 0)
		return 1;
	else
		return 0;
}



// Função que exibe todos os elementos da Fila 
void imprimirFila()
{
	int i, count;
	puts("\n===> Conteúdo da Fila:");
	
	for(i = inicio,count = 0; count<total; count++)
		printf("%d|", senhas[i++]);
	
	puts("\n");
}
