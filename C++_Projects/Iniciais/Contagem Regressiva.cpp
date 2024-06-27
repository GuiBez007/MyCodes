/*
	Name: Contagem Regressiva
	Author: GUilherme Bezerra
	Date: 18/04/2023 17:07
	Description: Realiza uma contagem regressiva a partir de um número inteiro digitado pelo usuário
*/

//Importação de Bibliotecas
#include <stdio.h>
#include <locale.h>
#include <windows.h>

main(){
	setlocale (LC_ALL, "Portuguese");
	int i, num;
	num = 0;
	
	printf ("Digite o número que iniciará a contagem regressiva: ");
	scanf ("%d", &num);
	
	for (i = num; i > 0; i--){
		printf ("%d\n", i);
		Sleep (1250);}
		
	printf ("FOGO!!");
	
}
