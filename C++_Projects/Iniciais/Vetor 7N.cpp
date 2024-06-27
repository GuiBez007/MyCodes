/*
	Name: Vetor 8
	Author: GUilherme Bezerra
	Date: 28/08/23 10:30h
	Description: Separa os n�meros de um vetor entre negativos e positivos
*/

//Libraries
#include <stdio.h>
#include <locale.h>

int main(){
	setlocale(LC_ALL, "Portuguese");
	int numeros[7], positivos[7], negativos[7], count_p, count_n;
	
	//Inicialization	
	for (int i=0; i<7; i++){
		positivos[i] = 0;
		negativos[i] = 0;
	}
	count_p = 0;
	count_n = 0;
	
	puts("Digite 7 n�meros a serem avaliados:");
	for (int i=0; i<7; i++)
		scanf("%i", &numeros[i]);
	
	//Increase the positive and negative numbers
	for (int i=0; i<7; i++){
		if (numeros[i] >= 0){
			positivos[count_p] = numeros[i];
			count_p++;
		}
		else{
			negativos[count_n] = numeros[i];
			count_n++;
		}
	}
	
	//Show the negative numbers
	if (count_n == 0)
		printf("\nO vetor de n�meros negativos est� vazio!\n");
	else{
		printf("Os n�meros negativos s�o: ");
		for (int i=0; i<count_n; i++){
			printf("%d ", negativos[i]);
		}
	}
	
	//Show the positive numbers
	if (count_p == 0)
		printf("\nO vetor de n�meros positivos est� vazio!\n");
	else{
		printf("Os n�meros positivos s�o: ");
		for (int i=0; i<count_p; i++){
			printf("%d ", positivos[i]);
		}
	}
	
getchar();
return 0;
	
}
