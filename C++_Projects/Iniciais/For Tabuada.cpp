/*
	Name: La�os2.cpp
	Author: GUilherme Bezerra
	Date: 18/04/2023
	Description: Programa para demonstrar a utiliza��o do la�o de repeti��o For (para)
*/

#include <stdio.h>
#include <locale.h>

main()
{
	setlocale (LC_ALL, "Portuguese");
	int i, num, resultado, x;
	num = resultado = 0;
	
	puts ("Programa da Tabuada!");
	puts ("===================================");
	
	for (x = 0; x < 500; x++){
		printf ("\nQuero saber a tabuada do n�mero: ");
		scanf ("%d", &num);
		
		for (i = 1; i < 11 ; i++){
			resultado = num*i;
			printf ("%d * %d = %d\n", num, i, resultado);}}
}
