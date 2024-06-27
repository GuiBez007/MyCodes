/*
	Name: Fila.cpp
	Author: GUilherme Bezerra
	Date: 03/04/24 09:48
	Description: Implementa��o do conceito de pilhas FIFO
*/

// Libraries
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>

// Prototipa��o
void Inserir(int);
int Retirar();
int isFull();
int isEmpty();
void imprimirFila();

// Vari�veis globais
int inicio, fim, total;
int senhas[5];

// Fun��o Main()
int main()
{
	setlocale(LC_ALL, "Portuguese");
	int menu;
	inicio = fim = total = menu = 0;
	
	while(1)
	{
		
		system("cls");
		printf("1 - Inserir na Fila \n2 - Retirar da Fila \n3 - Exibir Fila \n4 - Sair.. \nOp��o: ");
		scanf("%d", &menu);
		
		switch (menu)
		{
			case 1: int e;
				printf("Digite um n�mero para adicionar � Fila: ");
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
				printf("Op��o inv�lida!\n");
		} // Fim switch case
		//getch();
		system("pause");
	}
	
	return 0;
}



// Fun��o para inserir elemento na fila
void Inserir(int elemento)
{
	if (isFull() == 1)
		puts("\n======> A Fila est� cheia!");
	else
	{
		senhas[fim] = elemento;
		fim = (fim + 1) % 5;
		total++;
		puts("Senha criada!\n");
	}
}



// Fun��o para retirar elemento da Fila 
int Retirar()
{
	if(isEmpty() == 1)
		puts("\n\n======> A Fila est� vazia!");
	else
	{
		int elem;
		elem = senhas[inicio];
		inicio = (inicio + 1) % 5;
		total--;
		return elem;
	}
}



// Fun��o que verifica se a Fila  est� cheia - retorna 1
int isFull()
{
	if (total == 5)
		return 1;
	else
		return 0;
}



// Fun��o que verifica se a Fila est� vazia - retorna 1
int isEmpty()
{
	if (total == 0)
		return 1;
	else
		return 0;
}



// Fun��o que exibe todos os elementos da Fila 
void imprimirFila()
{
	int i, count;
	puts("\n===> Conte�do da Fila:");
	
	for(i = inicio,count = 0; count<total; count++)
		printf("%d|", senhas[i++]);
	
	puts("\n");
}
