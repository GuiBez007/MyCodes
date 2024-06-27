/*
	Name: Maior e menor N
	Author: GUilherme Bezerra
	Date: 25/04/2023 18:31
	Description: Indica qual foi o maior e o menor número de uma sequência (no caso 10)
*/

//Importação de Bibliotecas
#include <stdio.h>
#include <locale.h>

main (){
	setlocale (LC_ALL, "Portuguese");
	float num, maior, menor;
	int i;
	num = maior = menor = 0.0; i = 0;
	
	while (i < 10){
		printf ("N: ");
		scanf ("%f", &num);
				
		if (i == 0){ //passa uma única vez
			maior = num; menor = num;}
		else if (num > maior) //passa sempre, já que a primeira condição fica falsa
			maior = num;
		if (num < menor) //fica fora do 'else if' e do 'else'; sempre passa 
			menor = num;
	i++;}
	
	printf ("O maior número é %.2f e o menor número é %.2f.", maior, menor);
	
}
