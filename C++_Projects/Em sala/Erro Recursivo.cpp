/*
	Name: Recursividade.cpp
	Author: GUilherme Bezerra
	Date: 06/03/24 09:49
	Description: praticando a recursividade em funções
*/

// Libraries
#include <stdio.h>
#include <locale.h>

// Prototipação
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
		return 1; // a função ficaria em um loop eterno
	
	printf(x != 1 ? "%i-" : "%i-FOGO!", x);
	x--;
	Decrementar(x);
} 
// toda função recursiva deve possuir uma condição de saída
