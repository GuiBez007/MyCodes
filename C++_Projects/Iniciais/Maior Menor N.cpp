/*
	Name: Maior e menor N
	Author: GUilherme Bezerra
	Date: 25/04/2023 18:31
	Description: Indica qual foi o maior e o menor n�mero de uma sequ�ncia (no caso 10)
*/

//Importa��o de Bibliotecas
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
				
		if (i == 0){ //passa uma �nica vez
			maior = num; menor = num;}
		else if (num > maior) //passa sempre, j� que a primeira condi��o fica falsa
			maior = num;
		if (num < menor) //fica fora do 'else if' e do 'else'; sempre passa 
			menor = num;
	i++;}
	
	printf ("O maior n�mero � %.2f e o menor n�mero � %.2f.", maior, menor);
	
}
