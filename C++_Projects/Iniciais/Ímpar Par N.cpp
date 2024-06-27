/*
	Name: Ímpar/Par
	Author: GUilherme Bezerra 
	Date :29/04/2023 16:22
	Description: Determina se o número inteiro digitado pelo usuário é ímpar ou par
*/

//Importação de Bibliotecas
#include <stdio.h>
#include <locale.h>
#include <Windows.h>

main (){
	setlocale (LC_ALL, "Portuguese");
	int num, i;

	while (i == 0){    //repetição geral
		num = 0;
		
		printf ("Informe um número: ");
		scanf ("%d", &num);
		system ("cls"); //limpa a tela
		
		for (i = 0; i != num; i += 2){    					//o contador só indica os números ÍMPARES, se for PAR, saí do laço
			if (i == num + 1){    							//todo número PAR mais 2, também é PAR 
				printf ("O número %d é ímpar.\n\n", num);	//(se contador PAR == a um número PAR...)
				i = 0;										
			break;    										//break também funciona no for
			}
		}
		
		if (i == num)
			printf ("O número %d é par.\n\n", num);
			i = 0;
	}
		
}
