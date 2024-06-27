/*
	Name: Recursividade.cpp
	Author: GUilherme Bezerra
	Date: 06/03/24 09:49
	Description: praticando a recursividade em fun��es
*/

// Libraries
#include <stdio.h>
#include <locale.h>

// Prototipa��o
int Decrementar(int);

int main()
{
	int x = 0;
	printf("Digite um valor para X: ");
	scanf("%i", &x);
	Decrementar(x);
}



int Decrementar(int x)
{
	if (x == 0) // se essa parte estivesse comentada 
		return 1; // a fun��o ficaria em um loop eterno
	
	printf(x != 1 ? "%i-" : "%i-FOGO!", x);
	x--;
	Decrementar(x);
} 
// toda fun��o recursiva deve possuir uma condi��o de sa�da
