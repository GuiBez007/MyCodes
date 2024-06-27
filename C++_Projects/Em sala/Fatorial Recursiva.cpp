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
int Fatorial(int, int);

int main()
{
	setlocale(LC_ALL, "Portuguese");
	int num_main;
	
	printf("Digite um n�mero para o calculo de fatorial: ");
	scanf("%i", &num_main);
	printf("O fatorial do n�mero informado �: %i", Fatorial(num_main, num_main));
	
	return 0;
}



int Fatorial(int num, int i)
{
	if (num == 1)
		return 1;
	
	printf("%i * ", i);
		
	return num * Fatorial(num-1, --i);
}
