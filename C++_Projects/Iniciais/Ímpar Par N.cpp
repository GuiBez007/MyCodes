/*
	Name: �mpar/Par
	Author: GUilherme Bezerra 
	Date :29/04/2023 16:22
	Description: Determina se o n�mero inteiro digitado pelo usu�rio � �mpar ou par
*/

//Importa��o de Bibliotecas
#include <stdio.h>
#include <locale.h>
#include <Windows.h>

main (){
	setlocale (LC_ALL, "Portuguese");
	int num, i;

	while (i == 0){    //repeti��o geral
		num = 0;
		
		printf ("Informe um n�mero: ");
		scanf ("%d", &num);
		system ("cls"); //limpa a tela
		
		for (i = 0; i != num; i += 2){    					//o contador s� indica os n�meros �MPARES, se for PAR, sa� do la�o
			if (i == num + 1){    							//todo n�mero PAR mais 2, tamb�m � PAR 
				printf ("O n�mero %d � �mpar.\n\n", num);	//(se contador PAR == a um n�mero PAR...)
				i = 0;										
			break;    										//break tamb�m funciona no for
			}
		}
		
		if (i == num)
			printf ("O n�mero %d � par.\n\n", num);
			i = 0;
	}
		
}
